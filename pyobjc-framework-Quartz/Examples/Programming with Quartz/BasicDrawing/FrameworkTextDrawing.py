from Quartz import *
from Cocoa import *
import Utilities
import QuartzTextDrawing

import sys
import objc

def getTextString():
    # These unicode values are the characters: Q, u, a, r, t, z, 
    # eighthnote, floral heart, black chess queen, and two CJK characters.
    # Note: Create an NSString, because we'll use NSString-specific API's, otherwise
    # we could just have used a python unicode object
    return NSString.stringWithString_(u'\u0051\u0075\u0061\u0072\u0074\u007A\u266A\u2766\u265B\u3042\u304E')

doPointDrawing=1

def drawNSStringWithAttributes():
    textString = getTextString()
    if doPointDrawing:
        context = NSGraphicsContext.currentContext().graphicsPort()
    
    # Text Line 1. Draw with default attributes.
    p = NSMakePoint(20.0, 400.0)
        
    # Draw text with default text attributes. The point supplied is
    # not the text baseline but rather the lower-left corner of the box 
    # which bounds the text.
    textString.drawAtPoint_withAttributes_(p, None)

    if doPointDrawing:
        Utilities.drawPoint(context, p)

    # Text Line 2. Draw with a specific font and color.
    
    # Position the text 50 units below the previous text.
    p.y -= 50

    # Set attributes to use when drawing the string.
    stringAttributes = {
        # Use the font with the PostScript name "Times-Roman" at 40 point.
        NSFontAttributeName: NSFont.fontWithName_size_("Times-Roman", 40),

        # Set the color attribute to an opaque red.
        NSForegroundColorAttributeName: NSColor.colorWithCalibratedRed_green_blue_alpha_(0.663, 0, 0.031, 1.0)
    }

    # Draw the text.
    textString.drawAtPoint_withAttributes_(p, stringAttributes)

    if doPointDrawing:
        Utilities.drawPoint(context, p)

    # Text Line 3. Draw stroked text.
    
    # Position the text 50 units below the previous text.
    p.y -= 50

    # Panther and later support stroke attributes. A positive value 
    # of the stroke width attribute produces text that is stroked rather
    # than filled.
    stringAttributes[NSStrokeWidthAttributeName] = 3.0
    textString.drawAtPoint_withAttributes_(p, stringAttributes)

    if doPointDrawing:
        Utilities.drawPoint(context, p)

    # Text Line 4. Draw with fill and stroke.
    
    p.y -= 50

    # Panther and later support stroke attributes. A negative value 
    # of the stroke width attribute results in text that is both filled
    # and stroked.
    stringAttributes[NSStrokeWidthAttributeName] = -3.0
    # Set the stroke color attribute to black.
    stringAttributes[NSStrokeColorAttributeName] = NSColor.colorWithCalibratedRed_green_blue_alpha_(0, 0, 0, 1.0)
	
    textString.drawAtPoint_withAttributes_(p, stringAttributes)

    if doPointDrawing:
        Utilities.drawPoint(context, p)

    # Text Line 5. Draw at baseline.
    # Tiger and later support the drawWithRect method which allows 
    # string text drawing from a point on the text baseline. 
    p.y -= 50
    rect = NSRect(
            origin=p,
            size=NSSize(0,0),
        )
    textString.drawWithRect_options_attributes_(
            rect, NSStringDrawingDisableScreenFontSubstitution,
            stringAttributes)

    if doPointDrawing:
        Utilities.drawPoint(context, p)

_myLayout = None
_textStorage = None
_myTextRange = None
def drawWithNSLayout():
    global _myLayout, _textStorage, _myTextRange

    if _myLayout is None:
        # Initialize the text storage with the string to draw.
        _textStorage = NSTextStorage.alloc().initWithString_(getTextString())
        # Initialize the layout manager to use with the text storage.
        _myLayout = NSLayoutManager.alloc().init()
        # Allocate and initialize a text container object.
        textContainer = NSTextContainer.alloc().init()
        # Add the text container to the layout.
        _myLayout.addTextContainer_(textContainer)
        # Release the text container since the layout retains it and
        # this code no longer needs it.
        del textContainer
        # Add the layout to the text storage.
        _textStorage.addLayoutManager_(_myLayout)

        # Set attributes to use when drawing the string.
        stringAttributes = {
            # Use the font with the PostScript name "Times-Roman" at 40 point.
            NSFontAttributeName: NSFont.fontWithName_size_("Times-Roman", 40),

            # Set the text color attribute to an opaque red.
            NSForegroundColorAttributeName:  NSColor.colorWithCalibratedRed_green_blue_alpha_(0.663, 0, 0.031, 1.0),
        }

        # Create the range of text for the entire length of text
        # in the textStorage object.
        _myTextRange = NSMakeRange(0, _textStorage.length())
        # Set the attributes on the entire range of text. 
        _textStorage.setAttributes_range_(stringAttributes, _myTextRange)

    # Set the point for drawing the layout. 
    p = NSMakePoint(20.0, 400.0)

    # Draw the text range at the point.
    _myLayout.drawGlyphsForGlyphRange_atPoint_(_myTextRange, p)

    if doPointDrawing:
        context = NSGraphicsContext.currentContext().graphicsPort()
        Utilities.drawPoint(context, p)

# The interface to the NSLayoutManager subclass.
class MyNSLayoutManager (NSLayoutManager):
    # The extra instance variables for this subclass. 
    _textMode = objc.ivar()
    _fColor = objc.ivar()
    _sColor = objc.ivar()
    _yStartPosition = objc.ivar()
    _lineWidth = objc.ivar()
    _clippingDrawProc = objc.ivar()
    _clippingInfo = objc.ivar()

    # Public methods to set the special attributes
    # of the MyNSLayoutManager instance.
    def setTextMode_(self, textMode):
        self._textMode = textMode

    def setFillColor_(self, color):
        self._fColor = color

    def setStrokeColor_(self, color):
        self._sColor = color

    def setTextLineWidth_(self, width):
        self._lineWidth = width

    def setClippingDrawProc_withInfo_(self, clippingDrawProc, info):
	self._clippingDrawProc = clippingDrawProc
	self._clippingInfo = info

    def init(self):
        self = super(MyNSLayoutManager, self).init()
        if self is None:
            return None


        # Initialize the custom instance variables.
        self._textMode = kCGTextFill
        self._fColor = None
        self._sColor = None
        self._yStartPosition = 0
        self._lineWidth = 1
        self._clippingDrawProc = None
        self._clippingInfo = None
        return self

    # This code overrides this method to record the y coordinate
    # to use as the True baseline for the text drawing. 
    def drawGlyphsForGlyphRange_atPoint_(self, glyphsToShow, origin):
        self._yStartPosition = origin.y
        super(MyNSLayoutManager, self).drawGlyphsForGlyphRange_atPoint_(glyphsToShow, origin)

    # This is the rendering method of NSLayoutManager that the
    # code overrides to perform its custom rendering.
    def showPackedGlyphs_length_glyphRange_atPoint_font_color_printAdjustment_(
            self, glyphs, glyphLen, glyphRange, point, font, color, printingAdjustment):

       # Obtain the destination drawing context.
        context = NSGraphicsContext.currentContext().graphicsPort()

        # Adjust start position y value based on the adjusted y coordinate.
        # This ensures the text baseline is at the starting position
        # passed to drawGlyphsForGlyphRange. This technique won't work
        # for super, subscripts, or underlines but that's OK for this example.
        point.y = _yStartPosition

        # The Quartz graphics state should be preserved by showPackedGlyphs.
        CGContextSaveGState(context)
    
        # Set the desired text drawing mode.
        CGContextSetTextDrawingMode(context, self._textMode)
    
	# Set the fill color if needed.
        if (self._textMode == kCGTextFill or _self.textMode == kCGTextFillStroke or 
                self._textMode == kCGTextFillClip or _textMode == kCGTextFillStrokeClip):
            if self._fColor is not None:
                CGContextSetFillColorWithColor(context, self._fColor)
    
	# Set the  line width and the stroke color if needed.
        if (self._textMode == kCGTextStroke or self._textMode == kCGTextFillStroke or 
                self._textMode == kCGTextStrokeClip or self._textMode == kCGTextFillStrokeClip):
		CGContextSetLineWidth(context, self._lineWidth)
                if self._sColor is not None:
                    CGContextSetStrokeColorWithColor(context, self._sColor)

	# Now draw the text. Check whether to adjust for printing widths
        # and if needed adjust extra character spacing accordingly.
        if printingAdjustment.width != 0.0:
            # If printingAdjustment width is non-zero then the text 
            # needs to be adjusted. printingAdjustment is the per character
            # adjustment required for this piece of text. Because
            # the Quartz text character spacing set is transformed by
            # the text matrix, this code needs to factor out that effect
            # prior to setting it. Cocoa sets the text matrix to account
            # for the point size of the font so we factor that out of the
            # per character width supplied here.
            charAdjust = printingAdjustment.width / font.pointSize()
            CGContextSetCharacterSpacing(context, charAdjust)
        else:
            CGContextSetCharacterSpacing(context, 0.0)

        # Draw the glyphs. The total number of glyphs is the length
        # of the glyphs string passed to showPackedGlyphs, divided by 2 
        # since there are two bytes per glyph.
        CGContextShowGlyphsAtPoint(context, point.x, point.y, glyphs, glyphLen/2)

        # If the text drawing mode requires clipping and there is
        # a custom clipping proc, call it. This allows drawing through
        # clipped text before the graphics state is restored.
        if (self._textMode == kCGTextClip or self._textMode == kCGTextFillClip or
                self._textMode == kCGTextStrokeClip or 
                self._textMode == kCGTextFillStrokeClip) and self._clippingDrawProc is not None:

		self._clippingDrawProc(context, point.x, point.y, self._clippingInfo)
    
        CGContextRestoreGState(context)

def MyClipProc(c, x, y, info):
    CGContextTranslateCTM(c, x, y)
    CGContextSetStrokeColorWithColor(c, Utilities.getRGBOpaqueBlackColor())
    # Draw a grid of lines through the clip.    
    QuartzTextDrawing.drawGridLines(c); 

_myLayout = None
_textStorage = None
_myTextRange = None
def drawWithCustomNSLayout():
    global _myLayout, _textStorage, _myTextRange
    
    if _myLayout is None:
        textContainer = NSTextContainer.alloc().init()
		
        _textStorage = NSTextStorage.alloc().initWithString_(getTextString())
        # Create an instance of the MyNSLayoutManager subclass of NSLayoutManager.
        _myLayout = MyNSLayoutManager.alloc().init()
        _myLayout.addTextContainer_(textContainer)
        # The layout retains the text container so this code can release it.
        del textContainer
        _textStorage.addLayoutManager_(_myLayout)

        # Set attributes to use when drawing the string.
        stringAttributes = {
            # Use the font with the PostScript name "Times-Roman" at 40 point.
            NSFontAttributeName: NSFont.fontWithName_size_("Times-Roman", 40),
        }

        # Create the range.
        _myTextRange = NSMakeRange(0, _textStorage.length())
        # Set the attributes on the entire range of text. 
        _textStorage.setAttributes_range_(stringAttributes, _myTextRange)

    p = NSMakePoint(20.0, 400.0)

    # Set the custom attributes of the layout subclass so that
    # the text will be filled with black.
    _myLayout.setTextMode_(kCGTextFill)
    _myLayout.setFillColor_(Utilities.getRGBOpaqueBlackColor())
    
    # Draw text line 1.    
    _myLayout.drawGlyphsForGlyphRange_atPoint_(_myTextRange, p)

    if doPointDrawing:
        context = NSGraphicsContext.currentContext().graphicsPort()
        Utilities.drawPoint(context, p)

    # Set the custom attributes of the layout subclass so that
    # the text will be stroked with black.
    _myLayout.setTextMode_(kCGTextStroke)
    _myLayout.setStrokeColor_(Utilities.getRGBOpaqueBlackColor())
    _myLayout.setTextLineWidth_(2)

    # Draw text line 2.    
    p.y -= 50; 
    _myLayout.drawGlyphsForGlyphRange_atPoint_(_myTextRange, p)

    if doPointDrawing:
        Utilities.drawPoint(context, p)

    p.y -= 50; 

    # Set the custom attributes of the layout subclass so that
    # the text will be filled and stroked and the fill color
    # will be red. Since the stroke color hasn't changed it
    # will be stroked with black.
    _myLayout.setTextMode_(kCGTextFillStroke)
    _myLayout.setFillColor_(Utilities.getRGBOpaqueRedColor())
    # Draw text line 3.    
    _myLayout.drawGlyphsForGlyphRange_atPoint_(_myTextRange, p)

    if doPointDrawing:
        Utilities.drawPoint(context, p)

    p.y -= 50; 

    # Set the custom attributes of the layout subclass so that
    # the text will be filled, stroked, then clipped.
    _myLayout.setTextMode_(kCGTextFillStrokeClip)
    
    # Set the clipping proc to MyClipProc which requires
    # no info data.
    _myLayout.setClippingDrawProc_withInfo_(MyClipProc, None)
    
    # Draw text line 4.    
    _myLayout.drawGlyphsForGlyphRange_atPoint_(_myTextRange, p)
    
    if doPointDrawing:
        Utilities.drawPoint(context, p)

    # Set the clipping proc to None for future drawing.
    _myLayout.setClippingDrawProc_withInfo_(None, None)
