import time


class TimeTracker:
    """
    Tracks time spent on each application based on app switches.
    """

    def __init__(self):
      
        self.current_app = None
        self.start_time = None
        self.usage = {}

    def switch_app(self, app_name: str):
        """
        Call this whenever the active app changes.
        It updates time spent on the previous app.
        """
        now = time.time()
        if self.current_app is not None and self.start_time is not None:
            elapsed_time = now - self.start_time
            self.usage[self.current_app] = (
                self.usage.get(self.current_app, 0) + elapsed_time
            )

        self.current_app = app_name
        self.start_time = now

    def stop(self):
        """
        Call this when tracking stops (e.g., program exit)
        to save time for the currently active app.
        """
        if self.current_app and self.start_time:
            now = time.time()
            elapsed_time = now - self.start_time
            self.usage[self.current_app] = (
                self.usage.get(self.current_app, 0) + elapsed_time
            )

            self.current_app = None
            self.start_time = None

    def get_usage(self):
        """
        Returns usage data as a dictionary.
        """
        return self.usage


if __name__ == "__main__":
    tracker = TimeTracker()

    print("Tracking code for 2 seconds...")
    tracker.switch_app("code")
    time.sleep(2)

    print("Switching to chrome for 3 seconds...")
    tracker.switch_app("chrome")
    time.sleep(3)

    print("Switching to terminal...")
    tracker.switch_app("terminal")

    tracker.stop()

    print("\nUsage data (in seconds):")
    print(tracker.get_usage())
