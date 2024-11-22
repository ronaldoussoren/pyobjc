/*
 * Implements a function to fetch the list of objective-C classes known
 * in the runtime.
 */
#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

PyObject*
PyObjC_GetClassList(bool ignore_invalid_identifiers)
{
    PyObject* result    = NULL;
    Class*    buffer    = NULL;
    int       bufferLen = 0;
    int       neededLen = 0;
    int       i;

    /*
     * objc_getClassList returns the number of classes known in the runtime,
     * the documented way to fetch the list is:
     * 1. call ret = objc_getClassList(NULL, 0);
     * 2. allocate a buffer of 'ret' class-pointers
     * 3. call objc_getClassList again with this buffer.
     *
     * Step 3 might return more classes because another thread may have
     * loaded a new framework/bundle. This means we need a loop to be sure
     * we'll get all classes.
     */
    neededLen = objc_getClassList(NULL, 0);
    bufferLen = 0;
    buffer    = NULL;

    while (bufferLen < neededLen) {
        Class* newBuffer;
        bufferLen = neededLen;

        newBuffer = PyMem_Realloc(buffer, sizeof(Class) * bufferLen);
        if (newBuffer == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            PyErr_NoMemory();
            goto error;
            // LCOV_EXCL_STOP
        }

        buffer    = newBuffer;
        newBuffer = NULL;
        neededLen = objc_getClassList(buffer, bufferLen);
    }
    bufferLen = neededLen;

    result = PyList_New(0);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        goto error;       // LCOV_EXCL_LINE
    }

    for (i = 0; i < bufferLen; i++) {
        PyObject* pyclass;

        if (ignore_invalid_identifiers) {
            const char* name = class_getName(buffer[i]);


            if (strncmp(name, "__SwiftNative", 12) == 0) {
                /* FB12286520 */
                continue;
            }

            int skip = 0;
            while (*name != '\0') {
                if (!isalnum(*name) && *name != '_') {
                    skip = 1;
                    break;
                }
                name++;
            }
            if (skip) {
                continue;
            }

        }

#if PyObjC_BUILD_RELEASE > 1011
        /* Ancient compilers don't support @available, but
         * use @available for modern compilers to avoid
         * using this code block when it is not necessary.
         *
         * This block of code is only necessary when running
         * on macOS 10.12, 10.13 and 10.14. Both older and
         * newer versions don't have the bug this works around.
         *
         * Ignoring the entiry block when building on macOS 10.11
         * or earlier is fine, anyone deploying on multiple macOS
         * versions should build on the latest one (and preferably
         * use the "official" binary wheels).
         */
#if 0
        if (@available(macOS 10.15, *)) {
        } else  {
#else
        {
#endif
            /* A numbef of private(-ish) classes that cause
             * crashes when constructed here while running
             * on macOS 10.14
             */
            const char* name = class_getName(buffer[i]);
            bool skip = false;
            if (name[0] == 'Q' && name[1] == 'T') {
                static const char* IGNORE_NAMES[] = {
            	    "QTKeyedArchiverDelegate",
                    "QTMoviePlaybackController",
                    "QTHUDTimelineCell",
                    "QTHUDTimeline",
                    NULL
                };
                for (const char** cur = IGNORE_NAMES; *cur != NULL; cur++) {
                    if (strcmp(name, *cur) == 0) {
                        skip= true;
                        break;

                    }
                }
                if (skip) {
                    continue;
                }
            }

            /* The classes below are from a private framework (AnnotationKit), and at least some of them
             * cause a hard crash when they are looked at in the metadata sanity check.
             *
             * The obvious solution is to look at the bundle that defined the class, but using
             * +[NSBundle bundleForClass:] is enough to trigger class initialization and a crash.
             * Therefore look at a hardcoded list of class names.
             *
             * I have not tried to minimize the list.
             */
            if ((name[0] == 'A' && name[1] == 'K') || (name[0] == '_' && name[1] == 'A' && name[2] == 'K')) {
                static const char* IGNORE_NAMES[] = {
                    "AKAbsintheSigner",
                    "AKAccessibleContainerView",
                    "AKAccountManager",
                    "AKAccountRecoveryContext",
                    "AKActionController",
                    "AKAdornmentLayer",
                    "AKAlignedItem",
                    "AKAlignmentGuide",
                    "AKAlignmentGuideController",
                    "AKAlignmentGuideLineLayer",
                    "AKAlternateHandleLayer",
                    "AKAnisetteData",
                    "AKAnisetteProvisioningClientInterface",
                    "AKAnisetteProvisioningController",
                    "AKAnisetteProvisioningDaemonInterface",
                    "AKAnnotation",
                    "AKAnnotationEventHandler",
                    "AKAnnotationImageHelper",
                    "AKAnnotationLayer",
                    "AKAnnotationPointOfInterestHelper",
                    "AKAnnotationRenderer",
                    "AKAnnotationRendererUtilities",
                    "AKAnnotationTheme",
                    "AKAnnotationThemeBlue",
                    "AKAnnotationThemeGreen",
                    "AKAnnotationThemePink",
                    "AKAnnotationThemePurple",
                    "AKAnnotationThemeUnderline",
                    "AKAnnotationThemeYellow",
                    "AKAppleIDAuthenticationClientInterface",
                    "AKAppleIDAuthenticationContext",
                    "AKAppleIDAuthenticationController",
                    "AKAppleIDAuthenticationDaemonInterface",
                    "AKAppleIDAuthenticationInAppContext",
                    "AKAppleIDAuthenticationInAssistantContext",
                    "AKAppleIDAuthenticationMacOSExtenstionContext",
                    "AKAppleIDAuthenticationUISurrogateContext",
                    "AKAppleIDAuthenticationiCloudPrefPaneContext",
                    "AKAppleIDAuthenticationiCloudPrefPaneSecondFactorViewController",
                    "AKAppleIDAuthenticationiCloudPrefPaneViewController",
                    "AKAppleIDServerResourceLoadDelegate",
                    "AKAppleIDServerUIContextController",
                    "AKAppleIDServerUIDataHarvester",
                    "AKAppleIDSession",
                    "AKAppleIDSigningController",
                    "AKAppleIDSigningDaemonInterface",
                    "AKArrowAnnotation",
                    "AKArrowAnnotationEventHandler",
                    "AKArrowAnnotationRenderer",
                    "AKArrowShapeAnnotation",
                    "AKArrowShapeAnnotationEventHandler",
                    "AKArrowShapeAnnotationRenderer",
                    "AKArrowShapePointOfInterestHelper",
                    "AKAttestationSigner",
                    "AKAttributeController",
                    "AKAuthWebTabView",
                    "AKAuthenticationPromptController",
                    "AKAutoBugCapture",
                    "AKBaseSignInViewController",
                    "AKBezelFreeButtonCell_Mac",
                    "AKBezelFreeButton_Mac",
                    "AKBitmapFIFO",
                    "AKBorderMaskAnnotation",
                    "AKBorderMaskAnnotationRenderer",
                    "AKBorderMaskToolPointOfInterestHelper",
                    "AKBoxAdornmentLayer",
                    "AKBoxLayer",
                    "AKCDPFactory",
                    "AKCandidatePickerViewController",
                    "AKCardViewDataSource",
                    "AKCardViewDataSourceFactory",
                    "AKCardViewImageDataSource",
                    "AKCarrierBundlePhoneCertificate",
                    "AKCarrierBundleUtilities",
                    "AKCertificatePinning",
                    "AKCircleRequestContext",
                    "AKCircleRequestPayload",
                    "AKColorSwatchScrubberItemView",
                    "AKConfiguration",
                    "AKController",
                    "AKControllerForTesting",
                    "AKCropAdornmentLayer",
                    "AKCropAnnotation",
                    "AKCropAnnotationRenderer",
                    "AKCropToolPointOfInterestHelper",
                    "AKCursorController_Mac",
                    "AKDFRAnnotationPropertiesController",
                    "AKDFRColorPickerController",
                    "AKDFRController",
                    "AKDFRHighlightsController",
                    "AKDFRShapeController",
                    "AKDFRTextAttributesViewController",
                    "AKDFRTextColorController",
                    "AKDFRTextController",
                    "AKDateFormatter",
                    "AKDevice",
                    "AKDeviceInfo",
                    "AKDeviceListRequestContext",
                    "AKDoodleAnnotation",
                    "AKDoodleAnnotationEventHandler",
                    "AKDoodleAnnotationRenderer",
                    "AKELData",
                    "AKEightPointRectangularPointOfInterestHelper",
                    "AKEllipseLayer",
                    "AKFastLayerSnapshotHelper",
                    "AKFlexibleLinePointOfInterestHelper",
                    "AKFollowUpFactoryImpl",
                    "AKFollowUpProviderImpl",
                    "AKFollowUpServerPayloadFormatter",
                    "AKFollowUpTearDownContext",
                    "AKFontChooserUIItemDelegate",
                    "AKFormFeature",
                    "AKFormFeatureBox",
                    "AKFormFeatureCheckbox",
                    "AKFormFeatureDetector",
                    "AKFormFeatureDetectorController",
                    "AKFormFeatureLine",
                    "AKFormFeatureSegmented",
                    "AKFormTextBoxAnnotation",
                    "AKFourPointRectangularPointOfInterestHelper",
                    "AKGeneratedComplexCodeFormatter",
                    "AKGeometryHelper",
                    "AKGridView",
                    "AKGridViewBox",
                    "AKGridViewController",
                    "AKGridViewItem",
                    "AKHandleLayer",
                    "AKHeartAnnotation",
                    "AKHeartAnnotationEventHandler",
                    "AKHeartAnnotationRenderer",
                    "AKHighlightAnnotation",
                    "AKHighlightAnnotationController",
                    "AKHighlightAnnotationEventHandler",
                    "AKHighlightAnnotationRenderer",
                    "AKHighlightAppearanceHelper",
                    "AKHighlightAttributesViewController",
                    "AKHoverStateButton_Mac",
                    "AKICAWebKitViewController",
                    "AKIDPHandler",
                    "AKIDPProvidedSignInViewController",
                    "AKIDPProvidedSignInWindow",
                    "AKImageAnnotation",
                    "AKImageAnnotationEventHandler",
                    "AKImageAnnotationRenderer",
                    "AKInAssistantSecondFactorCodeEntry",
                    "AKInkAnnotation",
                    "AKInkAnnotationDrawingImageCache",
                    "AKInkAnnotationEventHandler",
                    "AKInkAnnotationRenderer",
                    "AKInkOverlayView",
                    "AKInkOverlayView_Mac",
                    "AKInkPageOverlayController",
                    "AKInkRendererHelper",
                    "AKInkSignatureView",
                    "AKInlineSignInViewController",
                    "AKInstantMessageAddressValueTransformer",
                    "AKKeepUsingController",
                    "AKLabelView",
                    "AKLabelViewCell",
                    "AKLabelViewCellItem",
                    "AKLayerPresentationManager",
                    "AKLegacyDoodleController",
                    "AKLegacyInlineSignInViewController",
                    "AKLightBackgroundImageCell_Mac",
                    "AKLineStyleMenuViewItem",
                    "AKLineStylesViewController_Mac",
                    "AKLongPressGestureRecognizer",
                    "AKLoupeAnnotation",
                    "AKLoupeAnnotationEventHandler",
                    "AKLoupeAnnotationImageUpdaterHelper",
                    "AKLoupeAnnotationRenderer",
                    "AKLoupePointOfInterestHelper",
                    "AKMainEventHandler",
                    "AKMainEventHandler_Mac",
                    "AKMasterToken",
                    "AKMaxLengthFormatter",
                    "AKMiniNoteLayer",
                    "AKMinimalColorChooserUserInterfaceItem",
                    "AKMinimalInkChooserUserInterfaceItem",
                    "AKMinimalTextColorUserInterfaceItem",
                    "AKMinimalUserInterfaceItem",
                    "AKModelController",
                    "AKMultiActionSegmentedControl",
                    "AKNativeAccountRecoveryController",
                    "AKNoCodeReceivedController",
                    "AKNoPointOfInterestHelper",
                    "AKNoteAnimationWindowController",
                    "AKNoteAnnotation",
                    "AKNoteAnnotationEventHandler",
                    "AKNoteAnnotationHelper",
                    "AKNoteAnnotationRenderer",
                    "AKNoteEditorController",
                    "AKNoteEditorWindowController",
                    "AKNoteMarginScrollView",
                    "AKNoteMarginScroller",
                    "AKNoteMarginTextView",
                    "AKNoteMarginView",
                    "AKNotePointOfInterestHelper",
                    "AKNoteStickyView",
                    "AKNoteWindow",
                    "AKOvalAnnotation",
                    "AKOvalAnnotationEventHandler",
                    "AKOvalAnnotationRenderer",
                    "AKOverlayView",
                    "AKPDFDocumentWrapper",
                    "AKPVSignaturePayload",
                    "AKPaddedTextFieldCell",
                    "AKPageController",
                    "AKPageControllerForTesting",
                    "AKPageModelController",
                    "AKPanGestureRecognizer",
                    "AKPinFieldBoxUIElement",
                    "AKPinFieldView",
                    "AKPolygonAdornmentLayer",
                    "AKPolygonAnnotation",
                    "AKPolygonAnnotationEventHandler",
                    "AKPolygonAnnotationRenderer",
                    "AKPolygonPointOfInterestHelper",
                    "AKPopoverActionForwarder_Mac",
                    "AKPopoverColorWell",
                    "AKPopoverStrokeColorWell",
                    "AKPopupAdornmentLayer",
                    "AKPopupAnnotation",
                    "AKPopupAnnotationEventHandler",
                    "AKPopupAnnotationRenderer",
                    "AKPotrace",
                    "AKRectAnnotation",
                    "AKRectAnnotationEventHandler",
                    "AKRectAnnotationRenderer",
                    "AKRectangularAnnotationEventHandler",
                    "AKRectangularPageSizedAnnotationEventHandler",
                    "AKRectangularShapeAnnotation",
                    "AKRemoteDevice",
                    "AKRotationGestureRecognizer",
                    "AKRoundLoginContainerView",
                    "AKSecondFactorCodeEntryController",
                    "AKSecureSerializationHelper",
                    "AKSegmentedCell",
                    "AKSegmentedCtrl",
                    "AKServerRequestConfiguration",
                    "AKShapeAnnotation",
                    "AKShapeDetectionController",
                    "AKShapeDetectionLogger",
                    "AKShapeToCHRecognitionResult",
                    "AKShapesGridViewController",
                    "AKShapesViewController",
                    "AKShortInlineSignInViewController",
                    "AKSignInPromptController",
                    "AKSignature",
                    "AKSignatureAnnotation",
                    "AKSignatureAnnotationEventHandler",
                    "AKSignatureAnnotationRenderer",
                    "AKSignatureBaselineView",
                    "AKSignatureCameraCaptureViewController_Mac",
                    "AKSignatureCaptureViewController_Mac",
                    "AKSignatureCaptureView_Mac",
                    "AKSignatureDecryptor_Mac",
                    "AKSignatureDetector",
                    "AKSignatureGestureCaptureViewController_Mac",
                    "AKSignatureModelController",
                    "AKSignatureOutputView_Mac",
                    "AKSignatureTableCellView_Mac",
                    "AKSignatureView",
                    "AKSignaturesTableRowView_Mac",
                    "AKSignaturesViewController_Mac",
                    "AKSketchServiceFakeButton",
                    "AKSmoothPathView",
                    "AKSmoothPathView_Mac",
                    "AKSocialProfileValueTransformer",
                    "AKSpeechBubbleAnnotation",
                    "AKSpeechBubbleAnnotationEventHandler",
                    "AKSpeechBubbleAnnotationRenderer",
                    "AKSpeechBubblePointOfInterestHelper",
                    "AKStarAnnotation",
                    "AKStarAnnotationEventHandler",
                    "AKStarAnnotationRenderer",
                    "AKStarShapePointOfInterestHelper",
                    "AKStatistics",
                    "AKStrokedAnnotation",
                    "AKTSDBezierPath",
                    "AKTSDBrushStroke",
                    "AKTSDLineEnd",
                    "AKTSDMutableBrushStroke",
                    "AKTSDPathCut",
                    "AKTSDPathIntersection",
                    "AKTSDShape",
                    "AKTableView",
                    "AKTapGestureRecognizer",
                    "AKTapToSignInViewController",
                    "AKTextAnnotationAttributeHelper",
                    "AKTextAnnotationRenderHelper",
                    "AKTextAttributesUIItemDelegate",
                    "AKTextAttributesViewController",
                    "AKTextBoxAnnotation",
                    "AKTextBoxAnnotationEventHandler",
                    "AKTextBoxAnnotationRenderer",
                    "AKTextEditorController",
                    "AKTextFieldAnnotation",
                    "AKTextFieldAnnotationEventHandler",
                    "AKTextLayoutManager",
                    "AKTextOverflowIndicatorLayer",
                    "AKTextView",
                    "AKThoughtBubbleAnnotation",
                    "AKThoughtBubbleAnnotationEventHandler",
                    "AKThoughtBubbleAnnotationRenderer",
                    "AKThoughtBubblePointOfInterestHelper",
                    "AKToken",
                    "AKTooManyAttemptsController",
                    "AKToolController",
                    "AKToolbarButtonItem_Mac",
                    "AKToolbarColorWellItem_Mac",
                    "AKToolbarHighlightControlItem_Mac",
                    "AKToolbarSeparatorItem_Mac",
                    "AKToolbarViewController",
                    "AKToolbarViewController_Mac",
                    "AKTouchBarController",
                    "AKTrackpadBackgroundView",
                    "AKTriangleAnnotation",
                    "AKTriangleAnnotationEventHandler",
                    "AKTriangleAnnotationRenderer",
                    "AKTrustedDeviceViewItem",
                    "AKTwoPointLinePointOfInterestHelper",
                    "AKTwoPointRectangularTextPointOfInterestHelper",
                    "AKURLBag",
                    "AKURLDataTask",
                    "AKURLRequestApprover",
                    "AKURLSession",
                    "AKUndoController",
                    "AKUserInterfaceItemHelper",
                    "AKUsernameFormatter",
                    "AKUtilities",
                    "AKVibrantSeparatorView_Mac",
                    "AKWebKitController",
                    "AKWebViewButtonBar",
                    "AKiCDPDeviceValidationFlowViewController",
                    "AKiCDPEnrollmentDeviceListViewController",
                    "AKiCDPEnrollmentDevicePasscodeViewController",
                    "AKiCDPRecoveryKeyViewController",
                    "AKiCDPValidationDevice",
                    "AKiCDPWaitForApprovalViewController",
                    "AKiCSCEntryView",
                    "_AKAnisetteProviderProxy",
                    "_AKAppleIDAuthenticationContextManager",
                    "_AKColorWellButtonCell",
                    "_AKInkOverlayDrawingUndoTarget",
                    NULL
                };
                for (const char** cur = IGNORE_NAMES; *cur != NULL; cur++) {
                    if (strcmp(name, *cur) == 0) {
                        skip= true;
                        break;

                    }
                }
                if (skip) {
                    continue;
                }
             }
        }
#endif /* PyObjC_BUILD_RELEASE > 1011 */
        pyclass = PyObjCClass_New(buffer[i]);
        if (pyclass == NULL) { // LCOV_BR_EXCL_LINE
            goto error;        // LCOV_EXCL_LINE
        }
        if (PyList_Append(result, pyclass) == -1) { // LCOV_BR_EXCL_LINE
            goto error;                             // LCOV_EXCL_LINE
        }
    }

    PyMem_Free(buffer);
    buffer = NULL;

    PyObject* tmp = PyList_AsTuple(result);
    Py_DECREF(result);

    return tmp;

error:
    // LCOV_EXCL_START
    if (buffer != NULL) {
        PyMem_Free(buffer);
    }
    Py_XDECREF(result);
    return NULL;
    // LCOV_EXCL_STOP
}

NS_ASSUME_NONNULL_END
