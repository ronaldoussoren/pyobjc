import warnings
import unittest
from PyObjCTest import loader
import os

# Reset loader.gTopdir to the
# current working directory to
# ensure it works when this
# script is compiled with Nuitka
loader.gTopdir = os.getcwd()

warnings.simplefilter("error")

suite = loader.makeTestSuite()

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)

# Print out summary. This is a structured format that
# should make it easy to use this information in scripts.
summary = {
    "count": result.testsRun,
    "fails": len(result.failures),
    "errors": len(result.errors),
    "xfails": len(getattr(result, "expectedFailures", [])),
    "xpass": len(getattr(result, "expectedSuccesses", [])),
    "skip": len(getattr(result, "skipped", [])),
}
print(f"SUMMARY: {summary}")

if not result.wasSuccessful():
    raise SystemExit(1)
else:
    raise SystemExit(0)
