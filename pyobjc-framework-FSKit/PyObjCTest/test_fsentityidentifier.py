from PyObjCTools.TestSupport import TestCase

import FSKit


class TestFSEntityIdentifier(TestCase):
    def test_methods(self):
        self.assertArgHasType(
            FSKit.FSEntityIdentifier.initWithUUID_byteQualifier_, 1, b"n^v"
        )
        self.assertArgIsVariableSize(
            FSKit.FSEntityIdentifier.initWithUUID_byteQualifier_, 1
        )

        self.assertArgHasType(
            FSKit.FSEntityIdentifier.initWithUUID_longByteQualifier_, 1, b"n^v"
        )
        self.assertArgIsVariableSize(
            FSKit.FSEntityIdentifier.initWithUUID_longByteQualifier_, 1
        )
