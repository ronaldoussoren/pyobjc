from PyObjCTools.TestSupport import TestCase, min_os_level

import ExecutionPolicy


class TestEPDeveloperTool(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(ExecutionPolicy.EPDeveloperToolStatus)

    def test_constants(self):
        self.assertEqual(ExecutionPolicy.EPDeveloperToolStatusNotDetermined, 0)
        self.assertEqual(ExecutionPolicy.EPDeveloperToolStatusRestricted, 1)
        self.assertEqual(ExecutionPolicy.EPDeveloperToolStatusDenied, 2)
        self.assertEqual(ExecutionPolicy.EPDeveloperToolStatusAuthorized, 3)

    @min_os_level("10.15")
    def test_methods(self):
        self.assertArgIsBlock(
            ExecutionPolicy.EPDeveloperTool.requestDeveloperToolAccessWithCompletionHandler_,  # noqa: B950
            0,
            b"vZ",
        )
