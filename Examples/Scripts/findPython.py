#!/usr/bin/pythonw
"""
Find the library name for the current Python interpreter
"""
import sys
import objc
from Foundation import *

def S(*args):
    return ''.join(args)

# these are void*
NSSymbol = 'I'
NSModule = 'I'

FUNCTIONS=[
    ( u'NSIsSymbolNameDefined', S(objc._C_BOOL, objc._C_CHARPTR) ),
    ( u'NSLookupAndBindSymbol', S(NSSymbol, objc._C_CHARPTR) ),
    ( u'NSModuleForSymbol', S(NSModule, NSSymbol) ),
    ( u'NSLibraryNameForModule', S(objc._C_CHARPTR, NSModule) ),
]

def libraryNameForSymbol(symbol):
    bndl = NSBundle.bundleWithPath_(u'/System/Library/Frameworks/System.framework')
    d = {}
    objc.loadBundleFunctions(bndl, d, FUNCTIONS)
    for (fn, sig) in FUNCTIONS:
        if fn not in d:
            raise ValueError("Couldn't find function %s" % (fn,))
    symbol = '_' + symbol
    if not d['NSIsSymbolNameDefined'](symbol):
        # symbol not defined
        return None
    sym = d['NSLookupAndBindSymbol'](symbol)
    if not sym:
        raise ValueError("Couldn't bind symbol %r" % (symbol,))
    mod = d['NSModuleForSymbol'](sym)
    if not mod:
        raise ValueError("Couldn't find module for symbol %r" % (symbol,))
    return d['NSLibraryNameForModule'](mod)

if __name__ == "__main__":
    print libraryNameForSymbol('Py_Initialize')
