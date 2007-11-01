#!/usr/bin/env python

import sys, os, os.path, re, string
from distutils.filelist import FileList
from util import *
import distutils.cmd

import traceback

import time, string

# re for CVS keywords
CVS_keyword = re.compile(r'[$][A-Za-z]+:\s+([^$]+?)\s+[$]')


def check_swig_version(swig_name):
	try:
		if hasattr( os, 'popen3'):
			sin,sout,stderr = os.popen3("%s -version" % swig_name)
			data = stderr.read()
		else:
			data = os.popen( "%s -version" % swig_name).read()
		if string.find(data,"1.3.23") == -1:
			return 0
		else:
			return 1
	except:
		if __debug__:
			traceback.print_exc(file = sys.stderr)
		return 0
	
def handle_wrong_swig_version():
	print "WARNING!!! wrong swig version.  Need 1.3.23, continuing anyway."
	time.sleep(3)


class build_w(distutils.cmd.Command):

	description = '"build" Python wrappers using SWIG.'

	user_options = [
		('force', 'f', "forcibly build everything (ignore file timestamps)"),
		]

	boolean_options = ['force']


	def initialize_options (self):
		self.force = None


	def finalize_options (self):
		self.set_undefined_options('build', ('force', 'force'))


	def run (self):
		# try to run swig
		self.swig_name = None
		
		for swig_name in ('swig', 'swig1.3'):
			try:
				# should do a version check
				self.spawn([swig_name, '-version'])
				self.swig_name = swig_name
				if not check_swig_version(swig_name):
					handle_wrong_swig_version()
					self.swig_name = None
				break
			except:
				pass

		# if brain dead spawn doesn't work...
		if self.swig_name is None:
			for swig_name in ('swig', 'swig1.3'):
				try:
					r = os.system("%s -version" % swig_name)
				except:
					r == 99999999
					if r == 256:
						self.swig_name = swig_name

						if not check_swig_version(swig_name):
							handle_wrong_swig_version()

						# found the swig name, stop checking.
						break
			

		if self.swig_name is None:
			self.warn("Can't find SWIG, will just have to do with the existing wrapper source.")
		else:
			self.mkpath('src/interface')
			self.mkpath('src/shadow')
	
			interfaces = []
			f = FileList()
			f.findall('interface')
			f.process_template_line('global-include *.i')
			f.files.sort()
			for file in f.files:
				interfaces.append(string.join(string.split(os.path.splitext(file)[0], os.sep)[1:], '.'))
			interfaces.sort()
	
			for full_module_name in interfaces:
				self.swig(full_module_name)


	def make_version_selector(self, path, config_path, pre_text, version_text, post_text, BUILD):
		module_name = os.path.splitext(os.path.basename(path))[0]
		f = open(path, 'w')
		# not really sure if we need to propagate the BUILD, specifically the libs value, to the C file
		# build_ext doesn't need it but build_py may.  If distutils supported preprocessing better than
		# we wouldn't need to link in in build_py, hence wouldn't need to to propagate the BUILD info.
		f.write('/*\n')
		for key, item in BUILD.items():
			# write the build info, but don't include stuff that setup.py doesn't need
			if key not in ('shadow', 'macro_template', 'api_versions', 'headers'):
				f.write('# BUILD %s %s\n' % (key, repr(item)))
		f.write('*/\n')
		# the headers including any needed by the module
		f.write('#include "%s"\n' % config_path)
		for header in BUILD['headers']:
			f.write('#include <%s>\n' % header)
		f.write('\n')

		f.write(pre_text)
		if BUILD.has_key('macro_template'):
			for i in range(len(BUILD['api_versions'])):
				# api_version_underscore should be a matter of convenience, but SWIG's preprocessor is dysfunctional
				api_version_underscore = '%d_%d' % ((BUILD['api_versions'][i] & 0xff00) >> 8, BUILD['api_versions'][i] & 0xff)
				# setup the testing macro
				macro = BUILD['macro_template'] % {'api_version':BUILD['api_versions'][i], 'api_version_underscore':api_version_underscore}
				if i == 0:
					f.write('#if ' + macro + '\n')
				elif not BUILD['api_version_check'] and i+1 == len(BUILD['api_versions']):
					f.write('#else\n')
				else:
					f.write('#elif ' + macro + '\n')
				f.write(version_text % BUILD['api_versions'][i])
			if BUILD['api_version_check']:
				f.write('#else\n')
				f.write('#error "Do not know how to compile %s for API version < 0x%04x"\n' % (module_name, BUILD['api_versions'][-1]))
			f.write('#endif\n')
		elif len(BUILD['api_versions']) > 1:
			print 'Multiple API versions specified for %s but no macro template provided!' % module_name
			sys.exit(1)
		else:
			f.write(version_text % BUILD['api_versions'][0])
		f.write(post_text)
		f.close()


	def make_wrappers(self, swig_cmd, module_name, source_path, shadow_path):
		self.swig_just_ran = 1
		try:
			# this shouldn't be req, but SWIG seems to like it
			os.remove(source_path)
		except:
			pass

		try:
			self.spawn(swig_cmd)

			if not os.path.exists(source_path):
				sys.exit(1)

			if shadow_path:
				# copy the shadow script
				t = module_name + '.py'
				# SWIG isn't very consistent in its placement of the shadow script
				for f in [t, os.path.join('src', t), os.path.join('src', 'interface', t), os.path.join( 'src','shadow',t)]:
					if os.path.exists(f):
						# does this screw up things on the Mac?
						x = open(f).read()
						x = string.replace(x, module_name + 'c', module_name + '_')
						open(shadow_path, 'w').write(x)
						os.remove(f)
						break

			f = open(source_path)
			x = f.read()
			f.close()
			# replace CVS keywords
			x = CVS_keyword.sub(r'\1', x)
			x = string.replace(x, module_name + 'c', module_name + '_')
			# find all the docstrings and put them into the function table
			for method in re.findall('static char _doc[_]([^[\s]+)', x):
				x = re.sub(
					r'[{]\s*\(\s*char\s*\*\s*\)\s*"%s"\s*,\s*([^ ",]+)\s*,\s*([^,"}]+)[}]' % method,
					r'{ (char *)"%s", \1, \2, _doc_%s}' % (method, method),
					x
				)
			f = open(source_path, 'w')
			f.write(x)
			f.close()
		except:
			if os.path.exists(source_path):
				os.remove(source_path)
			sys.exit(1)

		
	def swig(self, full_module_name):
		global CVS_keyword

		self.announce('Building wrappers for %s' % full_module_name)

		# split the full module name into the short name and the path
		m = string.split(full_module_name, '.')
		module_name = m[-1]
		if len(m) == 1:
			module_path = ''
		else:
			module_path = apply(os.path.join, m[:-1])

		# the swig cmd line
		swig_cmd = [self.swig_name, '-python', '-Iinterface']

		# create the req paths and figure out the interface name	
		base_path = apply(os.path.join, m)
		self.mkpath(string.join(['OpenGL'] + m[:-1], '/'))
		interface_path = os.path.join('interface', base_path + '.i')

		# retrieve the build info
		BUILD = get_build_info(interface_path)

		if BUILD['shadow']:
			mkdir(os.path.join('src', 'shadow'))
			# if this is a shadow interface then append a '_' to the end of the c module name
			m2 = m[:]
			m2[-1] = '_' + m2[-1]
			c_full_module_name = '.'.join( m2 )
			c_module_name = m2[-1]
			# insert the shadow option
			swig_cmd.append('-shadow')
			# figure out the script names
			shadow_version_selector_path = os.path.join('src', 'shadow', full_module_name + '.c')
			self.make_file([interface_path],
						   shadow_version_selector_path,
						   self.make_version_selector,
						   (shadow_version_selector_path,
							'src/config.h',
							'#include <stdio.h>\n\nint main(int argc, char **argv)\n{\n\tFILE *f = fopen("api_version", "w");\n',
							'\tfprintf(f, "%d");\n',
							'\tfclose(f);\n\treturn 0;\n}\n',
							BUILD),
						   exec_msg = 'Generating shadow version selector',
						   skip_msg = "Shadow version selector doesn't need updating")
		else:
			# no modification of the module name needed
			c_full_module_name = full_module_name
			c_module_name = module_name

		# fiqure out the interface source names
		src_wrapper_path = os.path.join('src', 'interface', c_full_module_name + '.c')

		c_version_selector_path = os.path.join('src', 'interface', c_full_module_name + '.c')
		self.make_file([interface_path],
					   c_version_selector_path,
					   self.make_version_selector,
					   (c_version_selector_path,
						'../config.h',
						'',
						'#include "%s.%%04x.inc"\n' % c_full_module_name,
						'',
						BUILD),
					   exec_msg = 'Generating C version selector',
					   skip_msg = "C version selector doesn't need updating")


		source_path_template = os.path.join('src', 'interface', c_full_module_name + '.%04x.inc')
		shadow_path_template = os.path.join('src', 'shadow', full_module_name + '.%04x.py')

		for api_version in BUILD['api_versions']:
			# fiqure out the paths
			source_path = source_path_template % api_version
			if BUILD['shadow']:
				shadow_path = shadow_path_template % api_version
				outfiles = (source_path, shadow_path)
			else:
				shadow_path = ''
				outfiles = (source_path,)

		
			this_swig_cmd = swig_cmd + ['-DAPI_VERSION=%d' % api_version, '-o', source_path, interface_path]

			self.swig_just_ran = 0
			args = (this_swig_cmd, module_name, source_path, shadow_path)
			exec_msg = 'Generating wrappers for API version 0x%04x' % api_version
			skip_msg = "Wrappers for API version 0x%04x don't need updating" % api_version

			for outfile in outfiles:
				if self.swig_just_ran:
					break
				self.make_file([interface_path],
							   outfile,
							   self.make_wrappers,
							   args,
							   exec_msg = exec_msg,
							   skip_msg = skip_msg)

		self.announce('')
		
