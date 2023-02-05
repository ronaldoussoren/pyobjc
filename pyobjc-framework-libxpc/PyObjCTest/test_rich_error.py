from PyObjCTools.TestSupport import TestCase

import xpc


class TestRichError(TestCase):
    def test_functions(self):
        self.assertResultIsNullTerminated(xpc.xpc_rich_error_copy_description)

        xpc.xpc_rich_error_can_retry
