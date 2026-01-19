import time

class TimeTracker:
    def __init__(self):
        self.current_app = None
        self.usage = {}
        self.last_tick = time.time()

    def set_active_app(self, app_name):
        self.current_app = app_name

    def tick(self):
        """
        Called every minute to add time to active app
        """
        if not self.current_app:
            return

        now = time.time()
        elapsed = now - self.last_tick
        self.last_tick = now

        self.usage[self.current_app] = (
            self.usage.get(self.current_app, 0) + elapsed
        )

    def get_usage(self):
        return self.usage
