"""
These functions can check the source code for manually wrapped methods. This
is not 100% correct, but should do.
"""
import os, re, sys

gRegisterRE = re.compile(r'''
        PyObjC_RegisterMethodMapping\s*\(\s*
            class([A-Za-z0-9_]*)\s*
            ,\s*@selector\(([^)]*)\)\s*
            ,\s*([A-Za-z0-9_]*)\s*,''', re.MULTILINE|re.VERBOSE)

def scanForWrappers(file):
    result = {}
    data = open(file, 'r').read()

    for item in gRegisterRE.findall(data):
        clsName, selector, wrapper = item

        if wrapper == 'PyObjCUnsupportedMethod_Caller':
            result[(clsName, selector)] = dict(ignore=True)
        else:
            result[(clsName, selector)] = dict(manual=True)
    return result

def scanModules(basedir):
    result = {}
    for framework in os.listdir(basedir):
        for fn in os.listdir(os.path.join(basedir, framework)):
            if not fn.endswith('.m') or fn.endswith('.c'): continue

            result.update(scanForWrappers(os.path.join(basedir, framework, fn)))

    return result
