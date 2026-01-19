import subprocess

# System / background processes to ignore
IGNORE_APPS = {
    "gnome-shell",
    "systemd",
    "dbus",
    "xdg-desktop-portal",
    "gsd",
    "ibus",
    "pipewire",
    "pulseaudio",
    "wireplumber",
    "evolution-data-server",
    "goa-daemon",
    "snap",
    "tracker-miner",
    "zeitgeist",
    "at-spi",
    "notification",
}


def get_active_app():
    """
    Returns the name of the currently focused user application (Linux / X11).
    """
    try:
        # Get active window id
        window_id = subprocess.check_output(
            ["xdotool", "getactivewindow"],
            stderr=subprocess.DEVNULL
        ).decode().strip()

        # Get window class
        output = subprocess.check_output(
            ["xprop", "-id", window_id, "WM_CLASS"],
            stderr=subprocess.DEVNULL
        ).decode().lower()

        # ----------------------------
        # 🎯 MAIN USER APPS
        # ----------------------------
        if "brave" in output:
            return "Brave Browser"
        if "firefox" in output:
            return "Firefox"
        if "chrome" in output:
            return "Chrome"

        if "code" in output:
            return "VS Code"
        if "postman" in output:
            return "Postman"
        if "mongo" in output or "compass" in output:
            return "MongoDB Compass"

        if "terminal" in output or "gnome-terminal" in output:
            return "Terminal"

        # ----------------------------
        # 📁 FILE MANAGERS (Folders)
        # ----------------------------
        if "nautilus" in output:
            return "Folders"
        if "thunar" in output:
            return "Folders"
        if "dolphin" in output:
            return "Folders"
        if "nemo" in output:
            return "Folders"

        # ----------------------------
        # 🚫 IGNORE SYSTEM APPS
        # ----------------------------
        for ignore in IGNORE_APPS:
            if ignore in output:
                return None

        # ----------------------------
        # 📦 EVERYTHING ELSE
        # ----------------------------
        return "Other Apps"

    except Exception:
        return None
