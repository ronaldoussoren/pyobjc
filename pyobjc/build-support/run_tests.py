#!/usr/bin/env python3
"""
A script that builds and tests the entire pyobjc tree
in a number of virtual environments:

- python 2.6
- python 2.7
- python 3.1
- python 3.2

- all in 32-bit, 3-way

- with command-line arguments to select specific 
  combinations

Assumptions:
- there are python frameworks for the various architectures: DbgPython-VARIANT.framework
- those frameworks contain distribute and virtualenv

(TODO: create script that builds a fresh copy of these frameworks from svn checkouts)
"""
import getopt, sys, os, shutil, logging, subprocess
from topsort import topological_sort

gUsage = """\
run_tests.py [-a archs] [--archs=archs] [-v versions] [--versions,versions]

archs:    32-bit,3-way   (values separated by commas)
versions: 2.6,2.7,3.1,3.2 (values seperated by commas)
"""

gBaseDir = os.path.dirname(os.path.abspath(__file__))
gRootDir = os.path.dirname(gBaseDir)

gVersions=["2.6", "2.7", "3.1", "3.2"]
gArchs=["32-bit", "3-way"]

def main():
    logging.basicConfig(level=logging.DEBUG)

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'a:v:h?', ["--help", "--archs=", "--versions="])
    except getopt.error as msg:
        print(msg, file=sys.stderr)
        print(gUsage, file=sys.stderr)
        sys.exit(1)

    if args:
        print("Additional arguments", file=sys.stderr)
        print(gUsage, file=sys.stderr)
        sys.exit(1)

    versions=gVersions
    archs=gArchs

    for k, v in opts:
        if k in ('-?', '-h', '--help'):
            print(gUsage)
            sys.exit(0)
        elif k in ['-a', '--archs']:
            archs=v.split(',')

            for v in archs:
                if v not in gArchs:
                    print("Unsupported architecture: {0}".format(v),
                            file=sys.stderr)
                    sys.exit(1)

        elif k in ['-v', '--versions']:
            versions=v.split(',')

            for v in versions:
                if v not in gVersions:
                    print("Unsupported Python version: {0}".format(v),
                            file=sys.stderr)
                    sys.exit(1)
        else:
            print("ERROR: Unhandled script option: {0}".format(k),
                    file=sys.stderr)
            sys.exit(2)

    all_results = []
    for ver in versions:
        for arch in archs:
            test_results = run_tests(ver, arch)
            all_results.append([ver, arch, test_results])

    report_results(all_results)

def report_results(all_results):
    for version, archs, test_results in all_results:
        title = "Architectures {1} for Python {0}".format(version, archs)
        print(title)
        print("="*len(title))
        print()
        
        for pkg, stdout, stderr in test_results:
            summary = stdout.splitlines()[-1]
            print("{0:>20}: {1}".format(pkg, summary))

        print()


def detect_frameworks():
    """
    Returns a list of framework wrappers in the order they should
    be build in.
    """
    topdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    frameworks = []
    partial_order = []

    for subdir in os.listdir(topdir):
        if not subdir.startswith('pyobjc-framework-'): continue

        setup = os.path.join(topdir, subdir, 'setup.py')

        requires = None
        with open(setup) as fp:
            for ln in fp:
                if requires is None:
                    if ln.strip().startswith('install_requires'):
                        requires = []
                else:
                    if ln.strip().startswith(']'):
                        break

                    dep = ln.strip()[1:-1]
                    if dep.startswith('pyobjc-framework'):
                        dep = dep.split('>')[0]
                        requires.append(dep)

        frameworks.append(subdir)
        for dep in requires:
            partial_order.append((dep, subdir))

    frameworks = topological_sort(frameworks, partial_order)
    return frameworks[:2]



def run_tests(version, archs):
    test_results = []

    lg = logging.getLogger("run_tests")

    lg.info("Run tests for Python %s with archs %s", version, archs)

    subdir = os.path.join(gBaseDir, "virtualenvs", "{0}.{1}".format(version, archs))
    if os.path.exists(subdir):
        lg.debug("Remove existing virtualenv")
        shutil.rmtree(subdir)

    base_python = "/Library/Frameworks/DbgPython-{0}.framework/Versions/{1}/bin/python".format(
            archs, version)
    if version[0] == '3':
        base_python += '3'

    if not os.path.exists(base_python):
        lg.warning("No python installation for Python %r %r", version, archs)
        raise RuntimeError(base_python)


    lg.debug("Create virtualenv in %s", subdir)
    if version[0] == '2':
        p = subprocess.Popen([
            base_python,
            "-mvirtualenv",
            subdir])
    else:
        p = subprocess.Popen([
            base_python,
            "-mvirtualenv3",
            subdir])

    xit = p.wait()
    if p != 0:
        lg.warning("Cannot create virtualenv in %s", subdir)
        raise RuntimeError(subdir)

    lg.debug("Install dependencies")
    pass # Nothing to do here


    lg.debug("Install base packages")
    # There are circular dependencies w.r.t. testing the Cocoa and Quartz wrappers,
    # install pyobjc-core, pyobjc-framework-Cocoa and pyobjc-framework-Quartz
    # to ensure we avoid those problems.
    for pkg in ["pyobjc-core-py3k", "pyobjc-framework-Cocoa", "pyobjc-framework-Quartz"]:
        pkgroot = os.path.join(gRootDir, pkg)
        pkgbuild = os.path.join(pkgroot, "build")
        if os.path.exists(pkgbuild):
            lg.debug("Remove build directory for %s", pkg)
            shutil.rmtree(pkgbuild)
        
        lg.debug("Install %s into %s", pkg, os.path.basename(subdir))
        p = subprocess.Popen([
            os.path.join(subdir, "bin", "python"),
            "setup.py", "install"],
            cwd=pkgroot)

        xit = p.wait()
        if xit != 0:
            lg.warning("Install %s failed", pkg)
            raise RuntimeError(pkg)

    lg.debug("Start testing cycle")
    for pkg in ["pyobjc-core-py3k"] + detect_frameworks():
        pkgroot = os.path.join(gRootDir, pkg)
        pkgbuild = os.path.join(pkgroot, "build")
        if os.path.exists(pkgbuild):
            lg.debug("Remove build directory for %s", pkg)
            shutil.rmtree(pkgbuild)

        lg.debug("Build %s for %s", pkg.os.path.basename(subdir))
        p = subprocess.Popen([
            os.path.join(subdir, "bin", "python"),
            "setup.py", "build"],
            cwd=pkgroot)

        xit = p.wait()
        if xit != 0:
            lg.warning("Build %s failed", pkg)
            raise RuntimeError(pkg)

        # TODO: 
        # - For python2.7/3.2: use `arch` to run tests with all architectures
        # - For python2.6/3.1: run tests using 'python-32' and 'python-64' 
        #   when those are available

        lg.debug("Test %s for %s", pkg.os.path.basename(subdir))
        p = subprocess.Popen([
            os.path.join(subdir, "bin", "python"),
            "setup.py", "test"],
            cwd=pkgroot, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()

        print("====STDOUT===")
        print(stdout)
        print("====STDERR===")
        print(stderr)
        print("====ENDEND===")

        test_results.append((pkg, stdout, stderr))

        xit = p.wait()
        if xit != 0:
            lg.warning("Test %s failed", pkg)
            raise RuntimeError(pkg)

        
        lg.debug("Install %s into %s", pkg, os.path.basename(subdir))
        p = subprocess.Popen([
            os.path.join(subdir, "bin", "python"),
            "setup.py", "install"],
            cwd=pkgroot)

        xit = p.wait()
        if xit != 0:
            lg.warning("Install %s failed", pkg)
            raise RuntimeError(pkg)

       
    return test_results

if __name__ == "__main__":
    try:
        main()
    except RuntimeError:
        sys.exit(1)
