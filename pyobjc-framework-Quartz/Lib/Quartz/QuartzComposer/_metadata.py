# This file is generated by objective.metadata
#
# Last update: Sun Aug  1 15:24:44 2021
#
# flake8: noqa

import objc, sys

if sys.maxsize > 2 ** 32:

    def sel32or64(a, b):
        return b


else:

    def sel32or64(a, b):
        return a


if objc.arch == "arm64":

    def selAorI(a, b):
        return a


else:

    def selAorI(a, b):
        return b


misc = {}
constants = """$QCCompositionAttributeBuiltInKey$QCCompositionAttributeCategoryKey$QCCompositionAttributeCopyrightKey$QCCompositionAttributeDescriptionKey$QCCompositionAttributeHasConsumersKey$QCCompositionAttributeIsTimeDependentKey$QCCompositionAttributeNameKey$QCCompositionCategoryDistortion$QCCompositionCategoryStylize$QCCompositionCategoryUtility$QCCompositionInputAudioPeakKey$QCCompositionInputAudioSpectrumKey$QCCompositionInputDestinationImageKey$QCCompositionInputImageKey$QCCompositionInputPaceKey$QCCompositionInputPreviewModeKey$QCCompositionInputPrimaryColorKey$QCCompositionInputRSSArticleDurationKey$QCCompositionInputRSSFeedURLKey$QCCompositionInputScreenImageKey$QCCompositionInputSecondaryColorKey$QCCompositionInputSourceImageKey$QCCompositionInputTrackInfoKey$QCCompositionInputTrackPositionKey$QCCompositionInputTrackSignalKey$QCCompositionInputXKey$QCCompositionInputYKey$QCCompositionOutputImageKey$QCCompositionOutputWebPageURLKey$QCCompositionPickerPanelDidSelectCompositionNotification$QCCompositionPickerViewDidSelectCompositionNotification$QCCompositionProtocolGraphicAnimation$QCCompositionProtocolGraphicTransition$QCCompositionProtocolImageFilter$QCCompositionProtocolMusicVisualizer$QCCompositionProtocolRSSVisualizer$QCCompositionProtocolScreenSaver$QCCompositionRepositoryDidUpdateNotification$QCPlugInAttributeCategoriesKey$QCPlugInAttributeCopyrightKey$QCPlugInAttributeDescriptionKey$QCPlugInAttributeExamplesKey$QCPlugInAttributeNameKey$QCPlugInExecutionArgumentEventKey$QCPlugInExecutionArgumentMouseLocationKey$QCPlugInPixelFormatARGB8$QCPlugInPixelFormatBGRA8$QCPlugInPixelFormatI8$QCPlugInPixelFormatIf$QCPlugInPixelFormatRGBAf$QCPortAttributeDefaultValueKey$QCPortAttributeMaximumValueKey$QCPortAttributeMenuItemsKey$QCPortAttributeMinimumValueKey$QCPortAttributeNameKey$QCPortAttributeTypeKey$QCPortTypeBoolean$QCPortTypeColor$QCPortTypeImage$QCPortTypeIndex$QCPortTypeNumber$QCPortTypeString$QCPortTypeStructure$QCRendererEventKey$QCRendererMouseLocationKey$QCViewDidStartRenderingNotification$QCViewDidStopRenderingNotification$"""
enums = """$kQCPlugInExecutionModeConsumer@3$kQCPlugInExecutionModeProcessor@2$kQCPlugInExecutionModeProvider@1$kQCPlugInTimeModeIdle@1$kQCPlugInTimeModeNone@0$kQCPlugInTimeModeTimeBase@2$"""
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"NSObject",
        b"CGLContextObj",
        {"required": True, "retval": {"type": b"^{_CGLContextObject=}"}},
    )
    r(b"NSObject", b"attributes", {"required": True, "retval": {"type": b"@"}})
    r(
        b"NSObject",
        b"bindTextureRepresentationToCGLContext:textureUnit:normalizeCoordinates:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"^{_CGLContextObject=}"},
                3: {"type": b"I"},
                4: {"type": b"Z"},
            },
        },
    )
    r(
        b"NSObject",
        b"bounds",
        {"required": True, "retval": {"type": b"{CGRect={CGPoint=dd}{CGSize=dd}}"}},
    )
    r(b"NSObject", b"bufferBaseAddress", {"required": True, "retval": {"type": b"^v"}})
    r(b"NSObject", b"bufferBytesPerRow", {"required": True, "retval": {"type": b"Q"}})
    r(
        b"NSObject",
        b"bufferColorSpace",
        {"required": True, "retval": {"type": b"^{CGColorSpace=}"}},
    )
    r(b"NSObject", b"bufferPixelFormat", {"required": True, "retval": {"type": b"@"}})
    r(b"NSObject", b"bufferPixelsHigh", {"required": True, "retval": {"type": b"Q"}})
    r(b"NSObject", b"bufferPixelsWide", {"required": True, "retval": {"type": b"Q"}})
    r(
        b"NSObject",
        b"canRenderWithCGLContext:",
        {
            "required": False,
            "retval": {"type": b"Z"},
            "arguments": {2: {"type": b"^{_CGLContextObject=}"}},
        },
    )
    r(
        b"NSObject",
        b"colorSpace",
        {"required": True, "retval": {"type": b"^{CGColorSpace=}"}},
    )
    r(
        b"NSObject",
        b"compositionParameterView:didChangeParameterWithKey:",
        {"retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"compositionParameterView:shouldDisplayParameterWithKey:attributes:",
        {
            "retval": {"type": b"Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"compositionPickerView:didSelectComposition:",
        {"retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"compositionPickerViewDidStartAnimating:",
        {"retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"compositionPickerViewWillStopAnimating:",
        {"retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(b"NSObject", b"compositionURL", {"required": True, "retval": {"type": b"@"}})
    r(
        b"NSObject",
        b"copyRenderedTextureForCGLContext:pixelFormat:bounds:isFlipped:",
        {
            "required": False,
            "retval": {"type": b"I"},
            "arguments": {
                2: {"type": b"^{_CGLContextObject=}"},
                3: {"type": b"@"},
                4: {"type": b"{CGRect={CGPoint=dd}{CGSize=dd}}"},
                5: {"type": b"^Z"},
            },
        },
    )
    r(
        b"NSObject",
        b"imageBounds",
        {"required": True, "retval": {"type": b"{CGRect={CGPoint=dd}{CGSize=dd}}"}},
    )
    r(
        b"NSObject",
        b"imageColorSpace",
        {"required": True, "retval": {"type": b"^{CGColorSpace=}"}},
    )
    r(b"NSObject", b"inputKeys", {"required": True, "retval": {"type": b"@"}})
    r(
        b"NSObject",
        b"lockBufferRepresentationWithPixelFormat:colorSpace:forBounds:",
        {
            "required": True,
            "retval": {"type": b"Z"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"^{CGColorSpace=}"},
                4: {"type": b"{CGRect={CGPoint=dd}{CGSize=dd}}"},
            },
        },
    )
    r(
        b"NSObject",
        b"lockTextureRepresentationWithColorSpace:forBounds:",
        {
            "required": True,
            "retval": {"type": b"Z"},
            "arguments": {
                2: {"type": b"^{CGColorSpace=}"},
                3: {"type": b"{CGRect={CGPoint=dd}{CGSize=dd}}"},
            },
        },
    )
    r(
        b"NSObject",
        b"logMessage:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}},
            "variadic": True,
        },
    )
    r(
        b"NSObject",
        b"outputImageProviderFromBufferWithPixelFormat:pixelsWide:pixelsHigh:baseAddress:bytesPerRow:releaseCallback:releaseContext:colorSpace:shouldColorMatch:",
        {
            "required": True,
            "retval": {"type": b"@"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"Q"},
                4: {"type": b"Q"},
                5: {"type": b"^v"},
                6: {"type": b"Q"},
                7: {"type": b"^?"},
                8: {"type": b"^v"},
                9: {"type": b"^{CGColorSpace=}"},
                10: {"type": b"Z"},
            },
        },
    )
    r(
        b"NSObject",
        b"outputImageProviderFromTextureWithPixelFormat:pixelsWide:pixelsHigh:name:flipped:releaseCallback:releaseContext:colorSpace:shouldColorMatch:",
        {
            "required": True,
            "retval": {"type": b"@"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"Q"},
                4: {"type": b"Q"},
                5: {"type": b"I"},
                6: {"type": b"Z"},
                7: {"type": b"^?"},
                8: {"type": b"^v"},
                9: {"type": b"^{CGColorSpace=}"},
                10: {"type": b"Z"},
            },
        },
    )
    r(b"NSObject", b"outputKeys", {"required": True, "retval": {"type": b"@"}})
    r(
        b"NSObject",
        b"propertyListFromInputValues",
        {"required": True, "retval": {"type": b"@"}},
    )
    r(
        b"NSObject",
        b"releaseRenderedTexture:forCGLContext:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"I"}, 3: {"type": b"^{_CGLContextObject=}"}},
        },
    )
    r(
        b"NSObject",
        b"renderToBuffer:withBytesPerRow:pixelFormat:forBounds:",
        {
            "required": False,
            "retval": {"type": b"Z"},
            "arguments": {
                2: {"type": b"^v"},
                3: {"type": b"Q"},
                4: {"type": b"@"},
                5: {"type": b"{CGRect={CGPoint=dd}{CGSize=dd}}"},
            },
        },
    )
    r(
        b"NSObject",
        b"renderWithCGLContext:forBounds:",
        {
            "required": False,
            "retval": {"type": b"Z"},
            "arguments": {
                2: {"type": b"^{_CGLContextObject=}"},
                3: {"type": b"{CGRect={CGPoint=dd}{CGSize=dd}}"},
            },
        },
    )
    r(
        b"NSObject",
        b"setInputValuesWithPropertyList:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"setValue:forInputKey:",
        {
            "required": True,
            "retval": {"type": b"Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(b"NSObject", b"shouldColorMatch", {"required": False, "retval": {"type": b"Z"}})
    r(
        b"NSObject",
        b"supportedBufferPixelFormats",
        {"required": False, "retval": {"type": b"@"}},
    )
    r(
        b"NSObject",
        b"supportedRenderedTexturePixelFormats",
        {"required": False, "retval": {"type": b"@"}},
    )
    r(
        b"NSObject",
        b"textureColorSpace",
        {"required": True, "retval": {"type": b"^{CGColorSpace=}"}},
    )
    r(b"NSObject", b"textureFlipped", {"required": True, "retval": {"type": b"Z"}})
    r(b"NSObject", b"textureMatrix", {"required": True, "retval": {"type": b"^f"}})
    r(b"NSObject", b"textureName", {"required": True, "retval": {"type": b"I"}})
    r(b"NSObject", b"texturePixelsHigh", {"required": True, "retval": {"type": b"Q"}})
    r(b"NSObject", b"texturePixelsWide", {"required": True, "retval": {"type": b"Q"}})
    r(b"NSObject", b"textureTarget", {"required": True, "retval": {"type": b"I"}})
    r(
        b"NSObject",
        b"unbindTextureRepresentationFromCGLContext:textureUnit:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"^{_CGLContextObject=}"}, 3: {"type": b"I"}},
        },
    )
    r(
        b"NSObject",
        b"unlockBufferRepresentation",
        {"required": True, "retval": {"type": b"v"}},
    )
    r(
        b"NSObject",
        b"unlockTextureRepresentation",
        {"required": True, "retval": {"type": b"v"}},
    )
    r(b"NSObject", b"userInfo", {"required": True, "retval": {"type": b"@"}})
    r(
        b"NSObject",
        b"valueForInputKey:",
        {"required": True, "retval": {"type": b"@"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"valueForOutputKey:",
        {"required": True, "retval": {"type": b"@"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"valueForOutputKey:ofType:",
        {
            "required": True,
            "retval": {"type": b"@"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(b"QCCompositionParameterView", b"drawsBackground", {"retval": {"type": b"Z"}})
    r(b"QCCompositionParameterView", b"hasParameters", {"retval": {"type": b"Z"}})
    r(
        b"QCCompositionParameterView",
        b"setDrawsBackground:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"QCCompositionPickerView", b"allowsEmptySelection", {"retval": {"type": b"Z"}})
    r(b"QCCompositionPickerView", b"drawsBackground", {"retval": {"type": b"Z"}})
    r(b"QCCompositionPickerView", b"isAnimating", {"retval": {"type": b"Z"}})
    r(
        b"QCCompositionPickerView",
        b"setAllowsEmptySelection:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"QCCompositionPickerView",
        b"setDrawsBackground:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"QCCompositionPickerView",
        b"setShowsCompositionNames:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"QCCompositionPickerView", b"showsCompositionNames", {"retval": {"type": b"Z"}})
    r(b"QCPlugIn", b"createViewController", {"retval": {"already_retained": True}})
    r(b"QCPlugIn", b"didValueForInputKeyChange:", {"retval": {"type": b"Z"}})
    r(b"QCPlugIn", b"execute:atTime:withArguments:", {"retval": {"type": b"Z"}})
    r(b"QCPlugIn", b"loadPlugInAtPath:", {"retval": {"type": b"Z"}})
    r(b"QCPlugIn", b"setValue:forOutputKey:", {"retval": {"type": b"Z"}})
    r(b"QCPlugIn", b"startExecution:", {"retval": {"type": b"Z"}})
    r(b"QCRenderer", b"renderAtTime:arguments:", {"retval": {"type": b"Z"}})
    r(b"QCView", b"autostartsRendering", {"retval": {"type": b"Z"}})
    r(b"QCView", b"isPausedRendering", {"retval": {"type": b"Z"}})
    r(b"QCView", b"isRendering", {"retval": {"type": b"Z"}})
    r(b"QCView", b"loadComposition:", {"retval": {"type": b"Z"}})
    r(b"QCView", b"loadCompositionFromFile:", {"retval": {"type": b"Z"}})
    r(b"QCView", b"renderAtTime:arguments:", {"retval": {"type": b"Z"}})
    r(b"QCView", b"setAutostartsRendering:", {"arguments": {2: {"type": b"Z"}}})
    r(b"QCView", b"startRendering", {"retval": {"type": b"Z"}})
    r(
        b"null",
        b"compositionParameterView:shouldDisplayParameterWithKey:attributes:",
        {"retval": {"type": b"Z"}},
    )
    r(b"null", b"didValueForInputKeyChange:", {"retval": {"type": b"Z"}})
    r(b"null", b"loadPlugInAtPath:", {"retval": {"type": b"Z"}})
    r(b"null", b"setValue:forOutputKey:", {"retval": {"type": b"Z"}})
finally:
    objc._updatingMetadata(False)
protocols = {
    "QCCompositionPickerViewDelegate": objc.informal_protocol(
        "QCCompositionPickerViewDelegate",
        [
            objc.selector(
                None,
                b"compositionPickerView:didSelectComposition:",
                b"v@:@@",
                isRequired=False,
            ),
            objc.selector(
                None,
                b"compositionPickerViewWillStopAnimating:",
                b"v@:@",
                isRequired=False,
            ),
            objc.selector(
                None,
                b"compositionPickerViewDidStartAnimating:",
                b"v@:@",
                isRequired=False,
            ),
        ],
    ),
    "QCCompositionParameterViewDelegate": objc.informal_protocol(
        "QCCompositionParameterViewDelegate",
        [
            objc.selector(
                None,
                b"compositionParameterView:didChangeParameterWithKey:",
                b"v@:@@",
                isRequired=False,
            ),
            objc.selector(
                None,
                b"compositionParameterView:shouldDisplayParameterWithKey:attributes:",
                b"Z@:@@@",
                isRequired=False,
            ),
        ],
    ),
}
expressions = {}

# END OF FILE
