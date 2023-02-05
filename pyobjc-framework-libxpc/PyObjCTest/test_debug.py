from PyObjCTools.TestSupport import TestCase

import xpc


class TestDebug(TestCase):
    def test_functions(self):
        # This API can only be used in a debugger, decleration
        # in the header ensures it is now seen by the metadata
        # tooling (and other user code)
        self.assertNotHasAttr(xpc, "xpc_debugger_api_misuse_info")
        # self.assertResultIsNullTerminated(xpc.xpc_debugger_api_misuse_info)
