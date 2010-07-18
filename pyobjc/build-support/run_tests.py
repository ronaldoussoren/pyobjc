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

"""
import sys
sys.dont_write_bytecode = True

import distribute_setup
distribute_setup.use_setuptools()

import pkg_resources
# Use Jinja2 for templating because that's the
# only one that supports Python3 at this time.
pkg_resources.require('Jinja2')

import getopt, os, shutil, logging, subprocess, time
from topsort import topological_sort

from jinja2 import Template

gBaseDir = '.'
gIndexTemplate = os.path.join(gBaseDir, 'templates', 'index.html')
gTestResults = os.path.join(gBaseDir, "testresults")


gUsage = """\
run_tests.py [-a archs] [--archs=archs] [-v versions] [--versions,versions]

archs:    32-bit,3-way (values separated by commas)
versions: 2.6,2.7,3.1,3.2    (values seperated by commas)
"""

gBaseDir = os.path.dirname(os.path.abspath(__file__))
gRootDir = os.path.dirname(gBaseDir)
gTestResults = os.path.join(gBaseDir, "testresults")

gFrameworkNameTemplate="DbgPython-{archs}"

gVersions=["3.2", "2.7", "3.1", "2.6"]
gArchs=["32-bit", "3-way"]

gArchMap={
    '3-way': ['ppc', 'i386', 'x86_64'],
    '32-bit': ['ppc', 'i386'],
    'intel': ['i386', 'x86_64'],
}


def supports_arch_command(version):

    # In virtualenvs both 2.6 and 2.7 support
    # the 'arch' command because virtualenv
    # copies the real interpreter into the 
    # virtualenv.
    return True

    # This code is true for the python 
    # interpreter outside of virtual environments:
    """
    major, minor = map(int, version.split('.'))
    if major == 2:
        return minor >= 7
    else:
        return minor >= 2
    """

def main():
    logging.basicConfig(level=logging.DEBUG)

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'a:v:h?', ["help", "archs=", "versions="])
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

    for ver in versions:
        for arch in archs:
            run_tests(ver, arch)

    gen_summary(versions, archs)

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
    return frameworks



def run_tests(version, archs):

    lg = logging.getLogger("run_tests")

    p = subprocess.Popen(["xcode-select", "-print-path" ],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    stdout, _ = p.communicate()
    path = stdout.strip()
    path = os.path.join(path.decode('UTF-8'), "Library", "PrivateFrameworks")
    ib_env = {
        'DYLD_FRAMEWORK_PATH': path,
    }
    del path
    

    lg.info("Run tests for Python %s with archs %s", version, archs)

    subdir = os.path.join(gBaseDir, "virtualenvs", "{0}--{1}".format(version, archs))
    if os.path.exists(subdir):
        lg.debug("Remove existing virtualenv")
        shutil.rmtree(subdir)

    if not os.path.exists(os.path.dirname(subdir)):
        os.mkdir(os.path.dirname(subdir))

    resultdir = os.path.join(gTestResults, "{0}--{1}".format(version, archs))
    if os.path.exists(resultdir):
        lg.debug("Remove existing results directory")
        shutil.rmtree(resultdir)

    if not os.path.exists(os.path.dirname(resultdir)):
        os.mkdir(os.path.dirname(resultdir))

    base_python = "/Library/Frameworks/{0}.framework/Versions/{1}/bin/python".format(
            gFrameworkNameTemplate.format(archs=archs, version=version), version)
    if version[0] == '3':
        base_python += '3'

    if os.path.exists(base_python + "-all"):
        base_python = base_python + "-all"

    lg.debug("Interpreter: %s", base_python)

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
    if xit != 0:
        lg.warning("Cannot create virtualenv in %s", subdir)
        raise RuntimeError(subdir)

    lg.debug("Install dependencies")
    pass # Nothing to do here


    lg.debug("Install base packages")
    if version[0] == '3':
        python = os.path.join(subdir, "bin", "python3")
    else:
        python = os.path.join(subdir, "bin", "python")
    # There are circular dependencies w.r.t. testing the Cocoa and Quartz wrappers,
    # install pyobjc-core, pyobjc-framework-Cocoa and pyobjc-framework-Quartz
    # to ensure we avoid those problems.
    for pkg in ["pyobjc-core", "pyobjc-framework-Cocoa", "pyobjc-framework-Quartz"]:
        if not os.path.exists(os.path.join(resultdir, pkg)):
            os.makedirs(os.path.join(resultdir, pkg))

        pkgroot = os.path.join(gRootDir, pkg)
        pkgbuild = os.path.join(pkgroot, "build")
        if os.path.exists(pkgbuild):
            lg.debug("Remove build directory for %s", pkg)
            shutil.rmtree(pkgbuild)
        
        lg.info("Install %s into %s", pkg, os.path.basename(subdir))
        p = subprocess.Popen([
            python, "setup.py", "install"],
            cwd=pkgroot, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        stdout, _ = p.communicate()

        with open(os.path.join(resultdir, pkg, "pre-build-stdout.txt"), "wb") as fd:
            fd.write(stdout)

        xit = p.wait()
        if xit != 0:
            lg.warning("Install %s failed", pkg)
            raise RuntimeError(pkg)

    lg.debug("Start testing cycle")
    for pkg in ["pyobjc-core"] + detect_frameworks():
        if not os.path.exists(os.path.join(resultdir, pkg)):
            os.makedirs(os.path.join(resultdir, pkg))

        pkgroot = os.path.join(gRootDir, pkg)

        if pkg == "pyobjc-framework-InterfaceBuilderKit":
            env = os.environ.copy()
            env.update(ib_env)
            
        else:
            env = os.environ

        pkgbuild = os.path.join(pkgroot, "build")
        if os.path.exists(pkgbuild):
            lg.debug("Remove build directory for %s", pkg)
            shutil.rmtree(pkgbuild)

        lg.debug("Build %s for %s", pkg, os.path.basename(subdir))
        p = subprocess.Popen([
            python, "setup.py", "install"],
            cwd=pkgroot, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        stdout, _ = p.communicate()
        with open(os.path.join(resultdir, pkg, "build-stdout.txt"), "wb") as fd:
            fd.write(stdout)

        xit = p.wait()
        if xit != 0:
            print(stdout)
            lg.warning("Build %s failed", pkg)
            #raise RuntimeError(pkg)
            continue

        # TODO: 
        # - For python2.7/3.2: use `arch` to run tests with all architectures
        # - For python2.6/3.1: run tests using 'python-32' and 'python-64' 
        #   when those are available

        if supports_arch_command(version):
            for a in gArchMap[archs]:
                lg.info("Test %s for %s (%s)", pkg, os.path.basename(subdir), a)
                p = subprocess.Popen([
                    '/usr/bin/arch', '-' + a,
                    python, "setup.py", "test"],
                    cwd=pkgroot, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=env)
                stdout, _ = p.communicate()

                with open(os.path.join(resultdir, pkg, "test-stdout-{0}.txt".format(a)), "wb") as fd:
                    fd.write(stdout)

                status = stdout.splitlines()
                if status[-1].startswith(b'['):
                    status = status[-2]
                else:
                    status = status[-1]
                status = status.decode('UTF-8')
                lg.info("Test %s for %s (%s): %s", pkg, os.path.basename(subdir), a, status)

                xit = p.wait()
                if xit != 0:
                    lg.warning("Test %s failed", pkg)

                with open(os.path.join(resultdir, pkg, "test-stdout-{0}.exit".format(a)), "w") as fd:
                    fd.write(str(xit))
                
        else:
            lg.debug("Test %s for %s", pkg, os.path.basename(subdir))
            p = subprocess.Popen([
                python, "setup.py", "test"],
                cwd=pkgroot, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                env=env)
            stdout, _ = p.communicate()

            with open(os.path.join(resultdir, pkg, "test-stdout.txt"), "wb") as fd:
                fd.write(stdout)

            status = stdout.splitlines()[-1]
            lg.info("Test %s for %s: %s", pkg, os.path.basename(subdir), status)

            xit = p.wait()
            if xit != 0:
                lg.warning("Test %s failed", pkg)
                continue
                #raise RuntimeError(pkg)

        
        lg.debug("Install %s into %s", pkg, os.path.basename(subdir))
        p = subprocess.Popen([
            python, "setup.py", "install"],
            cwd=pkgroot)

        xit = p.wait()
        if xit != 0:
            lg.warning("Install %s failed", pkg)
            raise RuntimeError(pkg)

       

def parse_tests(inputfile):
    result = {
        'test_pass':  0,
        'test_fail':  0,
        'test_error': 0,
    }
    last_line = ''
    with open(inputfile) as stream:
        for ln in stream:
            if not ln.startswith('['):
                last_line = ln
            ln = ln.rstrip()
            if ln.endswith('... ok'):
                result['test_pass'] += 1
            elif ln.endswith('... FAIL'):
                result['test_fail'] += 1
            elif ln.endswith('... ERROR'):
                result['test_error'] += 1

            elif 'Fatal Python error' in ln:
                # Interpreter aborted itself, 
                # treat this as a test error
                result['test_error'] += 1


    if not last_line.split()[0].isupper():
        # The last line of the output should
        # be the unittest status line, which
        # starts with an uppercase word. 
        # Not having it is an error (and tends
        # to be caused by interpreter crashes)
        result['test_error'] += 1

    result['class_pass'] = ''
    result['class_fail'] = ''
    result['class_error'] = ''
    if result['test_pass'] == 0  \
        and result['test_fail'] == 0 \
        and result['test_error'] == 0:
            result['class_pass'] = 'error'
    if result['test_fail']:
        result['class_fail'] = 'warning'
    if result['test_error']:
        result['class_error'] = 'error'

    if result['test_error'] + result['test_fail'] == 0:
        result['class_pass'] = 'ok'
                
    return result

def parse_build(inputfile):
    result = {
        'build_warnings': 0,
        'build_errors':   0,
    }
    with open(inputfile) as stream:
        for ln in stream:
            if 'warning: no directories found matching' in ln:
                # Completely harmless warning
                continue


            if 'error:' in ln:
                result['build_errors'] += 1

            elif ln.startswith('../../libxml2-src/') or \
                    ln.startswith('libffi-src'):
                # Ignore warnings in 3th-party libraries (pyobjc-core)
                continue


            elif 'is deprecated' in ln and 'objc/Protocol.h' in ln:
                # Pyobjc-core uses deprecated access methods for protocols
                # in 32-bit mode. 
                continue

            elif 'is deprecated' in ln:
                # Ignore all deprecation errors for now, framework wrappers
                # also trigger these when they contain manual wrappers for
                # deprecated APIs.
                continue

            elif 'warning:' in ln:
                result['build_warnings'] += 1

    result['class_warnings'] = ''
    result['class_errors'] = ''
    if result['build_warnings']:
        result['class_warnings'] = 'warning'
    if result['build_errors']:
        result['class_errors'] = 'error'

    if result['build_warnings'] + result['build_errors'] == 0:
        result['class_warnings'] = 'ok'
        result['class_errors'] = 'ok'

    return result

def get_svnversion():
    p = subprocess.Popen([
        'svnversion',
        ], cwd='..', stdout=subprocess.PIPE)
    stdout, _ = p.communicate()
    xit = p.wait()
    if xit != 0:
        raise RuntimeError(xit)

    return stdout.decode('UTF-8')

def get_svnurl():
    p = subprocess.Popen([
        'svn', 'info', '.'
        ], cwd='..', stdout=subprocess.PIPE)
    stdout, _ = p.communicate()
    xit = p.wait()
    if xit != 0:
        raise RuntimeError(xit)

    for ln in stdout.splitlines():
        if ln.startswith(b'URL'):
            return ln.split(None, 1)[1].decode('UTF-8')

def get_osx_version():
    p = subprocess.Popen([
        'sw_vers',
        ], cwd='..', stdout=subprocess.PIPE)
    stdout, _ = p.communicate()
    xit = p.wait()
    if xit != 0:
        raise RuntimeError(xit)

    r = {}
    for ln in stdout.splitlines():
        k, v = ln.decode('UTF-8').split(':', 1)
        r[k.strip()] = v.strip()

    return "{ProductName} {ProductVersion} ({BuildVersion})".format(**r)

def gen_summary(report_versions, report_archs):
    with open(gIndexTemplate) as fp:
        tmpl = Template(fp.read())

    svn={}
    svn['revision'] = get_svnversion()
    svn['url'] = get_svnurl()

    osx={}
    osx['version'] = get_osx_version()

    versions = {}

    for subdir in os.listdir(gTestResults):
        if subdir == 'index.html': continue
        version, style = subdir.split('--')

        if version not in report_versions: continue
        if style not in report_archs: continue

        versions[(version, style)] = modules = []

        for mod in os.listdir(os.path.join(gTestResults, subdir)):
            moddir = os.path.join(gTestResults, subdir, mod)
            info = parse_build(os.path.join(moddir, 'build-stdout.txt'))
            info['name'] = mod
            modules.append(info)
            info['archs'] = []
            info['class'] = None

            if info['build_errors']:
                info['class'] = 'error'
            #elif info['build_warnings']:
                #info['class'] = 'warning'

            for fn in os.listdir(moddir):
                if not fn.startswith('test'): continue
                if fn.endswith('exit'): continue

                if fn == 'test-stdout.txt':
                    a = 'all'

                else:
                    a = fn.split('-')[-1].split('.')[0]

                info['archs'].append(a)
                info[a] =  parse_tests(os.path.join(moddir, fn))

                with open (os.path.join(moddir, fn)[:-3] + 'exit') as fd:
                    info[a]['exit'] = fd.read().strip()


                if info[a]['test_fail'] and (info['class'] is None):
                    info['class'] = 'warning'

                if info[a]['test_error']:
                    info['class'] = 'error'

                if info[a]['exit'] != 0:
                    info['class'] = 'crash'


            if info['class'] is None:
                info['class'] = 'ok'

    with open(os.path.join(gTestResults, 'index.html'), 'w') as fp:
        fp.write(tmpl.render(
            svn=svn,
            osx=osx,
            versions=versions,
            sorted=sorted,
            timestamp=time.ctime(),
            ))

if __name__ == "__main__":
    try:
        main()
    except RuntimeError:
        sys.exit(1)
