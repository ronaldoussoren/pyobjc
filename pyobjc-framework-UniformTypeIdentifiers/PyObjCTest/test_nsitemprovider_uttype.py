from PyObjCTools.TestSupport import TestCase, min_os_level

import UniformTypeIdentifiers


class TestNSItemProvider_UTType(TestCase):
    @min_os_level("13.0")
    def test_methods(self):
        self.assertArgIsBOOL(
            UniformTypeIdentifiers.NSItemProvider.initWithContentsOfURL_contentType_openInPlace_coordinated_visibility_,
            2,
        )
        self.assertArgIsBOOL(
            UniformTypeIdentifiers.NSItemProvider.initWithContentsOfURL_contentType_openInPlace_coordinated_visibility_,
            3,
        )

        self.assertArgIsBlock(
            UniformTypeIdentifiers.NSItemProvider.registerDataRepresentationForContentType_visibility_loadHandler_,
            2,
            b"@@?",  # XXX
        )

        self.assertArgIsBlock(
            UniformTypeIdentifiers.NSItemProvider.loadDataRepresentationForContentType_completionHandler_,
            1,
            b"v@@",
        )

        self.assertArgIsBOOL(
            UniformTypeIdentifiers.NSItemProvider.loadFileRepresentationForContentType_openInPlace_completionHandler_,
            1,
        )
        self.assertArgIsBlock(
            UniformTypeIdentifiers.NSItemProvider.loadFileRepresentationForContentType_openInPlace_completionHandler_,
            2,
            b"v@Z@",
        )
