# Generated file, don't edit
# Source: BridgeSupport/QuartzCore.bridgesupport
# Last update: Sun Jul 24 21:38:05 2011

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
    "CATransform3D": objc.createStructType('CATransform3D', sel32or64(b'{CATransform3D="m11"f"m12"f"m13"f"m14"f"m21"f"m22"f"m23"f"m24"f"m31"f"m32"f"m33"f"m34"f"m41"f"m42"f"m43"f"m44"f}', b'{CATransform3D="m11"d"m12"d"m13"d"m14"d"m21"d"m22"d"m23"d"m24"d"m31"d"m32"d"m33"d"m34"d"m41"d"m42"d"m43"d"m44"d}'), None),
}
constants = '''$kCIOutputNativeSizeKey$kCAValueFunctionRotateX$kCAValueFunctionRotateY$kCAValueFunctionRotateZ$kCAValueFunctionScale$kCAValueFunctionScaleX$kCAValueFunctionScaleY$kCAValueFunctionScaleZ$kCAValueFunctionTranslate$kCAValueFunctionTranslateX$kCAValueFunctionTranslateY$kCAValueFunctionTranslateZ$kCATransactionAnimationTimingFunction$kCATransactionCompletionBlock$kCAMediaTimingFunctionDefault$kCAFillRuleNonZero$kCAFillRuleEvenOdd$kCALineJoinMiter$kCALineJoinRound$kCALineJoinRound$kCALineCapButt$kCALineCapRound$kCALineCapSquare$kCAFilterTrilinear$kCAGradientLayerAxial$kCAEmitterLayerPoint$kCAEmitterLayerLine$kCAEmitterLayerRectangle$kCAEmitterLayerCuboid$kCAEmitterLayerCircle$kCAEmitterLayerSphere$kCAEmitterLayerPoints$kCAEmitterLayerOutline$kCAEmitterLayerSurface$kCAEmitterLayerVolume$kCAEmitterLayerUnordered$kCAEmitterLayerOldestFirst$kCAEmitterLayerOldestLast$kCAEmitterLayerBackToFront$kCAEmitterLayerAdditive$kCAAlignmentCenter$kCAAlignmentJustified$kCAAlignmentLeft$kCAAlignmentNatural$kCAAlignmentRight$kCAAnimationDiscrete$kCAAnimationLinear$kCAAnimationPaced$kCAAnimationRotateAuto$kCAAnimationRotateAutoReverse$kCAFillModeBackwards$kCAFillModeBoth$kCAFillModeForwards$kCAFillModeFrozen$kCAFillModeRemoved$kCAFilterLinear$kCAFilterNearest$kCAGravityBottom$kCAGravityBottomLeft$kCAGravityBottomRight$kCAGravityCenter$kCAGravityLeft$kCAGravityResize$kCAGravityResizeAspect$kCAGravityResizeAspectFill$kCAGravityRight$kCAGravityTop$kCAGravityTopLeft$kCAGravityTopRight$kCAMediaTimingFunctionEaseIn$kCAMediaTimingFunctionEaseInEaseOut$kCAMediaTimingFunctionEaseOut$kCAMediaTimingFunctionLinear$kCAOnOrderIn$kCAOnOrderOut$kCAScrollBoth$kCAScrollHorizontally$kCAScrollNone$kCAScrollVertically$kCATransactionAnimationDuration$kCATransactionDisableActions$kCATransition$kCATransitionFade$kCATransitionFromBottom$kCATransitionFromLeft$kCATransitionFromRight$kCATransitionFromTop$kCATransitionMoveIn$kCATransitionPush$kCATransitionReveal$kCATruncationEnd$kCATruncationMiddle$kCATruncationNone$kCATruncationStart$kCIApplyOptionDefinition$kCIApplyOptionExtent$kCIApplyOptionUserInfo$kCIAttributeClass$kCIAttributeDefault$kCIAttributeDescription$kCIAttributeDisplayName$kCIAttributeFilterCategories$kCIAttributeFilterDisplayName$kCIAttributeFilterName$kCIAttributeIdentity$kCIAttributeMax$kCIAttributeMin$kCIAttributeName$kCIAttributeReferenceDocumentation$kCIAttributeSliderMax$kCIAttributeSliderMin$kCIAttributeType$kCIAttributeTypeAngle$kCIAttributeTypeBoolean$kCIAttributeTypeCount$kCIAttributeTypeDistance$kCIAttributeTypeGradient$kCIAttributeTypeInteger$kCIAttributeTypeOffset$kCIAttributeTypeOpaqueColor$kCIAttributeTypePosition$kCIAttributeTypePosition3$kCIAttributeTypeRectangle$kCIAttributeTypeScalar$kCIAttributeTypeTime$kCICategoryBlur$kCICategoryBuiltIn$kCICategoryColorAdjustment$kCICategoryColorEffect$kCICategoryCompositeOperation$kCICategoryDistortionEffect$kCICategoryFilterGenerator$kCICategoryGenerator$kCICategoryGeometryAdjustment$kCICategoryGradient$kCICategoryHalftoneEffect$kCICategoryHighDynamicRange$kCICategoryInterlaced$kCICategoryNonSquarePixels$kCICategoryReduction$kCICategorySharpen$kCICategoryStillImage$kCICategoryStylize$kCICategoryTileEffect$kCICategoryTransition$kCICategoryVideo$kCIContextOutputColorSpace$kCIContextUseSoftwareRenderer$kCIContextWorkingColorSpace$kCIFilterGeneratorExportedKey$kCIFilterGeneratorExportedKeyName$kCIFilterGeneratorExportedKeyTargetObject$kCIFormatARGB8@i$kCIFormatRGBA16@i$kCIFormatRGBAf@i$kCIImageColorSpace$kCIImageProviderTileSize$kCIImageProviderUserInfo$kCIInputAllowDraftModeKey$kCIInputAngleKey$kCIInputAspectRatioKey$kCIInputBackgroundImageKey$kCIInputBiasKey$kCIInputBoostKey$kCIInputBoostShadowAmountKey$kCIInputBrightnessKey$kCIInputCenterKey$kCIInputColorKey$kCIInputContrastKey$kCIInputDecoderVersionKey$kCIInputEVKey$kCIInputEnableChromaticNoiseTrackingKey$kCIInputEnableSharpeningKey$kCIInputExtentKey$kCIInputGradientImageKey$kCIInputIgnoreImageOrientationKey$kCIInputImageKey$kCIInputImageOrientationKey$kCIInputIntensityKey$kCIInputMaskImageKey$kCIInputNeutralChromaticityXKey$kCIInputNeutralChromaticityYKey$kCIInputNeutralLocationKey$kCIInputNeutralTemperatureKey$kCIInputNeutralTintKey$kCIInputRadiusKey$kCIInputRefractionKey$kCIInputSaturationKey$kCIInputScaleFactorKey$kCIInputScaleKey$kCIInputShadingImageKey$kCIInputSharpnessKey$kCIInputTargetImageKey$kCIInputTimeKey$kCIInputTransformKey$kCIInputWidthKey$kCIOutputImageKey$kCISamplerAffineMatrix$kCISamplerFilterLinear$kCISamplerFilterMode$kCISamplerFilterNearest$kCISamplerWrapBlack$kCISamplerWrapClamp$kCISamplerWrapMode$kCISupportedDecoderVersionsKey$kCIUIParameterSet$kCIUISetAdvanced$kCIUISetBasic$kCIUISetDevelopment$kCIUISetIntermediate$'''
constants_dict = {'CATransform3DIdentity': sel32or64('{CATransform3D=ffffffffffffffff}', '{CATransform3D=dddddddddddddddd}')}
enums = '''$CA_WARN_DEPRECATED@1$kCAConstraintHeight@7$kCAConstraintMaxX@2$kCAConstraintMaxY@6$kCAConstraintMidX@1$kCAConstraintMidY@5$kCAConstraintMinX@0$kCAConstraintMinY@4$kCAConstraintWidth@3$kCALayerBottomEdge@4$kCALayerHeightSizable@16$kCALayerLeftEdge@1$kCALayerMaxXMargin@4$kCALayerMaxYMargin@32$kCALayerMinXMargin@1$kCALayerMinYMargin@8$kCALayerNotSizable@0$kCALayerRightEdge@2$kCALayerTopEdge@8$kCALayerWidthSizable@2$'''
misc.update({'CGFLOAT_MAX': sel32or64(3.4028234663852886e+38, 1.7976931348623157e+308), 'CGFLOAT_MIN': sel32or64(1.1754943508222875e-38, 2.2250738585072014e-308)})
misc.update({})
functions = {'CATransform3DIsAffine': (sel32or64('B{CATransform3D=ffffffffffffffff}', 'B{CATransform3D=dddddddddddddddd}'),), 'CATransform3DInvert': (sel32or64('{CATransform3D=ffffffffffffffff}{CATransform3D=ffffffffffffffff}', '{CATransform3D=dddddddddddddddd}{CATransform3D=dddddddddddddddd}'),), 'CATransform3DIsIdentity': (sel32or64('B{CATransform3D=ffffffffffffffff}', 'B{CATransform3D=dddddddddddddddd}'),), 'CATransform3DMakeScale': (sel32or64('{CATransform3D=ffffffffffffffff}fff', '{CATransform3D=dddddddddddddddd}ddd'),), 'CATransform3DTranslate': (sel32or64('{CATransform3D=ffffffffffffffff}{CATransform3D=ffffffffffffffff}fff', '{CATransform3D=dddddddddddddddd}{CATransform3D=dddddddddddddddd}ddd'),), 'CATransform3DEqualToTransform': (sel32or64('B{CATransform3D=ffffffffffffffff}{CATransform3D=ffffffffffffffff}', 'B{CATransform3D=dddddddddddddddd}{CATransform3D=dddddddddddddddd}'),), 'CATransform3DRotate': (sel32or64('{CATransform3D=ffffffffffffffff}{CATransform3D=ffffffffffffffff}ffff', '{CATransform3D=dddddddddddddddd}{CATransform3D=dddddddddddddddd}dddd'),), 'CACurrentMediaTime': ('d',), 'CATransform3DMakeRotation': (sel32or64('{CATransform3D=ffffffffffffffff}ffff', '{CATransform3D=dddddddddddddddd}dddd'),), 'CATransform3DConcat': (sel32or64('{CATransform3D=ffffffffffffffff}{CATransform3D=ffffffffffffffff}{CATransform3D=ffffffffffffffff}', '{CATransform3D=dddddddddddddddd}{CATransform3D=dddddddddddddddd}{CATransform3D=dddddddddddddddd}'),), 'CATransform3DScale': (sel32or64('{CATransform3D=ffffffffffffffff}{CATransform3D=ffffffffffffffff}fff', '{CATransform3D=dddddddddddddddd}{CATransform3D=dddddddddddddddd}ddd'),), 'CATransform3DMakeTranslation': (sel32or64('{CATransform3D=ffffffffffffffff}fff', '{CATransform3D=dddddddddddddddd}ddd'),), 'CATransform3DGetAffineTransform': (sel32or64('{CGAffineTransform=ffffff}{CATransform3D=ffffffffffffffff}', '{CGAffineTransform=dddddd}{CATransform3D=dddddddddddddddd}'),), 'CATransform3DMakeAffineTransform': (sel32or64('{CATransform3D=ffffffffffffffff}{CGAffineTransform=ffffff}', '{CATransform3D=dddddddddddddddd}{CGAffineTransform=dddddd}'),)}
cftypes = []
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    pass
    r('CAEmitterCell', b'shouldArchiveValueForKey:', {'retval': {'type': b'Z'}})
    r('CAEmitterCell', b'isEnabled', {'retval': {'type': b'Z'}})
    r('CAEmitterCell', b'setEnabled:', {'arguments': {2: {'type': b'Z'}}})
    r('CAReplicatorLayer', b'preservesDepth', {'retval': {'type': b'Z'}})
    r('CAReplicatorLayer', b'setPreservesDepth:', {'arguments': {2: {'type': b'Z'}}})
    r('CAAnimation', b'shouldArchiveValueForKey:', {'retval': {'type': b'Z'}})
    r('CAAnimation', b'isRemovedOnCompletion', {'retval': {'type': b'Z'}})
    r('CAAnimation', b'setRemovedOnCompletion:', {'arguments': {2: {'type': b'Z'}}})
    r('CAEmitterLayer', b'preservesDepth', {'retval': {'type': b'Z'}})
    r('CAEmitterLayer', b'setPreservesDepth:', {'arguments': {2: {'type': b'Z'}}})
    r('CAPropertyAnimation', b'isAdditive', {'retval': {'type': b'Z'}})
    r('CAPropertyAnimation', b'setAdditive:', {'arguments': {2: {'type': b'Z'}}})
    r('CAPropertyAnimation', b'isCumulative', {'retval': {'type': b'Z'}})
    r('CAPropertyAnimation', b'setCumulative:', {'arguments': {2: {'type': b'Z'}}})
    r('CAKeyframeAnimation', b'path', {'retval': {'type': b'^{CGPath=}'}})
    r('CAKeyframeAnimation', b'setPath:', {'arguments': {2: {'type': b'^{CGPath=}'}}})
    r('CALayer', b'contentsAreFlipped', {'retval': {'type': b'Z'}})
    r('CALayer', b'needsDisplay', {'retval': {'type': b'Z'}})
    r('CALayer', b'needsLayout', {'retval': {'type': b'Z'}})
    r('CALayer', b'isGeometryFlipped', {'retval': {'type': b'Z'}})
    r('CALayer', b'setGeometryFlipped:', {'arguments': {2: {'type': b'Z'}}})
    r('CALayer', b'needsDisplayForKey:', {'retval': {'type': b'Z'}})
    r('CALayer', b'isHidden', {'retval': {'type': b'Z'}})
    r('CALayer', b'setHidden:', {'arguments': {2: {'type': b'Z'}}})
    r('CALayer', b'isDoubleSided', {'retval': {'type': b'Z'}})
    r('CALayer', b'setDoubleSided:', {'arguments': {2: {'type': b'Z'}}})
    r('CALayer', b'masksToBounds', {'retval': {'type': b'Z'}})
    r('CALayer', b'setMasksToBounds::', {'arguments': {2: {'type': b'Z'}}})
    r('CALayer', b'isOpaque', {'retval': {'type': b'Z'}})
    r('CALayer', b'setOpaque:', {'arguments': {2: {'type': b'Z'}}})
    r('CALayer', b'needsDisplayOnBoundsChange', {'retval': {'type': b'Z'}})
    r('CALayer', b'setNeedsDisplayOnBoundsChange:', {'arguments': {2: {'type': b'Z'}}})
    r('CALayer', b'backgroundColor', {'retval': {'type': b'^{CGColor=}'}})
    r('CALayer', b'borderColor', {'retval': {'type': b'^{CGColor=}'}})
    r('CALayer', b'containsPoint:', {'retval': {'type': b'Z'}})
    r('CALayer', b'drawInContext:', {'arguments': {2: {'type': b'^{CGContext=}'}}})
    r('CALayer', b'masksToBounds', {'retval': {'type': b'Z'}})
    r('CALayer', b'needsDisplayOnBoundsChange', {'retval': {'type': b'Z'}})
    r('CALayer', b'renderInContext:', {'arguments': {2: {'type': b'^{CGContext=}'}}})
    r('CALayer', b'setBackgroundColor:', {'arguments': {2: {'type': b'^{CGColor=}'}}})
    r('CALayer', b'setBorderColor:', {'arguments': {2: {'type': b'^{CGColor=}'}}})
    r('CALayer', b'setMasksToBounds:', {'arguments': {2: {'type': b'Z'}}})
    r('CALayer', b'setNeedsDisplayOnBoundsChange:', {'arguments': {2: {'type': b'Z'}}})
    r('CALayer', b'setShadowColor:', {'arguments': {2: {'type': b'^{CGColor=}'}}})
    r('CALayer', b'shadowColor', {'retval': {'type': b'^{CGColor=}'}})
    r('CALayer', b'shouldArchiveValueForKey:', {'retval': {'type': b'Z'}})
    r('CAOpenGLLayer', b'isAsynchronous', {'retval': {'type': b'Z'}})
    r('CAOpenGLLayer', b'setAsynchronous:', {'arguments': {2: {'type': b'Z'}}})
    r('CAOpenGLLayer', b'canDrawInCGLContext:pixelFormat:forLayerTime:displayTime:', {'retval': {'type': b'Z'}, 'arguments': {5: {'type_modifier': b'n'}}})
    r('CAOpenGLLayer', b'drawInCGLContext:pixelFormat:forLayerTime:displayTime:', {'arguments': {5: {'type_modifier': b'n'}}})
    r('CARenderer', b'beginFrameAtTime:timeStamp:', {'arguments': {3: {'type_modifier': b'n'}}})
    r('CARenderer', b'rendererWithCGLContext:options:', {'arguments': {2: {'type': b'^{_CGLContextObject=}'}}})
    r('CATransaction', b'disableActions', {'retval': {'type': b'Z'}})
    r('CATransaction', b'setDisableActions:', {'arguments': {2: {'type': b'Z'}}})
    r('CATransaction', b'completionBlock', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': '^v'}}}}})
    r('CATransaction', b'setCompletionBlock:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': '^v'}}}}}})
    r('CATextLayer', b'isWrapped', {'retval': {'type': b'Z'}})
    r('CATextLayer', b'setWrapped:', {'arguments': {2: {'type': b'Z'}}})
    r('CATextLayer', b'foregroundColor', {'retval': {'type': b'^{CGColor=}'}})
    r('CATextLayer', b'setForegroundColor:', {'arguments': {2: {'type': b'^{CGColor=}'}}})
    r('CIColor', b'colorSpace', {'retval': {'type': b'^{CGColorSpace=}'}})
    r('CIColor', b'colorWithCGColor:', {'arguments': {2: {'type': b'^{CGColor=}'}}})
    r('CIColor', b'components', {'retval': {'type': sel32or64(b'r^f', b'r^d'), 'c_array_of_variable_length': True}})
    r('CIColor', b'initWithCGColor:', {'arguments': {2: {'type': b'^{CGColor=}'}}})
    r('CIContext', b'contextWithCGContext:options:', {'arguments': {2: {'type': b'^{CGContext=}'}}})
    r('CIContext', b'contextWithCGLContext:pixelFormat:options:', {'arguments': {2: {'type': b'^{_CGLContextObject=}'}, 3: {'type': b'^{_CGLPixelFormatObject=}'}}})
    r('CIContext', b'createCGImage:fromRect:', {'retval': {'type': b'^{CGImage=}'}})
    r('CIContext', b'createCGImage:fromRect:format:colorSpace:', {'retval': {'type': b'^{CGImage=}'}, 'arguments': {5: {'type': b'^{CGColorSpace=}'}}})
    r('CIContext', b'createCGLayerWithSize:info:', {'retval': {'type': b'^{CGLayer=}'}, 'arguments': {3: {'type': b'^{__CFDictionary=}'}}})
    r('CIContext', b'render:toBitmap:rowBytes:bounds:format:colorSpace:', {'arguments': {3: {'type': b'^v', 'type_modifier': b'o', 'c_array_of_variable_length': True}, 7: {'type': b'^{CGColorSpace=}'}}})
    r('CIFilter', b'apply:', {'c_array_delimited_by_null': True, 'variadic': 'true'})
    r('CIFilter', b'filterWithName:keysAndValues:', {'c_array_delimited_by_null': True, 'variadic': 'true'})
    r('CIFilter', b'isEnabled', {'retval': {'type': b'Z'}})
    r('CIFilter', b'setEnabled:', {'arguments': {2: {'type': b'Z'}}})
    r('CIFilterGenerator', b'writeToURL:atomically:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type': b'Z'}}})
    r('CIFilterShape', b'transformBy:interior:', {'arguments': {3: {'type': b'Z'}}})
    r('CIImage', b'imageWithBitmapData:bytesPerRow:size:format:colorSpace:', {'arguments': {6: {'type': b'^{CGColorSpace=}'}}})
    r('CIImage', b'imageWithCGImage:', {'arguments': {2: {'type': b'^{CGImage=}'}}})
    r('CIImage', b'imageWithCGImage:options:', {'arguments': {2: {'type': b'^{CGImage=}'}}})
    r('CIImage', b'imageWithCGLayer:', {'arguments': {2: {'type': b'^{CGLayer=}'}}})
    r('CIImage', b'imageWithCGLayer:options:', {'arguments': {2: {'type': b'^{CGLayer=}'}}})
    r('CIImage', b'imageWithCVImageBuffer:', {'arguments': {2: {'type': b'^{__CVBuffer=}'}}})
    r('CIImage', b'imageWithCVImageBuffer:options:', {'arguments': {2: {'type': b'^{__CVBuffer=}'}}})
    r('CIImage', b'imageWithImageProvider:size:format:colorSpace:options:', {'arguments': {5: {'type': b'^{CGColorSpace=}'}}})
    r('CIImage', b'imageWithTexture:size:flipped:colorSpace:', {'arguments': {4: {'type': b'Z'}, 5: {'type': b'^{CGColorSpace=}'}}})
    r('CIImage', b'initWithBitmapData:bytesPerRow:size:format:colorSpace:', {'arguments': {6: {'type': b'^{CGColorSpace=}'}}})
    r('CIImage', b'initWithCGImage:', {'arguments': {2: {'type': b'^{CGImage=}'}}})
    r('CIImage', b'initWithCGImage:options:', {'arguments': {2: {'type': b'^{CGImage=}'}}})
    r('CIImage', b'initWithCGLayer:', {'arguments': {2: {'type': b'^{CGLayer=}'}}})
    r('CIImage', b'initWithCGLayer:options:', {'arguments': {2: {'type': b'^{CGLayer=}'}}})
    r('CIImage', b'initWithCVImageBuffer:', {'arguments': {2: {'type': b'^{__CVBuffer=}'}}})
    r('CIImage', b'initWithCVImageBuffer:options:', {'arguments': {2: {'type': b'^{__CVBuffer=}'}}})
    r('CIImage', b'initWithImageProvider:size:format:colorSpace:options:', {'arguments': {5: {'type': b'^{CGColorSpace=}'}}})
    r('CIImage', b'initWithTexture:size:flipped:colorSpace:', {'arguments': {4: {'type': b'Z'}, 5: {'type': b'^{CGColorSpace=}'}}})
    r('CIKernel', b'setROISelector:', {'arguments': {2: {'sel_of_type': sel32or64(b'{CGRect={CGPoint=ff}{CGSize=ff}}@:i{CGRect={CGPoint=ff}{CGSize=ff}}@', b'{CGRect={CGPoint=dd}{CGSize=dd}}@:i{CGRect={CGPoint=dd}{CGSize=dd}}@')}}})
    r('CIPlugIn', b'loadPlugIn:allowNonExecutable:', {'arguments': {3: {'type': b'Z'}}})
    r('CISampler', b'initWithImage:keysAndValues:', {'c_array_delimited_by_null': True, 'variadic': 'true'})
    r('CISampler', b'samplerWithImage:keysAndValues:', {'c_array_delimited_by_null': True, 'variadic': 'true'})
    r('CIVector', b'initWithValues:count:', {'arguments': {2: {'type': sel32or64(b'r^f', b'r^d'), 'type_modifier': b'n', 'c_array_length_in_arg': 3}}})
    r('CIVector', b'vectorWithValues:count:', {'arguments': {2: {'type': sel32or64(b'r^f', b'r^d'), 'type_modifier': b'n', 'c_array_length_in_arg': 3}}})
    r('NSObject', b'provideImageData:bytesPerRow:origin::size::userInfo:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'^v', 'type_modifier': b'o', 'c_array_of_variable_length': True}, 3: {'type': b'L'}, 4: {'type': b'L'}, 5: {'type': b'L'}, 6: {'type': b'L'}, 7: {'type': b'L'}, 8: {'type': b'@'}}})
    r('NSObject', b'autoreverses', {'retval': {'type': b'Z'}})
    r('NSObject', b'setAutoreverses:', {'arguments': {2: {'type': b'Z'}}})
    r('NSObject', b'animationDidStop:finished:', {'arguments': {3: {'type': b'Z'}}})
    r('NSObject', b'drawLayer:inContext:', {'arguments': {3: {'type': b'^{CGContext=}'}}})
    r('NSObject', b'load:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'^v'}}})
    r('NSObject', b'provideImageData:bytesPerRow:origin:size:userInfo:', {'arguments': {2: {'type': b'^v'}}})
finally:
    objc._updatingMetadata(False)
protocols={'CAAnimationDelegate': objc.informal_protocol('CAAnimationDelegate', [objc.selector(None, 'animationDidStart:', 'v@:@', isRequired=False), objc.selector(None, 'animationDidStop:finished:', 'v@:@Z', isRequired=False)]), 'CALayerDelegate': objc.informal_protocol('CALayerDelegate', [objc.selector(None, 'actionForLayer:forKey:', '@@:@@', isRequired=False), objc.selector(None, 'displayLayer:', 'v@:@', isRequired=False), objc.selector(None, 'drawLayer:inContext:', 'v@:@^{CGContext=}', isRequired=False)]), 'CIImageProvider': objc.informal_protocol('CIImageProvider', [objc.selector(None, 'provideImageData:bytesPerRow:origin:size:userInfo:', sel32or64('v@:^vLLL@', 'v@:^vQQQ@'), isRequired=False)]), 'CALayoutManager': objc.informal_protocol('CALayoutManager', [objc.selector(None, 'invalidateLayoutOfLayer:', 'v@:@', isRequired=False), objc.selector(None, 'layoutSublayersOfLayer:', 'v@:@', isRequired=False), objc.selector(None, 'preferredSizeOfLayer:', sel32or64('{CGSize=ff}@:@', '{CGSize=dd}@:@'), isRequired=False)])}
