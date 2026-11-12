"""Generate a plain-text status update for an incident.

Usage: python3 main.py incident.json
JSON fields: id, severity (P1-P4), service, status
(investigating, identified, monitoring, resolved), started
(ISO datetime), eta_minutes.
P1/P2 wording says customers are affected; P3/P4 says impact
is limited. The next update is due started + eta_minutes.
Output is plain text, ready to paste into a status page or email.
"""
import argparse, json, sys
from datetime import datetime, timedelta

IMPACT = {
    "P1": "Customers are affected. Service is unavailable or severely degraded.",
    "P2": "Customers are affected. A major feature is degraded.",
    "P3": "Impact is limited to a small number of users.",
    "P4": "Impact is minimal. No customer-facing effect expected.",
}

def render(incident):
    severity = str(incident.get("severity", "P4")).strip().upper()
    impact = IMPACT.get(severity, IMPACT["P4"])
    started = datetime.fromisoformat(incident["started"])
    eta = int(incident.get("eta_minutes", 60))
    next_update = started + timedelta(minutes=eta)
    lines = [
        f"Incident {incident['id']} [{severity}] — {incident['service']}",
        f"Status: {incident['status']}",
        f"Impact: {impact}",
        f"Started: {started.strftime('%Y-%m-%d %H:%M')}",
        f"Next update: {next_update.strftime('%Y-%m-%d %H:%M')} ({eta} minutes)",
    ]
    return "\n".join(lines)

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    with open(args.path, encoding="utf-8") as f:
        print(render(json.load(f)))
    return 0

if __name__ == "__main__":
    sys.exit(main())
