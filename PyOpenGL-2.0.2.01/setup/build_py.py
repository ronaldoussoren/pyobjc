from distutils import file_util
import distutils.command.build_py
import distutils.command.config
from distutils.sysconfig import *
from distutils.errors import *
from distutils.filelist import FileList
from util import *
import os, sys, string
from stat import ST_MODE


class build_py(distutils.command.build_py.build_py, distutils.command.config.config):

	def initialize_options (self):
		distutils.command.build_py.build_py.initialize_options(self)
		distutils.command.config.config.initialize_options(self)


	def finalize_options (self):
		distutils.command.build_py.build_py.finalize_options(self)
		distutils.command.config.config.finalize_options(self)
		self.include_dirs = self.include_dirs + [get_python_inc()]
		self.library_dirs = self.library_dirs + [get_python_lib()]

		# for extensions under windows use different directories
		# for Release and Debug builds.
		# also Python's library directory must be appended to library_dirs
		if os.name == 'nt':
			self.library_dirs.append(os.path.join(sys.exec_prefix, 'libs'))

		# for extensions under Cygwin Python's library directory must be
		# appended to library_dirs
		if sys.platform[:6] == 'cygwin':
			if string.find(sys.executable, sys.exec_prefix) != -1:
				# building third party extensions
				self.library_dirs.append(os.path.join(sys.prefix, "lib", "python" + sys.version[:3], "config"))
			else:
				# building python standard extensions
				self.library_dirs.append('.')



	def run(self):
		self._check_compiler()
		customize_compiler(self.compiler)
		for name, value in self.distribution.define_macros:
			self.compiler.define_macro(name, value)
		self.dump_source = 0
		f = FileList()
		f.process_template_line('include src/shadow/*.c')
		for file in f.files:
			try:
				BUILD = get_build_info(file)
				#if (not BUILD.has_key('platform_include') or sys.platform in BUILD['platform_include']) and (not BUILD.has_key('platform_exclude') or sys.platform not in BUILD['platform_exclude']):
				if not BUILD.has_key('gl_platforms') or self.distribution.gl_platform in BUILD['gl_platforms']:
					libs = ['GL', 'GLU']
					headers = []
					if BUILD.has_key('libs'):
						libs.extend(BUILD['libs'])
					if BUILD.has_key( 'include_dirs' ):
						headers = BUILD['include_dirs']
					self.libraries = self.distribution.transform_libs(libs)
					self.try_run(
						open(file).read(),
						library_dirs = self.distribution.library_dirs,
						include_dirs = self.distribution.include_dirs + headers,
					)
					api_version_string = open('api_version').read()
					if not api_version_string:
						self.warn( """No current api_version_string, expect %s to be improperly generated"""%( file, ))
						src = os.path.join(
							os.path.splitext(file)[0]+ '.py'
						)
					else:
						# has an api_version_string
						src = os.path.join(
							os.path.splitext(file)[0]+ '.%04x.py' % string.atoi(api_version_string)
						)
					names = string.split(os.path.splitext(os.path.split(file)[1])[0], '.')
					dest = self.get_module_outfile(self.build_lib, ['OpenGL'] + names[:-1], names[-1])
					self.mkpath(os.path.split(dest)[0])
					self.copy_file(src, dest)
					os.remove('api_version')
			except:
				import traceback
				traceback.print_exc()
				self.warn( """Failure compiling version-selector, likely will be missing shadow modules for %r"""%( file,))
			
		distutils.command.build_py.build_py.run(self)


	def copy_file (self, infile, outfile, preserve_mode=1, preserve_times=1, link=None, level=1):
		"""Copy a file respecting verbose, dry-run and force flags.  (The
		   former two default to whatever is in the Distribution object, and
		   the latter defaults to false for commands that don't define it.)"""

		i = open(infile)
		line = i.readline()
		
		mode_change = len(line) > 1 and line[:2] == '#!' and os.name == 'posix'
		adjust = string.rstrip(line) == '#!' and os.name == 'posix' and not self.dry_run
		
		if adjust:
			o = open(outfile, 'wt')
			o.writelines(['#!%s\n' % sys.executable] + i.readlines())
			x = (outfile, 1)
		else:
			x = file_util.copy_file(infile, outfile, preserve_mode, preserve_times, not self.force, link, self.verbose >= level, self.dry_run)
			
		if mode_change:
			if self.dry_run:
				self.announce("changing mode of %s" % outfile)
			else:
				mode = (os.stat(outfile)[ST_MODE]) | 0111
				self.announce("changing mode of %s to %o" % (outfile, mode))
				os.chmod(outfile, mode)

		return x


	def get_outputs(self, include_bytecode=1):
		outputs = []
		f = FileList()
		f.process_template_line('include src/shadow/*.c')
		for file in f.files:
			try:
				BUILD = get_build_info(file)
				#if (not BUILD.has_key('platform_include') or sys.platform in BUILD['platform_include']) and (not BUILD.has_key('platform_exclude') or sys.platform not in BUILD['platform_exclude']):
				if not BUILD.has_key('gl_platforms') or self.distribution.gl_platform in BUILD['gl_platforms']:
					names = string.split(os.path.splitext(os.path.split(file)[1])[0], '.')
					dest = self.get_module_outfile(self.build_lib, ['OpenGL'] + names[:-1], names[-1])
					outputs.append(dest)
					if include_bytecode:
						if self.compile:
							outputs.append(dest + "c")
						if self.optimize > 0:
							outputs.append(dest + "o")
			except:
				import traceback
				traceback.print_exc()
			
		return outputs + (distutils.command.build_py.build_py.get_outputs(self, include_bytecode) or [])


	# Copied from config to fix bug
	def try_run (self, body,
				 headers=None, include_dirs=None,
				 libraries=None, library_dirs=None,
				 lang="c"):
		"""Try to compile, link to an executable, and run a program
		built from 'body' and 'headers'.  Return true on success, false
		otherwise.
		"""
		from distutils.ccompiler import CompileError, LinkError
		self._check_compiler()
		try:
			src, obj, prog = self._link(body, headers, include_dirs,
							   libraries, library_dirs, lang)
			self.spawn([prog])
			ok = 1
		except (CompileError, LinkError, DistutilsExecError):
			ok = 0

		self._clean()
		return ok


	def _link (self, body,
			   headers, include_dirs,
			   libraries, library_dirs, lang):
		(src, obj) = self._compile(body, headers, include_dirs, lang)
		prog = os.path.splitext(os.path.basename(src))[0]
		self.compiler.link_executable([obj], prog,
									  libraries=libraries,
									  library_dirs=library_dirs)
		if sys.platform == 'win32':
			prog = prog + '.exe'
		self.temp_files.append(prog)
		return (src, obj, prog)

