# Generated file, don't edit
# Source: BridgeSupport/ImageKit.bridgesupport
# Last update: Thu Jul 21 17:06:25 2011

import objc, sys

if sys.maxint > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
constants = '''$IKFilterBrowserDefaultInputImage$IKFilterBrowserExcludeCategories$IKFilterBrowserExcludeFilters$IKFilterBrowserFilterDoubleClickNotification$IKFilterBrowserFilterSelectedNotification$IKFilterBrowserShowCategories$IKFilterBrowserShowPreview$IKFilterBrowserWillPreviewFilterNotification$IKImageBrowserBackgroundColorKey$IKImageBrowserCGImageRepresentationType$IKImageBrowserCGImageSourceRepresentationType$IKImageBrowserCellsHighlightedTitleAttributesKey$IKImageBrowserCellsOutlineColorKey$IKImageBrowserCellsSubtitleAttributesKey$IKImageBrowserCellsTitleAttributesKey$IKImageBrowserGroupBackgroundColorKey$IKImageBrowserGroupRangeKey$IKImageBrowserGroupStyleKey$IKImageBrowserGroupTitleKey$IKImageBrowserIconRefPathRepresentationType$IKImageBrowserIconRefRepresentationType$IKImageBrowserNSBitmapImageRepresentationType$IKImageBrowserNSDataRepresentationType$IKImageBrowserNSImageRepresentationType$IKImageBrowserNSURLRepresentationType$IKImageBrowserPathRepresentationType$IKImageBrowserQCCompositionPathRepresentationType$IKImageBrowserQCCompositionRepresentationType$IKImageBrowserQTMoviePathRepresentationType$IKImageBrowserQTMovieRepresentationType$IKImageBrowserQuickLookPathRepresentationType$IKImageBrowserSelectionColorKey$IKOverlayTypeBackground$IKOverlayTypeImage$IKPictureTakerAllowsEditingKey$IKPictureTakerAllowsFileChoosingKey$IKPictureTakerAllowsVideoCaptureKey$IKPictureTakerCropAreaSizeKey$IKPictureTakerImageTransformsKey$IKPictureTakerInformationalTextKey$IKPictureTakerOutputImageMaxSizeKey$IKPictureTakerShowAddressBookPicture$IKPictureTakerShowAddressBookPictureKey$IKPictureTakerShowEffectsKey$IKPictureTakerShowEmptyPicture$IKPictureTakerRemainOpenAfterValidateKey$IKPictureTakerShowEmptyPictureKey$IKPictureTakerShowRecentPictureKey$IKPictureTakerUpdateRecentPictureKey$IKSlideshowModeImages$IKSlideshowModeOther$IKSlideshowModePDF$IKSlideshowPDFDisplayBox$IKSlideshowPDFDisplayMode$IKSlideshowPDFDisplaysAsBook$IKSlideshowStartIndex$IKSlideshowScreen$IKSlideshowAudioFile$IKSlideshowPDFDisplayBox$IKSlideshowPDFDisplayMode$IKSlideshowPDFDisplaysAsBook$IKSlideshowStartPaused$IKSlideshowWrapAround$IKToolModeAnnotate$IKToolModeCrop$IKToolModeMove$IKToolModeNone$IKToolModeRotate$IKToolModeSelect$IKToolModeSelectRect$IKToolModeSelectEllipse$IKToolModeSelectLasso$IKToolModeCrop$IKToolModeRotate$IKToolModeAnnotate$IKUIFlavorAllowFallback$IKUISizeFlavor$IKUISizeMini$IKUISizeRegular$IKUISizeSmall$IKUImaxSize$IK_iPhotoBundleIdentifier$IK_ApertureBundleIdentifier$IK_MailBundleIdentifier$IKImageBrowserCellBackgroundLayer$IKImageBrowserCellForegroundLayer$IKImageBrowserCellSelectionLayer$IKImageBrowserCellPlaceHolderLayer$IKImageBrowserPDFPageRepresentationType$IKImageBrowserGroupHeaderLayer$IKImageBrowserGroupFooterLayer$IKImageBrowserCellLayerTypeBackground$IKImageBrowserCellLayerTypeForeground$IKImageBrowserCellLayerTypeSelection$IKImageBrowserCellLayerTypePlaceHolder$'''
enums = '''$IKDeviceBrowserViewDisplayModeTable@0$IKDeviceBrowserViewDisplayModeOutline@1$IKDeviceBrowserViewDisplayModeIcon@2$IKScannerDeviceViewTransferModeFileBased@0$IKScannerDeviceViewTransferModeMemoryBased@1$IKScannerDeviceViewDisplayModeSimple@0$IKScannerDeviceViewDisplayModeAdvanced@1$IKImageBrowserDropOn@0$IKImageBrowserDropBefore@1$IKImageStateNoImage@0$IKImageStateInvalid@1$IKImageStateReady@2$IKCameraDeviceViewDisplayModeTable@0$IKCameraDeviceViewDisplayModeIcon@1$IKCameraDeviceViewTransferModeFileBased@0$IKCameraDeviceViewTransferModeMemoryBased@1$IKCellsStyleNone@0$IKCellsStyleOutlined@2$IKCellsStyleShadowed@1$IKCellsStyleSubtitled@8$IKCellsStyleTitled@4$IKGroupBezelStyle@0$IKGroupDisclosureStyle@1$'''
misc.update({'IKImagePickerShowEffectsKey': 'IKPictureTakerShowEffectsKey', 'IKImagePickerOutputImageMaxSizeKey': 'IKPictureTakerOutputImageMaxSizeKey', 'IKImagePickerImageTransformsKey': 'IKPictureTakerImageTransformsKey', 'IKImagePickerAllowsFileChoosingKey': 'IKPictureTakerAllowsFileChoosingKey', 'IKImagePickerAllowsEditingKey': 'IKPictureTakerAllowsEditingKey', 'IKImagePickerInformationalTextKey': 'IKPictureTakerInformationalTextKey', 'IKImagePickerCropAreaSizeKey': 'IKPictureTakerCropAreaSizeKey', 'IKImagePickerAllowsVideoCaptureKey': 'IKPictureTakerAllowsVideoCaptureKey', 'IKImagePickerUpdateRecentPictureKey': 'IKPictureTakerUpdateRecentPictureKey', 'IKImagePickerShowRecentPictureKey': 'IKPictureTakerShowRecentPictureKey'})
functions = {}
cftypes = []
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    pass
    r('IKDeviceBrowserView', b'hasDisplayModeSimple', {'retval': {'type': b'Z'}})
    r('IKDeviceBrowserView', b'setHasDisplayModeSimple:', {'arguments': {2: {'type': b'Z'}}})
    r('IKDeviceBrowserView', b'displaysLocalCameras', {'retval': {'type': b'Z'}})
    r('IKDeviceBrowserView', b'setDisplaysLocalCameras:', {'arguments': {2: {'type': b'Z'}}})
    r('IKDeviceBrowserView', b'displaysNetworkCameras', {'retval': {'type': b'Z'}})
    r('IKDeviceBrowserView', b'setDisplaysNetworkCameras:', {'arguments': {2: {'type': b'Z'}}})
    r('IKDeviceBrowserView', b'displaysLocalScanners', {'retval': {'type': b'Z'}})
    r('IKDeviceBrowserView', b'setDisplaysLocalScanners:', {'arguments': {2: {'type': b'Z'}}})
    r('IKDeviceBrowserView', b'displaysNetworkScanners', {'retval': {'type': b'Z'}})
    r('IKDeviceBrowserView', b'setDisplaysNetworkScanners:', {'arguments': {2: {'type': b'Z'}}})
    r('IKScannerDeviceView', b'hasDisplayModeSimple', {'retval': {'type': b'Z'}})
    r('IKScannerDeviceView', b'setHasDisplayModeSimple:', {'arguments': {2: {'type': b'Z'}}})
    r('IKScannerDeviceView', b'hasDisplayModeAdvanced', {'retval': {'type': b'Z'}})
    r('IKScannerDeviceView', b'setHasDisplayModeAdvanced:', {'arguments': {2: {'type': b'Z'}}})
    r('IKScannerDeviceView', b'displaysDownloadsDirectoryControl', {'retval': {'type': b'Z'}})
    r('IKScannerDeviceView', b'setDisplaysDownloadsDirectoryControl:', {'arguments': {2: {'type': b'Z'}}})
    r('IKScannerDeviceView', b'displaysPostProcessApplicationControl', {'retval': {'type': b'Z'}})
    r('IKScannerDeviceView', b'setDisplaysPostProcessApplicationControl:', {'arguments': {2: {'type': b'Z'}}})
    r('IKImageBrowserView', b'canControlQuickLookPanel', {'retval': {'type': b'Z'}})
    r('IKImageBrowserView', b'setCanControlQuickLookPanel:', {'arguments': {2: {'type': b'Z'}}})
    r('IKImageBrowserView', b'allowsDroppingOnItems', {'retval': {'type': b'Z'}})
    r('IKImageBrowserView', b'setAllowsDroppingOnItems:', {'arguments': {2: {'type': b'Z'}}})
    r('IKImageBrowserCell', b'isSelected', {'retval': {'type': b'Z'}})
    r('IKCameraDeviceView', b'hasDisplayModeTable', {'retval': {'type': b'Z'}})
    r('IKCameraDeviceView', b'setHasDisplayModeTable:', {'arguments': {2: {'type': b'Z'}}})
    r('IKCameraDeviceView', b'hasDisplayModeIcon', {'retval': {'type': b'Z'}})
    r('IKCameraDeviceView', b'setHasDisplayModeIcon:', {'arguments': {2: {'type': b'Z'}}})
    r('IKCameraDeviceView', b'displaysDownloadsDirectoryControl', {'retval': {'type': b'Z'}})
    r('IKCameraDeviceView', b'setDisplaysDownloadsDirectoryControl:', {'arguments': {2: {'type': b'Z'}}})
    r('IKCameraDeviceView', b'displaysPostProcessApplicationControl', {'retval': {'type': b'Z'}})
    r('IKCameraDeviceView', b'setDisplaysPostProcessApplicationControl:', {'arguments': {2: {'type': b'Z'}}})
    r('IKCameraDeviceView', b'canRotateSelectedItemsLeft', {'retval': {'type': b'Z'}})
    r('IKCameraDeviceView', b'setCanRotateSelectedItemsLeft:', {'arguments': {2: {'type': b'Z'}}})
    r('IKCameraDeviceView', b'canRotateSelectedItemsRight', {'retval': {'type': b'Z'}})
    r('IKCameraDeviceView', b'setCanRotateSelectedItemsRight:', {'arguments': {2: {'type': b'Z'}}})
    r('IKCameraDeviceView', b'canDeleteSelectedItems', {'retval': {'type': b'Z'}})
    r('IKCameraDeviceView', b'setCanDeleteSelectedItems:', {'arguments': {2: {'type': b'Z'}}})
    r('IKCameraDeviceView', b'selectIndexes:byExtendingSelection:', {'arguments': {3: {'type': b'Z'}}})
    r('IKFilterBrowserPanel', b'beginSheetWithOptions:modalForWindow:modalDelegate:didEndSelector:contextInfo:', {'arguments': {5: {'sel_of_type': b'v@:@i^v', 'type': b':'}, 6: {'type': b'^v'}}})
    r('IKFilterBrowserPanel', b'beginWithOptions:modelessDelegate:didEndSelector:contextInfo:', {'arguments': {4: {'sel_of_type': b'v@:@i^v', 'type': b':'}, 5: {'type': b'^v'}}})
    r('IKFilterBrowserView', b'setPreviewState:', {'arguments': {2: {'type': b'Z'}}})
    r('IKImageBrowserView', b'constrainsToOriginalSize', {'retval': {'type': b'Z'}})
    r('IKImageBrowserView', b'allowsEmptySelection', {'retval': {'type': b'Z'}})
    r('IKImageBrowserView', b'allowsMultipleSelection', {'retval': {'type': b'Z'}})
    r('IKImageBrowserView', b'allowsReordering', {'retval': {'type': b'Z'}})
    r('IKImageBrowserView', b'animates', {'retval': {'type': b'Z'}})
    r('IKImageBrowserView', b'isGroupExpandedAtIndex:', {'retval': {'type': b'Z'}})
    r('IKImageBrowserView', b'setAllowsEmptySelection:', {'arguments': {2: {'type': b'Z'}}})
    r('IKImageBrowserView', b'setAllowsMultipleSelection:', {'arguments': {2: {'type': b'Z'}}})
    r('IKImageBrowserView', b'setAllowsReordering:', {'arguments': {2: {'type': b'Z'}}})
    r('IKImageBrowserView', b'setAnimates:', {'arguments': {2: {'type': b'Z'}}})
    r('IKImageBrowserView', b'setConstrainsToOriginalSize:', {'arguments': {2: {'type': b'Z'}}})
    r('IKImageBrowserView', b'setSelectionIndexes:byExtendingSelection:', {'arguments': {3: {'type': b'Z'}}})
    r('IKImagePicker', b'beginImagePickerSheetForWindow:withDelegate:didEndSelector:contextInfo:', {'arguments': {4: {'sel_of_type': sel32or64(b'v@:@I^v', b'v@:@Q^v'), 'type': b':'}, 5: {'type': b'^v'}}})
    r('IKImagePicker', b'beginImagePickerWithDelegate:didEndSelector:contextInfo:', {'arguments': {3: {'sel_of_type': sel32or64(b'v@:@I^v', b'v@:@Q^v'), 'type': b':'}, 4: {'type': b'^v'}}})
    r('IKImageView', b'autohidesScrollers', {'retval': {'type': b'Z'}})
    r('IKImageView', b'autoresizes', {'retval': {'type': b'Z'}})
    r('IKImageView', b'doubleClickOpensImageEditPanel', {'retval': {'type': b'Z'}})
    r('IKImageView', b'editable', {'retval': {'type': b'Z'}})
    r('IKImageView', b'hasHorizontalScroller', {'retval': {'type': b'Z'}})
    r('IKImageView', b'hasVerticalScroller', {'retval': {'type': b'Z'}})
    r('IKImageView', b'image', {'retval': {'type': b'^{CGImage=}'}})
    r('IKImageView', b'setAutohidesScrollers:', {'arguments': {2: {'type': b'Z'}}})
    r('IKImageView', b'setAutoresizes:', {'arguments': {2: {'type': b'Z'}}})
    r('IKImageView', b'setDoubleClickOpensImageEditPanel:', {'arguments': {2: {'type': b'Z'}}})
    r('IKImageView', b'setEditable:', {'arguments': {2: {'type': b'Z'}}})
    r('IKImageView', b'setHasHorizontalScroller:', {'arguments': {2: {'type': b'Z'}}})
    r('IKImageView', b'setHasVerticalScroller:', {'arguments': {2: {'type': b'Z'}}})
    r('IKImageView', b'setImage:imageProperties:', {'arguments': {2: {'type': b'^{CGImage=}'}}})
    r('IKImageView', b'setSupportsDragAndDrop:', {'arguments': {2: {'type': b'Z'}}})
    r('IKImageView', b'supportsDragAndDrop', {'retval': {'type': b'Z'}})
    r('IKPictureTaker', b'beginPictureTakerSheetForWindow:withDelegate:didEndSelector:contextInfo:', {'arguments': {4: {'sel_of_type': sel32or64(b'v@:@i^v', b'v@:@q^v'), 'type': b':'}, 5: {'type': b'^v'}}})
    r('IKPictureTaker', b'beginPictureTakerWithDelegate:didEndSelector:contextInfo:', {'arguments': {3: {'sel_of_type': sel32or64(b'v@:@i^v', b'v@:@q^v'), 'type': b':'}, 4: {'type': b'^v'}}})
    r('IKPictureTaker', b'mirroring', {'retval': {'type': b'Z'}})
    r('IKPictureTaker', b'popUpRecentsMenuForView:withDelegate:didEndSelector:contextInfo:', {'arguments': {4: {'sel_of_type': sel32or64(b'v@:@i^v', b'v@:@q^v'), 'type': b':'}, 5: {'type': b'^v'}}})
    r('IKPictureTaker', b'setMirroring:', {'arguments': {2: {'type': b'Z'}}})
    r('IKSlideshow', b'canExportToApplication:', {'retval': {'type': b'Z'}})
    r('NSObject', b'hasAdjustMode', {'retval': {'type': b'Z'}})
    r('NSObject', b'hasEffectsMode', {'retval': {'type': b'Z'}})
    r('NSObject', b'hasDetailsMode', {'retval': {'type': b'Z'}})
    r('NSObject', b'saveOptions:shouldShowUTType:', {'retval': {'type': b'Z'}})
    r('NSObject', b'canExportSlideshowItemAtIndex:toApplication:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type': sel32or64(b'I', b'Q')}}})
    r('NSObject', b'image', {'retval': {'type': b'^{CGImage=}'}})
    r('NSObject', b'imageBrowser:moveCellsAtIndexes:toIndex:', {'retval': {'type': b'Z'}})
    r('NSObject', b'imageBrowser:moveItemsAtIndexes:toIndex:', {'retval': {'type': b'Z'}})
    r('NSObject', b'isSelectable', {'retval': {'type': b'Z'}})
    r('NSObject', b'setImage:imageProperties:', {'arguments': {2: {'type': b'^{CGImage=}'}}})
    r('NSObject', b'thumbnailWithMaximumSize:', {'retval': {'type': b'^{CGImage=}'}, 'arguments': {2: {'type': sel32or64(b'{_NSSize=ff}', b'{CGSize=dd}')}}})
    r('NSObject', b'slideshowItemAtIndex:', {'arguments': {2: {'type': sel32or64(b'I', b'Q')}}})
    r('NSObject', b'nameOfSlideshowItemAtIndex:', {'arguments': {2: {'type': sel32or64(b'I', b'Q')}}})
    r('NSObject', b'slideshowDidChangeCurrentIndex:', {'arguments': {2: {'type': sel32or64(b'I', b'Q')}}})
finally:
    objc._updatingMetadata(False)
protocols={'IKImageBrowserItem': objc.informal_protocol('IKImageBrowserItem', [objc.selector(None, 'imageRepresentation', '@@:', isRequired=False), objc.selector(None, 'imageRepresentationType', '@@:', isRequired=False), objc.selector(None, 'imageSubtitle', '@@:', isRequired=False), objc.selector(None, 'imageTitle', '@@:', isRequired=False), objc.selector(None, 'imageUID', '@@:', isRequired=False), objc.selector(None, 'imageVersion', sel32or64('I@:', 'Q@:'), isRequired=False), objc.selector(None, 'isSelectable', 'Z@:', isRequired=False)]), 'IKImageBrowserDataSourceDeprecated': objc.informal_protocol('IKImageBrowserDataSourceDeprecated', [objc.selector(None, 'imageBrowser:cellAtIndex:', sel32or64('@@:@I', '@@:@Q'), isRequired=False), objc.selector(None, 'imageBrowser:moveCellsAtIndexes:toIndex:', sel32or64('Z@:@@I', 'Z@:@@Q'), isRequired=False), objc.selector(None, 'imageBrowser:removeCellsAtIndexes:', 'v@:@@', isRequired=False), objc.selector(None, 'imageBrowser:writeCellsAtIndexes:toPasteboard:', 'v@:@@@', isRequired=False), objc.selector(None, 'numberOfCellsInImageBrowser:', sel32or64('I@:@', 'Q@:@'), isRequired=False)]), 'IKImageBrowserDelegate': objc.informal_protocol('IKImageBrowserDelegate', [objc.selector(None, 'imageBrowser:backgroundWasRightClickedWithEvent:', 'v@:@@', isRequired=False), objc.selector(None, 'imageBrowser:cellWasDoubleClickedAtIndex:', sel32or64('v@:@I', 'v@:@Q'), isRequired=False), objc.selector(None, 'imageBrowser:cellWasRightClickedAtIndex:withEvent:', sel32or64('v@:@I@', 'v@:@Q@'), isRequired=False), objc.selector(None, 'imageBrowserSelectionDidChange:', 'v@:@', isRequired=False)]), 'IKImageBrowserDataSource': objc.informal_protocol('IKImageBrowserDataSource', [objc.selector(None, 'imageBrowser:groupAtIndex:', sel32or64('@@:@I', '@@:@Q'), isRequired=False), objc.selector(None, 'imageBrowser:itemAtIndex:', sel32or64('@@:@I', '@@:@Q'), isRequired=False), objc.selector(None, 'imageBrowser:moveItemsAtIndexes:toIndex:', sel32or64('Z@:@@I', 'Z@:@@Q'), isRequired=False), objc.selector(None, 'imageBrowser:removeItemsAtIndexes:', 'v@:@@', isRequired=False), objc.selector(None, 'imageBrowser:writeItemsAtIndexes:toPasteboard:', sel32or64('I@:@@@', 'Q@:@@@'), isRequired=False), objc.selector(None, 'numberOfGroupsInImageBrowser:', sel32or64('I@:@', 'Q@:@'), isRequired=False), objc.selector(None, 'numberOfItemsInImageBrowser:', sel32or64('I@:@', 'Q@:@'), isRequired=False)])}
