from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2**32:
    import ModelIO

    class TestMDLAssetHelper (ModelIO.NSObject):
        def boundingBox(self): return 1
        def setBoundingBox_(self, v): pass

        def sphericalHarmonicsLevel(self): return 1
        def setSphericalHarmonicsLevel_(self, v): pass

    class TestMDLAsset (TestCase):
        def testMethods(self):
            self.assertArgIsBOOL(ModelIO.MDLAsset.initWithURL_vertexDescriptor_bufferAllocator_preserveTopology_error_, 3)
            self.assertArgIsOut(ModelIO.MDLAsset.initWithURL_vertexDescriptor_bufferAllocator_preserveTopology_error_, 4)

            self.assertResultIsBOOL(ModelIO.MDLAsset.exportAssetToURL_)

            self.assertResultIsBOOL(ModelIO.MDLAsset.exportAssetToURL_error_)
            self.assertArgIsOut(ModelIO.MDLAsset.exportAssetToURL_error_, 1)

            self.assertResultIsBOOL(ModelIO.MDLAsset.canImportFileExtension_)

            self.assertResultIsBOOL(ModelIO.MDLAsset.canExportFileExtension_)

            # XXX: SIMD types
            #self.assertResultHasType(TestMDLAssetHelper.boundingBox, ...)
            #self.assertArgHasType(TestMDLAssetHelper.setBoundingBox_, 0, ...)
            #self.assertArgHasType(TestMDLAssetHelper.sphericalHarmonicsCoefficientsAtPosition_, 0, ...)

            self.assertResultHasType(TestMDLAssetHelper.sphericalHarmonicsLevel, objc._C_NSUInteger)
            self.assertArgHasType(TestMDLAssetHelper.setSphericalHarmonicsLevel_, 0, objc._C_NSUInteger)

        @min_os_level('10.13')
        def testMethods10_13(self):
            self.assertArgIsBOOL(ModelIO.MDLAsset.initWithURL_bufferAllocator_preserveIndexing_error_, 2)
            self.assertArgIsOut(ModelIO.MDLAsset.initWithURL_bufferAllocator_preserveIndexing_error_, 3)

        def testProtocolObjects(self):
            objc.protocolNamed('MDLLightProbeIrradianceDataSource')

if __name__ == "__main__":
    main()
