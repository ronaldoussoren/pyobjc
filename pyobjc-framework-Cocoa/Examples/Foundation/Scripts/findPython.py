#!/usr/bin/pythonw
"""
Find the library name for the current Python interpreter
"""
import objc
from Foundation import NSBundle


def S(*args):
    return b"".join(args)


# these are void*
NSSymbol = b"I"
NSModule = b"I"

FUNCTIONS = [
    ("NSIsSymbolNameDefined", S(objc._C_BOOL, objc._C_CHARPTR)),
    ("NSLookupAndBindSymbol", S(NSSymbol, objc._C_CHARPTR)),
    ("NSModuleForSymbol", S(NSModule, NSSymbol)),
    ("NSLibraryNameForModule", S(objc._C_CHARPTR, NSModule)),
]


def libraryNameForSymbol(symbol):
    bndl = NSBundle.bundleWithPath_("/System/Library/Frameworks/System.framework")
    d = {}
    objc.loadBundleFunctions(bndl, d, FUNCTIONS)
    for (fn, _sig) in FUNCTIONS:
        if fn not in d:
            raise ValueError("Couldn't find function %s" % (fn,))
    symbol = b"_" + symbol
    if not d["NSIsSymbolNameDefined"](symbol):
        # symbol not defined
        return None
    sym = d["NSLookupAndBindSymbol"](symbol)
    if not sym:
        raise ValueError("Couldn't bind symbol %r" % (symbol,))
    mod = d["NSModuleForSymbol"](sym)
    if not mod:
        raise ValueError("Couldn't find module for symbol %r" % (symbol,))
    return d["NSLibraryNameForModule"](mod)


if __name__ == "__main__":
    print(libraryNameForSymbol(b"Py_Initialize"))
