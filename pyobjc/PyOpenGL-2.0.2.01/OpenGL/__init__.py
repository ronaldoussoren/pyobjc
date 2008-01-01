# This is statement is required by the build system to query build info
if __name__ == '__build__':
	raise Exception


def __set_attributes():
	global __date__, __version__, __build__
	
	import string, os.path

	__date__ = string.join(string.split('$Date: 2004/11/14 23:33:24 $')[1:3], ' ')
		
	filename = os.path.join(os.path.dirname(__file__), 'version')
	__version__ = string.strip(open(filename).read())
	__build__ = int(string.split(__version__, '.')[3])


__set_attributes()

__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>\nMike C. Fletcher <mcfletch@users.sourceforge.net>'
__doc__ = '''This is PyOpenGL 2.  For information regarding PyOpenGL see:
    http://pyopengl.sourceforge.net

For information on OpenGL see:
    http://www.opengl.org'''
from GL._GL__init__ import __numeric_present__, __numeric_support__

