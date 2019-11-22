import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import ExecutionPolicy

    class TestEPDeveloperTool(TestCase):
        def test_constants(self):
            self.assertEqual(ExecutionPolicy.EPDeveloperToolStatusNotDetermined, 0)
            self.assertEqual(ExecutionPolicy.EPDeveloperToolStatusRestricted, 1)
            self.assertEqual(ExecutionPolicy.EPDeveloperToolStatusDenied, 2)
            self.assertEqual(ExecutionPolicy.EPDeveloperToolStatusAuthorized, 3)

        @min_os_level("10.15")
        def test_methods(self):
            self.assertArgIsBlock(
                ExecutionPolicy.EPDeveloperTool.requestDeveloperToolAccessWithCompletionHandler_,
                0,
                b"vZ",
            )
