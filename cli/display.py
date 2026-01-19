from rich.console import Console
from rich.table import Table

console = Console()

def fmt(sec):
    m = int(sec // 60)
    h = m // 60
    m = m % 60
    return f"{h}h {m}m" if h else f"{m}m"

def show_week_table(data, days):
    table = Table(title="Weekly App Usage (Day-wise)")

    table.add_column("Application")
    for d in days:
        table.add_column(d)
    table.add_column("Total")

    for app, usage in data.items():
        total = sum(usage.values())
        row = [app]

        for d in days:
            row.append(fmt(usage.get(d, 0)) if d in usage else "-")

        row.append(fmt(total))
        table.add_row(*row)

    console.print(table)
