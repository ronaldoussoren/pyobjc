# Generated file, don't edit
# Source: BridgeSupport/QuartzComposer.bridgesupport
# Last update: Thu Jul 21 17:06:26 2011

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
constants = '''$QCCompositionInputMeshKey$QCCompositionAttributeBuiltInKey$QCCompositionAttributeCategoryKey$QCCompositionAttributeCopyrightKey$QCCompositionAttributeDescriptionKey$QCCompositionAttributeHasConsumersKey$QCCompositionAttributeIsTimeDependentKey$QCCompositionAttributeNameKey$QCCompositionCategoryDistortion$QCCompositionCategoryStylize$QCCompositionCategoryUtility$QCCompositionInputAudioPeakKey$QCCompositionInputAudioSpectrumKey$QCCompositionInputDestinationImageKey$QCCompositionInputImageKey$QCCompositionInputPaceKey$QCCompositionInputPreviewModeKey$QCCompositionInputPrimaryColorKey$QCCompositionInputRSSArticleDurationKey$QCCompositionInputRSSFeedURLKey$QCCompositionInputScreenImageKey$QCCompositionInputSecondaryColorKey$QCCompositionInputSourceImageKey$QCCompositionInputTrackInfoKey$QCCompositionInputTrackPositionKey$QCCompositionInputTrackSignalKey$QCCompositionInputXKey$QCCompositionInputYKey$QCCompositionOutputImageKey$QCCompositionOutputWebPageURLKey$QCCompositionPickerPanelDidSelectCompositionNotification$QCCompositionPickerViewDidSelectCompositionNotification$QCCompositionProtocolGraphicAnimation$QCCompositionProtocolGraphicTransition$QCCompositionProtocolImageFilter$QCCompositionProtocolMusicVisualizer$QCCompositionProtocolRSSVisualizer$QCCompositionProtocolScreenSaver$QCCompositionRepositoryDidUpdateNotification$QCPlugInAttributeCopyrightKey$QCPlugInAttributeDescriptionKey$QCPlugInAttributeNameKey$QCPlugInExecutionArgumentEventKey$QCPlugInExecutionArgumentMouseLocationKey$QCPlugInPixelFormatARGB8$QCPlugInPixelFormatBGRA8$QCPlugInPixelFormatI8$QCPlugInPixelFormatIf$QCPlugInPixelFormatRGBAf$QCPortAttributeDefaultValueKey$QCPortAttributeMaximumValueKey$QCPortAttributeMenuItemsKey$QCPortAttributeMinimumValueKey$QCPortAttributeNameKey$QCPortAttributeTypeKey$QCPortTypeBoolean$QCPortTypeColor$QCPortTypeImage$QCPortTypeIndex$QCPortTypeNumber$QCPortTypeString$QCPortTypeStructure$QCRendererEventKey$QCRendererMouseLocationKey$QCViewDidStartRenderingNotification$QCViewDidStopRenderingNotification$'''
enums = '''$kQCPlugInExecutionModeConsumer@3$kQCPlugInExecutionModeProcessor@2$kQCPlugInExecutionModeProvider@1$kQCPlugInTimeModeIdle@1$kQCPlugInTimeModeNone@0$kQCPlugInTimeModeTimeBase@2$'''
misc.update({})
functions = {}
cftypes = []
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    pass
    r('NSObject', b'CGLContextObj', {'retval': {'type': b'^{_CGLContextObject=}'}})
    r('NSObject', b'bindTextureRepresentationToCGLContext:textureUnit:normalizeCoordinates:', {'arguments': {2: {'type': b'^{_CGLContextObject=}'}, 4: {'type': b'Z'}}})
    r('NSObject', b'bufferBaseAddress', {'retval': {'type': b'^v'}})
    r('NSObject', b'bufferColorSpace', {'retval': {'type': b'^{CGColorSpace=}'}})
    r('NSObject', b'canRenderWithCGLContext:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'^{_CGLContextObject=}'}}})
    r('NSObject', b'colorSpace', {'retval': {'type': b'^{CGColorSpace=}'}})
    r('NSObject', b'compositionParameterView:shouldDisplayParameterWithKey:attributes:', {'retval': {'type': b'Z'}})
    r('NSObject', b'copyRenderedTextureForCGLContext:pixelFormat:bounds:isFlipped:', {'arguments': {2: {'type': b'^{_CGLContextObject=}'}, 5: {'type': b'^Z'}}})
    r('NSObject', b'imageColorSpace', {'retval': {'type': b'^{CGColorSpace=}'}})
    r('NSObject', b'imageColorSpace', {'retval': {'type': b'^{CGColorSpace=}'}})
    r('NSObject', b'lockBufferRepresentationWithPixelFormat:colorSpace:forBounds:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type': b'^{CGColorSpace=}'}}})
    r('NSObject', b'lockTextureRepresentationWithColorSpace:forBounds:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'^{CGColorSpace=}'}}})
    r('NSObject', b'logMessage:', {'arguments': {2: {'printf_format': True}}, 'variadic': 'true'})
    r('NSObject', b'outputImageProviderFromBufferWithPixelFormat:pixelsWide:pixelsHigh:baseAddress:bytesPerRow:releaseCallback:releaseContext:colorSpace:shouldColorMatch:', {'arguments': {8: {'type': b'^v'}, 9: {'type': b'^{CGColorSpace=}'}, 10: {'type': b'Z'}, 5: {'type': b'^v'}, 7: {'type': b'^?'}}})
    r('NSObject', b'outputImageProviderFromTextureWithPixelFormat:pixelsWide:pixelsHigh:name:flipped:releaseCallback:releaseContext:colorSpace:shouldColorMatch:', {'arguments': {8: {'type': b'^v'}, 9: {'type': b'^{CGColorSpace=}'}, 10: {'type': b'Z'}, 6: {'type': b'Z'}, 7: {'type': b'^?'}}})
    r('NSObject', b'releaseRenderedTexture:forCGLContext:', {'arguments': {3: {'type': b'^{_CGLContextObject=}'}}})
    r('NSObject', b'renderToBuffer:withBytesPerRow:pixelFormat:forBounds:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'^v'}}})
    r('NSObject', b'renderWithCGLContext:forBounds:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'^{_CGLContextObject=}'}}})
    r('NSObject', b'setValue:forInputKey:', {'retval': {'type': b'Z'}})
    r('NSObject', b'shouldColorMatch', {'retval': {'type': b'Z'}})
    r('NSObject', b'shouldColorMatch', {'retval': {'type': b'Z'}})
    r('NSObject', b'textureColorSpace', {'retval': {'type': b'^{CGColorSpace=}'}})
    r('NSObject', b'textureFlipped', {'retval': {'type': b'Z'}})
    r('NSObject', b'textureMatrix', {'retval': {'type': b'^f'}})
    r('NSObject', b'unbindTextureRepresentationFromCGLContext:textureUnit:', {'arguments': {2: {'type': b'^{_CGLContextObject=}'}}})
    r('QCCompositionParameterView', b'drawsBackground', {'retval': {'type': b'Z'}})
    r('QCCompositionParameterView', b'hasParameters', {'retval': {'type': b'Z'}})
    r('QCCompositionParameterView', b'setDrawsBackground:', {'arguments': {2: {'type': b'Z'}}})
    r('QCCompositionPickerView', b'allowsEmptySelection', {'retval': {'type': b'Z'}})
    r('QCCompositionPickerView', b'drawsBackground', {'retval': {'type': b'Z'}})
    r('QCCompositionPickerView', b'isAnimating', {'retval': {'type': b'Z'}})
    r('QCCompositionPickerView', b'setAllowsEmptySelection:', {'arguments': {2: {'type': b'Z'}}})
    r('QCCompositionPickerView', b'setDrawsBackground:', {'arguments': {2: {'type': b'Z'}}})
    r('QCCompositionPickerView', b'setShowsCompositionNames:', {'arguments': {2: {'type': b'Z'}}})
    r('QCCompositionPickerView', b'showsCompositionNames', {'retval': {'type': b'Z'}})
    r('QCPlugIn', b'didValueForInputKeyChange:', {'retval': {'type': b'Z'}})
    r('QCPlugIn', b'execute:atTime:withArguments:', {'retval': {'type': b'Z'}})
    r('QCPlugIn', b'loadPlugInAtPath:', {'retval': {'type': b'Z'}})
    r('QCPlugIn', b'setValue:forOutputKey:', {'retval': {'type': b'Z'}})
    r('QCPlugIn', b'startExecution:', {'retval': {'type': b'Z'}})
    r('QCRenderer', b'initOffScreenWithSize:colorSpace:composition:', {'arguments': {3: {'type': b'^{CGColorSpace=}'}}})
    r('QCRenderer', b'initWithCGLContext:pixelFormat:colorSpace:composition:', {'arguments': {2: {'type': b'^{_CGLContextObject=}'}, 3: {'type': b'^{_CGLPixelFormatObject=}'}, 4: {'type': b'^{CGColorSpace=}'}}})
    r('QCRenderer', b'initWithComposition:colorSpace:', {'arguments': {3: {'type': b'^{CGColorSpace=}'}}})
    r('QCRenderer', b'renderAtTime:arguments:', {'retval': {'type': b'Z'}})
    r('QCView', b'autostartsRendering', {'retval': {'type': b'Z'}})
    r('QCView', b'isPausedRendering', {'retval': {'type': b'Z'}})
    r('QCView', b'isRendering', {'retval': {'type': b'Z'}})
    r('QCView', b'loadComposition:', {'retval': {'type': b'Z'}})
    r('QCView', b'loadCompositionFromFile:', {'retval': {'type': b'Z'}})
    r('QCView', b'renderAtTime:arguments:', {'retval': {'type': b'Z'}})
    r('QCView', b'setAutostartsRendering:', {'arguments': {2: {'type': b'Z'}}})
    r('QCView', b'startRendering', {'retval': {'type': b'Z'}})
finally:
    objc._updatingMetadata(False)
protocols={'QCCompositionPickerViewDelegate': objc.informal_protocol('QCCompositionPickerViewDelegate', [objc.selector(None, 'compositionPickerView:didSelectComposition:', 'v@:@@', isRequired=False), objc.selector(None, 'compositionPickerViewDidStartAnimating:', 'v@:@', isRequired=False), objc.selector(None, 'compositionPickerViewWillStopAnimating:', 'v@:@', isRequired=False)]), 'QCCompositionParameterViewDelegate': objc.informal_protocol('QCCompositionParameterViewDelegate', [objc.selector(None, 'compositionParameterView:didChangeParameterWithKey:', 'v@:@@', isRequired=False), objc.selector(None, 'compositionParameterView:shouldDisplayParameterWithKey:attributes:', 'Z@:@@@', isRequired=False)])}
