"""
A distutils script to make a standalone .exe of superdoodle for
Windows platforms.  You can get py2exe from
http://py2exe.sourceforge.net/.  Use this command to build the .exe
and collect the other needed files:

    python setup.py py2exe

A distutils script to make a standalone .app of superdoodle for
Mac OS X.  You can get py2app from http://undefined.org/python/py2app.
Use this command to build the .app and collect the other needed files:

   python setup.py py2app
"""



from distutils.core import setup
import sys
if sys.platform == 'darwin':
    import py2app
    buildstyle = 'app'
elif sys.platform == 'win32':
    import py2exe
    # buildstyle = 'console'
    buildstyle = 'windows'

setup(
    name="superdoodle",
    **{buildstyle : ['superdoodle.py']}
)
