from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import Quartz
import objc


class TestPDFViewHelper(Quartz.NSObject):
    def PDFViewWillChangeScaleFactor_toScale_(self, f, s):
        return 1.0

    def PDFViewWillClickOnLink_withURL_(self, s, u):
        pass

    def PDFViewPrintJobTitle_(self, s):
        return "a"

    def PDFViewPerformFind_(self, s):
        pass

    def PDFViewPerformGoToPage_(self, s):
        pass

    def PDFViewPerformPrint_(self, s):
        pass

    def PDFViewOpenPDF_forRemoteGoToAction_(self, s, a):
        pass


class TestPDFView(TestCase):
    def testConstants(self):
        self.assertEqual(Quartz.kPDFDisplaySinglePage, 0)
        self.assertEqual(Quartz.kPDFDisplaySinglePageContinuous, 1)
        self.assertEqual(Quartz.kPDFDisplayTwoUp, 2)
        self.assertEqual(Quartz.kPDFDisplayTwoUpContinuous, 3)
        self.assertEqual(Quartz.kPDFNoArea, 0)
        self.assertEqual(Quartz.kPDFPageArea, 1)
        self.assertEqual(Quartz.kPDFTextArea, 2)
        self.assertEqual(Quartz.kPDFAnnotationArea, 4)
        self.assertEqual(Quartz.kPDFLinkArea, 8)
        self.assertEqual(Quartz.kPDFControlArea, 16)
        self.assertEqual(Quartz.kPDFTextFieldArea, 32)
        self.assertEqual(Quartz.kPDFIconArea, 64)
        self.assertEqual(Quartz.kPDFPopupArea, 128)
        self.assertEqual(Quartz.kPDFImageArea, 256)

        self.assertIsInstance(Quartz.PDFViewDocumentChangedNotification, str)
        self.assertIsInstance(Quartz.PDFViewChangedHistoryNotification, str)
        self.assertIsInstance(Quartz.PDFViewPageChangedNotification, str)
        self.assertIsInstance(Quartz.PDFViewScaleChangedNotification, str)
        self.assertIsInstance(Quartz.PDFViewAnnotationHitNotification, str)
        self.assertIsInstance(Quartz.PDFViewCopyPermissionNotification, str)
        self.assertIsInstance(Quartz.PDFViewPrintPermissionNotification, str)
        self.assertIsInstance(Quartz.PDFViewVisiblePagesChangedNotification, str)

        self.assertEqual(Quartz.kPDFDisplayDirectionVertical, 0)
        self.assertEqual(Quartz.kPDFDisplayDirectionHorizontal, 1)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(Quartz.PDFViewAnnotationWillHitNotification, str)
        self.assertIsInstance(Quartz.PDFViewSelectionChangedNotification, str)
        self.assertIsInstance(Quartz.PDFViewDisplayModeChangedNotification, str)
        self.assertIsInstance(Quartz.PDFViewDisplayBoxChangedNotification, str)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertEqual(Quartz.kPDFInterpolationQualityNone, 0)
        self.assertEqual(Quartz.kPDFInterpolationQualityLow, 1)
        self.assertEqual(Quartz.kPDFInterpolationQualityHigh, 2)

    def testMethods(self):
        self.assertResultIsBOOL(Quartz.PDFView.canGoToFirstPage)
        self.assertResultIsBOOL(Quartz.PDFView.canGoToLastPage)
        self.assertResultIsBOOL(Quartz.PDFView.canGoToNextPage)
        self.assertResultIsBOOL(Quartz.PDFView.canGoToPreviousPage)
        self.assertResultIsBOOL(Quartz.PDFView.canGoBack)
        self.assertResultIsBOOL(Quartz.PDFView.canGoForward)

        self.assertResultIsBOOL(Quartz.PDFView.displaysPageBreaks)
        self.assertArgIsBOOL(Quartz.PDFView.setDisplaysPageBreaks_, 0)
        self.assertResultIsBOOL(Quartz.PDFView.displaysAsBook)
        self.assertArgIsBOOL(Quartz.PDFView.setDisplaysAsBook_, 0)
        self.assertResultIsBOOL(Quartz.PDFView.shouldAntiAlias)
        self.assertArgIsBOOL(Quartz.PDFView.setShouldAntiAlias_, 0)

        self.assertResultIsBOOL(Quartz.PDFView.canZoomIn)
        self.assertResultIsBOOL(Quartz.PDFView.canZoomOut)
        self.assertResultIsBOOL(Quartz.PDFView.autoScales)
        self.assertArgIsBOOL(Quartz.PDFView.setAutoScales_, 0)

        self.assertArgIsBOOL(Quartz.PDFView.pageForPoint_nearest_, 1)

        self.assertResultIsBOOL(Quartz.PDFView.allowsDragging)
        self.assertArgIsBOOL(Quartz.PDFView.setAllowsDragging_, 0)

    @min_os_level("10.5")
    def testMethods10_5(self):
        self.assertArgIsBOOL(Quartz.PDFView.setCurrentSelection_animate_, 1)
        self.assertArgIsBOOL(Quartz.PDFView.printWithInfo_autoRotate_, 1)
        self.assertArgIsBOOL(Quartz.PDFView.printWithInfo_autoRotate_pageScaling_, 1)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(Quartz.PDFView.enableDataDetectors)
        self.assertArgIsBOOL(Quartz.PDFView.setEnableDataDetectors_, 0)

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertResultIsBOOL(Quartz.PDFView.displaysRTL)
        self.assertArgIsBOOL(Quartz.PDFView.setDisplaysRTL_, 0)

        self.assertResultIsBOOL(Quartz.PDFView.acceptsDraggedFiles)
        self.assertArgIsBOOL(Quartz.PDFView.setAcceptsDraggedFiles_, 0)

    @min_os_level("10.14")
    def testMethods10_14(self):
        self.assertResultIsBOOL(Quartz.PDFView.pageShadowsEnabled)
        self.assertArgIsBOOL(Quartz.PDFView.enablePageShadows_, 0)

    @min_sdk_level("10.13")
    def testProtocols(self):
        objc.protocolNamed("PDFViewDelegate")

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestPDFViewHelper.PDFViewWillChangeScaleFactor_toScale_, 1, objc._C_CGFloat
        )
        self.assertResultHasType(
            TestPDFViewHelper.PDFViewWillChangeScaleFactor_toScale_, objc._C_CGFloat
        )
