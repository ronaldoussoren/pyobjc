import PrintCore
from PyObjCTools.TestSupport import TestCase


class TestPrintCore(TestCase):
    def test_functional(self):
        res, value = PrintCore.PMCreatePrintSettings(None)
        self.assertEqual(res, 0)

        self.assertIsInstance(value, PrintCore.PMPrintSettings)

        PrintCore.PMRetain(value)
        PrintCore.PMRelease(value)

        # Release the final reference
        PrintCore.PMRelease(value)
