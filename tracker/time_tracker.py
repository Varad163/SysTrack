import time

class TimeTracker:
    def __init__(self):
        self.current_app = None
        self.start_time = None
        self.usage = {}

    def switch_app(self, app_name):
        now = time.time()

        if self.current_app:
            elapsed = now - self.start_time
            self.usage[self.current_app] = (
                self.usage.get(self.current_app, 0) + elapsed
            )

        self.current_app = app_name
        self.start_time = now

    def stop(self):
        if self.current_app:
            now = time.time()
            elapsed = now - self.start_time
            self.usage[self.current_app] = (
                self.usage.get(self.current_app, 0) + elapsed
            )

    def get_usage(self):
        return self.usage
