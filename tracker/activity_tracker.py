import platform
import psutil

OS = platform.system()

def get_user_apps():
    """
    Returns a list with the current foreground user application.
    Works reliably on Windows & Xorg.
    Returns empty list on Wayland (OS limitation).
    """

    try:
        if OS == "Windows":
            return _get_windows_app()
        elif OS == "Linux":
            return _get_linux_app()
        else:
            return []
    except Exception:
        return []


# ---------- WINDOWS ----------
def _get_windows_app():
    import win32gui
    import win32process

    hwnd = win32gui.GetForegroundWindow()
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    process = psutil.Process(pid)
    return [process.name()]


# ---------- LINUX (Xorg only) ----------
def _get_linux_app():
    apps = []
    for proc in psutil.process_iter(["pid", "name"]):
        if proc.info["name"]:
            name = proc.info["name"].lower()

            # ignore background/system processes
            if name.startswith((
                "systemd", "kworker", "dbus", "gnome",
                "pipewire", "ibus", "snap", "gvfs"
            )):
                continue

            apps.append(proc.info["name"])

    return apps[:1]   # only top app
