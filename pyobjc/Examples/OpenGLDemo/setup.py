try:
    import OpenGL.GL
except ImportError:
    import sys
    print >>sys.stderr, "This example requires pyOpenGL, which is not installed"
    sys.exit(1)

from distutils.core import setup
import py2app

plist = dict(NSMainNibFile='OpenGLDemo')
setup(
    app = ['OpenGLDemo.py'],
    data_files = ["OpenGLDemo.nib"],
    options = dict(py2app=dict(plist=plist)),
)
