"""Run conformance fixtures with all temporary files under an explicit caller-owned folder."""
import argparse
import sys
import tempfile
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
root = Path(__file__).resolve().parent
sys.path.insert(0, str(root))
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--tmp", type=Path, required=True)
args = parser.parse_args()
args.tmp.mkdir(parents=True, exist_ok=True)
tempfile.tempdir = str(args.tmp.resolve())
suite = unittest.defaultTestLoader.discover(str(root / "tests"))
result = unittest.TextTestRunner(verbosity=2).run(suite)
raise SystemExit(0 if result.wasSuccessful() else 1)
