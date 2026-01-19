import json
from pathlib import Path
from datetime import date

DATA_FILE = Path("data/usage.json")

def load_usage():
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text())
    return {}

def save_usage(data):
    DATA_FILE.parent.mkdir(exist_ok=True)
    DATA_FILE.write_text(json.dumps(data, indent=2))

def update_today_usage(today_usage):
    data = load_usage()
    today = date.today().isoformat()

    if today not in data:
        data[today] = {}

    for app, seconds in today_usage.items():
        data[today][app] = data[today].get(app, 0) + seconds

    save_usage(data)
