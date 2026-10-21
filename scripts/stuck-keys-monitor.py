#!/home/karthik/.config/toshy/.venv/bin/python
# Log any key held down >15s on any keyboard (physical, Toshy, Wispr helper),
# to catch the "keyboard half-dead until reboot" bug. Log: journalctl --user -u stuck-keys-monitor
#
# Known cause: after a paste, Wispr's helper sometimes presses Right Ctrl (Toshy's Cmd)
# and never releases it. The helper never legitimately holds a key, so after HELPER_THRESHOLD
# it is killed: its virtual keyboard goes away (releasing the key) and Wispr respawns it.
import subprocess
import time
import evdev

THRESHOLD = 15
HELPER_THRESHOLD = 2
held = {}   # (path, key) -> first seen time
devs = {}

while True:
    for p in evdev.list_devices():
        if p not in devs:
            try:
                d = evdev.InputDevice(p)
                if evdev.ecodes.EV_KEY in d.capabilities() and 'Keyboard' in d.name or 'Wispr' in d.name:
                    devs[p] = d
            except OSError:
                pass
    now = time.time()
    seen = set()
    for p, d in list(devs.items()):
        try:
            keys = d.active_keys()
        except (OSError, SystemError):  # device removed (SystemError from evdev on ENODEV)
            del devs[p]
            continue
        for k in keys:
            seen.add((p, k))
            first = held.setdefault((p, k), now)
            if 'Wispr' in d.name and now - first >= HELPER_THRESHOLD:
                print(f'Wispr helper stuck on {evdev.ecodes.KEY.get(k, k)}, restarting helper', flush=True)
                subprocess.run(['pkill', '-x', 'wispr-flow-linu'])
                held[(p, k)] = now  # don't re-kill before the device is gone
            elif now - first >= THRESHOLD and first > 0:
                print(f'STUCK? {d.name} ({p}) {evdev.ecodes.KEY.get(k, k)} held {int(now - first)}s', flush=True)
                held[(p, k)] = -first  # log once
    for pk in set(held) - seen:
        if held[pk] < 0:
            print(f'released {pk[0]} {evdev.ecodes.KEY.get(pk[1], pk[1])} after {int(now + held[pk])}s', flush=True)
        del held[pk]
    time.sleep(1)
