import sys, string
from distutils.core import Command
from distutils.util import *


if sys.platform == 'win32':
	try:
		from win32com.shell import shell
		import pythoncom
		create_shortcuts = 1
	except ImportError:
		create_shortcuts = 0
else:
	create_shortcuts = 0


shortcuts = ({'name':'PyOpenGL/Documentation/PyOpenGL Manual - HTMLHelp',
			  'description':'PyOpenGL Manual in HTMLHelp format.',
			  'path':'$lib/OpenGL/doc/manual.chm'},
			 {'name':'PyOpenGL/Documentation/PyOpenGL Manual - HTML',
			  'description':'PyOpenGL Manual in HTML format.',
			  'path':'$lib/OpenGL/doc/html/index.html'},
			 {'name':'PyOpenGL/Documentation/PyOpenGL Manual - XHTML',
			  'description':'PyOpenGL Manual in XHTML format.',
			  'path':'$lib/OpenGL/doc/xhtml/index.xml'},
			 {'name':'PyOpenGL/Documentation/PyOpenGL Manual - Online',
			  'description':'PyOpenGL Manual in HTML format.',
			  'path':'http://pyopengl.sourceforge.net/documentation/manual/'})


class install_shortcuts(Command):

	user_options = []

	def initialize_options(self):
		pass


	def finalize_options(self):
		pass


	def create_win32(self, name, path, description):
		s = pythoncom.CoCreateInstance(shell.CLSID_ShellLink, None, pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IShellLink)
		s.SetPath(path)
		s.SetDescription(description)
		filename = os.path.join(r'c:\windows\Start Menu\Programs', name + '.lnk')
		self.mkpath(os.path.dirname(filename))
		s.QueryInterface(pythoncom.IID_IPersistFile).Save(filename, 0)


	def run(self):
		if create_shortcuts:
			install_cmd = self.get_finalized_command('install')
			vars = {'lib':install_cmd.install_lib,
					'headers':install_cmd.install_headers,
					'scripts':install_cmd.install_scripts,
					'data':install_cmd.install_data}

			for shortcut in shortcuts:
				if string.split(shortcut['path'], ':')[0] == 'http':
					path = shortcut['path']
				else:
					path = convert_path(subst_vars(shortcut['path'], vars))
				name = convert_path(shortcut['name'])
				if sys.platform == 'win32':
					self.create_win32(name, path, shortcut['description'])
			