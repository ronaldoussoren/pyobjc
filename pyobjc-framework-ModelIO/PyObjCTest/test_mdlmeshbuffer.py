from PyObjCTools.TestSupport import TestCase
import objc
import ModelIO


class TestMDLMeshBufferHelper(ModelIO.NSObject):
    def fillData_offset_(self, d, o):
        pass

    def length(self):
        return 1

    def type(self):  # noqa: A003
        return 1

    def capacity(self):
        return 1

    def newZone_(self, c):
        return None

    def newBuffer_type_(self, c, t):
        return None

    def newBufferWithData_type_(self, c, t):
        return None

    def newBufferFromZone_length_type_(self, z, x, t):
        return None

    def newBufferFromZone_data_type_(self, z, d, t):
        return None


class TestMDLMeshBuffer(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(ModelIO.MDLMeshBufferType)

    def test_constants(self):
        self.assertEqual(ModelIO.MDLMeshBufferTypeVertex, 1)
        self.assertEqual(ModelIO.MDLMeshBufferTypeIndex, 2)
        self.assertEqual(ModelIO.MDLMeshBufferTypeCustom, 3)

    def test_methods(self):
        self.assertArgIsVariableSize(
            ModelIO.MDLMeshBufferMap.initWithBytes_deallocator_, 0
        )
        self.assertArgIsBlock(
            ModelIO.MDLMeshBufferMap.initWithBytes_deallocator_, 1, b"v"
        )

        self.assertResultIsVariableSize(ModelIO.MDLMeshBufferMap.bytes)

        self.assertArgHasType(
            TestMDLMeshBufferHelper.fillData_offset_, 1, objc._C_NSUInteger
        )
        self.assertResultHasType(TestMDLMeshBufferHelper.length, objc._C_NSUInteger)
        self.assertResultHasType(TestMDLMeshBufferHelper.type, objc._C_NSUInteger)
        self.assertResultHasType(TestMDLMeshBufferHelper.capacity, objc._C_NSUInteger)
        self.assertArgHasType(TestMDLMeshBufferHelper.newZone_, 0, objc._C_NSUInteger)
        self.assertArgHasType(
            TestMDLMeshBufferHelper.newBuffer_type_, 0, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMDLMeshBufferHelper.newBuffer_type_, 1, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMDLMeshBufferHelper.newBufferWithData_type_, 1, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMDLMeshBufferHelper.newBufferFromZone_length_type_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMDLMeshBufferHelper.newBufferFromZone_length_type_,
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMDLMeshBufferHelper.newBufferFromZone_data_type_, 2, objc._C_NSUInteger
        )

    def test_protocols(self):
        self.assertProtocolExists("MDLMeshBuffer", ModelIO)
        self.assertProtocolExists("MDLMeshBufferZone", ModelIO)
        self.assertProtocolExists("MDLMeshBufferAllocator", ModelIO)
