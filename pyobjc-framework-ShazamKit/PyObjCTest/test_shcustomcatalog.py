from PyObjCTools.TestSupport import TestCase
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

        # XXX: unavailable -init, +new
