#!/usr/bin/env python
"""
This script will rewrite the macho headers of the frameworks in the
nightly webkit snapshot, to make sure PyObjC can use them.
"""
import os, shutil

from macholib.MachO import MachO

def rewriteFramework(framework, frameworkMap):

    basename = os.path.splitext(os.path.basename(framework))[0]
    dyld = os.path.abspath(os.path.join(framework, basename))

    macho = MachO(dyld)

    def changefunc(key):
        if key == dyld:
            return dyld

        dirname, filename = os.path.split(key)
        return frameworkMap.get(filename)

    macho.rewriteLoadCommands(changefunc)
    macho.write(open(dyld, 'rb+'))

def rewriteFrameworksInDirectory(dirname):
    frameworks = [
            fn for fn in os.listdir(dirname) if fn.endswith('.framework') ]
    mapping = {}
    for fn in frameworks:
        mapping[os.path.splitext(fn)[0]] = os.path.join(os.path.abspath(dirname), fn , os.path.splitext(fn)[0])

    for fn in frameworks:
        rewriteFramework(fn, mapping)

def extractWebKitApp(pathToApp, outputDir):
    resources = os.path.join(pathToApp, 'Contents', 'Resources')
    frameworks = [
            fn for fn in os.listdir(resources) if fn.endswith('.framework') ]
    for framework in frameworks:
        if os.path.exists(os.path.join(outputDir, framework)):
            shutil.rmtree(os.path.join(outputDir, framework))

        shutil.copytree(
                os.path.join(resources, framework),
                os.path.join(outputDir, framework), symlinks=True)

        rewriteFrameworksInDirectory(outputDir)

def main():
    extractWebKitApp('WebKit.app', '.')


if __name__ == '__main__':
    main()
