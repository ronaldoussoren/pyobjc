#!

# This is statement is required by the build system to query build info
if __name__ == '__build__':
	raise Exception

import os.path, imp, sys, string


def _visit(args, dirname, names):
	if '__init__.py' in names and os.path.isfile(os.path.join(dirname, '__init__.py')):
		root, modules = args
		package = ['OpenGL']
		current_root = dirname
		while root != current_root:
			current_root, package_name = os.path.split(current_root)
			package.insert(1, package_name)
		exts = map(lambda x: x[0], imp.get_suffixes())
		for name in names:
			if os.path.isfile(os.path.join(dirname, name)):
				module, ext = os.path.splitext(name)
				if ext in exts:
					if module == '__init__':
						module = string.join(package, '.')
					elif module[-1] == '_':
						module = None
					else:
						module = string.join(package + [module], '.')
					if module and module not in modules:
						modules.append(module)
	else:
		names = []
									   

def _get_modules():
	import OpenGL
	path = os.path.split(sys.modules['OpenGL'].__file__)[0]
	modules = []
	os.path.walk(path, _visit, (path, modules))
	return modules


def _query():
	module_info = {}
	for module_name in _get_modules():
		info = None

		try:
			module = __import__(module_name, globals(), locals(), ['*'])

			if module_name == 'OpenGL':
				info = __OpenGL_info(module)
			else:
				info = getattr(module, '__info')()
			if info is not None:
				if hasattr(module, '__api_version__'):
					info.insert(0, ('API Version', '0x%04x' % getattr(module, '__api_version__')))

				if hasattr(module, '__version__'):
					if module_name == 'OpenGL':
						version_name = 'PyOpenGL Version'
					else:
						version_name = 'File Version'
					info.insert(0, ('File Version', getattr(module, '__version__')))
		except:
			pass

		if info:
			module_info[module_name] = info

	return module_info


def _boolean(x):
	if x:
		return 'Yes'
	return 'No'
	

def __OpenGL_info(module):
	import sys
	
	info = []

	info.append(('Platform', sys.platform))
	info.append(('Python Version', sys.version))
	info.append(('Numeric support', _boolean(module.__numeric_support__)))
	info.append(('Numeric connected', _boolean(module.__numeric_present__)))

	try:
		import numeric_version
		info.append(('Numeric Version', numeric_version.version))
	except ImportError:
		info.append(('Numeric Version', 'None'))
		pass

	try:
		import Image
		info.append(('PIL Version', Image.VERSION))
	except ImportError:
		info.append(('PIL Version', 'None'))

	try:
		import wxPython
		info.append(('wxPython Version', wxPython.__version__))
	except ImportError:
		info.append(('wxPython Version', 'None'))

	try:
		import pygame
		info.append(('pygame Version', pygame.ver))
	except ImportError:
		info.append(('pygame Version', 'None'))

	try:
		import FXPy
		info.append(('FXPy available', 'Yes'))
	except ImportError:
		info.append(('FXPy available', 'No'))

	return info


if __name__ == '__main__':
	print 'Writing PyOpenGL info to "PyOpenGL_info.html" (this may take a while)...'
	
	import sys, operator
	from OpenGL.GLUT import *
	from OpenGL.GL import glGetIntegerv, glGetBooleanv, glGetDoublev, glGetString, GLerror
	from OpenGL.GLU import gluGetString
	
	glutInit(sys.argv)
	glutCreateWindow('foo')

	f = open('PyOpenGL_info.html', 'w')
	f.write('<html><title>PyOpenGL Information</title><body><h1>PyOpenGL Information</h1><br>')

	info = _query()
	module_names = info.keys()
	module_names.sort()
	for module_name in module_names:
		if module_name == 'OpenGL':
			desc = 'General'
		else:
			desc = string.split(module_name, '.', 1)[1]
		f.write('<table border="1" cellspacing="0" cellpadding="2"><thead><tr><h2>%s</h2></tr></thead>' % desc)
		for i in info[module_name]:
			try:
				if len(i) == 2:
					key, value = i
				else:
					key, id, t = i
					if t[0] == 'b':
						value = glGetBooleanv(id)
						if operator.isSequence(value):
							value = map(_boolean, value)
						else:
							value = _boolean(value)
					elif t[0] == 'i':
						value = glGetIntegerv(id)
					elif t[0] == 'd':
						value = glGetDoublev(id)
					elif t[0] == 'e':
						if len(t) > 1:
							if t[1] == 'u':
								x = gluGetString(id)
							else:
								x = glGetString(id)
						else:
							x = id
						x = string.split(x)
						x.sort()
						y = []
						for ext in x:
							try:
								__import__('OpenGL.' + string.replace(ext, '_', '.', 2), globals(), locals(), ['*'])
								y.append('<b>%s</b>' % ext)
							except ImportError:
								y.append(ext)
						value = string.join(y, '<br>')
					else:
						if len(t) > 1:
							if t[1] == 'u':
								value = gluGetString(id)
							else:
								value = glGetString(id)
						else:
							value = id
				f.write('<tr><td valign="top">%s</td><td valign="top">%s</td>' % (key, value))
			except GLerror:
				pass
		f.write('</table><br>')

	f.write('</body></html>')



