from PyObjCTools import AppHelper

# Make sure all code is loaded
import AppDrawing
import BitmapContext
import ColorAndGState
import CoordinateSystem
import DataProvidersAndConsumers
import DrawingBasics
import EPSPrinting
import FrameworkTextDrawing
import FrameworkUtilities
import ImageMasking
import Images
import MyAppController
import MyView
import PDFHandling
import PathDrawing
import PatternDrawing
import QuartzTextDrawing
import Shadings
import ShadowsAndTransparencyLayers
import Utilities

import objc; objc.setVerbose(True)

AppHelper.runEventLoop()
