#!/usr/bin/env python3
"""Local content receipts. No Arweave transaction, DOI or publication is fabricated."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re


def digest_file(path):
    path = Path(path)
    if path.is_symlink() or not path.is_file() or path.stat().st_size > 100 * 1024 * 1024:
        raise ValueError("regular file up to 100 MiB required")
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest(), path.stat().st_size


def record(file, timestamp=None, producer="unspecified"):
    stamp = timestamp or datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    if not isinstance(stamp, str) or not stamp.endswith("Z"):
        raise ValueError("UTC timestamp ending in Z required")
    datetime.fromisoformat(stamp.replace("Z", "+00:00"))
    digest, size = digest_file(file)
    return {"schema": "pva.local-receipt/v1", "artifact_id": "sha256:" + digest,
            "sha256": digest, "bytes": size, "source_filename": Path(file).name,
            "recorded_at": stamp, "producer_declared": producer,
            "external_publication": "not_performed", "external_references": [],
            "authorship_verified": False, "network_used": False}


def verify(receipt, file):
    if not isinstance(receipt, dict) or receipt.get("schema") != "pva.local-receipt/v1":
        raise ValueError("unsupported receipt")
    if receipt.get("external_publication") != "not_performed" or receipt.get("external_references") != []:
        raise ValueError("external claims require a different verified contract")
    digest = receipt.get("sha256", "")
    if not isinstance(digest, str) or not re.fullmatch("[0-9a-f]{64}", digest):
        raise ValueError("invalid digest")
    actual, size = digest_file(file)
    valid = digest == actual and receipt.get("artifact_id") == "sha256:" + actual and receipt.get("bytes") == size
    return {"schema": "pva.local-receipt-verification/v1", "content_matches": valid,
            "sha256": actual, "external_publication_verified": False, "authorship_verified": False}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    create = sub.add_parser("record")
    create.add_argument("file", type=Path)
    create.add_argument("--timestamp")
    create.add_argument("--producer", default="unspecified")
    create.add_argument("--output", type=Path)
    check = sub.add_parser("verify")
    check.add_argument("receipt", type=Path)
    check.add_argument("--file", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == "record":
            result = record(args.file, args.timestamp, args.producer)
        else:
            if args.receipt.stat().st_size > 1024 * 1024:
                raise ValueError("receipt too large")
            result = verify(json.loads(args.receipt.read_text(encoding="utf-8")), args.file)
        content = json.dumps(result, indent=2, sort_keys=True) + "\n"
        if args.command == "record" and args.output:
            with args.output.open("x", encoding="utf-8") as target:
                target.write(content)
        print(content, end="")
        return 1 if result.get("content_matches") is False else 0
    except (OSError, ValueError, TypeError):
        parser.exit(2, "Blocked: invalid source, receipt or output collision.\n")


if __name__ == "__main__":
    raise SystemExit(main())
