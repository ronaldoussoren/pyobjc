import objc
from PyObjCTools.TestSupport import TestCase


import SceneKit


class TestSCNBoundingVolumeHelper(SceneKit.NSObject):
    def getBoundingBoxMin_max_(self, a, b):
        return 1

    def getBoundingSphereCenter_radius_(self, center, radius):
        return 1

    def setBoundingBoxMin_max_(self, a, b):
        return 1


class TestSCNBoundingVolume(TestCase):
    def testProtocols(self):
        self.assertProtocolExists("SCNBoundingVolume")

    def testProtocolMethods(self):
        self.assertResultIsBOOL(TestSCNBoundingVolumeHelper.getBoundingBoxMin_max_)
        self.assertArgHasType(
            TestSCNBoundingVolumeHelper.getBoundingBoxMin_max_,
            0,
            b"o^" + SceneKit.SCNVector3.__typestr__,
        )
        self.assertArgHasType(
            TestSCNBoundingVolumeHelper.getBoundingBoxMin_max_,
            1,
            b"o^" + SceneKit.SCNVector3.__typestr__,
        )

        self.assertResultIsBOOL(
            TestSCNBoundingVolumeHelper.getBoundingSphereCenter_radius_
        )
        self.assertArgHasType(
            TestSCNBoundingVolumeHelper.getBoundingSphereCenter_radius_,
            0,
            b"o^" + SceneKit.SCNVector3.__typestr__,
        )
        self.assertArgHasType(
            TestSCNBoundingVolumeHelper.getBoundingSphereCenter_radius_,
            1,
            b"o^" + objc._C_CGFloat,
        )

        self.assertArgHasType(
            TestSCNBoundingVolumeHelper.setBoundingBoxMin_max_,
            0,
            b"n^" + SceneKit.SCNVector3.__typestr__,
        )
        self.assertArgHasType(
            TestSCNBoundingVolumeHelper.setBoundingBoxMin_max_,
            1,
            b"n^" + SceneKit.SCNVector3.__typestr__,
        )
