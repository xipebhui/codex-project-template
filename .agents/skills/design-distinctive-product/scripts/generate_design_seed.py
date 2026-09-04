#!/usr/bin/env python3
"""Generate a recorded random seed for a distinctive design variation."""

from __future__ import annotations

import argparse
import json
import secrets
from datetime import datetime, timezone


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--bytes",
        type=int,
        default=32,
        dest="byte_count",
        help="Number of random bytes to generate (default: 32)",
    )
    args = parser.parse_args()
    if args.byte_count < 16:
        parser.error("--bytes must be at least 16")

    generated_at = datetime.now(timezone.utc).replace(microsecond=0)
    random_string = secrets.token_hex(args.byte_count)
    print(
        json.dumps(
            {
                "seed_id": f"{generated_at:%Y%m%dT%H%M%SZ}-{random_string[:8]}",
                "generated_at": generated_at.isoformat().replace("+00:00", "Z"),
                "random_string": random_string,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
