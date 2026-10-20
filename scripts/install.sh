#!/usr/bin/env bash
# Fresh setup: remove old Kinto/Toshy leftovers, install Toshy, then apply customizations.
# Needs sudo (Toshy installer asks for it). Run from a normal terminal.
set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"
TOSHY_SRC="$HOME/src/toshy"

echo "==> Removing old Kinto/xkeysnail leftovers"
rm -rf "$HOME/.config/kinto"
rm -f "$HOME"/.config/autostart/xkeysnail.desktop "$HOME"/.config/autostart/kintotray.desktop
sudo pip3 uninstall -y xkeysnail --break-system-packages 2>/dev/null || true
sudo rm -f /usr/local/bin/xkeysnail

if [ -x "$HOME/.local/bin/toshy-services-status" ]; then
    echo "==> Toshy already installed, skipping installer"
else
    echo "==> Removing broken Toshy autostart/app entries"
    rm -f "$HOME"/.config/autostart/Toshy_*.desktop \
          "$HOME"/.local/share/applications/Toshy_Tray.desktop \
          "$HOME"/.local/share/applications/app.toshy.preferences.desktop

    echo "==> Installing Toshy"
    rm -rf "$TOSHY_SRC"
    git clone --depth 1 https://github.com/RedBearAK/toshy.git "$TOSHY_SRC"
    (cd "$TOSHY_SRC" && ./setup_toshy.py install)
fi

"$DIR/apply.sh"
echo "==> Done. Log out and back in if the installer asked for a reboot."
