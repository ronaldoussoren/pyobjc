"""Setup general build environment for PyOpenGL

This is where most of the "magic" occurs in PyOpenGL's
setup.  This module is responsible for determining the
config files to use, and ultimately, the packages to
install.
"""
import distutils.dist
from setup.util import *
import sys, os, os.path, string, re
from ConfigParser import ConfigParser
from distutils.core import setup,Extension
from distutils.sysconfig import *
from distutils.filelist import FileList

def find_file_visit(arg, dirname, names):
	name, dirs = arg
	if name in names:
		dirs.append(dirname)
	

def find_file(root, name):
	dirs = []
	os.path.walk(root, find_file_visit, (name, dirs))
	return dirs


def config_list(x):
	l = map(string.strip, string.split(x, os.pathsep))
	while l.count(''):
		l.remove('')
	return l


class Distribution(distutils.dist.Distribution):

##	def find_config_files(self):
##		files = distutils.dist.Distribution.find_config_files(self)
##		config_name = os.path.join('config', sys.platform + '.cfg')
##		print files
##		if os.path.exists(config_name):
##			files.append(config_name)
##		else:
##			print 'sdf'
##		return files


	def finalize_options(self):
		distutils.dist.Distribution.finalize_options(self)

		cfg = ConfigParser()
		name = sys.platform
		config_name = os.path.join('config', name + '.cfg')
		while len(name) and not os.path.exists(config_name):
			name = name[:-1]
			config_name = os.path.join('config', name + '.cfg')

		if not os.path.exists(config_name):
			print "Can't find a config file for the \"%s\" platform.  Look in the config directory." % sys.platform
			sys.exit(1)

		try:
			self.announce( "Using cfg file: %s"%( config_name,))
			cfg.read(config_name)
		except ParsingError:
			print "parse error in config file."
			sys.exit(1)

		self.lib_aliases = {}

		for section in cfg.sections():
			if section != 'General':
				try:
					self.lib_aliases[section] = config_list(cfg.get(section, 'libs'))
				except:
					pass

		try:
			self.include_dirs = config_list(cfg.get('General', 'include_dirs'))
		except:
			self.include_dirs = []

		try:
			self.library_dirs = config_list(cfg.get('General', 'library_dirs'))
		except:
			self.library_dirs = []

		try:
			self.BUILD_TOGL = cfg.getint('General', 'build_togl')
		except:
			self.BUILD_TOGL = 0
			
		try:
			self.extra_link_args = config_list(cfg.get('General', 'extra_link_args'))
		except:
			self.extra_link_args = []

		try:
			self.define_macros = [(string.upper(string.strip(cfg.get('General', 'gl_platform'))) + '_PLATFORM', None)]
			self.gl_platform = cfg.get('General', 'gl_platform')
		except:
			self.define_macros = []
			print 'No gl_platform defined in the config file "%s"' % config_name

		self.togl_libs = self.transform_libs(['GL', 'GLU', 'Togl'])

##		build_togl = self.get_command_obj( 'build_togl' )
##		for field in ('tk-source','tcl-source'):
##			if not getattr(build_togl, field, None):
##				try:
##					setattr(build_togl, field.replace('-','_'), cfg.get('Togl', field))
##				except:
##					pass
		
		try:
			import Numeric
			include_dirs = find_file(get_python_inc(), 'arrayobject.h')
			if not len(include_dirs):
				self.announce("Successfully imported Numeric, but can't find the Numeric headers!")
				self.HAS_NUMERIC = 0
			else:
				self.include_dirs = self.include_dirs + include_dirs
				self.HAS_NUMERIC = 1
		except ImportError:
			self.HAS_NUMERIC = 0

		if self.HAS_NUMERIC:
			Numeric_version = 'yes'
			self.define_macros.append(('NUMERIC', None))
			try:
				import numeric_version
				Numeric_version = numeric_version.version
##				if int(string.split(Numeric_version, '.')[0]) == 20:
##					self.announce('Numeric %s is present...beware!  This is buggy!')
			except:
				pass
		else:
			Numeric_version = 'no'

		boolean = ['no', 'yes']

		self.announce('PyOpenGL %s setup' % self.get_version())
		self.announce('')
		self.announce('System configuration:')
		self.announce('    Platform    = %s' % sys.platform)
		self.announce('    GL Platform = %s' % self.gl_platform)
		self.announce('    Numeric     = %s' % Numeric_version)
		self.announce('    Build Togl  = %s' % boolean[self.BUILD_TOGL])
		self.announce('')

		# get the list of platforms
		self.announce('Getting the list of platforms...')
		self.metadata.platforms = []
		f = FileList()
		f.findall('config')
		f.process_template_line('global-include *.cfg')
		for file in f.files:
			self.metadata.platforms.append(os.path.splitext(os.path.split(file)[1])[0])

		# get the list of packages for this platform
		self.announce('Getting the list of packages...')
		if self.packages is None:
			self.packages = []
		f = FileList()
		# first the real packages
		if os.path.exists('OpenGL'):
			f.findall('OpenGL')
			f.process_template_line('global-include __init__.py')
			# second the Demo's
			Demo = os.path.join('OpenGL', 'Demo')
			if os.path.exists(Demo):
				f.findall(Demo)
				f.process_template_line('global-include *.py')
			# last the scripts
			scripts = os.path.join('OpenGL', 'scripts')
			if os.path.exists(scripts):
				f.findall(scripts)
				f.process_template_line('global-include *.py')
		for file in f.files:
			package = string.replace(os.path.dirname(file), os.sep, '.')
			if package not in self.packages:
				g = {'__name__':'__build__'}
				l = {}
				try:
					exec open(file) in g, l
				except:
					pass
				if not l.has_key('gl_platforms') or self.gl_platform in l['gl_platforms']:
					self.packages.append(package)

		# get the list of extension modules for this platform
		self.announce('Getting the list of extension modules...')
		if self.ext_modules is None:
			self.ext_modules = []

		f = FileList()
		f.findall('interface')
		f.process_template_line('global-include *.i')
		if not len(f.files):
			print "Whoa!  I can't find any interfaces...panic!"
			sys.exit()

		f.files.sort()
		for file in f.files:
			BUILD = get_build_info(file)
			actual_libs = []

			if not BUILD.has_key('gl_platforms') or self.gl_platform in BUILD['gl_platforms']:
				# everything requires GL and GLU
				libs = ['GL', 'GLU']
				if BUILD.has_key('libs'):
					libs.extend(BUILD['libs'])


				directory,name = os.path.split( os.path.splitext(file)[0] )
				module = ".".join(
					directory.split( os.sep)[1:] +
					[ '_'+ name ],
				)

				BUILD['sources'].append('src/interface/' + module + '.c')
				self.ext_modules.append(Extension(module,
												  BUILD['sources'],
												  include_dirs = BUILD['include_dirs'],
												  define_macros = self.define_macros,
												  libraries = self.transform_libs(libs),
												  library_dirs = self.library_dirs,
												  extra_link_args = self.extra_link_args))

#		print self.libraries
		l = []
		for i in range(len(self.libraries)):
			d = self.libraries[i][1]
			d['include_dirs'] = [get_python_inc()] + self.include_dirs
			d['macros'] = self.define_macros
			l.append((self.libraries[i][0], d))
		self.libraries = l


##	def parse_config_files(self, filenames=None):
##		distutils.dist.Distribution.parse_config_files(self, filenames)
##		self.dump_option_dicts()
##		print self.include_dirs
##


	def transform_libs(self, libs):
		# should do checks to see if the libs exist
		new_libs = []
		for lib in libs:
			if self.lib_aliases.has_key(lib):
				for new_lib in self.lib_aliases[lib]:
					if new_lib not in new_libs:
						new_libs.append(new_lib)
			else:
				if lib not in new_libs:
					new_libs.append(lib)
		return new_libs

		