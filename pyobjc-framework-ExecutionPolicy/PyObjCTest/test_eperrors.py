from PyObjCTools.TestSupport import TestCase

import ExecutionPolicy


class TestEPErrors(TestCase):
    def test_constants(self):
        self.assertIsInstance(ExecutionPolicy.EPErrorDomain, str)

        self.assertEqual(ExecutionPolicy.EPErrorGeneric, 1)
        self.assertEqual(ExecutionPolicy.EPErrorNotADeveloperTool, 2)
