'''togl_setup.py

Compiles and installs Togl.

We create a sub-class of the standard build_ext command,
named build_togl, which is responsible for compiling the
Tk Togl widget.  Our sub-class of install then takes care
of installing the resulting .dll/.so into the Python
installation against which we have compiled.

The setup process uses the headers from a source
distribution of tcl (from the tcl project on sourceforge)
and the .lib files from the Python Tkinter directory.
'''

# created 2000/08/01, Rene Liebscher <R.Liebscher@gmx.de>

import sys,os,string, os.path
import distutils.command.install
import distutils.command.build_ext
from distutils.dep_util import newer_group

# this is also a simple test if we need to build Togl
# without Tkinter it is not neccessary
try:
	import Tkinter
	tk = Tkinter.Tk()
	if tk.getvar('tk_version') < '8.1' or tk.getvar('tcl_version') < '8.1':
		Togl = 'Togl-1.5'
		togl_version_decimal = '1.5.0'
	else:
		Togl = 'Togl-1.6'
		togl_version_decimal = '1.6.0'
##	if tk.getvar( 'tk_version' ) >= '8.4':
##		raise ImportError( """Preventing (doomed) attempts to build togl with Tk 8.4""" )
	# if the Togl sources are not included then don't build
	if not os.path.exists(os.path.join('src', Togl)):
		tk = None
except ImportError:
	tk = None
	Togl = None
	togl_version_decimal = ''
except Exception, err:
	sys.stderr.write( """Unable to initialise Tk: %s\n"""%(err,))
	tk = None
	Togl = None
	togl_version_decimal = ''
	
if Togl:
	print 'Togl to be built:', Togl
else:
	print 'Togl not to be built change config/%s.cfg to enable'%(sys.platform,)

class build_togl( distutils.command.build_ext.build_ext):
	"""Build the togl.dll/togl.so shared library for Tk/Tkinter

	The build_togl extension is a pretty minimal sub-class
	of build_ext.  It has a two extra options for specifying
	the tk-source and tcl-source directories which will be
	used for adding new directories to the include path for
	the command.

	The command also makes sure that the Python Tkinter .lib
	files are in the command's lib
	"""
	user_options = distutils.command.build_ext.build_ext.user_options + [
		('tk-source=', None,
		"The Tk source directory (e.g. the tk8.4.5 directory from a source distribution)"),
		('tcl-source=', None,
		"The Tcl source directory  (e.g. the tcl8.4.5 directory from a source distribution)"),
	]
	def build_extensions(self):
		"""Do the actual creation of the togl shared library"""
		if tk is not None and self.distribution.BUILD_TOGL:
			self.togl_build(
				self.distribution.togl_libs,
			)
	def initialize_options (self):
		"""Do normal initialisation and initialise our own options"""
		distutils.command.build_ext.build_ext.initialize_options( self )
		self.tk_source = None
		self.tcl_source = None
	def finalize_options (self):
		"""Finalise the options for building, we add Togl-specific includes/libs"""
		distutils.command.build_ext.build_ext.finalize_options( self )
		self.distribution._set_command_options(
			self, self.distribution.get_option_dict('build_togl')
		)
		if not Togl or not self.distribution.BUILD_TOGL:
			return
		tkDirs = ['generic', 'xlib' ]
		tclDirs = [ 'generic', 'win', ] #'include', ]
		newIncludes = [
			os.path.join( 'src', Togl ),
			os.path.join(tk.getvar('tk_library'), '..', '..', 'include'),
		]
		if not (self.tk_source or self.tcl_source):
			tk_version = tk.getvar( 'tk_version' )
			self.warn(
				"""Neither --tk-source nor --tcl-source specified for build_togl

    Unless your Tk and Tcl source-distribution headers and libraries are
    already on the system search path the building of Togl will likely
    fail.  To remedy the situation, download the Tk and Tcl sources from:

        https://sourceforge.net/project/showfiles.php?group_id=10894

    for version %(tk_version)s and unpack them into some directory
    somewhere.  Then specify:

        setup.py build_togl --tk-source=/path/to/source --tcl-source=/path/to/source

    on the command line for building PyOpenGL.""" % locals())

		if self.tk_source:
			if not self.tcl_source:
				tkDirs = tkDirs + tclDirs
			for fragment in tkDirs:
				directory = os.path.join( self.tk_source, fragment )
				if os.path.isdir( directory ):
					newIncludes.append( directory )
				else:
					self.warn(
						"""Warning, build_togl tk_source/%s (%s) doesn't exist, Togl build will likely fail!"""%(
							fragment, directory,
					))
		if self.tcl_source:
			if not self.tk_source:
				tclDirs = tkDirs + tclDirs
			for fragment in tclDirs:
				directory = os.path.join( self.tcl_source, fragment )
				if os.path.isdir( directory ):
					newIncludes.append( directory )
				else:
					self.warn(
						"""Warning, build_togl tcl_source/%s (%s) doesn't exist, Togl build will likely fail!"""%(
							fragment, directory,
					))
		self.include_dirs.extend( newIncludes )
		self.library_dirs.append( os.path.normpath(os.path.join(tk.getvar('tk_library'), '..')) )
		self.include_dirs.extend( self.distribution.include_dirs )
		self.library_dirs.extend( self.distribution.library_dirs )
		
		extra_compile_args = []

		if sys.platform == 'win32':
			# VC++ 6.0 needs this, why togl doesn't use _WIN32?
			extra_compile_args.append('-DWIN32=1')
			
			self.libraries.append('tcl' + string.replace(tk.getvar('tcl_version'), '.', ''))
			self.libraries.append('tk' + string.replace(tk.getvar('tk_version'), '.', ''))
			if Togl == 'Togl-1.6':
				self.libraries.append('tclstub' + string.replace(tk.getvar('tcl_version'), '.', ''))
				self.libraries.append('tkstub' + string.replace(tk.getvar('tk_version'), '.', ''))
		else:
			self.include_dirs.append(os.path.normpath(os.path.join(tk.getvar('tcl_library'), '..', '..', 'include')))
			
			self.library_dirs.append(os.path.normpath(os.path.join(tk.getvar('tcl_library'), '..')))
			
			self.libraries.append('tcl' + tk.getvar('tcl_version'))
			self.libraries.append('tk' + tk.getvar('tk_version'))

		if os.environ.has_key('CFLAGS'):
			extra_compile_args.extend(string.split(os.environ['CFLAGS']))

		# these should really be coming from the setup, shouldn't they?
		self.extra_compile_args = extra_compile_args


	def togl_build(self, libs):
		"""Core functionality of the togl_build command"""
		# we subclass build_ext because need an initialized
		# compiler object from build_ext, but we also need a pointer
		# to the build command instance
		build = self.get_finalized_command ('build')
		
		libs = libs + []
		
		extra_link_args = [] # ['-s']
		# Name for the shared lib: (distutils will change it to Togl.{so|dll})
		output_name = 'Togl'
		# where to put the built shared object (only for build process)
		output_dir = Togl + '-tk' + tk.getvar('tk_version')
		export_symbols = ['Togl_Init']
		sources = [os.path.join('src',Togl,'togl.c')]
		
		runtime_library_dirs = None


		# rest of this function was inspired by build_ext.py , build_extensions() 
		
		if not self.inplace:
			output_dir = os.path.join (build.build_base, output_dir)

		# what is the name of the resulting file
		output_filename = self.compiler.shared_object_filename(
				basename=output_name,
				output_dir=output_dir)

		if not (self.force or newer_group(sources, output_filename, 'newer')):
			self.announce ('skipping "%s" (up-to-date)' % output_name)  
		else:
			self.announce ('building "%s"' % output_name)

			# compile source files        
			objects = self.compiler.compile (sources,
								output_dir=self.build_temp,
								macros=[
									('USE_TCL_STUBS',1),
									('USE_TK_STUBS',1),
								],
								include_dirs=self.include_dirs,
								debug=self.debug,
								extra_postargs=self.extra_compile_args)

			# link all together
			self.compiler.link_shared_object (
					objects, 
					output_filename,
					'', # <= output_dir
					libraries=libs,
					library_dirs=self.library_dirs,
					runtime_library_dirs=runtime_library_dirs,
					extra_postargs=extra_link_args,
					export_symbols=export_symbols, 
					debug=self.debug,
					build_temp=self.build_temp)


class install(distutils.command.install.install):

	togl_outfiles = None

	def run(self):
		distutils.command.install.install.run(self)
		# togl_install can read instance variables of install_lib
		# it has to return the filenames of all installed files
		if tk is not None and self.distribution.BUILD_TOGL:
			self.togl_outfiles = togl_install(self) 


	def get_outputs(self):
		if self.togl_outfiles is None:
			if tk is not None and self.distribution.BUILD_TOGL:
				self.togl_outfiles = togl_install(self,dry_run=1)
			else:
				self.togl_outfiles = []
		return distutils.command.install.install.get_outputs(self) + self.togl_outfiles              



def replace_lib(include_dirs, path):
	components = [path]
	rep = 0
	while 1:
		head, tail = os.path.split(components[0])
		if tail:
			if tail == 'lib':
				rep = 1
				components[0] = 'include'
			else:
				components[0] = tail
			components.insert(0, head)
		else:
			break
	if rep:
		include_dirs.append(apply(os.path.join, components))


# build togl

	# building togl shared library

# togl_build    


from distutils.util import change_root
# install togl
#
# It is possibly to do this all in the build step, but then
# it is not included in a RPM distribution.
#

pkgIndex_tcl = r"""if {![package vsatisfies [package provide Tcl] 8]} {return}
package ifneeded Togl %(togl_version)s \
    [list load [file join $dir %(togl)s] Togl]"""

def togl_install(self,dry_run=0): # a simple function, not a class !!!

	outfiles = [] # we have to return all files we have installed
	
	# get path to Tk directory
	togl_dir = os.path.normpath(os.path.join(self.install_lib,'OpenGL','Tk', \
				sys.platform + '-tk' + tk.getvar('tk_version')))
	self.mkpath(togl_dir)       
	# how are the built files called, and 
	# which names should have the installed files
	if sys.platform == 'win32':
		togl = 'Togl.dll'
	else:
		togl = 'Togl.so'
	togl_src = os.path.join(self.build_base,
				Togl + '-tk' + tk.getvar('tk_version'), togl)
	togl_dst = os.path.join(togl_dir,togl)
	# copy togl in tk directory
	if not dry_run:
		from types import TupleType
		out = self.copy_file(togl_src, togl_dst)
		if type(out) is TupleType:
			out = out[0] 
	else:
		out = togl_dst
	outfiles.append(out)

	# make package index for tcl/tk
	indexFile = os.path.join( togl_dir, 'pkgIndex.tcl' )
	if not dry_run: 
		# only if real install
		self.announce( 'creating pkgIndex.tcl in %(togl_dir)s for %(togl)s'%locals())
		file = open( indexFile, 'w')
		togl_version = togl_version_decimal
		file.write( pkgIndex_tcl % locals())
		file.close()
	outfiles.append(indexFile)

	return outfiles
