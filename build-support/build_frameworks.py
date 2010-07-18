#!/usr/bin/env python3
"""
Script that builds a number of python frameworks as
used by the run_tests.py script

FIXME:
- Both variants need to be build with simular options
  to the official builds: 32-bit with SDK 10.4u and deployment
  target 10.3, 3-way without SDK and depl. target 10.5.

  This will have to wait until my sdkroot patches get committed,
  without that patch I cannot build the 32-bit variant on 
  SL.
- get rid of the global variables
"""
import sys
sys.dont_write_bytecode = True

import subprocess, getopt, logging, os, shutil
from urllib.request import urlopen


gUsage="""\
build_frameworks.py [-v versions] [--versions=versions] [-a archs] [--arch archs]

- versions: comma seperated list of python versiosn, defaults to "2.6,2.7,3.1,3.2"
- archs: comma seperated list of build variations, defaults to "32-bit,3-way"
"""

gBaseDir = os.path.dirname(os.path.abspath(__file__))

gArchs = ("32-bit", "3-way")


# Name of the Python framework and any additional arguments
# passed to the configure command.
gFlavours = [
        dict(
            name="debug",
            template="DbgPython-{archs}",
            flags=[
                "--with-pydebug",
            ],
        ),
#        dict(
#            name="release",
#            template="ReleasePython-{archs}",
#            flags=[
#            ],
#        ),
]


# Location of the SVN branches to be used
gURLMap = {
    '2.6': 'http://svn.python.org/projects/python/branches/release26-maint',
    '2.7': 'http://svn.python.org/projects/python/branches/release27-maint',

    '3.1': 'http://svn.python.org/projects/python/branches/release31-maint',
    '3.2': 'http://svn.python.org/projects/python/branches/py3k',
}


# Name of the OSX SDK used to build the framework, keyed of the architecture
# variant.
gSdkMap={
    '32-bit': '/Developer/SDKs/MacOSX10.4u.sdk',
    '3-way': '/',
    'intel': '/',
}

# Name of the OSX Deployment Target used to build the framework, keyed of 
# the architecture variant.
gDeploymentTargetMap={
    '32-bit': '10.3',
    #'32-bit': '10.5',
    '3-way':  '10.5',
    'intel':  '10.5',
}

class ShellError (Exception):
    """ An error occurred while running a shell command """
    pass

def create_checkout(version):
    """
    Create or update the checkout of the given version
    of Python.
    """
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

def build_framework(flavour, version, archs):
    """
    Build the given version of Python in the given architecture
    variant. 

    This also installs distribute and virtualenv (the latter using
    a local copy of the package).
    """
    lg = logging.getLogger("build_framework")
    lg.info("Build %s framework version=%r archs=%r", flavour["name"], version, archs)

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
            "--with-framework-name={0}".format(flavour["template"].format(version=version, archs=archs)),
            "--enable-universalsdk={0}".format(gSdkMap[archs]),
            "--with-universal-archs={0}".format(archs),
            ] + flavour["flags"] + [
            "MACOSX_DEPLOYMENT_TARGET={0}".format(gDeploymentTargetMap[archs]),
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

def install_distribute(flavour, version, archs):
    lg = logging.getLogger("install_distribute")
    lg.debug("Installing distribute")

    distribute_dir = os.path.join(gBaseDir, "distribute-0.6.12-patched")
    builddir = os.path.join(distribute_dir, "build")
    if os.path.exists(builddir):
        lg.debug("Remove existing 'build' subdir")
        shutil.rmtree(builddir)

    frameworkName=flavour["template"].format(archs=archs, version=version)

    python = "/Library/Frameworks/{0}.framework/Versions/{1}/bin/python".format(
            frameworkName, version)
    if version[0] == '3':
        python += '3'


    lg.debug("Run setup script with '%s'", python)
    p = subprocess.Popen([
        python, "setup.py", "install"],
        cwd=distribute_dir)
    xit = p.wait()
    if xit != 0:
        lg.warning("Installing 'distribute' failed")
        raise ShellError(xit)


def install_virtualenv(flavour, version, archs):
    lg = logging.getLogger("install_virtualenv")

    lg.info("Installing virtualenv from local source")

    frameworkName=flavour["template"].format(archs=archs, version=version)

    python = "/Library/Frameworks/{0}.framework/Versions/{1}/bin/python".format(
            frameworkName, version)
    if version[0] == '3':
        python += '3'

    # Sadly enough plain virtualenv doens't support 
    # python3 yet, but there is a fork that does.
    # Therefore install the real virtualenv for python 2.x
    # and the fork for python 3.x
    if version[0] == '2':
        srcdir = os.path.join(gBaseDir, 'virtualenv-src')
    else:
        srcdir = os.path.join(gBaseDir, 'virtualenv3-src')

    p = subprocess.Popen([ python, "setup.py", "install" ],
            cwd=srcdir)

    xit = p.wait()
    if xit != 0:
        lg.warning("Installing 'virtualenv' failed")
        raise ShellError(xit)


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

    lg = logging.getLogger("build_frameworks")
    lg.info("Building versions: %s", versions)
    lg.info("Building architectures: %s", archs)
    try:
        for version in sorted(versions):
            create_checkout(version)

            for flavour in gFlavours:
                for arch in sorted(archs):
                    try:
                        lg.info('Building %s framework for python %s (%s)', flavour["name"], version, arch)
                        build_framework(flavour, version, arch)
                        lg.info('Installing distribute for python %s (%s)', version, arch)
                        install_distribute(flavour, version, arch)
                        lg.info('Installing virtualenv for python %s (%s)', version, arch)
                        install_virtualenv(flavour, version, arch)
                        lg.info('Done %s python %s (%s)', flavour["name"], version, arch)
                    except Exception as exc:
                        lg.warning("building %s for pyton %s (%s) failed: %s",
                                flavour["name"], version, arch, exc)
                        import traceback
                        traceback.print_exc()
    
    except ShellError:
        sys.exit(1)

if __name__ == "__main__":
    main()
