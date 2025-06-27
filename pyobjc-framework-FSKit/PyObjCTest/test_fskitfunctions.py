from PyObjCTools.TestSupport import TestCase

import FSKit


class TestFSKitFunctions(TestCase):
    def test_functions(self):
        FSKit.fs_errorForPOSIXError
        FSKit.fs_errorForMachError
        FSKit.fs_errorForCocoaError
