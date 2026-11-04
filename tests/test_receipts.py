import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("ledger", ROOT / "cli.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ReceiptTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.file = Path(self.temp.name) / "artifact.txt"
        self.file.write_text("bounded evidence")
        self.stamp = "2026-11-04T03:00:00Z"

    def test_deterministic_receipt(self):
        a = MODULE.record(self.file, self.stamp)
        self.assertEqual(a, MODULE.record(self.file, self.stamp))
        self.assertEqual(a["external_references"], [])
        self.assertFalse(a["network_used"])

    def test_verify_actual_content(self):
        r = MODULE.record(self.file, self.stamp)
        self.assertTrue(MODULE.verify(r, self.file)["content_matches"])
        self.file.write_text("changed")
        self.assertFalse(MODULE.verify(r, self.file)["content_matches"])

    def test_no_fabricated_external_claims(self):
        r = MODULE.record(self.file, self.stamp)
        r["external_references"] = ["invented-transaction"]
        with self.assertRaises(ValueError):
            MODULE.verify(r, self.file)

    def test_timestamp_and_symlink(self):
        with self.assertRaises(ValueError):
            MODULE.record(self.file, "2026-11-04")
        link = Path(self.temp.name) / "link"
        link.symlink_to(self.file)
        with self.assertRaises(ValueError):
            MODULE.record(link, self.stamp)

    def test_metadata_cannot_substitute_hash(self):
        r = MODULE.record(self.file, self.stamp)
        r["bytes"] += 1
        self.assertFalse(MODULE.verify(r, self.file)["content_matches"])

    def test_cli_create_verify_and_collision(self):
        output = Path(self.temp.name) / "receipt.json"
        cmd = [sys.executable, str(ROOT / "cli.py"), "record", str(self.file),
               "--timestamp", self.stamp, "--output", str(output)]
        p = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stderr)
        before = output.read_bytes()
        self.assertEqual(subprocess.run(cmd, capture_output=True).returncode, 2)
        self.assertEqual(output.read_bytes(), before)
        p = subprocess.run([sys.executable, str(ROOT / "cli.py"), "verify", str(output),
                            "--file", str(self.file)], capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertTrue(json.loads(p.stdout)["content_matches"])

    def test_publish_does_not_claim_success(self):
        p = subprocess.run([sys.executable, str(ROOT / "cli.py"), "publish", str(self.file), "--zenodo"],
                           capture_output=True, text=True)
        self.assertNotEqual(p.returncode, 0)


if __name__ == "__main__":
    unittest.main()
