import time
import argparse

from tracker.activity_tracker import get_active_app
from tracker.time_tracker import TimeTracker
from tracker.storage import update_today_usage, save_usage
from utils.report_utils import get_week_daywise_usage
from cli.display import show_week_table

TICK_INTERVAL = 60  # 1 minute

def run_tracker():
    tracker = TimeTracker()
    print("Tracking started (background safe)")

    try:
        while True:
            app = get_active_app()
            if app:
                tracker.set_active_app(app)

            tracker.tick()
            update_today_usage(tracker.get_usage())

            time.sleep(TICK_INTERVAL)

    except KeyboardInterrupt:
        pass  # systemd will restart it automatically

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["track", "week", "reset"])
    args = parser.parse_args()

    if args.command == "track":
        run_tracker()

    elif args.command == "week":
        table, days = get_week_daywise_usage()
        show_week_table(table, days)

    elif args.command == "reset":
        save_usage({})
        print("Data reset")

if __name__ == "__main__":
    main()
