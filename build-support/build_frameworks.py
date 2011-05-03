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
build_frameworks.py [-v versions] [--versions=versions] [-a archs] [--arch archs] \\
   [--refresh-clone|--no-refresh-clone]

- versions: comma seperated list of python versiosn, defaults to "2.6,2.7,3.1,3.2"
- archs: comma seperated list of build variations, defaults to "32-bit,3-way"
"""

gBaseDir = os.path.dirname(os.path.abspath(__file__))

gArchs = ("32-bit", "3-way", "intel")


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

gHgURL='http://hg.python.org/cpython'
gBranchMap={
    '2.6': '2.6',
    '2.7': '2.7',
    '3.1': '3.1',
    '3.2': '3.2',
    '3.3': 'default',
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

def refresh_local_clone():
    lg = logging.getLogger("refresh_local_clone")
    lg.info("Refreshing local clone")

    checkoutdir = os.path.join(gBaseDir, "checkout")
    if not os.path.exists(checkoutdir):
        lg.debug("Create directory %r", checkoutdir)
        os.makedirs(checkoutdir)

    if not os.path.exists(os.path.join(checkoutdir, '.hg')):
        lg.debug("Initial clone")
        p = subprocess.Popen([
            'hg', 'clone', gHgURL, checkoutdir
        ])

    else:
        lg.debug("Update clone")
        p = subprocess.Popen([
            'hg', 'pull', '-u'],
            cwd=checkoutdir,
        )

    xit = p.wait()
    if xit == 0:
        lg.info("Local clone is now up-to-date")
    else:
        lg.warn("Pull for local clone failed")
        raise ShellError(xit)


def switch_branch(version):
    """
    Create or update the checkout of the given version
    of Python.
    """
    lg = logging.getLogger("switch_branch")
    lg.info("Switch to branch %s", version)

    checkoutdir = os.path.join(gBaseDir, "checkout")
    if not os.path.exists(checkoutdir):
        lg.error("No local clone available")
        raise ShellError(1)

    p = subprocess.Popen([
        'hg', 'up', '-C', version],
        cwd=checkoutdir)

    xit = p.wait()
    if xit == 0:
        lg.info("Branch for %s is now up-to-date", version)
    else:
        lg.warn("Branch for %s failed", version)
        raise ShellError(xit)

    p = subprocess.Popen([
        'hg', 'branch'],
        cwd=checkoutdir,
        stdout=subprocess.PIPE)
    data = p.communicate()[0]
    data = data.decode('utf-8').strip()
    xit = p.wait()
    if data != version:
        lg.warn("Switching branch failed")
        raise ShellExit(1)


def build_framework(flavour, version, archs):
    """
    Build the given version of Python in the given architecture
    variant. 

    This also installs distribute and virtualenv (the latter using
    a local copy of the package).
    """
    lg = logging.getLogger("build_framework")
    lg.info("Build %s framework version=%r archs=%r", flavour["name"], version, archs)

    builddir = os.path.join(gBaseDir, "checkout", "build")
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



    lg.debug('Removing unwanted installation bits from Makefile')
    fp = open(os.path.join(builddir, 'Makefile'))
    contents = fp.read()
    fp.close()
    
    # Ensure that nothing gets installed in /Applications
    contents = contents.replace('frameworkinstallapps4way', '')
    contents = contents.replace('frameworkinstallapps', '')

    # Ensure that nothting gets installed in /usr/local
    contents = contents.replace(' frameworkinstallunixtools4way', ' ')
    contents = contents.replace(' frameworkinstallunixtools', ' ')
    
    fp = open(os.path.join(builddir, 'Makefile'), 'w')
    fp.write(contents)
    fp.close()




    fp = open(os.path.join(builddir, 'Mac', 'Makefile'))
    contents = fp.read()
    fp.close()

    contents = contents.replace('"$(PYTHONAPPSDIR)"', '')
    fp = open(os.path.join(builddir, 'Mac', 'Makefile'), 'w')
    fp.write(contents)
    fp.close()



    
    lg.debug("Running 'make'")
    p = subprocess.Popen([
            "make",
        ], cwd=builddir)

    xit = p.wait()
    if xit != 0:
        lg.debug("Make failed for %s", version)
        raise ShellError(xit)

    install_tree = "/Library/Frameworks/{0}.framework/Versions/{1}".format(
            flavour["template"].format(version=version, archs=archs), version)
    if os.path.exists(install_tree):
        lg.debug("Removing existing tree (%s)", install_tree)
        #shutil.rmtree(install_tree)

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

    distribute='distribute-0.6.15'

    if not os.path.exists(os.path.join(gBaseDir, 'cache')):
        os.mkdir(os.path.join(gBaseDir, 'cache'))

    if not os.path.exists(os.path.join(gBaseDir, 'cache', distribute + '.tar.gz')):
        lg.warning("Downloading %s from PyPI"%(distribute,))
        url = 'http://pypi.python.org/packages/source/d/distribute/' + distribute + '.tar.gz'
        fp = urlopen(url)
        data = fp.read()
        fp.close()

        fp = open(os.path.join(gBaseDir, 'cache', distribute + '.tar.gz'), 'wb')
        fp.write(data)
        fp.close()

    if not os.path.exists(os.path.join(gBaseDir, 'cache', distribute)):
        lg.warning("Unpacking %s archive"%(distribute,))
        shutil.unpack_archive(
            os.path.join(gBaseDir, 'cache', distribute + '.tar.gz'),
            os.path.join(gBaseDir, 'cache'))

    distribute_dir = os.path.join(gBaseDir, "cache", distribute)
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
    lg = logging.getLogger("install_distribute")
    lg.debug("Installing virtualenv")

    virtualenv='virtualenv-1.6'

    if not os.path.exists(os.path.join(gBaseDir, 'cache')):
        os.mkdir(os.path.join(gBaseDir, 'cache'))

    if not os.path.exists(os.path.join(gBaseDir, 'cache', virtualenv + '.tar.gz')):
        lg.warning("Downloading %s from PyPI"%(virtualenv,))
        url = 'http://pypi.python.org/packages/source/v/virtualenv/' + virtualenv + '.tar.gz'
        fp = urlopen(url)
        data = fp.read()
        fp.close()

        fp = open(os.path.join(gBaseDir, 'cache', virtualenv + '.tar.gz'), 'wb')
        fp.write(data)
        fp.close()

    if not os.path.exists(os.path.join(gBaseDir, 'cache', virtualenv)):
        lg.warning("Unpacking %s archive"%(virtualenv,))
        shutil.unpack_archive(
            os.path.join(gBaseDir, 'cache', virtualenv + '.tar.gz'),
            os.path.join(gBaseDir, 'cache'))

    virtualenv_dir = os.path.join(gBaseDir, "cache", virtualenv)
    virtualenv_dir = os.path.join(gBaseDir, virtualenv)
    builddir = os.path.join(virtualenv_dir, "build")
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
        cwd=virtualenv_dir)
    xit = p.wait()
    if xit != 0:
        lg.warning("Installing 'virtualenv' failed")
        raise ShellError(xit)



def main():
    logging.basicConfig(level=logging.DEBUG)
    import sysconfig

    import os
    os.environ['PATH'] = '/Developer/usr/bin:' + os.environ['PATH']

    if 'MACOSX_DEPLOYMENT_TARGET' in os.environ:
        del os.environ['MACOSX_DEPLOYMENT_TARGET']
    os.unsetenv('MACOSX_DEPLOYMENT_TARGET')

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'v:a:h?', ['help', 'versions=', 'archs=', 
            'refresh-clone', 'no-refresh-clone'])
    except getopt.error as msg:
        print(msg, file=sys.stderr)
        print(gUsage, file=sys.stderr)
        sys.exit(1)

    versions = sorted(gBranchMap.keys())
    archs = gArchs
    refresh_clone = True

    if args:
        print("Additional arguments", file=sys.stderr)
        print(gUsage, file=sys.stderr)
        sys.exit(1)



    for k, v in opts:
        if k in ('-h', '-?', '--help'):
            print(gUsage)
            sys.exit(0)

        elif k == '--refresh-clone':
            refresh_clone=True

        elif k == '--no-refresh-clone':
            refresh_clone=False

        elif k in ('-v', '--versions'):
            versions = v.split(',')

            for v in versions:
                if v not in gBranchMap:
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
    if refresh_clone:
        refresh_local_clone()
    try:
        for version in sorted(versions):
            switch_branch(gBranchMap[version])

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

                    except ShellError:
                        raise
                    except Exception as exc:
                        lg.warning("building %s for pyton %s (%s) failed: %s",
                                flavour["name"], version, arch, exc)
                        import traceback
                        traceback.print_exc()
    
    except ShellError:
        sys.exit(1)

if __name__ == "__main__":
    main()
