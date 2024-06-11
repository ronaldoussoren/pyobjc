from PyObjCTools.TestSupport import TestCase, min_os_level
import ShazamKit


class TestSHCustomCatalog(TestCase):
    def test_classes(self):
        ShazamKit.SHCustomCatalog

    def test_methods(self):
        self.assertResultIsBOOL(
            ShazamKit.SHCustomCatalog.addReferenceSignature_representingMediaItems_error_
        )
        self.assertArgIsOut(
            ShazamKit.SHCustomCatalog.addReferenceSignature_representingMediaItems_error_,
            2,
        )

        self.assertResultIsBOOL(
            ShazamKit.SHCustomCatalog.addCustomCatalogFromURL_error_
        )
        self.assertArgIsOut(ShazamKit.SHCustomCatalog.addCustomCatalogFromURL_error_, 1)

        self.assertResultIsBOOL(ShazamKit.SHCustomCatalog.writeToURL_error_)
        self.assertArgIsOut(ShazamKit.SHCustomCatalog.writeToURL_error_, 1)

    @min_os_level("15.0")
    def test_methods15_0(self):
        self.assertResultIsBOOL(
            ShazamKit.SHCustomCatalog.initWithDataRepresentation_error_
        )
        self.assertArgIsOut(
            ShazamKit.SHCustomCatalog.initWithDataRepresentation_error_, 1
        )
