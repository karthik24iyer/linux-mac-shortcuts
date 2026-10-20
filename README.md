# linux-mac-shortcuts

macOS-style keyboard shortcuts on **Pop!_OS 24.04 (COSMIC, Wayland)** using
[Toshy](https://github.com/RedBearAK/toshy), plus COSMIC and browser tweaks for the
gaps Toshy doesn't cover.

## Layout

```
config/toshy-user-apps.py          Custom Toshy keymaps (goes in toshy_config.py "user_apps" slice)
config/cosmic-custom-shortcuts.ron  COSMIC custom shortcuts (~/.config/cosmic/.../Shortcuts/v1/custom)
browser/mac-cmd-arrow-history.user.js  Violentmonkey userscript: Cmd+Left/Right = Back/Forward
scripts/install.sh                 Fresh machine: clean Kinto/Toshy leftovers, install Toshy, run apply.sh (needs sudo)
scripts/apply.sh                   Re-apply all customizations to an installed Toshy (no sudo, idempotent)
scripts/keylog.py                  Show the keys Toshy actually emits (debugging)
```

## Quick start

```bash
# New machine
./scripts/install.sh

# After a Toshy upgrade/reinstall, or if COSMIC settings get reset
./scripts/apply.sh
```

Then, in each Firefox-based browser (Zen, Firefox):
1. Install [Violentmonkey](https://addons.mozilla.org/firefox/addon/violentmonkey/).
2. Drag `browser/mac-cmd-arrow-history.user.js` into a tab and click **Install**
   (or Violentmonkey dashboard → **+ → New**, paste, save).

`apply.sh` backs up what it overwrites to `toshy_config.py.bak` and `custom.bak`.

## Modifier mapping (PC keyboard)

Toshy maps by position, like a Mac keyboard:

| Mac | Physical key | Toshy config name |
|---|---|---|
| ⌘ Cmd | **Alt** | `RC` |
| ⌥ Option | **Win/Super** | `Alt` |
| ⌃ Control | **Ctrl** | `Super` in GUI apps, `LC` in terminals |

So "Mac Ctrl" shortcuts must be mapped twice in custom keymaps: `Super-…` (GUI) and `LC-…` (terminals).
Keymaps in the `user_apps` slice are checked before Toshy's built-in ones, so they take priority.

## Shortcuts

✅ = works · ❌ = no COSMIC equivalent

### Text editing / clipboard (Toshy built-in)
| macOS | Status |
|---|---|
| ⌘C/V/X/Z/⇧Z/A/S/F/G/P/O/N/W/T, ⌘, | ✅ |
| ⌘←/→ line start/end, ⌘↑/↓ doc start/end (+⇧ to select) | ✅ |
| ⌥←/→ word jump, ⌥⌫ delete word, ⌘⌫ delete to line start | ✅ |
| ⌃A/E/B/F/N/P/K/D (Emacs-style) | ✅ |

### Windows, apps, Spaces
| macOS | Does | Source |
|---|---|---|
| ⌘Space | Launcher (Super+/) | Toshy built-in |
| ⌘Tab / ⌘⇧Tab | Window switcher (per window, not per app) | Toshy built-in |
| ⌘Q / ⌘W | Quit / close | Toshy built-in |
| ⌃⌘F | Maximize | Toshy built-in |
| ⌘H / ⌘M | Minimize | **custom** |
| ⌘⌥Esc | GNOME System Monitor (force quit) | **custom** |
| ⌃⌘Q / ⌘⇧Q | Lock screen / log out | **custom** |
| ⌃↑ | Workspace overview (Mission Control) | **custom** |
| ⌃←/→ | Previous/next workspace | **custom** |
| ⌃⌘↑ | Maximize toggle (not fullscreen) | **custom** |
| ⌃⌘← / ⌃⌘→ | Snap to left/right half (floating windows; again = next monitor) | **custom** |
| ⌃⌥ + arrows | Focus window in that direction (was COSMIC Super+arrows) | **custom** |
| ⌃⌥A / F / B | App Library / Files / Browser (were COSMIC Super+A/F/B) | **custom** |
| ⌃1…9 | Workspace 1–9 | COSMIC (Ctrl→Super) |
| ⌘⇧3/4/5 | Screenshots | Toshy built-in |
| ⌘\`, ⌘⌥H, ⌃↓, show desktop, ⌃⌘Space emoji | — | ❌ |

### Browser (Zen/Firefox/Chrome)
| macOS | Status |
|---|---|
| ⌘L/T/W/R, ⌘⇧T reopen tab, ⌘1…9 tab by position | ✅ Toshy built-in |
| ⌃Tab / ⌃⇧Tab, ⌘⇧[ ], ⌘[ ] | ✅ Toshy built-in |
| ⌘← / ⌘→ Back/Forward (line start/end while typing) | ✅ userscript |

### COSMIC Terminal
| macOS | Status |
|---|---|
| ⌘C/V (⌃C still SIGINT), ⌘T/W/N, ⌘K/L | ✅ Toshy built-in |
| ⌃Tab / ⌃⇧Tab, ⌘⇧[ ], ⌘⇧←/→ next/prev tab | ✅ **custom** (Toshy sent Ctrl+PageDown, which cosmic-term ignores) |
| ⌘1…9 tab by position | ✅ **custom** (→ Ctrl+Shift+1…9) |

## System changes made

| Change | Why |
|---|---|
| Removed Kinto (`~/.config/kinto`, `xkeysnail` pip pkg, `/usr/local/bin/xkeysnail`) | X11-only, doesn't work on COSMIC Wayland |
| Removed broken Toshy autostart/app entries from a previous partial install | Pointed to deleted files |
| Toshy installed from `~/src/toshy` (keep it for upgrades/uninstall) | |
| COSMIC xkb: removed `compose:rctrl` | Toshy uses Right Ctrl as virtual Cmd; Compose broke copy/paste |
| COSMIC custom shortcuts: `Super+Ctrl+Alt+M` → Minimize, `Super+Ctrl+Alt+F` → `gnome-system-monitor` | Targets for ⌘H/⌘M and ⌘⌥Esc (Toshy can't minimize or launch apps) |
| COSMIC custom shortcuts: Super tap → Disable | Physical Ctrl is Super in GUI apps, so Ctrl+Tab was opening the launcher |

Side effects: tapping Win no longer opens the launcher (use ⌘Space); physical Home/End
go Back/Forward in browsers when not typing (⌘↑/↓ still scroll to top/bottom).

## Troubleshooting

```bash
toshy-services-status              # all 3 should be active: config, cosmic-dbus, session-monitor
toshy-services-restart             # restart all (restarting only toshy-config can leave cosmic-dbus down)
toshy-xkb-check                    # detects XKB options that break Toshy
journalctl --user -u toshy-config -f
./scripts/keylog.py 60             # see what a shortcut actually sends
```

- **A shortcut does nothing** → run `keylog.py`, press it. No output = Toshy swallowed it;
  correct output = the app/COSMIC isn't handling that key.
- **App-specific mappings misbehave (e.g. terminal)** → `toshy-cosmic-dbus` is probably down;
  run `toshy-services-restart`.
- **Toshy upgrade** → re-run `~/src/toshy/setup_toshy.py install`, then `./scripts/apply.sh`.
  The `user_apps` slice survives upgrades, but `apply.sh` is safe either way.
- **Toshy installer without sudo**: if system prep is already done (packages, `input` group,
  udev rule, uinput), answer `n` to the admin question and type the secret code it prints
  to do a user-only install.
