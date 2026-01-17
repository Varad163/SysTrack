import psutil

SYSTEM_KEYWORDS = [
    "kworker", "irq", "migration", "rcu",
    "systemd", "dbus", "gvfs", "pipewire",
    "cups", "network", "bluetooth", "snap",
    "tracker", "ibus", "xdg", "gsd", "avahi",
    "polkit", "upower", "modem", "colord"
]

def is_user_app(proc):
    try:
        name = proc.name().lower()

        # 1️⃣ Ignore system keywords
        if any(word in name for word in SYSTEM_KEYWORDS):
            return False

        # 2️⃣ Ignore root processes
        if proc.username() == "root":
            return False

        # 3️⃣ Ignore very tiny background tasks
        if proc.memory_info().rss < 30 * 1024 * 1024:  # < 30 MB
            return False

        return True

    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return False


def get_user_apps():
    apps = set()

    for proc in psutil.process_iter():
        if is_user_app(proc):
            apps.add(proc.name())

    return sorted(apps)


if __name__ == "__main__":
    print(get_user_apps())
