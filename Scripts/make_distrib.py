#!/usr/bin/env python

import sys
import getopt
import os
import errno
import buildpkg
import shutil

DOC_ONLY=0

USAGE='Usage: %s [-p python | --with-python=%s] [-h|--help] [-o release-dir|--output-directory=release-dir]\n'%(
	sys.argv[0], sys.executable)

PYTHON=sys.executable

def rest2HTML(irrelevant, dirName, names):
    for aName in names:
        if aName.endswith('.txt'):
            anInputPath = os.path.join(dirName, aName)
            if irrelevant is not None and anInputPath in irrelevant:
                continue
            anOutputPath = anInputPath[:-4] + '.html'
            print '- %s'%(anInputPath)
            os.system("docarticle.py '%s' > '%s' || rm '%s'"%(
                escquotes(anInputPath), escquotes(anOutputPath), 
                escquotes(anOutputPath)))

def package_version():
	fp = open('Modules/objc/pyobjc.h', 'r')  
	for ln in fp.readlines():
		if ln.startswith('#define OBJC_VERSION'):
			fp.close()
                        break
	return ln.split()[-1][1:-1]

	raise ValueError, "Version not found"

packageVersion = package_version()
if (len(packageVersion) < 3) or (len(packageVersion) > 7):
        raise ValueError, "Version 'found' (%s), but seems preposterously short or long." % packageVersion

BUILDDIR='release-dir'
OUTPUTDIR='release-dir/PyObjC-%s' % package_version()

def escquotes(val):
	return val.replace("'", "'\"'\"'")

try:
	opts, args = getopt.getopt(
		sys.argv[1:],
		'p:h?o:', ['with-python=', 'help', 'output-directory='])
except getopt.error, msg:
	sys.stderr.write('%s: %s\n'%(sys.argv[0], msg))
	sys.stderr.write(USAGE)
	sys.exit(1)

for key, value in opts:
	if key in [ '-h', '-?', '--help' ]:
		sys.stdout.write(USAGE)
		sys.exit(0)
	elif key in [ '-p', '--with-python' ]:
		PYTHON=value
	elif key in [ '-o', '--output-directory' ]:
		BUILDDIR=value
	else:
		raise ValueError, "Unsupported option: %s=%s"%(key, value)

def makeDir(basedir, *path):
        base = basedir
        for p in path:
                base = os.path.join(base, p)
                try:
                        os.mkdir(base)
                except OSError, e:
                        if e.errno <> errno.EEXIST: raise


if not os.path.exists(BUILDDIR):
        apply(makeDir, ["."] + BUILDDIR.split(os.sep))

if not os.path.exists(OUTPUTDIR):
        apply(makeDir, ["."] + OUTPUTDIR.split(os.sep))


if PYTHON==sys.executable:
	PYTHONVER='.'.join(map(str, sys.version_info[:2]))
	PYTHONPATH=sys.path
else:
	fd = os.popen("'%s' -c 'import sys;print \".\".join(map(str, sys.version_info[:2]))'"%(
		escquotes(PYTHON)))
	PYTHONVER=fd.readline().strip()
	fd = os.popen("'%s' -c 'import sys;print \"\\n\".join(sys.path)'"%(
		escquotes(PYTHON)))
	PYTHONPATH=map(lambda x:x[:-1], fd.readlines())


basedir = ''
for p in PYTHONPATH:
	if p.endswith('lib/python%s'%PYTHONVER):
		basedir = os.path.split(os.path.split(p)[0])[0]
		break

if not basedir:
	sys.stderr.write("%s: Cannot determine basedir\n"%(sys.argv[0]))
	sys.exit(1)

print "Generating HTML documentation"
os.path.walk('Doc', rest2HTML, ['Doc/announcement.txt'])
rest2HTML(None, '.', ['Install.txt', 'ReadMe.txt', 'Examples/00ReadMe.txt', 'Installer Package/ReadMe.txt', 'ProjectBuilder Extras/Project Templates/00README.txt'])
os.rename('ProjectBuilder Extras/Project Templates/00README.html', 'Doc/ProjectBuilder-Templates.html')

if DOC_ONLY:
    sys.exit(0)

print "Running: '%s' setup.py sdist -d '%s'"%(
			escquotes(PYTHON), escquotes(OUTPUTDIR))
fd = os.popen("'%s' setup.py sdist -d '%s'"%(
			escquotes(PYTHON), escquotes(OUTPUTDIR)), 'r')
for ln in fd.xreadlines():
	sys.stdout.write(ln)

print "Running: '%s' setup.py install --prefix='%s/package%s' --install-scripts=%s/package%s/lib/python%s/site-packages/PyObjC/bin"%(
	escquotes(PYTHON), escquotes(BUILDDIR), escquotes(basedir), escquotes(BUILDDIR), escquotes(basedir), PYTHONVER)
fd = os.popen("'%s' setup.py install --prefix='%s/package%s' --install-scripts=%s/package%s/lib/python%s/site-packages/PyObjC/bin"%(
	escquotes(PYTHON), escquotes(BUILDDIR), escquotes(basedir), escquotes(BUILDDIR), escquotes(basedir), PYTHONVER), 'r')
for ln in fd.xreadlines():
	sys.stdout.write(ln)

print "Copying readme and license"
shutil.copyfile("Installer Package/ReadMe.html", os.path.join(OUTPUTDIR, "ReadMe First.html"))
shutil.copyfile("License.txt", os.path.join(OUTPUTDIR, "License.txt"))

print "Setting up developer templates"

nastyFiles = ['.DS_Store', '.gdb_history']

def killNasties(irrelevant, dirName, names):
        for aName in names:
                if aName in nastyFiles:
                        os.remove( os.path.join(dirName, aName) )
        if dirName.find(".pbproj") > 0:
                for aName in names:
                        if aName.find(".pbxuser") > 0:
                                os.remove( os.path.join(dirName, aName) )
	if dirName[-3:] == 'CVS':
		while len(names): del names[0]
		shutil.rmtree(dirName)

basedir = '%s/package'%(BUILDDIR)

makeDir(basedir, 'Developer', 'ProjectBuilder Extras', 'Project Templates', 'Application')
templateDestination = os.path.join(basedir, 'Developer', 'ProjectBuilder Extras',
                                   'Project Templates', 'Application')

templateDir = os.path.join('ProjectBuilder Extras', 'Project Templates')
for dname in os.listdir(templateDir):
    if dname == 'CVS': continue
    path = os.path.join(templateDir, dname)
    if not os.path.isdir(path): continue
    shutil.copytree(path, os.path.join(templateDestination, dname))

print "Setting up project builder Python language specifications"
makeDir(basedir, 'Developer', 'ProjectBuilder Extras')
pbxSpecificationsDestination = os.path.join(basedir, 'Developer', 'ProjectBuilder Extras', 'Specifications')
shutil.copytree(os.path.join('ProjectBuilder Extras','Specifications'), pbxSpecificationsDestination)

print "Setting up developer examples & documentation"

DOCDIR=os.path.join(OUTPUTDIR, "PyObjC Documentation & Examples")
makeDir(OUTPUTDIR, "PyObjC Documentation & Examples")

examplesDestination = os.path.join(DOCDIR, "Examples")
shutil.copytree('Examples', examplesDestination)

docsDestination = os.path.join(DOCDIR, "Documentation")
shutil.copytree('Doc', docsDestination)

os.path.walk(templateDestination, killNasties, None)
os.path.walk(examplesDestination, killNasties, None)
os.path.walk(docsDestination, killNasties, None)
os.path.walk(docsDestination, rest2HTML, None)

print 'Building package'
pm = buildpkg.PackageMaker('PyObjC', package_version(), 
"""\
Python <-> Objective-C bridge that supports building full featured Cocoa
applications.
""")
pm.build(os.path.join(basedir), 
	resources=os.path.join(os.getcwd(), 'Installer Package', 'Resources'),
	OutputDir=os.path.join(os.getcwd(), OUTPUTDIR),
	Version=package_version(),
	NeedsAuthorization="YES",
	Relocatable="NO",
        RootVolumeOnly="YES")

print "Done. Don't forget to test the output!"
