from PyObjCTools.TestSupport import TestCase

import FSKit


class TestFSFileName(TestCase):
    def test_methods(self):
        self.assertArgIsIn(FSKit.FSFileName.initWithCString_, 0)
        self.assertArgIsNullTerminated(FSKit.FSFileName.initWithCString_, 0)

        self.assertArgIsIn(FSKit.FSFileName.initWithBytes_length_, 0)
        self.assertArgSizeInArg(FSKit.FSFileName.initWithBytes_length_, 0, 1)

        self.assertArgIsIn(FSKit.FSFileName.nameWithCString_, 0)
        self.assertArgIsNullTerminated(FSKit.FSFileName.nameWithCString_, 0)

        self.assertArgIsIn(FSKit.FSFileName.nameWithBytes_length_, 0)
        self.assertArgSizeInArg(FSKit.FSFileName.nameWithBytes_length_, 0, 1)
