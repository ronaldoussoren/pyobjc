#!/usr/bin/env python
"""Builds different documentation formats from docbook src

Here's the basic approach:
	A driver file defines system entities point to source-files
		(manual.xml)
	On reading the driver file, the parser pulls together all
	of the source-files into one big document.

	For the reference-manual, we merge in Python-specific
	annotations from a seperate directory tree with a (slow)
	merge.xsl template.

	Once we have the merged file, we can use the docbook-xsl
	templates to generate html, htmlhelp, or xhtml documents.
	Apparently we can also use latex/pdflatex if we have them
	to process this docbook file.

	For HTML files, we run David Carlisle' mathml XSL
	stylesheets in stand-alone mode to create IE-compatible
	HTML (with Javascript).

Note:
	This process is slow, even with Saxon (which is fairly
	fast).  It's untenably slow with the 4Suite XSLT package.

XXX Plans/desires:

	Eventually, I want to break the processing up into multiple
	distutils commands to allow for explicitly specifying which
	commands should be run, rather than having a single channel
	which decides which parts of itself to run:

		doc_merge_python -- merge individual sections with python
			annotations into combined document fragments
		doc_collect -- collect all individual section document
			fragments into a single large manual document
		doc_merge_samples -- add sample sections to the manual
		doc_build_xhtml -- use docbook-xsl to generate xHTML files
		doc_build_html -- convert xhtml to html
			doc_convert_mathml -- process html to make the html files
				work under IE 5 and 6
		doc_build_htmlhelp -- use docbook-xsl to generate HTMLHelp
			files
			doc_convert_mathml -- process html to make the html files
				work under IE 5 and 6

	and make the individual stages capable of optimizing in
	such a way that changing a particular python-specific
	document will only require merging that particular document
	and integrating it into the already-built manual, then
	running the appropriate doc_build_XXX commands. This will
	require completely rewriting the merge.xsl style sheet,
	and the driver code for manipulating it, as well as the
	build directory structure for holding the temporary files.

	I would also like to parameterize most of the functions
	so that we can generate/process the manual in non-standard
	places (to allow for, for instance, a special doc_build_html
	run which uses doc_merge_samples to not overwrite the
	standard manual).

	Should also eliminate the practice of directly writing to the
	OpenGL/doc directory during building, as this will cause
	problems if later build procedures fail.  Should generate the
	documents entirely within the build tree, and only copy them on
	complete success.
"""
import sys, os, os.path, re, string
from distutils.filelist import FileList
from distutils.errors import *
from util import *
import distutils.cmd
import glob, shutil

def show_formats ():
	"""Print all possible values for the 'formats' option (used by
	the "--help-formats" command-line option).
	"""
	from distutils.fancy_getopt import FancyGetopt
	formats=['html', 'xhtml', 'htmlhelp']
	formats.sort()
#	pretty_printer = FancyGetopt(formats)
#	pretty_printer.print_help(
#		"List of available source distribution formats:")


code_re = re.compile('&#([0-9]+);')

MATHPLAYER_BOILERPLATE = """
<object id="MathPlayer" classid="clsid:32F66A20-7614-11D4-BD11-00104BD3F987"></object>
<?import namespace="mml" IMPLEMENTATION="#MathPlayer" ?>
"""

CUSTOM_XSL = os.path.join("doc","xsl","html")
DOCBOOK_XSL_HOME = os.path.join("doc","docbook-xsl")
DOCBOOK_DTD_HOME = os.path.join("doc","docbook")
MATHML_CSS_HOME = os.path.join("doc","xsl","mathml")


class build_doc(distutils.cmd.Command):
	"""Build HTML/XHTML documentation for PyOpenGL"""
	description = '"build" documentation.'

	user_options = [
		('force', 'f', "forcibly build everything (ignore file timestamps)"),
		('formats=', None, 'Formats for documentation'),
		('kaffe', 'k', 'Use Kaffe instead of Java'),
		]

	boolean_options = ['force']

	help_options = [
		(
			'help-formats', None,
			'list available distribution formats', show_formats
		),
	]
	def initialize_options (self):
		self.force = None
		self.formats = None
		self.kaffe = None
	def finalize_options (self):
		self.set_undefined_options('build', ('force', 'force'))
		self.ensure_string_list('formats')
		if self.formats is None:
			self.formats = ['html']
		if 'all' in self.formats:
			self.formats = ['html', 'xhtml', 'web', 'htmlhelp']
		if self.kaffe:
			self.java = 'kaffe'
			self.acp = '-addclasspath'
		else:
			self.java = 'java'
			self.acp = '-cp'

	### Overall driver for process
	def run(self):
		"""The primary driver for the documentation-building system
		"""
		## Build our Java class-path value
		paths = []
		for (variable,jarName, packageName) in [
			("SAXON_HOME", "saxon.jar", "Saxon XSL Processor"),
			("RESOLVER_HOME","resolver.jar", "Sun Resolver XML Package"),
		]:
			if not os.environ.has_key(variable):
				self.warn( """Could not find %(variable)s environmental variable.
Install %(packageName)s and set environmental variable %(variable)s to point
to the directory holding %(jarName)s.
Aborting documentation generation."""%locals() )
				return
			paths.append( os.path.join(os.environ[variable], jarName) )
		# Add the docbook-xsl extensions
		os.path.join(DOCBOOK_XSL_HOME, 'extensions', 'saxon643.jar')
		for path in paths:
			if not os.path.isfile( path ):
				self.warn( """The class-path value %s does not appear to be a valid file, errors may result.  Please check environmental variables."""%(path,) )
		# Following puts the CatalogManager.properties file on the
		# path, though that doesn't seem to actually help much in
		# reducing reliance on networked files :( 
		paths.append( DOCBOOK_DTD_HOME )
		self.cp = string.join( paths, os.pathsep )

		f = FileList()
		f.findall('doc')
		f.process_template_line('global-include *.xml')
		manualTemp = os.path.join('build', 'doc', 'manual.xml')
		self.make_file(
			f.files,
			manualTemp,
			self.merge_doc,
			(
				os.path.join('doc', 'manual', 'manual.xml'),
				manualTemp,
			),
			exec_msg = 'Merging manpages and Python-specific documentation',
			skip_msg = 'Manpages already merged with Python-specific documentation'
		)

		for format in self.formats:
			name = 'run_' + format
			if hasattr(self, name):
				self.announce( """Building format %s"""%( format,))
				getattr(self, name)()	
			else:
				self.announce( """No support available for format %s"""%( format,))

	### Pre-processing to generate the docbook document from which all formats are generated
	def merge_doc(self, source, destination, **arguments ):
		"""Merge reference document with Python-specific annotations"""
		arguments['output'] = destination
		arguments['PyOpenGL_version']= self.distribution.get_version()
		rValue = apply(
			self.saxon, (
				os.path.join('doc', 'xsl', 'merge.xsl'),
				source,
			),
			arguments
		)
		# copy so that we have a backup if the later processing
		# mucks up the merged document...
		self.copy_file(destination, os.path.join('OpenGL','doc'))
		return rValue

	### Format-specific drivers
	def run_html(self):
		"""Top-level command for generating HTML documentation"""
		self.build_xhtml('.html', os.path.join('OpenGL','doc','html'), self.fix_html_mathmlcss)


	def run_xhtml(self):
		"""Top-level command for generating XHTML documentation"""
		self.build_xhtml('.xml', os.path.join('OpenGL','doc','xhtml'), self.fix_xhtml_ns)


	def gen_xhtml(self, ext, base_dir):
		"""Generate xhtml documentation to base_dir with file extensions ext"""
		try:
			self.saxon(
				os.path.join('doc', 'xsl', 'html', 'xhtml_chunk.xsl'),
				os.path.join('build', 'doc', 'manual.xml'),
				base_dir = base_dir + '/',
				html_ext = ext
			)
		except:
			self.rmtree(base_dir)
			raise


	def build_xhtml(self, ext, base_dir, cleanupFunction=None):
		"""Build an xhtml documentation set, running cleanupFunction afterward"""
		self.make_file(
			[os.path.join('build','doc','manual.xml')],
			os.path.join(base_dir , 'index' + ext),
			self.gen_xhtml,
			(ext, base_dir)
		)
		if cleanupFunction:
			cleanupFunction(
				os.path.join( base_dir, '*' + ext )
			)
	def copy_misc( self, base_dir ):
		"""Copy miscellaneous formatting files to a base_dir"""
		self.copy_file(os.path.join('doc','misc','style.css'), base_dir)
		self.copy_file(os.path.join('doc','misc','greypinstripe.png'), base_dir)

	def run_htmlhelp(self):
		"""Generate MS HTMLHelp documentation"""
		self.make_file(['build/doc/manual.xml'],
		               'build/doc/htmlhelp/index.html',
		               self.gen_html,
		               ('build/doc/htmlhelp', 'build/doc/htmlhelp', 'htmlhelp.xsl'))

		self.mkpath('build/doc/htmlhelp')

		for file in ('manual.hhp', 'manual.hhc'):
			if os.path.exists(file):
				x = open(file).read()
##				x = string.replace(x, 'build/doc/htmlhelp_raw/', '')
				x = string.replace(x, 'build/doc/htmlhelp/', '')
				open(os.path.join('build', 'doc', 'htmlhelp', file), 'w').write(x)
				os.remove(file)
			
#		self.move_file('manual.hhp', 'build/doc/htmlhelp')
#		self.move_file('toc.hhc', 'build/doc/htmlhelp')
		
##		self.make_file(['build/doc/htmlhelp_raw/index.html'],
##		               'build/doc/htmlhelp/index.html',
##		               self.xform_html,
##		               ('build/doc/htmlhelp_raw', 'build/doc/htmlhelp'))

		self.copy_file('doc/misc/style.css', 'build/doc/htmlhelp')
		self.copy_file('doc/misc/greypinstripe.png', 'build/doc/htmlhelp')
	
		f = FileList()
		f.findall('build/doc/htmlhelp')
		f.process_template_line('global-include *')
		self.make_file(f.files,
		               'build/doc/htmlhelp/manual.chm',
		               self.hhc,
		               ())

		self.copy_file('build/doc/htmlhelp/manual.chm', 'OpenGL/doc')

	def hhc(self):
		"""Spawn the HTMLHelp compiler"""
		try:
			self.spawn(['hhc', os.path.join('build', 'doc', 'htmlhelp', 'manual.hhp')])
		except DistutilsExecError, e:
			print e
			

	def pdflatex(self):
		for i in range(3):
			self.spawn(['pdflatex', '&pdfxmltex', 'manual.xml'])


	def latex(self):
		for i in range(3):
			self.spawn(['latex', '&xmltex', 'manual.xml'])


	### Utility functions
	def saxon(self, xsl, source, output = None, **params):
		"""Run the saxon XSL processor in our environment

		Most functions wind up working through this method
		one way or another.  Basically anything which uses
		XSL transformations will call this method
		"""
		saxon_cmd = [self.java,
		             self.acp,
		             self.cp,
		             'com.icl.saxon.StyleSheet',
		             '-x',
		             'com.sun.resolver.tools.ResolvingXMLReader',
		             '-y',
		             'com.sun.resolver.tools.ResolvingXMLReader',
		             '-r',
		             'com.sun.resolver.tools.CatalogResolver']
		if output is not None:
			saxon_cmd.extend(['-o', output])
		saxon_cmd.extend([source, xsl])
		for key, value in params.items():
			saxon_cmd.append('%s=%s' % (string.replace(key, '_', '.'), value))
		self.spawn(saxon_cmd)



	def fix_xhtml_ns(self, path):
		"""Minor postprocessing to add namespace declarations for xhtml compliance"""
		self.announce('Fixing XHTML namespace attribute: %s'%(path,))
		for i in glob.glob(path):
			if os.path.isfile(i):
				x = open(i).read()
				if string.count(x, '<html>'):
					x = string.replace(x, '<html>', """<html
	xmlns="http://www.w3.org/1999/xhtml"
	xmlns:mml="http://www.w3.org/1998/Math/MathML"
>""")
					open(i, 'w').write(x)
	def fix_html_mathmlcss( self, path ):
		"""Use the MathML XSL->CSS style sheet to convert xhtml->html"""
		self.announce('Doing xhtml->html+css conversion: %s'%(path,))
		requireExtra = []
		def target( filename ):
			"""Return .html version of filename"""
			return os.path.splitext( filename )[0]+ '.html'
		for i in glob.glob(path):
			if os.path.isfile(i):
				targetName = target( i )
				x = open(i).read()
				if x.find('mml:') > -1:
					requireExtra.append( (i, targetName) )
				x = string.replace(x, '<html>', """<html
xmlns:mml="http://www.w3.org/1998/Math/MathML"
>""")
##				if x.find('mml:') > -1:
##					x = finder.sub( r'%s</head'%(MATHPLAYER_BOILERPLATE), x )
				open(targetName, 'w').write(x)
		for filename, targetName in requireExtra:
			self._fix_html_mathmlcss( targetName, targetName )
	def _fix_html_mathmlcss( self, source, target ):
		"""Do single MathML->HTML+CSS conversion"""
		self.announce('MathML Render: %s'%(source, ))
		self.saxon(
			os.path.join(MATHML_CSS_HOME, 'pmathmlcss.xsl'),
			source,
			target,
		)

	def fix_html_mathplayer(self, path):
		"""Add IE+MathPlayer specific support to HTML files (obsolete)"""
		self.announce('Adding MathPlayer support to files: %s'%(path,))
		
		finder = re.compile( "\<\/head" )
		for i in glob.glob(path):
			if os.path.isfile(i):
				x = open(i).read()
				x = string.replace(x, '<html>', """<html
xmlns:mml="http://www.w3.org/1998/Math/MathML"
>""")
				if x.find('mml:') > -1:
					x = finder.sub( r'%s</head'%(MATHPLAYER_BOILERPLATE), x )
				open(i, 'w').write(x)

	def rmtree(self, dir):
		"""Forcibly recursively remove a directory tree

		Note: this isn't cross-platform at the moment...
		"""
		try:
			shutil.rmtree(apply(os.path.join, string.split(dir, '/')))
		except:
			pass

				