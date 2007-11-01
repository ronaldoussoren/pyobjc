import string
__version__ = string.split('$Revision: 1.3 $')[1]
__date__ = string.join(string.split('$Date: 2001/06/23 20:22:06 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/3DFX/3dfx_multisample.txt'
__api_version__ = 0x101


GLX_SAMPLE_BUFFERS_3DFX =			    0x8050
GLX_SAMPLES_3DFX =			    0x8051
