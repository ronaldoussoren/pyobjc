import Metal
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestMTL4AccelerationStructure(TestCase):
    @min_os_level("26.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            Metal.MTL4AccelerationStructureGeometryDescriptor.opaque
        )
        self.assertArgIsBOOL(
            Metal.MTL4AccelerationStructureGeometryDescriptor.setOpaque_, 0
        )

        self.assertResultIsBOOL(
            Metal.MTL4AccelerationStructureGeometryDescriptor.allowDuplicateIntersectionFunctionInvocation
        )
        self.assertArgIsBOOL(
            Metal.MTL4AccelerationStructureGeometryDescriptor.setAllowDuplicateIntersectionFunctionInvocation_,
            0,
        )
