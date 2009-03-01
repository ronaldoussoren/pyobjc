
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFViewHelper (NSObject):
    def PDFViewWillChangeScaleFactor_toScale_(self, f, s): return 1.0
    def PDFViewWillClickOnLink_withURL_(self, s, u): pass
    def PDFViewPrintJobTitle_(self, s): return u'a'
    def PDFViewPerformFind_(self, s): pass
    def PDFViewPerformGoToPage_(self, s): pass
    def PDFViewPerformPrint_(self, s): pass
    def PDFViewOpenPDF_forRemoteGoToAction_(self, s, a): pass


class TestPDFView (TestCase):
    def testConstants(self):
        self.failUnlessEqual(kPDFDisplaySinglePage, 0)
        self.failUnlessEqual(kPDFDisplaySinglePageContinuous, 1)
        self.failUnlessEqual(kPDFDisplayTwoUp, 2)
        self.failUnlessEqual(kPDFDisplayTwoUpContinuous, 3)
        self.failUnlessEqual(kPDFNoArea, 0)
        self.failUnlessEqual(kPDFPageArea, 1)
        self.failUnlessEqual(kPDFTextArea, 2)
        self.failUnlessEqual(kPDFAnnotationArea, 4)
        self.failUnlessEqual(kPDFLinkArea, 8)
        self.failUnlessEqual(kPDFControlArea, 16)
        self.failUnlessEqual(kPDFTextFieldArea, 32)
        self.failUnlessEqual(kPDFIconArea, 64)
        self.failUnlessEqual(kPDFPopupArea, 128)

        self.failUnlessIsInstance(PDFViewDocumentChangedNotification, unicode)
        self.failUnlessIsInstance(PDFViewChangedHistoryNotification, unicode)
        self.failUnlessIsInstance(PDFViewPageChangedNotification, unicode)
        self.failUnlessIsInstance(PDFViewScaleChangedNotification, unicode)
        self.failUnlessIsInstance(PDFViewAnnotationHitNotification, unicode)
        self.failUnlessIsInstance(PDFViewCopyPermissionNotification, unicode)
        self.failUnlessIsInstance(PDFViewPrintPermissionNotification, unicode)

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.failUnlessIsInstance(PDFViewAnnotationWillHitNotification, unicode)
        self.failUnlessIsInstance(PDFViewSelectionChangedNotification, unicode)
        self.failUnlessIsInstance(PDFViewDisplayModeChangedNotification, unicode)
        self.failUnlessIsInstance(PDFViewDisplayBoxChangedNotification, unicode)

    def testMethods(self):
        self.failUnlessResultIsBOOL(PDFView.canGoToFirstPage)
        self.failUnlessResultIsBOOL(PDFView.canGoToLastPage)
        self.failUnlessResultIsBOOL(PDFView.canGoToNextPage)
        self.failUnlessResultIsBOOL(PDFView.canGoToPreviousPage)
        self.failUnlessResultIsBOOL(PDFView.canGoBack)
        self.failUnlessResultIsBOOL(PDFView.canGoForward)

        self.failUnlessResultIsBOOL(PDFView.displaysPageBreaks)
        self.failUnlessArgIsBOOL(PDFView.setDisplaysPageBreaks_, 0)
        self.failUnlessResultIsBOOL(PDFView.displaysAsBook)
        self.failUnlessArgIsBOOL(PDFView.setDisplaysAsBook_, 0)
        self.failUnlessResultIsBOOL(PDFView.shouldAntiAlias)
        self.failUnlessArgIsBOOL(PDFView.setShouldAntiAlias_, 0)

        self.failUnlessResultIsBOOL(PDFView.canZoomIn)
        self.failUnlessResultIsBOOL(PDFView.canZoomOut)
        self.failUnlessResultIsBOOL(PDFView.autoScales)
        self.failUnlessArgIsBOOL(PDFView.setAutoScales_, 0)

        self.failUnlessArgIsBOOL(PDFView.pageForPoint_nearest_, 1)

        self.failUnlessResultIsBOOL(PDFView.allowsDragging)
        self.failUnlessArgIsBOOL(PDFView.setAllowsDragging_, 0)

    @min_os_level('10.5')
    def testMethods10_5(self):
        self.failUnlessArgIsBOOL(PDFView.setCurrentSelection_animate_, 1)
        self.failUnlessArgIsBOOL(PDFView.printWithInfo_autoRotate_, 1)
        self.failUnlessArgIsBOOL(PDFView.printWithInfo_autoRotate_pageScaling_, 1)

    def testProtocols(self):
        self.failUnlessIsInstance(protocols.PDFViewDelegate, objc.informal_protocol)

        self.failUnlessArgHasType(TestPDFViewHelper.PDFViewWillChangeScaleFactor_toScale_, 1, objc._C_CGFloat)
        self.failUnlessResultHasType(TestPDFViewHelper.PDFViewWillChangeScaleFactor_toScale_, objc._C_CGFloat)

if __name__ == "__main__":
    main()
