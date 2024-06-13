from PyObjCTools.TestSupport import TestCase

import FSKit


class TestFSEntityIdentifier(TestCase):
    def test_methods(self):
        self.assertArgIsHasType(
            FSKit.FSEntityIdentifier.initWithBytes_length_, 0, b"n^v"
        )
        self.assertArgSizeInArg(FSKit.FSEntityIdentifier.initWithBytes_length_, 0, 1)

        self.fail("various bytequalifier methods with unclear signature")
