import time
import argparse

from tracker.activity_tracker import get_active_app
from tracker.time_tracker import TimeTracker
from tracker.storage import update_today_usage, save_usage
from utils.report_utils import get_week_daywise_usage
from cli.display import show_week_table

POLL_INTERVAL = 3  # seconds


def run_tracker():
    tracker = TimeTracker()
    last_app = None

    print("Tracking started (Ctrl+C to stop)")

    try:
        while True:
            current_app = get_active_app()

            # Only switch when the focused app actually changes
            if current_app and current_app != last_app:
                tracker.switch_app(current_app)
                last_app = current_app

            time.sleep(POLL_INTERVAL)

    except KeyboardInterrupt:
        print("\nTracking stopped")

    finally:
        tracker.stop()
        update_today_usage(tracker.get_usage())
        print("Usage saved")


def main():
    parser = argparse.ArgumentParser(description="Linux App Time Tracker")
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
