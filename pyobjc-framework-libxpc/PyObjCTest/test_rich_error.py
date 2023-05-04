from PyObjCTools.TestSupport import TestCase, min_os_level

import xpc


class TestRichError(TestCase):
    @min_os_level("13.0")
    def test_functions(self):
        self.assertResultIsNullTerminated(xpc.xpc_rich_error_copy_description)

        xpc.xpc_rich_error_can_retry
