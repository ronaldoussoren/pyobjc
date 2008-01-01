# This is statement is required by the build system to query build info
if __name__ == '__build__':
	gl_platforms = ['GLX']
	raise Exception

import string
__version__ = string.split('$Revision: 1.4 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/08 18:26:50 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'

