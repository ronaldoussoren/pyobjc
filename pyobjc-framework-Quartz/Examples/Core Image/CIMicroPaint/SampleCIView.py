"""
SampleCIView - simple OpenGL based CoreImage view
"""

from Cocoa import *
from Quartz import *
import CGL

from OpenGL.GL import *

# XXX: this may or may not be a bug in the OpenGL bindings
from OpenGL.GL.APPLE.transform_hint import *

import objc

# The default pixel format
_pf = None

class SampleCIView (NSOpenGLView):
    _context = objc.ivar()
    _image = objc.ivar()
    _lastBounds = objc.ivar(type=NSRect.__typestr__)

    @classmethod
    def defaultPixelFormat(self):
        global _pf

        if _pf is None:
            # Making sure the context's pixel format doesn't have a recovery
            # renderer is important - otherwise CoreImage may not be able to
            # create deeper context's that share textures with this one.

            attr = ( NSOpenGLPFAAccelerated,
                    NSOpenGLPFANoRecovery, NSOpenGLPFAColorSize, 32 )
            _pf = NSOpenGLPixelFormat.alloc().initWithAttributes_(attr)

        return _pf

    def image(self):
        return self._image

    def setImage_dirtyRect_(self, image, r):
        if self._image is not image:
            self._image = image

            if CGRectIsInfinite(r):
                self.setNeedsDisplay_(True)
            else:
                self.setNeedsDisplayInRect_(r)

    def setImage_(self, image):
        self.setImage_dirtyRect_(image, CGRectInfinite)

    def prepareOpenGL(self):
        parm = 1

        # Enable beam-synced updates.

        self.openGLContext().setValues_forParameter_(
                (parm,), NSOpenGLCPSwapInterval)

        # Make sure that everything we don't need is disabled. Some of these
        # are enabled by default and can slow down rendering.

        glDisable(GL_ALPHA_TEST)
        glDisable(GL_DEPTH_TEST)
        glDisable(GL_SCISSOR_TEST)
        glDisable(GL_BLEND)
        glDisable(GL_DITHER)
        glDisable(GL_CULL_FACE)
        glColorMask(GL_TRUE, GL_TRUE, GL_TRUE, GL_TRUE)
        glDepthMask(GL_FALSE)
        glStencilMask(0)
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glHint (GL_TRANSFORM_HINT_APPLE, GL_FASTEST)

    def viewBoundsDidChange_(self, bounds):
        # For subclasses.
        pass

    def updateMatrices(self):
        r = self.bounds()

        if r != self._lastBounds:
            self.openGLContext().update()

            # Install an orthographic projection matrix (no perspective)
            # with the origin in the bottom left and one unit equal to one
            # device pixel.

            glViewport(0, 0, r.size.width, r.size.height)

            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            glOrtho(0, r.size.width, 0, r.size.height, -1, 1)

            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()

            self._lastBounds = r

            self.viewBoundsDidChange_(r)

    def drawRect_(self, r):
        self.openGLContext().makeCurrentContext()

        # Allocate a CoreImage rendering context using the view's OpenGL
        # context as its destination if none already exists.

        if self._context is None:
            pf = self.pixelFormat()
            if pf is None:
                pf = type(self).defaultPixelFormat()

            self._context=CIContext.contextWithCGLContext_pixelFormat_options_(
                CGL.CGLGetCurrentContext(), pf.CGLPixelFormatObj(), None)

        ir = CGRectIntegral(r)

        if NSGraphicsContext.currentContextDrawingToScreen():
            self.updateMatrices()

            # Clear the specified subrect of the OpenGL surface then
            # render the image into the view. Use the GL scissor test to
            # clip to * the subrect. Ask CoreImage to generate an extra
            # pixel in case * it has to interpolate (allow for hardware
            # inaccuracies)

            rr = CGRectIntersection (CGRectInset(ir, -1.0, -1.0),
                        self._lastBounds)

            glScissor(ir.origin.x, ir.origin.y, ir.size.width, ir.size.height)
            glEnable(GL_SCISSOR_TEST)

            glClear(GL_COLOR_BUFFER_BIT)

            if self.respondsToSelector_('drawRect:inCIContext:'):
                self.drawRect_inCIContext_(rr, self._context)

            elif self._image is not None:
                self._context.drawImage_atPoint_fromRect_(
                    self._image, rr.origin, rr)

            glDisable(GL_SCISSOR_TEST)

            # Flush the OpenGL command stream. If the view is double
            # buffered this should be replaced by [[self openGLContext]
            # flushBuffer].

            glFlush ()

        else:
            # Printing the view contents. Render using CG, not OpenGL.

            if self.respondsToSelector_('drawRect:inCIContext:'):
                self.drawRect_inCIContext_(ir, self._context)

            elif self._image is not None:
                cgImage = self._context.createCGImage_fromRect_(
                    self._image, ir)

                if cgImage is not None:
                    CGContextDrawImage(
                            NSGraphicsContext.currentContext().graphicsPort(),
                            ir, cgImage)
