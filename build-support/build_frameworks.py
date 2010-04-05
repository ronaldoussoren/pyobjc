#!/usr/bin/env python3
"""
Script that builds a number of python frameworks as
used by the run_tests.py script
"""
import subprocess, getopt, logging, os, sys, shutil

gBaseDir = os.path.dirname(os.path.abspath(__file__))

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

    lg.info("Installation of %r done", version)

def main():
    logging.basicConfig(level=logging.DEBUG)

    try:
        for version in ("2.6", "2.7", "3.1", "3.2"):
            create_checkout(version)

            for archs in ("32-bit", "intel"):
                build_framework(version, archs)
    
    except ShellError:
        sys.exit(1)

if __name__ == "__main__":
    main()
