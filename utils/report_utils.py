from datetime import date, timedelta
from tracker.storage import load_usage

def get_today_usage():
    data = load_usage()
    return data.get(date.today().isoformat(), {})

def get_week_daywise_usage():
    data = load_usage()
    today = date.today()

    days = []
    table = {}

    for i in range(6, -1, -1):
        d = today - timedelta(days=i)
        key = d.isoformat()
        label = d.strftime("%d/%m")
        days.append(label)

        day_data = data.get(key, {})
        for app, sec in day_data.items():
            table.setdefault(app, {})[label] = sec

    return table, days
