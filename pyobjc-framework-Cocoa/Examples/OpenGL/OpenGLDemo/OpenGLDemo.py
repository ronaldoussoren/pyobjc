"""OpenGLDemo.py -- A simple demo of using OpenGL with Cocoa

To build the demo program, run this line in Terminal.app:

    $ python setup.py py2app -A

This creates a directory "dist" containing OpenGLDemo.app. (The
-A option causes the files to be symlinked to the .app bundle instead
of copied. This means you don't have to rebuild the app if you edit the
sources or nibs.)

This example requires PyOpenGL
"""

from Cocoa import (
    NSOpenGLView,
    NSOpenGLPFANoRecovery,
    NSOpenGLPFAWindow,
    NSOpenGLPFAAccelerated,
    NSOpenGLPFADoubleBuffer,
    NSOpenGLPFAColorSize,
    NSOpenGLPFAAlphaSize,
    NSOpenGLPFADepthSize,
    NSOpenGLPFAStencilSize,
    NSOpenGLPFAAccumSize,
    NSOpenGLPixelFormat,
)
from OpenGL.GL import (
    glViewport,
    glClearColor,
    glClear,
    GL_COLOR_BUFFER_BIT,
    GL_DEPTH_BUFFER_BIT,
    GL_STENCIL_BUFFER_BIT,
)
from PyObjCTools import AppHelper
import objc
from objc import super

ClearColors = redIndex, greenIndex, blueIndex, alphaIndex = range(4)


class OpenGLDemoView(NSOpenGLView):
    def awakeFromNib(self):
        self.color_index = alphaIndex

    def initWithFrame_(self, frame):
        attribs = [
            NSOpenGLPFANoRecovery,
            NSOpenGLPFAWindow,
            NSOpenGLPFAAccelerated,
            NSOpenGLPFADoubleBuffer,
            NSOpenGLPFAColorSize,
            24,
            NSOpenGLPFAAlphaSize,
            8,
            NSOpenGLPFADepthSize,
            24,
            NSOpenGLPFAStencilSize,
            8,
            NSOpenGLPFAAccumSize,
            0,
        ]
        fmt = NSOpenGLPixelFormat.alloc().initWithAttributes_(attribs)
        self = super(OpenGLDemoView, self).initWithFrame_pixelFormat_(frame, fmt)
        return self

    @objc.IBAction
    def setClearColor_(self, sender):
        self.color_index = sender.tag()
        self.setNeedsDisplay_(True)

    def drawRect_(self, pos, siz):
        x, y = pos
        w, h = siz
        glViewport(0, 0, w, h)
        clear_color = [0.0] * 4
        clear_color[self.color_index] = 1.0
        glClearColor(*clear_color)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT | GL_STENCIL_BUFFER_BIT)
        self.openGLContext().flushBuffer()


if __name__ == "__main__":
    AppHelper.runEventLoop()
