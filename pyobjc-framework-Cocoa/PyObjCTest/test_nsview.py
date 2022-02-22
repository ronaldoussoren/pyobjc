import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSViewHelper(AppKit.NSObject):
    def view_stringForToolTip_point_userData_(self, a, b, c, d):
        return 1

    def layer_shouldInheritContentsScale_fromWindow_(self, a, b, c):
        return 1


class ObjCTestNSView_KnowPageRange(AppKit.NSView):
    def knowsPageRange_(self, aRange):
        return objc.YES, (1, 10)

    def rectForPage_(self, page):
        return ((1, 1), (2, 2))


class TestNSView(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AppKit.NSDefinitionOptionKey, str)
        self.assertIsTypedEnum(AppKit.NSDefinitionPresentationType, str)
        self.assertIsTypedEnum(AppKit.NSViewFullScreenModeOptionKey, str)

    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSAutoresizingMaskOptions)
        self.assertIsEnumType(AppKit.NSBorderType)
        self.assertIsEnumType(AppKit.NSViewLayerContentsPlacement)
        self.assertIsEnumType(AppKit.NSViewLayerContentsRedrawPolicy)

    def test_knowsPageRange(self):
        method = ObjCTestNSView_KnowPageRange.knowsPageRange_
        self.assertEqual(
            method.__metadata__()["arguments"][2]["type"],
            b"o^" + AppKit.NSRange.__typestr__,
        )

    def test_rectForPage(self):
        method = ObjCTestNSView_KnowPageRange.rectForPage_

        self.assertResultHasType(method, AppKit.NSRect.__typestr__)
        self.assertEqual(
            objc.splitSignature(method.signature),
            objc.splitSignature(AppKit.NSRect.__typestr__ + b"@:" + objc._C_NSInteger),
        )


class TestHeader(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSViewNotSizable, 0)
        self.assertEqual(AppKit.NSViewMinXMargin, 1)
        self.assertEqual(AppKit.NSViewWidthSizable, 2)
        self.assertEqual(AppKit.NSViewMaxXMargin, 4)
        self.assertEqual(AppKit.NSViewMinYMargin, 8)
        self.assertEqual(AppKit.NSViewHeightSizable, 16)
        self.assertEqual(AppKit.NSViewMaxYMargin, 32)

        self.assertEqual(AppKit.NSNoBorder, 0)
        self.assertEqual(AppKit.NSLineBorder, 1)
        self.assertEqual(AppKit.NSBezelBorder, 2)
        self.assertEqual(AppKit.NSGrooveBorder, 3)

        self.assertIsInstance(AppKit.NSViewFrameDidChangeNotification, str)
        self.assertIsInstance(AppKit.NSViewFocusDidChangeNotification, str)
        self.assertIsInstance(AppKit.NSViewBoundsDidChangeNotification, str)
        self.assertIsInstance(AppKit.NSViewGlobalFrameDidChangeNotification, str)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(AppKit.NSFullScreenModeAllScreens, str)
        self.assertIsInstance(AppKit.NSFullScreenModeSetting, str)
        self.assertIsInstance(AppKit.NSFullScreenModeWindowLevel, str)
        self.assertIsInstance(AppKit.NSViewDidUpdateTrackingAreasNotification, str)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(
            AppKit.NSFullScreenModeApplicationPresentationOptions, str
        )

        self.assertEqual(AppKit.NSViewLayerContentsRedrawNever, 0)
        self.assertEqual(AppKit.NSViewLayerContentsRedrawOnSetNeedsDisplay, 1)
        self.assertEqual(AppKit.NSViewLayerContentsRedrawDuringViewResize, 2)
        self.assertEqual(AppKit.NSViewLayerContentsRedrawBeforeViewResize, 3)

        self.assertEqual(AppKit.NSViewLayerContentsPlacementScaleAxesIndependently, 0)
        self.assertEqual(AppKit.NSViewLayerContentsPlacementScaleProportionallyToFit, 1)
        self.assertEqual(
            AppKit.NSViewLayerContentsPlacementScaleProportionallyToFill, 2
        )
        self.assertEqual(AppKit.NSViewLayerContentsPlacementCenter, 3)
        self.assertEqual(AppKit.NSViewLayerContentsPlacementTop, 4)
        self.assertEqual(AppKit.NSViewLayerContentsPlacementTopRight, 5)
        self.assertEqual(AppKit.NSViewLayerContentsPlacementRight, 6)
        self.assertEqual(AppKit.NSViewLayerContentsPlacementBottomRight, 7)
        self.assertEqual(AppKit.NSViewLayerContentsPlacementBottom, 8)
        self.assertEqual(AppKit.NSViewLayerContentsPlacementBottomLeft, 9)
        self.assertEqual(AppKit.NSViewLayerContentsPlacementLeft, 10)
        self.assertEqual(AppKit.NSViewLayerContentsPlacementTopLeft, 11)

        self.assertIsInstance(AppKit.NSDefinitionPresentationTypeKey, str)
        self.assertIsInstance(AppKit.NSDefinitionPresentationTypeOverlay, str)
        self.assertIsInstance(
            AppKit.NSDefinitionPresentationTypeDictionaryApplication, str
        )

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertEqual(AppKit.NSViewLayerContentsRedrawCrossfade, 4)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSView.isDescendantOf_)
        self.assertResultIsBOOL(AppKit.NSView.isHidden)
        self.assertResultIsBOOL(AppKit.NSView.isHiddenOrHasHiddenAncestor)
        self.assertArgIsBOOL(AppKit.NSView.setHidden_, 0)
        self.assertResultIsBOOL(AppKit.NSView.needsToDrawRect_)
        self.assertResultIsBOOL(AppKit.NSView.wantsDefaultClipping)

        self.assertArgIsFunction(
            AppKit.NSView.sortSubviewsUsingFunction_context_, 0, b"i@@@", False
        )
        self.assertArgHasType(AppKit.NSView.sortSubviewsUsingFunction_context_, 1, b"@")

        self.assertResultIsBOOL(AppKit.NSView.postsFrameChangedNotifications)
        self.assertArgIsBOOL(AppKit.NSView.setPostsFrameChangedNotifications_, 0)
        self.assertResultIsBOOL(AppKit.NSView.autoresizesSubviews)
        self.assertArgIsBOOL(AppKit.NSView.setAutoresizesSubviews_, 0)
        self.assertResultIsBOOL(AppKit.NSView.isFlipped)
        self.assertResultIsBOOL(AppKit.NSView.isRotatedFromBase)
        self.assertResultIsBOOL(AppKit.NSView.isRotatedOrScaledFromBase)
        self.assertResultIsBOOL(AppKit.NSView.isOpaque)
        self.assertResultIsBOOL(AppKit.NSView.canDraw)
        self.assertArgIsBOOL(AppKit.NSView.setNeedsDisplay_, 0)
        self.assertResultIsBOOL(AppKit.NSView.needsDisplay)
        self.assertResultIsBOOL(AppKit.NSView.lockFocusIfCanDraw)
        self.assertResultIsBOOL(AppKit.NSView.lockFocusIfCanDrawInContext_)
        self.assertResultIsBOOL(AppKit.NSView.scrollRectToVisible_)
        self.assertResultIsBOOL(AppKit.NSView.autoscroll_)
        self.assertResultIsBOOL(AppKit.NSView.mouse_inRect_)
        self.assertResultIsBOOL(AppKit.NSView.performKeyEquivalent_)
        self.assertResultIsBOOL(AppKit.NSView.acceptsFirstMouse_)
        self.assertResultIsBOOL(AppKit.NSView.shouldDelayWindowOrderingForEvent_)
        self.assertResultIsBOOL(AppKit.NSView.needsPanelToBecomeKey)
        self.assertResultIsBOOL(AppKit.NSView.mouseDownCanMoveWindow)
        self.assertArgHasType(
            AppKit.NSView.addTrackingRect_owner_userData_assumeInside_, 2, b"^v"
        )
        self.assertArgIsBOOL(
            AppKit.NSView.addTrackingRect_owner_userData_assumeInside_, 3
        )
        self.assertResultIsBOOL(AppKit.NSView.shouldDrawColor)
        self.assertResultIsBOOL(AppKit.NSView.postsBoundsChangedNotifications)
        self.assertArgIsBOOL(AppKit.NSView.setPostsBoundsChangedNotifications_, 0)
        self.assertResultIsBOOL(AppKit.NSView.inLiveResize)
        self.assertResultIsBOOL(AppKit.NSView.preservesContentDuringLiveResize)

        self.assertArgHasType(
            AppKit.NSView.getRectsExposedDuringLiveResize_count_,
            0,
            b"o^" + AppKit.NSRect.__typestr__,
        )
        m = AppKit.NSView.getRectsExposedDuringLiveResize_count_.__metadata__()[
            "arguments"
        ][2]
        self.assertEqual(m["c_array_of_fixed_length"], 4)
        self.assertArgIsOut(AppKit.NSView.getRectsExposedDuringLiveResize_count_, 1)

        self.assertResultIsBOOL(AppKit.NSView.performMnemonic_)
        self.assertResultIsBOOL(AppKit.NSView.canBecomeKeyView)
        self.assertResultIsBOOL(AppKit.NSView.knowsPageRange_)
        self.assertArgIsOut(AppKit.NSView.adjustPageWidthNew_left_right_limit_, 0)
        self.assertArgIsOut(AppKit.NSView.adjustPageHeightNew_top_bottom_limit_, 0)

        self.assertArgIsBOOL(
            AppKit.NSView.dragImage_at_offset_event_pasteboard_source_slideBack_, 6
        )
        self.assertResultIsBOOL(AppKit.NSView.dragFile_fromRect_slideBack_event_)
        self.assertArgIsBOOL(AppKit.NSView.dragFile_fromRect_slideBack_event_, 2)
        self.assertResultIsBOOL(
            AppKit.NSView.dragPromisedFilesOfTypes_fromRect_source_slideBack_event_
        )
        self.assertArgIsBOOL(
            AppKit.NSView.dragPromisedFilesOfTypes_fromRect_source_slideBack_event_, 3
        )

    @min_os_level("10.5")
    def testMethods10_5(self):
        self.assertArgIsBOOL(AppKit.NSView.setWantsLayer_, 0)
        self.assertResultIsBOOL(AppKit.NSView.wantsLayer)
        self.assertResultIsBOOL(AppKit.NSView.enterFullScreenMode_withOptions_)
        self.assertResultIsBOOL(AppKit.NSView.isInFullScreenMode)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(AppKit.NSView.canDrawConcurrently)
        self.assertArgIsBOOL(AppKit.NSView.setCanDrawConcurrently_, 0)
        self.assertResultIsBOOL(AppKit.NSView.acceptsTouchEvents)
        self.assertArgIsBOOL(AppKit.NSView.setAcceptsTouchEvents_, 0)
        self.assertResultIsBOOL(AppKit.NSView.wantsRestingTouches)
        self.assertArgIsBOOL(AppKit.NSView.setWantsRestingTouches_, 0)

        self.assertArgHasType(
            AppKit.NSView.showDefinitionForAttributedString_atPoint_,
            1,
            AppKit.NSPoint.__typestr__,
        )

        self.assertArgHasType(
            AppKit.NSView.showDefinitionForAttributedString_range_options_baselineOriginProvider_,  # noqa: B950
            1,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgIsBlock(
            AppKit.NSView.showDefinitionForAttributedString_range_options_baselineOriginProvider_,  # noqa: B950
            3,
            AppKit.NSPoint.__typestr__ + AppKit.NSRange.__typestr__,
        )

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(AppKit.NSView.isDrawingFindIndicator)

        try:
            AppKit.NSView.layer_shouldInheritContentsScale_fromWindow_
        except AttributeError:
            pass
        else:
            self.assertResultIsBOOL(
                AppKit.NSView.layer_shouldInheritContentsScale_fromWindow_
            )

        self.assertResultIsBOOL(
            TestNSViewHelper.layer_shouldInheritContentsScale_fromWindow_
        )

    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertResultIsBOOL(AppKit.NSView.wantsUpdateLayer)

    @min_os_level("10.9")
    def testMethods10_9(self):
        self.assertResultIsBOOL(AppKit.NSView.canDrawSubviewsIntoLayer)
        self.assertArgIsBOOL(AppKit.NSView.setCanDrawSubviewsIntoLayer_, 0)
        self.assertResultIsBOOL(AppKit.NSView.layerUsesCoreImageFilters)
        self.assertArgIsBOOL(AppKit.NSView.setLayerUsesCoreImageFilters_, 0)
        self.assertResultIsBOOL(AppKit.NSView.isCompatibleWithResponsiveScrolling)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(AppKit.NSView.allowsVibrancy)

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBOOL(AppKit.NSView.wantsExtendedDynamicRangeOpenGLSurface)
        self.assertArgIsBOOL(
            AppKit.NSView.setWantsExtendedDynamicRangeOpenGLSurface_, 0
        )

    def testProtocol(self):
        self.assertArgHasType(
            TestNSViewHelper.view_stringForToolTip_point_userData_,
            2,
            AppKit.NSPoint.__typestr__,
        )
        self.assertArgHasType(
            TestNSViewHelper.view_stringForToolTip_point_userData_, 3, b"^v"
        )

    @min_sdk_level("10.14")
    def testProtocolObjects(self):
        objc.protocolNamed("NSViewLayerContentScaleDelegate")
        objc.protocolNamed("NSViewToolTipOwner")

    def testMissingTests(self):
        v = AppKit.NSView.alloc().init()
        v.setNeedsDisplayInRect_(((0, 0), (50, 50)))
        r = v.getRectsBeingDrawn_count_(None, None)
        self.assertIsInstance(r, tuple)
        self.assertEqual(len(r), 2)
        self.assertIsInstance(r[0], tuple)
        self.assertIsInstance(r[1], int)
        if r[1] != 0:
            self.assertIsInstance(r[0][0], AppKit.NSRect)
