import time
import argparse

from tracker.activity_tracker import get_active_app
from tracker.time_tracker import TimeTracker
from tracker.storage import update_today_usage, save_usage
from utils.report_utils import get_week_daywise_usage
from cli.display import show_week_table

POLL_INTERVAL = 1  # 1 second


def run_tracker():
    tracker = TimeTracker()
    print("App Time Tracker running (1-second polling)...")

    try:
        while True:
            # Detect focused app
            active_app = get_active_app()
            if active_app:
                tracker.set_active_app(active_app)

            # Get delta usage since last tick (≈1 sec)
            delta_usage = tracker.tick()

            # Save ONLY delta (prevents time inflation)
            if delta_usage:
                update_today_usage(delta_usage)

            time.sleep(POLL_INTERVAL)

    except KeyboardInterrupt:
        # systemd will handle restarts; no Ctrl+C needed normally
        pass


def main():
    parser = argparse.ArgumentParser(
        description="Linux App Usage Time Tracker (second-level)"
    )
    parser.add_argument(
        "command",
        choices=["track", "week", "reset"],
        help="Command to run"
    )
    args = parser.parse_args()

    if args.command == "track":
        run_tracker()

    elif args.command == "week":
        table, days = get_week_daywise_usage()
        show_week_table(table, days)

    elif args.command == "reset":
        save_usage({})
        print("All usage data reset.")


if __name__ == "__main__":
    main()
