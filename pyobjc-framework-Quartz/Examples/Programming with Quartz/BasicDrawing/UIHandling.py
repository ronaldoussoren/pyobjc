# ***    Drawing Basics ***

kHICommandSimpleRect		= 1000
kHICommandStrokedRect		= 1001
kHICommandStrokedAndFilledRect	= 1002   
kHICommandPathRects		= 1003
kHICommandAlphaRects		= 1004
kHICommandDashed		= 1005
kHICommandSimpleClip		= 1006
kHICommandPDFDoc		= 1007

# ***    Coordinate System ***
kHICommandRotatedEllipses	= 1008
kHICommandDrawSkewCoordinates	= 1082

# ***    Path Drawing ***
kHICommandBezierEgg	   	    = 1009
kHICommandRoundedRects	            = 1010
kHICommandStrokeWithCTM		    = 1011
kHICommandRotatedEllipsesWithCGPath = 1012
kHICommandPixelAligned		    = 1099

# ***    Color and GState ***
kHICommandDeviceFillAndStrokeColor  = 1013
kHICommandCLUTDrawGraphics	    = 1014
kHICommandDrawWithGlobalAlpha	    = 1015
kHICommandDrawWithBlendMode	    = 1068
kHICommandDrawWithColorRefs	    = 1016
kHICommandFunctionsHaveOwnGSave	    = 1017

# ***    Images ***
kHICommandDrawJPEGImage		    	= 1018
kHICommandColorImageFromFile		= 1019
kHICommandColorImageFromData		= 1020
kHICommandColorImageFromCallbacks	= 1021
kHICommandGrayRamp			= 1022
kHICommandDrawWithCGImageSource		= 1023
kHICommandDrawWithCGImageSourceIncremental = 1024
kHICommandDrawWithQuickTime		= 1025
kHICommandSubstituteImageProfile	= 1026
kHICommandDoSubImage			= 1027
kHICommandExportWithQuickTime		=  1028

# ***    Image Masking ***
kHICommandMaskTurkeyImage		= 1029
kHICommandImageMaskedWithMask		= 1030
kHICommandImageMaskedWithGrayImage	= 1031
kHICommandMaskImageWithColor		= 1033
kHICommandClipToMask			= 1080
kHICommandExportWithCGImageDestination	= 1034

# *** Bitmap Graphics Context and CGLayerRef ***
kHICommandSimpleCGLayer			= 1090
kHICommandAlphaOnlyContext		= 1091
kHICommandDrawNoOffScreenImage		= 1035
kHICommandDrawOffScreenImage		= 1036
kHICommandDrawWithLayer			= 1037

# ***    Text ***
kHICommandQuartzRomanText		= 1038
kHICommandQuartzTextModes		= 1039
kHICommandQuartzTextMatrix		= 1040

kHICommandDrawNSString			= 1041
kHICommandDrawNSLayoutMgr		= 1042
kHICommandDrawCustomNSLayoutMgr		= 1043

# ***    Advanced Drawing ***
kHICommandSimplePattern			= 1050
kHICommandPatternMatrix			= 1051
kHICommandPatternPhase			= 1052
kHICommandUncoloredPattern		= 1053
kHICommandDrawWithPDFPattern		= 1054

kHICommandSimpleShadow			= 1055
kHICommandShadowScaling			= 1056
kHICommandShadowProblems		= 1057
kHICommandComplexShadow			= 1058

kHICommandMultipleShapeComposite	= 1059
kHICommandFillAndStrokeWithShadow 	= 1085
kHICommandPDFDocumentShadow		= 1060

kHICommandSimpleAxialShading		= 1061
kHICommandExampleAxialShadings		= 1062
kHICommandSimpleRadialShading		= 1063
kHICommandExampleRadialShadings		= 1064
kHICommandEllipseShading		= 1065

# *** EPS drawing ***
kHICommandDoCompatibleEPS		= 1066
