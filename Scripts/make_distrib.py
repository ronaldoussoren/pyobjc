#!/usr/bin/env python

# Build the distribution. Requires Python2.2 on Jaguar, docutils and DocArticle.
# 
# NOTES: Really needs a rewrite!

import sys
import getopt
import os
import errno
import buildpkg
import shutil

DOC_ONLY=0

USAGE='Usage: %s [-p python | --with-python=%s] [-h|--help] [-o release-dir|--output-directory=release-dir]\n'%(
        sys.argv[0], sys.executable)

osvers = os.popen('sw_vers | grep ProductVersion').readline().strip().split()[-1]
osvers = '.'.join(osvers.split('.')[:2])

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
rest2HTML(None, '.', ['Install.txt', 'ReadMe.txt', 'Examples/00ReadMe.txt', 'Installer Package/10.2/ReadMe.txt', 'Installer Package/10.3/ReadMe.txt', 'ProjectBuilder Extras/Project Templates/00README.txt'])
os.rename('ProjectBuilder Extras/Project Templates/00README.html', 'Doc/ProjectBuilder-Templates.html')

if DOC_ONLY:
    sys.exit(0)

print "Running: '%s' setup.py sdist -d '%s'"%(
        		escquotes(PYTHON), escquotes(OUTPUTDIR))
fd = os.popen("'%s' setup.py sdist -d '%s'"%(
        		escquotes(PYTHON), escquotes(OUTPUTDIR)), 'r')
for ln in fd.xreadlines():
        sys.stdout.write(ln)

#
# NOTE: We first install our scripts into the python tree and later on move
# them to /usr/local to avoid clobbering a /usr/local symlink installed by
# the user.
print "Running: '%s' setup.py install --prefix='%s/package%s' --install-scripts=%s/package%s/lib/python%s/site-packages/PyObjC/bin"%(
        escquotes(PYTHON), escquotes(BUILDDIR), escquotes(basedir), escquotes(BUILDDIR), escquotes(basedir), PYTHONVER)
fd = os.popen("'%s' setup.py install --prefix='%s/package%s' --install-scripts=%s/package%s/lib/python%s/site-packages/PyObjC/bin"%(
        escquotes(PYTHON), escquotes(BUILDDIR), escquotes(basedir), escquotes(BUILDDIR), escquotes(basedir), PYTHONVER), 'r')
for ln in fd.xreadlines():
        sys.stdout.write(ln)

if osvers != '10.2':
    # Move the python packages into the right location, 'site-packages' is a
    # symlink on Panther and we don't want to clobber that.
    makeDir(BUILDDIR, 'package', 'Library', 'Python', str(PYTHONVER))
    os.rename(
        '%s/package%s/lib/python%s/site-packages/PyObjC'%(BUILDDIR, basedir, PYTHONVER),
        '%s/package/Library/Python/%s/PyObjC'%(BUILDDIR, PYTHONVER))
    os.rename(
        '%s/package%s/lib/python%s/site-packages/PyObjC.pth'%(BUILDDIR, basedir, PYTHONVER),
        '%s/package/Library/Python/%s/PyObjC.pth'%(BUILDDIR, PYTHONVER))

print "Copying readme and license"
shutil.copyfile("Installer Package/%s/ReadMe.html"%(osvers,), os.path.join(OUTPUTDIR, "ReadMe First.html"))
shutil.copyfile("License.txt", os.path.join(OUTPUTDIR, "License.txt"))


print "Building installer for %s"%(osvers,)
nastyFiles = ['.DS_Store', '.gdb_history']

def killNasties(irrelevant, dirName, names):
        for aName in names:
                if aName in nastyFiles:
                        os.remove( os.path.join(dirName, aName) )
        if dirName.find(".pbproj") > 0 and dirName.find('.xcode') > 0:
                for aName in names:
                        if aName.find(".pbxuser") > 0:
                                os.remove( os.path.join(dirName, aName) )
        if dirName[-3:] == 'CVS':
        	while len(names): del names[0]
        	shutil.rmtree(dirName)

basedir = '%s/package'%(BUILDDIR)


if osvers == '10.2':
    print "Setting up Project Builder templates"
    makeDir(basedir, 'Developer', 'ProjectBuilder Extras', 'Project Templates', 'Application')
    templateDestination = os.path.join(basedir, 
            'Developer', 'ProjectBuilder Extras', 
            'Project Templates', 'Application')

    templateDir = os.path.join('ProjectBuilder Extras', 'Project Templates')
    for dname in os.listdir(templateDir):
        if dname == 'CVS': continue
        path = os.path.join(templateDir, dname)
        if not os.path.isdir(path): continue
        shutil.copytree(path, os.path.join(templateDestination, dname))

    print "Setting up Project Builder Python language specifications"
    makeDir(basedir, 'Developer', 'ProjectBuilder Extras')
    pbxSpecificationsDestination = os.path.join(basedir, 'Developer', 'ProjectBuilder Extras', 'Specifications')
    shutil.copytree(os.path.join('ProjectBuilder Extras','Specifications'), pbxSpecificationsDestination)

elif osvers == '10.3':
    print "Setting up Xcode templates"
    makeDir(basedir, 
            'Library', 'Application Support', 'Apple', 
            'Developer Tools', 'Project Templates', 'Application')
    templateDestination = os.path.join(basedir, 
            'Library', 'Application Support', 'Apple', 
            'Developer Tools', 'Project Templates', 'Application')
    templateDir = os.path.join('Xcode', 'Project Templates')
    for dname in os.listdir(templateDir):
        if dname == 'CVS': continue
        path = os.path.join(templateDir, dname)
        if not os.path.isdir(path): continue
        shutil.copytree(path, os.path.join(templateDestination, dname))

else:
    raise ValueError, "Don't know how to build installer for %s"%(osvers,)

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
        resources=os.path.join(os.getcwd(), 'Installer Package', osvers, 'Resources'),
        OutputDir=os.path.join(os.getcwd(), OUTPUTDIR),
        Version=package_version(),
        NeedsAuthorization="YES",
        Relocatable="NO",
        RootVolumeOnly="YES")

print "Fixing up the installer..."
fn = os.path.join(OUTPUTDIR, 'PyObjC.pkg', 'Contents', 'Resources', 'Description.plist')
data = open(fn, 'r').read()
data = data.replace('@@VERSION@@', package_version())
open(fn, 'w').write(data)

#
# build 'objc_extras.tar.gz', and archive containing stuff not included in
# the binary PackMan installer (which is built manually)
#
print "Running: '%s' setup.py bdist -d '%s'"%(
        		escquotes("python2.3"), escquotes(OUTPUTDIR))
fd = os.popen("'%s' setup.py bdist -d '%s'"%(
        		escquotes("python2.3"), escquotes(OUTPUTDIR)), 'r')
for ln in fd.xreadlines():
        sys.stdout.write(ln)

print 'building "pyobjc_extras-%s.tar.gz"'%(package_version(),)
OUTPUTDIR='release-dir/extra_work/Applications/MacPython-2.3/Extras/pyobjc-%s'%(
        package_version(),)
makeDir(*(OUTPUTDIR.split('/')))
shutil.copytree(docsDestination, os.path.join(OUTPUTDIR, "Doc"))
shutil.copytree(examplesDestination, os.path.join(OUTPUTDIR, "Examples"))
for fn in [ 
    'HISTORIC.txt', 'Install.html', 'Install.txt', 'License.txt',
    'NEWS.html', 'ReadMe.html', 'ReadMe.txt' ]:

        shutil.copyfile(fn, os.path.join(OUTPUTDIR, fn))

os.system('cd release-dir/extra_work && tar zcf ../pyobjc_extras-%s.tar.gz Applications/MacPython-2.3/Extras/pyobjc-%s'%(
        package_version(), package_version()))


print "Done. Don't forget to test the output!"
print "-- hdiutil create -imagekey zlib-level=9 -srcfolder PyObjC-1.1a0 pyobjc-1.1a0-panther.dmg"

