from Quartz import *
import Utilities

import sys


def RedBlackRedRampEvaluate(info, input, output):
    # The domain of this function is 0 - 1. For an input value of 0
    # this function returns the color to paint at the start point
    # of the shading. For an input value of 1 this function returns
    # the color to paint at the end point of the shading. This
    # is a 1 in, 4 out function where the output values correspond
    # to an r,g,b,a color.
    #		
    # For an RGB color space as the shading color space, this
    # function evaluates to produce a blend from pure, opaque
    # red at the start point to a pure opaque black at the 
    # midpoint, and back to pure opaque red at the end point.

    return (
        # The red component evaluates to 1 for an input value of 0
        # (the start point of the shading). It smoothly reduces
        # to zero at the midpoint of the shading (input value 0.5)  
        # and increases up to 1 at the endpoint of the shading (input
        # value 1.0).
        abs(1.0 - input[0]*2),
        # The green and blue components are always 0.
        0, 0,
        # The alpha component is 1 for the entire shading.
        1,
    )

def createFunctionForRGB(evaluationFunction):
    # This is a 1 in, 4 out function for drawing shadings 
    # in a 3 component (plus alpha) color space. Shadings 
    # parameterize the endpoints such that the starting point
    # represents the function input value 0 and the ending point 
    # represents the function input value 1. 
    domain = (0, 1)
    
    # The range is the range for the output colors. For an rgb
    # color space the values range from 0-1 for the r,g,b, and a
    # components. 
   
    range = (
        # The red component, min and max.    
        0, 1,
        # The green component, min and max.    
        0, 1,
        # The blue component, min and max.    
        0, 1,
        # The alpha component, min and max.    
        0, 1
    )
    
    # Dimension of domain is 1 and dimension of range is 4.    
    function = CGFunctionCreate(None, 1, domain, 4, range, 
            (
                evaluationFunction,
                None
            ))

    if function is None:
        print >>sys.stderr, "Couldn't create the CGFunction!"
        return None

    return function

def doSimpleAxialShading(context):
    # This shading paints colors in the calibrated Generic RGB 
    # color space so it needs a function that evaluates 1 in to 4 out.
    axialFunction = createFunctionForRGB(RedBlackRedRampEvaluate)
    if axialFunction is None:
        return 
    
    # Start the shading at the point (20,20) and
    # end it at (420,20). The axis of the shading
    # is a line from (20,20) to (420,20).
    startPoint = CGPoint(x = 20, y = 20)
    endPoint = CGPoint(x = 420, y = 20)

    # Don't extend this shading.
    extendStart = extendEnd = False

    shading = CGShadingCreateAxial(Utilities.getTheCalibratedRGBColorSpace(), 
			    startPoint, endPoint, 
			    axialFunction, 
			    extendStart, extendEnd)
    # The shading retains the function and this code
    # is done with the function so it should release it.
    del axialFunction
    if shading is None:
        print >>sys.stderr, "Couldn't create the shading!"
        return

    # Draw the shading. This paints the shading to
    # the destination context, clipped by the
    # current clipping area.
    CGContextDrawShading(context, shading)

def RedGreenRampEvaluate(info, input, output):
    # The domain of this function is 0 - 1. For an input value of 0
    # this function returns the color to paint at the start point
    # of the shading. For an input value of 1 this function returns
    # the color to paint at the end point of the shading. This
    # is a 1 in, 4 out function where the output values correspond
    # to an r,g,b,a color.
    # 
    # For an RGB color space as the shading color space, this
    # function evaluates to produce a blend from pure, opaque
    # red at the start point to a pure opaque green at the end point.


    return (
        # The red component starts at 1 and reduces to zero as the input 
        # goes from 0 (the start point of the shading) and increases 
        # to 1 (the end point of the shading).
        1.0 - input[0],
        # The green component starts at 0 for an input of 0
        # (the start point of the shading) and increases to 1 
        # for an input value of 1 (the end point of the shading).
        input[0],
        # The blue component is always 0.
        0,
        # The alpha component is always 1, the shading is always opaque.
        1,
    )

def doExampleAxialShading(context):
    rect = CGRectMake(0, 0, 240, 240)
    
    # This shading paints colors in the calibrated Generic RGB 
    # color space so it needs a function that evaluates 1 in to 4 out.
    redGreenFunction = createFunctionForRGB(RedGreenRampEvaluate)
    if redGreenFunction is None:
        return

    # Start the shading at the point (20,20) and
    # end it at (220,220). The axis of the shading
    # is a diagonal line from (20,20) to (220,220).
    startPoint = CGPoint(x = 20, y = 20)
    endPoint = CGPoint(x = 220, y = 220)
    
    # Don't extend this shading.
    extendStart = extendEnd = False
    shading = CGShadingCreateAxial(Utilities.getTheCalibratedRGBColorSpace(), 
			    startPoint, endPoint, 
			    redGreenFunction, 
			    extendStart, extendEnd)
    
    if shading is None:
        print >>sys.stderr, "Couldn't create the shading!"
        return

    # Position for the first portion of the drawing.
    CGContextTranslateCTM(context, 40, 260)
    
    # Stroke a black rectangle that will frame the shading.
    CGContextSetLineWidth(context, 2)
    CGContextSetStrokeColorWithColor(context, Utilities.getRGBOpaqueBlackColor())
    CGContextStrokeRect(context, rect)

    CGContextSaveGState(context)
    if 1:
        # Clip to the rectangle that was just stroked.
        CGContextClipToRect(context, rect)
        # Draw the shading. This paints the shading to
        # the destination context, clipped to rect.
        CGContextDrawShading(context, shading)
        # Release the shading once the code is finished with it.
        del shading
	# Restore the graphics state so that the rectangular 
	# clip is no longer present.
    CGContextRestoreGState(context)

    # Prepare for the next shading.
    CGContextTranslateCTM(context, 0, -250)
    
    # Extend this shading.
    extendStart = extendEnd = True
    shading = CGShadingCreateAxial(Utilities.getTheCalibratedRGBColorSpace(), 
			    startPoint, endPoint, 
			    redGreenFunction, 
			    extendStart, extendEnd)
    # The shading retains the function and this code
    # is done with the function so it should release it.
    del redGreenFunction
    if shading is None:
        print >>sys.stderr, "Couldn't create the shading!"
        return
    
    # Stroke with the current stroke color.
    CGContextStrokeRect(context, rect)

    CGContextSaveGState(context)
    if 1:
	CGContextClipToRect(context, rect)
	# Draw the shading. This paints the shading to
	# the destination context, clipped to rect.
	CGContextDrawShading(context, shading)
    CGContextRestoreGState(context)
    
    # Now paint some text with a shading.
    CGContextSaveGState(context)
    if 1:
	CGContextTranslateCTM(context, 260, 0)
	CGContextSetTextMatrix(context, CGAffineTransformIdentity)
       
	# Set the font with the PostScript name "Times-Roman", at
	# 80 points, with the MacRoman encoding.
	CGContextSelectFont(context, "Times-Roman", 80, 
					    kCGEncodingMacRoman)

	# Rotate so that the text characters are rotated
	# relative to the page.
	CGContextRotateCTM(context, Utilities.DEGREES_TO_RADIANS(45))
	# Set the text drawing mode to clip so that
	# the characters in the string are intersected with
	# the clipping area.
	CGContextSetTextDrawingMode(context, kCGTextClip)
	CGContextShowTextAtPoint(context, 30, 0, "Shading", 7)
	
	# At this point nothing has been painted; the
	# glyphs in the word "Shading" have been intersected
	# with the previous clipping area to create a new
	# clipping area.
	
	# Rotate the coordinate system back so that the
	# shading is not rotated relative to the page.
	CGContextRotateCTM(context, Utilities.DEGREES_TO_RADIANS(-45))
	
	# Draw the shading, painting the shading 
	# to the destination context, clipped by the glyphs.
	CGContextDrawShading(context, shading)
	
    CGContextRestoreGState(context)
    # Release the shading once the code is finished with it.
    del shading

class MyStartEndColor (object):
    def __init__(self):
        self.startColor = [0.0] * 3
        self.endColor = [0.0] * 3

def StartColorEndColorEvaluate(info, input, output):
    # The domain of this function is 0 - 1. For an input value of 0
    # this function returns the color to paint at the start point
    # of the shading. For an input value of 1 this function returns
    # the color to paint at the end point of the shading. This
    # is a 1 in, 4 out function where the output values correspond
    # to an r,g,b,a color.
    # 
    # This function evaluates to produce a blend from startColor to endColor.
    # 
    # Note that the returned results are clipped to the range
    # by Quartz so this function doesn't worry about values
    # that are outside the range 0-1.	

    # Weight the starting and ending color components depending
    # on what position in the blend the input value specifies.
    return (
        (info.startColor[0]*(1-input[0]) + info.endColor[0]*input[0]),
        (info.startColor[1]*(1-input[0]) + info.endColor[1]*input[0]),
        (info.startColor[2]*(1-input[0]) + info.endColor[2]*input[0]),
        # The alpha component is always 1, the shading is always opaque.
        1,
    )

def createFunctionWithStartEndColorRamp(startColor, endColor):
    # Use a pointer to a MyStartEndColor as a way of 
    # parameterizing the color ramp this function produces.
    startEndColorP =  MyStartEndColor()
    
    # Set up start and end colors in the info structure.
    startEndColorP.startColor[0] = startColor[0]
    startEndColorP.startColor[1] = startColor[1]
    startEndColorP.startColor[2] = startColor[2]

    startEndColorP.endColor[0] = endColor[0]
    startEndColorP.endColor[1] = endColor[1]
    startEndColorP.endColor[2] = endColor[2]

    # This is a 1 in, 4 out function for drawing shadings 
    # in a 3 component (plus alpha) color space. Shadings 
    # parameterize the endpoints such that the starting point
    # represents the function input value 0 and the ending point 
    # represents the function input value 1. 
    domain = (0, 1)
    
    # The range is the range for the output colors. For an rgb
    # color space the values range from 0-1 for the r,g,b, and a
    # components.
    
    range = (
        # The red component, min and max.    
        0, 1,
        # The green component, min and max.    
        0, 1,
        # The blue component, min and max.    
        0, 1,
        # The alpha component, min and max.    
        0, 1,
    ) 
    
    # Pass startEndColorP as the info parameter.
    function = CGFunctionCreate(startEndColorP, 1, domain, 4, 
                        range, (StartColorEndColorEvaluate, None))

    if function is None:
        print >>sys.stderr, "Couldn't create the CGFunction!"
        return None
    
    return function

def doSimpleRadialShading(context):
    startColor = [ 0.663, 0.0, 0.031 ] # Red.
    endColor   = [ 1.0,   0.8, 0.4   ] # Light yellow.

    # This function describes a color ramp where the starting color
    # is red and the ending color is blue.
    redYellowFunction = createFunctionWithStartEndColorRamp(
					startColor, endColor)
    if redYellowFunction is None:
        return

    CGContextTranslateCTM(context, 120, 120)

    # Circles whose origin is the same.
    circleACenter = CGPoint(x = 0, y = 0)
    circleBCenter = circleACenter
    
    # The starting circle is inside the ending circle.
    circleARadius = 50
    circleBRadius = 100
    
    #  Don't extend the shading.
    extendStart = extendEnd = False
    shading = CGShadingCreateRadial(
		Utilities.getTheCalibratedRGBColorSpace(), 
		circleACenter, circleARadius,
		circleBCenter, circleBRadius,
		redYellowFunction, 
		extendStart, extendEnd)
    
    del redYellowFunction
    if shading is None:
        print >>sys.stderr, "Couldn't create the shading!"
        return
    CGContextDrawShading(context, shading)

def doExampleRadialShadings(context):
    magenta   = [ 1,    0, 1    ] # Pure magenta.
    magenta30 = [ 0.3,  0, 0.3  ] # 30% magenta.
    black     = [ 0,    0, 0    ]
    red       = [ 1,    0, 0    ]
    green     = [ 0,    1, 0    ]
    blue      = [ 0,    0, 1    ]
    redgreen  = [ 0.66, 1, 0.04 ] # A red-green shade.
    
    CGContextTranslateCTM(context, 120, 550)
    
    # This function describes a color ramp where the starting color
    # is a full magenta, the ending color is 30% magenta.
    magentaFunction = createFunctionWithStartEndColorRamp(
			    magenta, magenta30)
    if magentaFunction is None:
        print >>sys.stderr, "Couldn't create the magenta function!"
        return

    # Shading 1. Circle A is completely inside circle B but with 
    # different origins. Circle A has radius 0 which produces
    # a point source.

    # The center of circle A is offset from the origin.
    circleACenter = CGPoint(x=30, y=40)
    # The center of circle B is at the origin.
    circleBCenter = CGPoint(x=0, y=0)
    
    # A radius of zero produces a point source.
    circleARadius = 0
    circleBRadius = 100
    
    # Don't extend the shading.
    extendStart = extendEnd = False
    shading = CGShadingCreateRadial(
		Utilities.getTheCalibratedRGBColorSpace(), 
		circleACenter, circleARadius,
		circleBCenter, circleBRadius,
		magentaFunction, 
		extendStart, extendEnd)
    # Finished with the magenta function so release it.
    del magentaFunction
    if shading is None:
        print >>sys.stderr, "Couldn't create the shading!"
        return

    CGContextDrawShading(context, shading)
    # Finished with the shading so release it.
    del shading

    # Shading 2. Circle A is completely inside
    # circle B but with different origins.

    # The starting color is red and the ending color is green.
    redGreenFunction = createFunctionWithStartEndColorRamp(
			    red, green)
    if redGreenFunction is None:
        print >>sys.stderr, "Couldn't create the red-Green function!"
        return

    circleACenter.x = 55
    circleACenter.y = 70
    circleBCenter.x = 20
    circleBCenter.y = 0
    circleARadius = 10
    # The outer circle is outside the clipping path so the
    # color at the edge of the shape is not
    # that at the radius of the outer circle.
    circleBRadius = 200
    # Extend the end point of this shading.
    extendStart = False
    extendEnd = True
    shading = CGShadingCreateRadial(
		    Utilities.getTheCalibratedRGBColorSpace(), 
		    circleACenter, circleARadius,
		    circleBCenter, circleBRadius,
		    redGreenFunction, 
		    extendStart, extendEnd)
    # Finished with this function so release it.
    del redGreenFunction
    if shading is None:
        print >>sys.stderr, "Couldn't create the shading!"
        return

    # Set a clipping area to bound the extend. This code
    # sets a clipping area that corresponds to a circular 
    # wedge. The starting circle is inside the clipping
    # area and the ending circle is outside.
    CGContextSaveGState(context)
    if 1:
	CGContextTranslateCTM(context, 250, 0)
	CGContextBeginPath(context)
	CGContextMoveToPoint(context, 25, 0)
	CGContextAddArc(context, 
			25, 0, 130,
			Utilities.DEGREES_TO_RADIANS(30), 
			Utilities.DEGREES_TO_RADIANS(-30), 
			0)
	CGContextClip(context)
	# Paint the shading.
	CGContextDrawShading(context, shading)
	# Finished with the shading so release it.
	del shading
    CGContextRestoreGState(context)

    CGContextTranslateCTM(context, -40, -250)

    # Shading 3. The starting circle is completely outside
    # the ending circle, no extension. The circles
    # have the same radii.
    circleACenter.x = 0
    circleACenter.y = 0
    circleBCenter.x = 125
    circleBCenter.y = 0
    
    circleARadius = 50
    circleBRadius = 50

    extendStart = extendEnd = False

    # Create a function that paints a red to black ramp.
    redBlackFunction = createFunctionWithStartEndColorRamp(
			    red, black)
    if redBlackFunction is None:
        print >>sys.stderr, "Couldn't create the red-black function!"
        return
    
    shading = CGShadingCreateRadial(
		    Utilities.getTheCalibratedRGBColorSpace(), 
		    circleACenter, circleARadius,
		    circleBCenter, circleBRadius,
		    redBlackFunction, 
		    extendStart, extendEnd)
    if shading is None:
        print >>sys.stderr, "Couldn't create the shading!"
        return
    
    CGContextDrawShading(context, shading)
    # Finished with the shading so release it.
    del shading

    # Shading 4. The starting circle is completely outside
    # the ending circle. The circles have different radii.
    circleACenter.x = 120
    circleACenter.y = 0
    circleBCenter.x = 0
    circleBCenter.y = 0
    
    circleARadius = 75
    circleBRadius = 30

    # Extend at the start and end.
    extendStart = extendEnd = True
    shading = CGShadingCreateRadial(
		Utilities.getTheCalibratedRGBColorSpace(), 
		circleACenter, circleARadius,
		circleBCenter, circleBRadius,
		redBlackFunction, 
		extendStart, extendEnd)
    # Finished with this function so release it.
    del redBlackFunction
    if shading is None:
        print >>sys.stderr, "Couldn't create the shading!"
        return

    CGContextSaveGState(context)
    if 1:
	CGContextTranslateCTM(context, 270, 0)
	# Clip to an elliptical path so the shading
	# does not extend to infinity at the larger end.
	CGContextBeginPath(context)
	Utilities.myCGContextAddEllipseInRect(context, 
			CGRectMake(-200, -200, 450, 400))
	CGContextClip(context)
	CGContextDrawShading(context, shading)
	# Finished with the shading so release it.
	del shading
    CGContextRestoreGState(context)

    CGContextTranslateCTM(context, 30, -200)

    # The starting color is blue, the ending color is a red-green color.
    blueGreenFunction = createFunctionWithStartEndColorRamp(
			    blue, redgreen)
    if blueGreenFunction is None:
        print >>sys.stderr, "Couldn't create the blue-Green function!"
        return
   
    # Shading 5. The circles partially overlap and have
    # different radii with the larger circle at the start.
    circleACenter.x = 0
    circleACenter.y = 0
    circleBCenter.x = 90
    circleBCenter.y = 30
    
    circleARadius = 75
    circleBRadius = 45

    extendStart = extendEnd = False
    shading = CGShadingCreateRadial(
		    Utilities.getTheCalibratedRGBColorSpace(), 
		    circleACenter, circleARadius,
		    circleBCenter, circleBRadius,
		    blueGreenFunction, 
		    extendStart, extendEnd)
    if shading is None:
        print >>sys.stderr, "Couldn't create the shading!"
        return

    CGContextDrawShading(context, shading)
    # Finished with the shading so release it.
    del shading

    CGContextTranslateCTM(context, 200, 0)

    # Shading 6. The circles partially overlap and have 
    # different radii with the larger circle at the end.
    
    circleARadius = 45
    circleBRadius = 75
    shading = CGShadingCreateRadial(
		    Utilities.getTheCalibratedRGBColorSpace(), 
		    circleACenter, circleARadius,
		    circleBCenter, circleBRadius,
		    blueGreenFunction, 
		    extendStart, extendEnd)
    # Finished with this function so release it.
    del blueGreenFunction
    if shading is None:
        print >>sys.stderr, "Couldn't create the shading!"
        return

    CGContextDrawShading(context, shading)

def doEllipseShading(context):
    black = [ 0, 0, 0 ]
    red   = [ 1, 0, 0 ]

    # This function describes a color ramp where the starting color
    # is red, the ending color is black.
    redBlackFunction = createFunctionWithStartEndColorRamp(
			    red, black)
    if redBlackFunction is None:
        print >>sys.stderr, "Couldn't create the red-black function!"
        return
    
    CGContextTranslateCTM(context, 100, 300)
    # Shading 1.
    #   To obtain an elliptical shading requires that user space
    #   at the time the shading is painted is transformed so that
    #   the circles which define the radial shading geometry are
    #   rotated and elliptical. User space will be rotated
    #   by 45 degrees, then scaled by 1 in x and 2 in y to produce
    #   the ellipses.

    # Compute the transform needed to create the rotated ellipses. 
    t = CGAffineTransformMakeRotation(Utilities.DEGREES_TO_RADIANS(45))
    t = CGAffineTransformScale(t, 1, 2)

    circleACenter = CGPoint(x=0, y=0)
    circleBCenter = CGPoint(x=circleACenter.x + 144, y=circleACenter.y)
    circleARadius = 45
    circleBRadius = 45

    # Don't extend this shading.
    extendStart = extendEnd = False

    shading = CGShadingCreateRadial(
		    Utilities.getTheCalibratedRGBColorSpace(), 
		    circleACenter, circleARadius,
		    circleBCenter, circleBRadius,
		    redBlackFunction, 
		    extendStart, extendEnd)
    if shading is None:
        # Couldn't create the shading so release
        # the function before returning.
        print >>sys.stderr, "Couldn't create the shading!"
        return
    
    CGContextSaveGState(context)
    if 1:
	# Transform coordinates for the drawing of the shading.
	# This transform produces the rotated elliptical shading.
	# This produces the left shading in the figure, the
	# one where both the ellipses and the shading are
	# rotated relative to default user space.
	CGContextConcatCTM(context, t)
	
	CGContextDrawShading(context, shading)
	del shading
    CGContextRestoreGState(context)

    CGContextTranslateCTM(context, 300, 10)
    
    
    # Shading 2.
    #    Now draw the shading where the shading ellipses are
    #    rotated but the axis between the origins of 
    #    the ellipses lies parallel to the x axis in default
    #    user space. This is similar to the shading drawn
    #    manually in Chapter 5. 
    #    
    #    To compute the correct origins for the shading, 
    #    the code needs to compute the points that, 
    #    transformed by the matrix t used to paint the shading, 
    #    produce the desired coordinates. We want coordinates
    #    that are transformed as follows:
    #    
    #            P' = P x t
    #            
    #    where P' is the point in untransformed user space that
    #    we want as the origin, P is the point in transformed
    #    user space that will be transformed by t, the matrix
    #    which transforms the circles into rotated ellipses.
    #
    #    So we want to calculate P such that P' = P x t .
    #
    #    Notice that if P = P' x Inverse(t) then:
    #    
    #    P' = P' x Inverse(t) x t = P' x Identity = P'.
    #    
    #    This means that we can calculate the point P
    #    by computing P' x Inverse(t).

    inverseT = CGAffineTransformInvert(t)
    # Now the code can transform the coordinates through the
    # inverse transform to compute the new coordinates. These
    # coordinates, when transformed with the transform t, 
    # produce the original coordinate.
    circleACenter = CGPointApplyAffineTransform(circleACenter, inverseT)
    circleBCenter = CGPointApplyAffineTransform(circleBCenter, inverseT)

    shading = CGShadingCreateRadial(
		    Utilities.getTheCalibratedRGBColorSpace(), 
		    circleACenter, circleARadius,
		    circleBCenter, circleBRadius,
		    redBlackFunction, 
		    extendStart, extendEnd)
    # The code is finished with the function so release it. 
    del redBlackFunction
    if shading is None:
        print >>sys.stderr, "Couldn't create the shading!"
        return

    # Transform coordinates for the drawing of the shading.
    # This transform produces the rotated elliptical shading.
    CGContextConcatCTM(context, t)
    
    CGContextDrawShading(context, shading)
