from bundlebuilder import buildapp

try:
    import OpenGL.GL
except ImportError:
    import sys
    print >>sys.stderr, "This example requires pyOpenGL, which is not installed"
    sys.exit(1)

buildapp(
	mainprogram = "OpenGLDemo.py",
	resources = ["OpenGLDemo.nib"],
	nibname = "OpenGLDemo",
)
