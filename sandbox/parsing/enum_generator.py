from pyparsing import *
from itertools import *
import re
try:
    set
except NameError:
    from sets import Set as set

_enum_parser = None
def enum_parser():
    global _enum_parser
    if _enum_parser is not None:
        return _enum_parser

    singleLineComment = "//" + restOfLine
    anyComment = singleLineComment | cStyleComment

    ident = Word(alphas + "_", alphanums + "_")

    anyInteger = Word( '+-'+nums, nums)
    anyDecimal = Combine( anyInteger
        + Optional( Literal('.') + Optional( Word( nums ) ) )
        + Optional( CaselessLiteral('e') + anyInteger )
        + Optional( CaselessLiteral('f') )
    )
    anyHex = Literal('0x') + Word(nums + 'abcdefABCDEF')
    anyOctal = Word('0', '01234567', min=2)
    anyNumber = anyOctal | anyDecimal | anyHex
    
    lineContinuation = Literal("\\") + LineEnd()

    KEYWORDS = "extern volatile void const typedef static const"
    defineValue = (
        ~oneOf(KEYWORDS) +
        ( ident | anyNumber | quotedString )
    )
    validDefineValue = ( defineValue
        | Combine( Literal('(')
            + defineValue
            + Literal(')')
            , adjacent=False )
    )
    define = Combine( Literal("#")
        + Literal("define")
        + ident.setResultsName("define")
        + validDefineValue
        + LineEnd()
        , adjacent=False
    ).setName('define').setResultsName('DEFINE')
    
    enumValue = ZeroOrMore( CharsNotIn(',}') ).setName('enumValue')
    enumValue.ignore( anyComment )

    enumPair = ident + Suppress( enumValue )
    enumPair.ignore( anyComment )
    
    enum = Combine( Optional( Literal("typedef") )
        + Literal("enum")
        + Optional( ident )
        + Literal("{")
        + delimitedList( enumPair ).setResultsName("enum")
        + Literal("}")
        , adjacent=False
    ).setName('enum').setResultsName('ENUM')
    
    bnf = define | enum
    bnf.ignore( anyComment )
    bnf.ignore( lineContinuation )
    _enum_parser = bnf
    return _enum_parser
    

HEADERSTUB = r"""
#import <Foundation/Foundation.h>
#import <Python/Python.h>
#import <stdio.h>
#import <unistd.h>

#define _C_ID       '@'
#define _C_CLASS    '#'
#define _C_SEL      ':'
#define _C_CHR      'c'
#define _C_UCHR     'C'
#define _C_SHT      's'
#define _C_USHT     'S'
#define _C_INT      'i'
#define _C_UINT     'I'
#define _C_LNG      'l'
#define _C_ULNG     'L'
#define _C_LNG_LNG  'q'
#define _C_ULNG_LNG 'Q'
#define _C_FLT      'f'
#define _C_DBL      'd'
#define _C_BFLD     'b'
#define _C_VOID     'v'
#define _C_UNDEF    '?'
#define _C_PTR      '^'
#define _C_CHARPTR  '*'
#define _C_ATOM     '%'
#define _C_ARY_B    '['
#define _C_ARY_E    ']'
#define _C_UNION_B  '('
#define _C_UNION_E  ')'
#define _C_STRUCT_B '{'
#define _C_STRUCT_E '}'
#define _C_VECTOR   '!'

static void printPythonRepresentation(char *name, char *typecode, void *data) {
    PyObject *obj = NULL;
    int typelen = strlen(typecode);
    if (typecode[1] == '\0') {
        switch (typecode[0]) {
            case _C_INT:
            case _C_LNG:
                obj = PyInt_FromLong(*((long *)data));
                break;
            case _C_UINT:
            case _C_ULNG:
                obj = PyLong_FromUnsignedLong(*((unsigned long *)data));
                break;
            case _C_LNG_LNG:
                obj = PyLong_FromLongLong(*((long long *)data));
                break;
            case _C_ULNG_LNG:
                obj = PyLong_FromUnsignedLongLong(*((unsigned long long *)data));
                break;
            case _C_FLT:
                obj = PyFloat_FromDouble((double)(*(float *)data));
                break;
            case _C_DBL:
                obj = PyFloat_FromDouble(*((double *)data));
                break;
        }
    } else {
        if (typelen > 3 && typecode[0] == '[' && typecode[typelen-1] == ']' && typecode[typelen-2] == 'c') {
            obj = PyString_FromString((const char *)(*((char **)data)));
        }
    }
    if (obj == NULL) { 
        printf("# unrecognized type code for %s : \"%s\"\n", name, typecode);
    } else { 
        PyObject *repr = PyObject_Repr(obj); 
        Py_DECREF(obj); 
        if (repr == NULL) { 
            printf("# exception during repr for %s\n", name); 
        } else { 
            printf("%s = %s\n", name, PyString_AsString(repr)); 
            Py_DECREF(repr); 
        } 
    } 
}
#define PRINT_DECLARATION(name) do { \
    typeof(name) name##copy = name; \
    printPythonRepresentation(#name, @encode(typeof(name)), (void *)&(name##copy)); \
} while (0)

"""

MAINBEGIN = """
int main(int argc, char **argv)
{
    Py_Initialize();
"""

MAINEND = """
    Py_Finalize();
    return 1;
}
"""

def emit_enum(names):
    for name in names:
        yield "    PRINT_DECLARATION(%s);" % (name,)

def emit_define(name):
    yield "#if defined(%s)" % (name,)
    yield "    PRINT_DECLARATION(%s);" % (name,)
    yield "#endif"

def scanForImports(fn, framework):
    data = file(fn).read()
    return re.compile(r'#\s*import\s+<' + framework + r'/([^>]+)>').findall(data)

import os
import sys
import glob

def codeGeneratorForFramework(frameworkname, basepath, fileobj=None):
    if fileobj is None:
        fileobj = sys.stdout
    if fileobj == sys.stdout:
        flush = fileobj.flush
    else:
        flush = lambda: None
    frameworkpath = os.path.join(basepath, frameworkname + '.framework', 'Headers')
    files = [frameworkname + '.h']
    processed = []
    while files:
        fn = files.pop(0)
        if fn in processed:
            continue
        processed.append(fn)
        files.extend(scanForImports(os.path.join(frameworkpath, fn), frameworkname))

    print '#import <%s/%s.h>' % (frameworkname, frameworkname)
    print HEADERSTUB
    print MAINBEGIN
    for fn in processed:
        fn = os.path.join(frameworkpath, fn)
        print r'    printf("# %s\n");' % (fn.replace('"', r'\"'),)
        sys.stdout.flush()
        for obj, s, e in enum_parser().scanString(file(fn).read()):
            print r'    printf("# POS(%s:%s)\n");' % (s, e)
            names = ()
            if obj.ENUM:
                emitter = emit_enum(obj.ENUM.enum)
            elif obj.DEFINE:
                emitter = emit_define(obj.DEFINE.define)
            for line in emitter:
                print line
            sys.stdout.flush()
    print MAINEND

if __name__ == '__main__':
    codeGeneratorForFramework('Foundation', '/System/Library/Frameworks')
