#!/usr/bin/env bash
# Apply customizations on top of an installed Toshy (no sudo needed).
# Safe to re-run, e.g. after a Toshy upgrade or COSMIC settings reset.
set -euo pipefail

DIR="$(cd "$(dirname "$0")/.." && pwd)"
TOSHY_CFG="$HOME/.config/toshy/toshy_config.py"
COSMIC_SHORTCUTS="$HOME/.config/cosmic/com.system76.CosmicSettings.Shortcuts/v1/custom"
COSMIC_XKB="$HOME/.config/cosmic/com.system76.CosmicComp/v1/xkb_config"

echo "==> Toshy: writing user_apps slice"
cp "$TOSHY_CFG" "$TOSHY_CFG.bak"
python3 -I - "$TOSHY_CFG" "$DIR/config/toshy-user-apps.py" <<'EOF'
import re, sys
cfg_path, slice_path = sys.argv[1], sys.argv[2]
cfg = open(cfg_path).read()
body = open(slice_path).read()
pat = re.compile(r'(###  SLICE_MARK_START: user_apps  ###[^\n]*\n)(.*?)(###  SLICE_MARK_END: user_apps  ###)', re.S)
if not pat.search(cfg):
    sys.exit('user_apps slice markers not found')
open(cfg_path, 'w').write(pat.sub(lambda m: m.group(1) + body + m.group(3), cfg))
EOF
"$HOME/.config/toshy/.venv/bin/python" -m py_compile "$TOSHY_CFG"

echo "==> COSMIC: custom shortcuts (minimize, system monitor, disable Super tap)"
mkdir -p "$(dirname "$COSMIC_SHORTCUTS")"
[ -f "$COSMIC_SHORTCUTS" ] && cp "$COSMIC_SHORTCUTS" "$COSMIC_SHORTCUTS.bak"
cp "$DIR/config/cosmic-custom-shortcuts.ron" "$COSMIC_SHORTCUTS"

echo "==> COSMIC: removing compose:rctrl (breaks Toshy's virtual Cmd key)"
[ -f "$COSMIC_XKB" ] && sed -i -E 's/(,compose:rctrl|compose:rctrl,?)//; s/Some\(""\)/None/' "$COSMIC_XKB"

echo "==> Claude Code: Alt+V image paste"
mkdir -p "$HOME/.claude"
[ -f "$HOME/.claude/keybindings.json" ] || cp "$DIR/config/claude-keybindings.json" "$HOME/.claude/keybindings.json"

echo "==> Restarting Toshy services"
"$HOME/.local/bin/toshy-services-restart" >/dev/null
sleep 6
systemctl --user is-active toshy-config toshy-cosmic-dbus toshy-session-monitor
"$HOME/.local/bin/toshy-xkb-check" | grep 'Result'
