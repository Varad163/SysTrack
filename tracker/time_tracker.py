import time

class TimeTracker:
    def __init__(self):
        self.current_app = None
        self.last_tick = time.time()

    def set_active_app(self, app):
        self.current_app = app

    def tick(self):
        now = time.time()
        elapsed = now - self.last_tick
        self.last_tick = now

        if not self.current_app:
            return {}

        return {self.current_app: elapsed}
