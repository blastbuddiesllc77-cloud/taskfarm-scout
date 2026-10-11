from datetime import datetime
import json
from pathlib import Path

DATA_FILE = Path("opportunities.json")


def load_opportunities():
    if DATA_FILE.exists():
        try:
            return json.loads(DATA_FILE.read_text())
        except (json.JSONDecodeError, OSError):
            return []
    return []


def main():
    opportunities = load_opportunities()

    print("=" * 45)
    print("       TASKFARM SCOUT")
    print("  Online Opportunity Tracker")
    print("=" * 45)
    print(f"Checked: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"Saved opportunities: {len(opportunities)}")
    print()
    print("Next: connect verified task sources and")
    print("track their requirements and payout methods.")
    print("No earnings are assumed or guaranteed.")


if __name__ == "__main__":
    main()
