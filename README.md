# incident-communication-template-generator

Generate a plain-text status update for an incident from a JSON file: severity-based impact wording (P1/P2 = customers affected), status, start time and the next-update time (started + ETA minutes).

## How to run

```sh
python3 main.py incident.json
```

## Example output

```
Incident INC-42 [P1] — Email
Status: investigating
Impact: Customers are affected. Service is unavailable or severely degraded.
Started: 2026-11-08 09:00
Next update: 2026-11-08 10:00 (60 minutes)
```

Standard library only. Run the tests with `python3 -m unittest discover`.
