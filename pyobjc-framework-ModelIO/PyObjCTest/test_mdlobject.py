from PyObjCTools.TestSupport import TestCase, min_os_level
import ModelIO


class TestMDLObject(TestCase):
    @min_os_level("10.12")
    def testMethods(self):
        self.assertResultHasType(
            ModelIO.MDLObject.boundingBoxAtTime_,
            ModelIO.MDLAxisAlignedBoundingBox.__typestr__,
        )

        self.assertResultIsBOOL(ModelIO.MDLObject.hidden)
        self.assertArgIsBOOL(ModelIO.MDLObject.setHidden_, 0)

        self.assertArgIsBlock(
            ModelIO.MDLObject.enumerateChildObjectsOfClass_root_usingBlock_stopPointer_,
            2,
            b"v@o^Z",
        )
        self.assertArgHasType(
            ModelIO.MDLObject.enumerateChildObjectsOfClass_root_usingBlock_stopPointer_,
            3,
            b"N^Z",
        )  # XXX: Undocumented
