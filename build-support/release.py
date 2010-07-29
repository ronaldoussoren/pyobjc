#!/usr/bin/env python3
# TODO: 
# - create and upload eggs for 'intel' builds of 2.7 and 3.2
# - create and upload documentation (to packages.python.org)
# - sign release files using gpg (distutils has support, need to find a way
#   to avoid typing password dozens of times)
import getopt
import subprocess
import shutil
import os
import sys
from topsort import topological_sort


gUsage="""\
    release.py --all
or
    release.py package...
"""

gTopDir = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)))

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'h?',
                ['all', 'help', 'identity='])
    except getopt.error as msg:
        print(msg, file=sys.stderr)
        print(gUsage, file=sys.stderr)
        sys.exit(1)

    all=False
    packages = args
    identity = 'ronaldoussoren@mac.com'
    upload = ['upload',]

    for k, v in opts:
        if k in ('-h', '-?', '--help'):
            print(gUsage)
            sys.exit(0)

        elif k in ('--all',):
            all=True

        elif k in ('--identity',):
            identity = v

        elif k in ('--no-upload',):
            upload = []

        elif k in ('--upload',):
            upload = ['upload',]

        else:
            raise ValueError("Unhandled option: %s"%(k,))

    if all and packages:
        print("Specify either --all or a list of packages", file=sys.stderr)
        sys.exit(1)

    if not all and not packages:
        print("Specify either --all or a list of packages", file=sys.stderr)
        sys.exit(1)

    if all:
        packages = [ 'pyobjc-core' ] 
        packages += detect_frameworks()
        packages += ['pyobjc']

    for pkg in packages:
        print("== ", pkg)
        srcdir = os.path.join(gTopDir, pkg)
        if not os.path.exists(srcdir):
            print("No such package:", srcdir, file=sys.stderr)
            continue

        if os.path.exists(os.path.join(srcdir, 'build')):
            shutil.rmtree(os.path.join(srcdir, 'build'))

        if os.path.exists(os.path.join(srcdir, 'dist')):
            shutil.rmtree(os.path.join(srcdir, 'dist'))

        print(" - sdist")
        p = subprocess.Popen(
            ['python2.7', 'setup.py', 'sdist', ] + upload,
                # 'upload', '--sign', '--identity',  identity ],
            cwd=srcdir, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        lines, _ = p.communicate()
        exit = p.wait()

        if exit != 0:
            print(lines.decode('utf-8'))
            print("Creating or uploading sdist failed")
            sys.exit(1)

        for python in ('python2.6', 'python2.7', 'python3.1', 'python3.2'):
            print(" -", python)

            # Force removal of 'build', I ran into 2to3 issues for some python
            # versions.
            if os.path.exists(os.path.join(srcdir, 'build')):
                shutil.rmtree(os.path.join(srcdir, 'build'))

            p = subprocess.Popen(
                [python, 'setup.py', 'bdist_egg', ] + upload,
                    # 'upload', '--sign', '--identity',  identity ],
                cwd=srcdir, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            lines, _ = p.communicate()
            exit = p.wait()
            if exit != 0:
                print(lines.decode('utf-8'))
                print("Creating or uploading bdist_egg for", python, "failed")
                sys.exit(1)

            p = subprocess.Popen(
                [python, 'setup.py', 'install'], 
                cwd=srcdir, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            lines, _ = p.communicate()
            exit = p.wait()
            if exit != 0:
                print(lines.decode('utf-8'))
                print("Installing for", python, "failed")
                sys.exit(1)


        # TODO: create and upload eggs for 'intel' builds of 2.7 and 3.2
        # TODO: create and upload documentation (to packages.python.org)

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
    return frameworks

if __name__ == "__main__":
    main()
