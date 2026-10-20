#!/home/karthik/.config/toshy/.venv/bin/python
# Print keys Toshy actually emits (its virtual keyboard), to debug a remap.
# Usage: keylog.py [seconds]   (default 60)
import select, sys, time
import evdev

dev = next((evdev.InputDevice(p) for p in evdev.list_devices()
            if 'XWayKeyz' in evdev.InputDevice(p).name), None)
if not dev:
    sys.exit('Toshy virtual keyboard not found - is toshy-config running?')

end = time.time() + (int(sys.argv[1]) if len(sys.argv) > 1 else 60)
print(f'Logging {dev.name} ({dev.path}), Ctrl+C to stop')
while time.time() < end:
    if select.select([dev], [], [], 1)[0]:
        for e in dev.read():
            if e.type == evdev.ecodes.EV_KEY and e.value in (0, 1):
                print(time.strftime('%H:%M:%S'), evdev.ecodes.KEY[e.code], 'down' if e.value else 'up', flush=True)
