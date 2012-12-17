from Cocoa import *
from Quartz import *
from CGImageUtils import *

class CGImageView (NSView):
    _image = objc.ivar()

    def setImage_(self, img):
        if img is not None and self._image is not img:
            self._image = img;
            # Mark this view as needing to be redisplayed.
            self.setNeedsDisplay_(True)

    def image(self):
        return self._image

    def drawRect_(self, rect):
        # Obtain the current context
        ctx = NSGraphicsContext.currentContext().graphicsPort()

        # Draw the image in the context
        IIDrawImageTransformed(self._image, ctx,
                CGRectMake(rect.origin.x, rect.origin.y, rect.size.width, rect.size.height))

        # Draw the view border, just a simple stroked rectangle
        CGContextAddRect(ctx, CGRectMake(rect.origin.x, rect.origin.y, rect.size.width, rect.size.height))
        CGContextSetRGBStrokeColor(ctx, 1.0, 0.0, 0.0, 1.0)
        CGContextStrokePath(ctx)
