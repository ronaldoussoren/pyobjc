from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2**32:
    import ModelIO

    class TestMDLMeshBufferHelper (ModelIO.NSObject):
        def fillData_offset_(self, d, o): pass
        def length(self): return 1
        def type(self): return 1

        def capacity(self): return 1

        def newZone_(self, c): return None
        def newBuffer_type_(self, c, t): return None
        def newBufferWithData_type_(self, c, t): return None
        def newBufferFromZone_length_type_(self, z, l, t): return None
        def newBufferFromZone_data_type_(self, z, d, t): return None

    class TestMDLMeshBuffer (TestCase):
        def testConstants(self):
            self.assertEqual(ModelIO.MDLMeshBufferTypeVertex, 1)
            self.assertEqual(ModelIO.MDLMeshBufferTypeIndex, 2)

        def testMethods(self):
            self.assertArgIsVariableSize(ModelIO.MDLMeshBufferMap.initWithBytes_deallocator_, 0)
            self.assertArgIsBlock(ModelIO.MDLMeshBufferMap.initWithBytes_deallocator_, 1, b'v')

            self.assertResultIsVariableSize(ModelIO.MDLMeshBufferMap.bytes)

            self.assertArgHasType(TestMDLMeshBufferHelper.fillData_offset_, 1, objc._C_NSUInteger)
            self.assertResultHasType(TestMDLMeshBufferHelper.length, objc._C_NSUInteger)
            self.assertResultHasType(TestMDLMeshBufferHelper.type, objc._C_NSUInteger)
            self.assertResultHasType(TestMDLMeshBufferHelper.capacity, objc._C_NSUInteger)
            self.assertArgHasType(TestMDLMeshBufferHelper.newZone_, 0, objc._C_NSUInteger)
            self.assertArgHasType(TestMDLMeshBufferHelper.newBuffer_type_, 0, objc._C_NSUInteger)
            self.assertArgHasType(TestMDLMeshBufferHelper.newBuffer_type_, 1, objc._C_NSUInteger)
            self.assertArgHasType(TestMDLMeshBufferHelper.newBufferWithData_type_, 1, objc._C_NSUInteger)
            self.assertArgHasType(TestMDLMeshBufferHelper.newBufferFromZone_length_type_, 1, objc._C_NSUInteger)
            self.assertArgHasType(TestMDLMeshBufferHelper.newBufferFromZone_length_type_, 2, objc._C_NSUInteger)
            self.assertArgHasType(TestMDLMeshBufferHelper.newBufferFromZone_data_type_, 2, objc._C_NSUInteger)

        def testProtocolObjects(self):
            objc.protocolNamed('MDLMeshBuffer')
            objc.protocolNamed('MDLMeshBufferZone')
            objc.protocolNamed('MDLMeshBufferAllocator')


if __name__ == "__main__":
    main()
