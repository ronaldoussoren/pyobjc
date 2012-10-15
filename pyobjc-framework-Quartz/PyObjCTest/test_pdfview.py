
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

try:
    unicode
except NameError:
    unicode = str

class TestPDFViewHelper (NSObject):
    def PDFViewWillChangeScaleFactor_toScale_(self, f, s): return 1.0
    def PDFViewWillClickOnLink_withURL_(self, s, u): pass
    def PDFViewPrintJobTitle_(self, s): return b'a'.decode('latin1')
    def PDFViewPerformFind_(self, s): pass
    def PDFViewPerformGoToPage_(self, s): pass
    def PDFViewPerformPrint_(self, s): pass
    def PDFViewOpenPDF_forRemoteGoToAction_(self, s, a): pass


class TestPDFView (TestCase):
    def testConstants(self):
        self.assertEqual(kPDFDisplaySinglePage, 0)
        self.assertEqual(kPDFDisplaySinglePageContinuous, 1)
        self.assertEqual(kPDFDisplayTwoUp, 2)
        self.assertEqual(kPDFDisplayTwoUpContinuous, 3)
        self.assertEqual(kPDFNoArea, 0)
        self.assertEqual(kPDFPageArea, 1)
        self.assertEqual(kPDFTextArea, 2)
        self.assertEqual(kPDFAnnotationArea, 4)
        self.assertEqual(kPDFLinkArea, 8)
        self.assertEqual(kPDFControlArea, 16)
        self.assertEqual(kPDFTextFieldArea, 32)
        self.assertEqual(kPDFIconArea, 64)
        self.assertEqual(kPDFPopupArea, 128)

        self.assertIsInstance(PDFViewDocumentChangedNotification, unicode)
        self.assertIsInstance(PDFViewChangedHistoryNotification, unicode)
        self.assertIsInstance(PDFViewPageChangedNotification, unicode)
        self.assertIsInstance(PDFViewScaleChangedNotification, unicode)
        self.assertIsInstance(PDFViewAnnotationHitNotification, unicode)
        self.assertIsInstance(PDFViewCopyPermissionNotification, unicode)
        self.assertIsInstance(PDFViewPrintPermissionNotification, unicode)

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertIsInstance(PDFViewAnnotationWillHitNotification, unicode)
        self.assertIsInstance(PDFViewSelectionChangedNotification, unicode)
        self.assertIsInstance(PDFViewDisplayModeChangedNotification, unicode)
        self.assertIsInstance(PDFViewDisplayBoxChangedNotification, unicode)

    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertEqual(kPDFInterpolationQualityNone, 0)
        self.assertEqual(kPDFInterpolationQualityLow, 1)
        self.assertEqual(kPDFInterpolationQualityHigh, 2)

    def testMethods(self):
        self.assertResultIsBOOL(PDFView.canGoToFirstPage)
        self.assertResultIsBOOL(PDFView.canGoToLastPage)
        self.assertResultIsBOOL(PDFView.canGoToNextPage)
        self.assertResultIsBOOL(PDFView.canGoToPreviousPage)
        self.assertResultIsBOOL(PDFView.canGoBack)
        self.assertResultIsBOOL(PDFView.canGoForward)

        self.assertResultIsBOOL(PDFView.displaysPageBreaks)
        self.assertArgIsBOOL(PDFView.setDisplaysPageBreaks_, 0)
        self.assertResultIsBOOL(PDFView.displaysAsBook)
        self.assertArgIsBOOL(PDFView.setDisplaysAsBook_, 0)
        self.assertResultIsBOOL(PDFView.shouldAntiAlias)
        self.assertArgIsBOOL(PDFView.setShouldAntiAlias_, 0)

        self.assertResultIsBOOL(PDFView.canZoomIn)
        self.assertResultIsBOOL(PDFView.canZoomOut)
        self.assertResultIsBOOL(PDFView.autoScales)
        self.assertArgIsBOOL(PDFView.setAutoScales_, 0)

        self.assertArgIsBOOL(PDFView.pageForPoint_nearest_, 1)

        self.assertResultIsBOOL(PDFView.allowsDragging)
        self.assertArgIsBOOL(PDFView.setAllowsDragging_, 0)

    @min_os_level('10.5')
    def testMethods10_5(self):
        self.assertArgIsBOOL(PDFView.setCurrentSelection_animate_, 1)
        self.assertArgIsBOOL(PDFView.printWithInfo_autoRotate_, 1)
        self.assertArgIsBOOL(PDFView.printWithInfo_autoRotate_pageScaling_, 1)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBOOL(PDFView.enableDataDetectors)
        self.assertArgIsBOOL(PDFView.setEnableDataDetectors_, 0)

    def testProtocols(self):
        self.assertIsInstance(protocols.PDFViewDelegate, objc.informal_protocol)

        self.assertArgHasType(TestPDFViewHelper.PDFViewWillChangeScaleFactor_toScale_, 1, objc._C_CGFloat)
        self.assertResultHasType(TestPDFViewHelper.PDFViewWillChangeScaleFactor_toScale_, objc._C_CGFloat)

if __name__ == "__main__":
    main()
