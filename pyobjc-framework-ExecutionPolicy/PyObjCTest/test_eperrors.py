import sys

from PyObjCTools.TestSupport import TestCase

if sys.maxsize > 2 ** 32:
    import ExecutionPolicy

    class TestEPErrors(TestCase):
        def test_constants(self):
            self.assertIsInstance(ExecutionPolicy.EPErrorDomain, str)

            self.assertEqual(ExecutionPolicy.EPErrorGeneric, 1)
            self.assertEqual(ExecutionPolicy.EPErrorNotADeveloperTool, 2)
