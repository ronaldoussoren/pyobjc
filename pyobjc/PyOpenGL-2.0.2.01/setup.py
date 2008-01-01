#!/usr/bin/env python

## created 2000/08/01, Rene Liebscher <R.Liebscher@gmx.de>

import distutils, re, sys, string, os, os.path

# get the Distutils version, we need at least 1.0.2pre
versions = re.findall(r'(\d+)[.](\d+)(?:[.](\d+))?', distutils.__version__)
version = 0
if len(versions):
	version = 0x10000*int(versions[0][0]) + 0x100*int(versions[0][1])
	if versions[0][2] != '':
		version = version + int(versions[0][2])

if version < 0x010002:
	print 'PyOpenGL setup requires at least version 1.0.2pre of Distutils.'
	print 'Please get the latest version at:'
	print 'http://www.python.org/sigs/distutils-sig/download.html'
	sys.exit(1)

# Add the current directory to the PATH, needed since build_py has to
# execute shadow selectors.
if os.environ.has_key('PATH'):
	path = string.split(os.environ['PATH'], os.pathsep)
else:
	path = []

if os.curdir not in path:
	path.append(os.curdir)
	os.environ['PATH'] = string.join(path, os.pathsep)

from distutils.sysconfig import *
from distutils.core import setup
from distutils.command.sdist import sdist

from setup.build import build
from setup.util import *
from setup.my_install_data import *
from setup.build_w import build_w
from setup.build_py import build_py
from setup.config import config
from setup.build_doc import build_doc
from setup.dist import Distribution
from setup.togl_setup import install, build_togl
from setup.install_shortcuts import install_shortcuts
from setup.bdist_wininst import NumericWinInstaller

#######################################################################
## platform specific stuff
## see config/<platform>.cfg for any configurable options

# Bob's patch for OSX here...
if sys.platform == 'darwin':
	from distutils.unixccompiler import UnixCCompiler
	UnixCCompiler.executables['ranlib'] = ['ranlib']
	del UnixCCompiler

try:
	import Numeric
	if string.split(Numeric.__version__,'.')[0] > '21':
		numeric_requires = ",python-numeric >= 22.0"
	else:
		numeric_requires = ",python-numeric <= 21.0"
except ImportError:
		numeric_requires = ""

setup (
	name = 'PyOpenGL',
	version = get_version(),
	description = 'OpenGL bindings for Python',
	long_description = 'OpenGL bindings for Python including support for GL extensions, GLU, WGL, GLUT, GLE, and Tk',
	maintainer = 'PyOpenGL SourceForge group',
	maintainer_email = 'pyopengl-devel@lists.sourceforge.net',
	url = 'http://pyopengl.sourceforge.net',
	
	license = 'License :: OSI Approved :: BSD License',
	ext_package = 'OpenGL',
	options = {
		'sdist':{'use_defaults':0, 'force_manifest':1},
		'bdist_rpm':{
			'group':'Libraries/Python',
			'provides':'python-OpenGL,python-GLU,python-GLUT,python-GLE,tk-togl,python-GLX,python-togl',
			# Numeric exports itself as python-numeric,  but at least one distro calls it python-numpy :(
			# the rest of them do appear to have their requirements exported
			'requires':'glut,tkinter'+numeric_requires,
		},
		'bdist_wininst':{
			'bitmap':os.path.join('setup', 'wininst_logo.bmp'),
		},
		'register':{
			'keywords': 'Graphics,3D,OpenGL,GLU,GLUT,GLE,GLX,WGL,TOGL,EXT,ARB,Mesa',
			'summary':'OpenGL and OpenGL-related library support',
			'description':"""SWIG-based OpenGL, GLU, GLUT, WGL, GLX and GLE extensions

PyOpenGL is the defacto "official" Python OpenGL binding.
The project provides accesss to the core GL, and GLU
libraries, as well as the GLUT, GLE, GLX, and WGL
extensions.  It is compatible with most OpenGL-friendly
GUI libraries, including wxPython, PyGame, FxPy, and
Tkinter (with the included togl widget).
""",
			'classifiers': [
				"""License :: OSI Approved :: BSD License""",
				"""Programming Language :: Python""",
				"""Topic :: Multimedia :: Graphics :: 3D Rendering""",
				"""Topic :: Software Development :: Libraries :: Python Modules""",
				"""Intended Audience :: Developers""",
			],
			'download_url': "http://sourceforge.net/project/showfiles.php?group_id=5988",
		},
	},
	   
	distclass = Distribution,
	# Overridden command classes
	cmdclass = {
		'build':build,
		'build_w':build_w,
		'build_doc':build_doc,
		'config':config,
		'build_py':build_py,
		'build_togl':build_togl,
		'install':install,
		'install_shortcuts':install_shortcuts,
		# the next line is very important
		# because we use another format for data_files
		'install_data': my_install_data,
		'bdist_wininst': NumericWinInstaller,
	},
	data_files = [Data_Files(
	   
		base_dir='install_lib',
		copy_to = 'OpenGL',
		strip_dirs = 1,
		template=[
			# take the whole tree
			'graft OpenGL',
			'global-exclude *.py',
			'global-exclude Cvs/*',
			'global-exclude CVS/*',
		],
		preserve_path=1
	)],
	libraries = [
		(
			'interface_util',
			{
				'sources':[
					'src/interface_util/interface_util.c',
					'src/interface_util/platform.c'
				],
				#,#, 'include_dirs':[get_python_inc()] + include_dirs, 'macros':define_macros}),
			}
		)
	]
)


