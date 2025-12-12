import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENV_FILE = ROOT / ".env"
OUT_FILE = ROOT / "vercel.json"

CRON_PATH = "/api/cron/send-daily"


def load_dotenv_if_present():
    """Minimal .env loader (no extra dependency). Only sets vars not already set."""
    if not ENV_FILE.exists():
        return
    for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        k = k.strip()
        v = v.strip().strip('"').strip("'")
        os.environ.setdefault(k, v)


def must_int(name: str, lo: int, hi: int) -> int:
    raw = os.getenv(name)
    if raw is None:
        raise SystemExit(f"Missing env var: {name}")
    try:
        val = int(raw)
    except ValueError:
        raise SystemExit(f"{name} must be an int, got: {raw!r}")
    if not (lo <= val <= hi):
        raise SystemExit(f"{name} out of range ({lo}-{hi}), got: {val}")
    return val


def main():
    load_dotenv_if_present()

    hour = must_int("SEND_HOUR", 0, 23)
    minute = must_int("SEND_MINUTES", 0, 59)

    vercel_json = {
        "crons": [
            {
                "path": CRON_PATH,
                "schedule": f"{minute} {hour} * * *", #utc
            }
        ]
    }

    OUT_FILE.write_text(json.dumps(vercel_json, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUT_FILE} with schedule: {minute} {hour} * * * (UTC)")


if __name__ == "__main__":
    main()
