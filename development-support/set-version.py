#!/usr/bin/env python3
"""
A simple script for updating the version numbers throughout the
pyobjc project.

Usage::

    python3 set-version.py 2.3

Run tests aftwards before doing a commit.
"""
import os, sys, re

DRYRUN=False


topdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if len(sys.argv) != 2:
    print ("Usage: %s VERSION"%(sys.argv[0],))
    sys.exit(1)

VERSION=sys.argv[1]

def load_file(fn):
    with open(fn) as fp:
        return fp.read()

if DRYRUN:
    def save_file(fn, data):
        pass

else:
    def save_file(fn, data):
        with open(fn, "w") as fp:
            fp.write(data)


# Wrapper project
print ("Updating 'pyobjc'")
fn = os.path.join(topdir, "pyobjc", "setup.py")
r = re.compile('^VERSION=.*$', re.MULTILINE)
data = r.sub('VERSION="%s"'%(VERSION,), load_file(fn))
save_file(fn, data)

# pyobjc-core, version is in a header file
print ("Updating 'pyobjc-core'")
fn = os.path.join(topdir, "pyobjc-core", "Modules", "objc", "pyobjc.h")
r = re.compile('^#define OBJC_VERSION .*$', re.MULTILINE)
data = r.sub('#define OBJC_VERSION "%s"'%(VERSION,), load_file(fn))
save_file(fn, data)

# and the various framework wrappers
for subdir in os.listdir(topdir):
    if not subdir.startswith("pyobjc-framework-"):
        continue

    print ("Updating '%s'"%(subdir,))
    fn = os.path.join(topdir, subdir, "setup.py")
    r = re.compile('^\s*version=.*$', re.MULTILINE)
    data = r.sub('    version="%s",'%(VERSION,), load_file(fn))

    r = re.compile('^\s*\'pyobjc-core>=.*$', re.MULTILINE)
    data = r.sub('        \'pyobjc-core>=%s\','%(VERSION,), data)

    r = re.compile('^\s*\'pyobjc-framework-([^>]*)>=.*$', re.MULTILINE)
    data = r.sub('        \'pyobjc-framework-\\1>=%s\','%(VERSION,), data)
   
    save_file(fn, data)
