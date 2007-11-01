import re, os, os.path, string


def get_build_info(file):
	BUILD = {'api_versions':[0x100], 'shadow':1, 'headers':[], 'api_version_check':0, 'include_dirs':[], 'sources':[]}
		
	x = open(file).read()
	x = string.replace(x, '\r\n', '\n')
	x = string.replace(x, '\r', '\n')
	for name, value in re.findall(r'[#]\s*BUILD\s+([^\s]+)\s+((?:[^\n\\]+|\\.|\\\n)+)', x):
		BUILD[name] = eval(string.strip(string.replace(value, '\\\n', ' ')))

	BUILD['api_versions'].sort()
	BUILD['api_versions'].reverse()

	return BUILD	


def outdated(x, dependencies):
	if not os.path.exists(x):
		return 1
	x_mtime = os.path.getmtime(x)
	for dependency in dependencies:
		if x_mtime < os.path.getmtime(dependency):
			return 1
	return 0


def mkdir(x):
	head, tail = os.path.split(x)
	if head != '':
		mkdir(head)
	if not os.path.exists(x):
		os.mkdir(x)


build_re = re.compile("__build__\s*=\s*(.+)")


def get_version():
	return string.strip(open(os.path.join('OpenGL', 'version')).read())


def increment_build():
	p = os.path.join('OpenGL', '__init__.py')
	x = open(p).read()
	builds = build_re.findall(x)
	if len(builds):
		x = build_re.sub('__build__ = %d' % (int(builds[0]) + 1), x)
		open(p, 'w').write(x)
	