#!/usr/bin/env python3
"""
Script that builds a number of python frameworks as
used by the run_tests.py script
"""
import subprocess, getopt, logging, os, sys, shutil
from urllib.request import urlopen

gUsage="""\
build_frameworks.py [-v versions] [--versions=versions] [-a archs] [--arch archs]

- versions: comma seperated list of python versiosn, defaults to "2.6,2.7,3.1,3.2"
- archs: comma seperated list of build variations, defaults to "32-bit,intel"
"""

gBaseDir = os.path.dirname(os.path.abspath(__file__))

gArchs = ("32-bit", "intel")

gURLMap = {
    '2.6': 'http://svn.python.org/projects/python/branches/release26-maint',
    '2.7': 'http://svn.python.org/projects/python/trunk',

    '3.1': 'http://svn.python.org/projects/python/branches/release31-maint',
    '3.2': 'http://svn.python.org/projects/python/branches/py3k',
}


class ShellError (Exception):
    pass

def create_checkout(version):
    lg = logging.getLogger("create_checkout")
    lg.info("Create checkout for %s", version)

    checkoutdir = os.path.join(gBaseDir, "checkouts", version)
    if not os.path.exists(checkoutdir):
        lg.debug("Create directory %r", checkoutdir)
        os.makedirs(checkoutdir)

    if os.path.exists(os.path.join(checkoutdir, '.svn')):
        lg.debug("Update checkout")
        p = subprocess.Popen([
            'svn', 'up'],
            cwd=checkoutdir)
    else:
        lg.debug("Initial checkout checkout")
        p = subprocess.Popen([
            'svn', 'co', gURLMap[version], checkoutdir])

    xit = p.wait()
    if xit == 0:
        lg.info("Checkout for %s is now up-to-date", version)
    else:
        lg.warn("Checkout for %s failed", version)
        raise ShellError(xit)

def build_framework(version, archs):
    lg = logging.getLogger("build_framework")
    lg.info("Build framework version=%r archs=%r", version, archs)

    builddir = os.path.join(gBaseDir, "checkouts", version, "build")
    if os.path.exists(builddir):
        lg.debug("Remove existing build tree")
        shutil.rmtree(builddir)

    lg.debug("Create build tree %r", builddir)
    os.mkdir(builddir)

    lg.debug("Running 'configure'")
    p = subprocess.Popen([
        "../configure",
            "--enable-framework",
            "--with-framework-name=DbgPython-{0}".format(archs),
            "--enable-universalsdk=/",
            "--with-universal-archs={0}".format(archs),
            "--with-pydebug",
        ], cwd=builddir)

    xit = p.wait()
    if xit != 0:
        lg.debug("Configure failed for %s", version)
        raise ShellError(xit)
    
    lg.debug("Running 'make'")
    p = subprocess.Popen([
            "make",
        ], cwd=builddir)

    xit = p.wait()
    if xit != 0:
        lg.debug("Make failed for %s", version)
        raise ShellError(xit)

    lg.debug("Running 'make install'")
    p = subprocess.Popen([
            "make",
            "install",
        ], cwd=builddir)

    xit = p.wait()
    if xit != 0:
        lg.debug("Install failed for %r", version)
        raise ShellError(xit)

    lg.debug("Installing distribute")

    lg.debug("Download distribute_setup script")
    fd = urlopen("http://python-distribute.org/distribute_setup.py")
    data = fd.read()
    fd.close()

    scriptfn = os.path.join(builddir, "distribute_setup.py")
    fd = open(scriptfn, "wb")
    fd.write(data)
    fd.close()

    python = "/Library/Frameworks/DbgPython-{0}.framework/Versions/{1}/bin/python".format(
            archs, version)
    if version[0] == '3':
        python += '3'


        # Script is in python2 format, translate to python3 before 
        # trying to run it.
        lg.debug("Convert install script to python3")
        p = subprocess.Popen([
            os.path.join(os.path.dirname(python), "2to3"),
            scriptfn])
        xit = p.wait()
        if xit != 0:
            lg.warning("Running 2to3 failed")
            raise ShellError(xit)

    lg.debug("Run distribute_setup script")
    p = subprocess.Popen([
        python,
        scriptfn])
    xit = p.wait()
    if xit != 0:
        lg.warning("Installing 'distribute' failed")
        raise ShellError(xit)

    lg.debug("Installing virtualenv")

    # Sadly enough plain virtualenv doens't support 
    # python3 yet, but there is a fork that does.
    # Therefore install the real virtualenv for python 2.x
    # and the fork for python 3.x
    if version[0] == '2':
        p = subprocess.Popen([
            os.path.join(os.path.dirname(python), "easy_install"),
            "virtualenv"])
    else:
        p = subprocess.Popen([
            os.path.join(os.path.dirname(python), "easy_install"),
            "virtualenv3"])

    xit = p.wait()
    if xit != 0:
        lg.warning("Installing 'distribute' failed")
        raise ShellError(xit)

    lg.info("Installation of %r done", version)

def main():
    logging.basicConfig(level=logging.DEBUG)

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'v:a:h?', ['help', 'versions=', 'archs='])
    except getopt.error as msg:
        print(msg, file=sys.stderr)
        print(gUsage, file=sys.stderr)
        sys.exit(1)

    versions = sorted(gURLMap.keys())
    archs = gArchs

    if args:
        print("Additional arguments", file=sys.stderr)
        print(gUsage, file=sys.stderr)
        sys.exit(1)

    for k, v in opts:
        if k in ('-h', '-?', '--help'):
            print(gUsage)
            sys.exit(0)

        elif k in ('-v', '--versions'):
            versions = v.split(',')

            for v in versions:
                if v not in gURLMap:
                    print("Unsupported python version: {0}".format(v), 
                            file=sys.stderr)
                    sys.exit(1)

        elif k in ('-a', '--archs'):
            archs = v.split(',')

            for v in archs:
                if v not in gArchs:
                    print("Unsupported python architecture: {0}".format(v), 
                            file=sys.stderr)
                    sys.exit(1)

        else:
            print("ERROR: unhandled script option: {0}".format(k), 
                    file=sys.stderr)
            sys.exit(2)

    try:
        for version in sorted(versions):
            create_checkout(version)

            for archs in gArchs:
                build_framework(version, archs)
    
    except ShellError:
        sys.exit(1)

if __name__ == "__main__":
    main()
