from PyObjCTools.TestSupport import TestCase

import xpc


class TestEndpoint(TestCase):
    def test_functions(self):
        self.assertResultIsRetained(xpc.xpc_endpoint_create)
