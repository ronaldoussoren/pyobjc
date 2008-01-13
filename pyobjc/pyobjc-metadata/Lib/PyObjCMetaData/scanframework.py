"""
The actual metadata generator.

Missing features:
    * Sync with the RubyCocoa stuff
      - ignored_headers in the exceptions file
    * Support for class methods
    * The script should also work with non-system frameworks
    * Suppress argument nodes in the metadata when there isn't any metadata
      (e.g. we've determineted that there should be an exception but no
       exception is present) -> keeps the metadata nice and small when we
       guess incorrect.
    * Load the framework and iterate over all classes to look for methods
      with difficult signatures (for compatibility with the current meta
      data in PyObjC).

Cleanup:
    * Merge FrameworkScanner and FrameworkMetadata?
    * Can we avoid the PPC compile? This is needed to find four-character-codes,
      and these now slow down metadata generation for the majority of frameworks
      that don't use these :-( :-(

Testing:
    * Run this script on frameworks and check by hand if all required 
      information is present.
    * Also compare with PyObjC-trunk

Performance:
    * We're currently compiling and running an awful lot of proglets, that
      makes development easier but isn't very good for speed. As one shouldn't
      have to run the tool very often anyway and the problem is most glaring
      on big frameworks like Foundation, I don't think I'll refactor for this.
"""
import objc
import os
import optparse
import string
import pkg_resources
import StringIO

# Temporary definitions, to help find problematic API's
##objc._C_UNICHAR = 'T'
##objc._C_CHAR_AS_TEXT = 't'
##objc._C_CPPBOOL = 'Z'
##objc._C_CHAR_AS_INT = 'z'

try:
    set
except NameError:
    from sets import Set as set

try:
    sorted
except NameError:
    def sorted(seq):
        seq2 = list(seq)
        seq2.sort()
        return seq2

import pprint
import glob
import sys
from macholib.dyld import framework_find
from itertools import *
from textwrap import dedent
from itertools import imap
import logging 
import subprocess
import cPickle as pickle
import re

from PyObjCMetaData.tokenize_header import *
from PyObjCMetaData.et import *


gStructFieldNameRe = re.compile('"[^"]*"')

gBooleanAttributesDefaultingTrue=[
    'function_pointer_retained',
    'null_accepted',
]

gBooleanAttributesDefaultingFalse=[
    'nsstring',
    'already_retained',
    'already_cfretained',
    'class_method',
    'c_array_length_in_result',
    'c_array_delimited_by_null',
    'c_array_of_variable_length',
    'printf_format',
    'function_pointer',
    'magic_cookie',
]

gTypeModifierAttributes = [
    'c_array_length_in_arg',
    'c_array_of_fixed_length',
    'c_array_delimited_by_null',
    'c_array_length_in_result',
    'c_array_of_variable_length',
    'type_modifier',
    'sel_of_type',
]

gExceptionAttributes = dict(
    constant = [ 'type', 'type64', 'magic_cookie' ],

    struct = [ 'type', 'type64' ],

    string_constant = [ 'value', 'nsstring' ],

    retval = [ 
            'type', 'type64', 
            'already_retained',
            'already_cfretained',
            'numeric',
            'c_array_length_in_arg',
            'c_array_of_fixed_length',
            'c_array_delimited_by_null',
            'c_array_of_variable_length',
            'sel_of_type',
            'function_pointer',
            'function_pointer_retained',
        ],
    arg = [ 
            'type', 'type64', 
            'type_modifier', 
            'null_accepted', 
            'already_retained',
            'already_cfretained',
            'numeric',
            'c_array_length_in_arg',
            'c_array_of_fixed_length',
            'c_array_delimited_by_null',
            'c_array_length_in_result',
            'printf_format',
            'c_array_of_variable_length',
            'sel_of_type',
            'function_pointer',
            'function_pointer_retained',
        ],

    cftype = [ 'gettypeid_func', 'tollfree', ],

    method = [ 'suggestion', 'c_array_delimited_by_null'],
)
gExceptionAttributes[None] = [ 'ignore', 'comment' ]


# XML header for the metadata files, needed because ElementTree won't write
# and XML declaration or doctype
HEADER='''\
<?xml version='1.0'?>
<!DOCTYPE signatures SYSTEM "file://localhost/System/Library/DTDs/BridgeSupport.dtd">'''


COMPILE_FILE='''\
#import <Foundation/Foundation.h> /* to pick up std definitions */
#import <AppKit/AppKit.h> /* Because Automator framework sucks... */
%(includes)s
#include <stdio.h>

%(globalDefinitions)s

int main(void)
{
    NSAutoreleasePool* pool = [[NSAutoreleasePool alloc] init];
%(mainBody)s

    [pool release];
    return 0;
}
'''

IVAR_TYPE_DEFINITIONS='''\
#import <objc/objc-class.h>

@interface _SCANFRAMEWORK : NSObject
{
    %(ivarType)s ivar;
}
@end
@implementation _SCANFRAMEWORK
@end

#ifndef MAC_OS_X_VERSION_10_5
/* ^^^ What's actually needed is some configure-like logic to detect if
 * ivar_getTypeEncoding is available.
 */
#define ivar_getTypeEncoding(ivar) ((ivar)->ivar_type)
#endif
'''

IVAR_TYPE_MAIN='''\
    printf("%s\\n", ivar_getTypeEncoding(class_getInstanceVariable([_SCANFRAMEWORK class], "ivar")));
'''


#
# Some code for printing the values for enums and simple defines. The code works
# without knowing the type of the to-be-printed value beforehand.
#

ENUM_DEFINITIONS='''\
#include <objc/objc-runtime.h>
#include <ctype.h>

#ifndef _C_LNG_LNG
#define _C_LNG_LNG 'q'
#endif

#ifndef _C_ULNG_LNG
#define _C_ULNG_LNG 'Q'
#endif
'''

# NOTE: the circumspect way of printing is needed to avoid compile-time errors.
ENUM_MAIN=r'''
    __typeof__(%(name)s) tmpval = %(name)s;

    const char* tp = @encode(__typeof__(tmpval));
    if (*tp == _C_ARY_B) {
        tp++;
        while (isdigit(*tp)) tp++;
        if (*tp == _C_CHR) {
            printf("%%c\n", _C_CHARPTR);
            printf("%%s\n", tmpval);
            return 0;
        } 
    }

    printf("%%s\n", @encode(__typeof__(tmpval)));
    switch (*@encode(__typeof__(tmpval))) {
    case _C_LNG_LNG: 
        printf("%%lld\n", *(long long*)&tmpval);
        break;
    case _C_LNG:
        printf("%%lld\n", (long long)*(long*)&tmpval);
        break;
    case _C_INT:
        printf("%%lld\n", (long long)*(int*)&tmpval);
        break;
    case _C_SHT:
        printf("%%lld\n", (long long)*(short*)&tmpval);
        break;
    case _C_CHR:
        printf("%%lld\n", (long long)*(char*)&tmpval);
        break;

    case _C_ULNG_LNG:
        printf("%%llu\n", *(unsigned long long*)&tmpval);
        break;
    case _C_ULNG:
        printf("%%lld\n", (unsigned long long)*(unsigned long*)&tmpval);
        break;
    case _C_UINT:
        printf("%%lld\n", (unsigned long long)*(unsigned int*)&tmpval);
        break;
    case _C_USHT:
        printf("%%lld\n", (unsigned long long)*(unsigned short*)&tmpval);
        break;
    case _C_UCHR:
        printf("%%lld\n", (unsigned long long)*(unsigned char*)&tmpval);
        break;

    case _C_DBL:
        printf("%%.17g", *(double*)&tmpval);
        break;

    case _C_FLT:
        printf("%%.17g", (double)*(float*)&tmpval);
        break;

    case _C_CHARPTR:
        printf("%%s\n", tmpval);
        break;

    case _C_ID:
        /* This is ugly as hell, but needed to get this code through the
         * compiler when the value isn't an object.
         */
        if ([*(NSObject**)&tmpval isKindOfClass:[NSString class]]) {
            printf("%%s\n", ([*(NSString**)&tmpval UTF8String]));
            break;
        }
        /* FALL THROUGH */

    default:
        if (strcmp(@encode(__typeof__(tmpval)),@encode( __typeof__(CFSTR("")))) == 0) {
            printf("%%s\n", ([*(NSString**)&tmpval UTF8String]));
            break;

        } else if (*@encode(__typeof__(tmpval)) == _C_ARY_B)  {
            char* eltype = @encode(__typeof__(tmpval));
            eltype += 1;
            while (isdigit(*eltype)) eltype++;
            if (*eltype == _C_CHR) {
                printf("%%s\n", *(char**)&tmpval);
            }
            break;
        }
        fprintf(stderr, "Sorry, don't know how to print %(name)s: %%s\n",
            @encode(__typeof__(tmpval)));
        return 1;
    }
    return 0;
'''

def simpleValue(value):
    try:
        v = int(value.strip(), 0)
        return True
    except ValueError:
        return False

def indentET(elem, level=0):
    """ Add whitespace to an elementtree to make it print nicely """

    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        for el in elem:
            indentET(el, level+1)
        if not el.tail or not el.tail.strip():
            el.tail = i
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

class cleanfile(file):
    def write(self, s):
        file.write(self, cleanup_text(s))

    def writelines(self, lines):
        file.writelines(self, imap(cleanup_text, lines))

class typedict(object):
    def __init__(self):
        self.headers = set()
        self.dct = {'%% HEADERS %%': self.headers}
        
    def update(self, dct):
        if not isinstance(dct, dict):
            dct = dict(dct)
        for k,v in dct.iteritems():
            self[k] = v


    def __len__(self):
        return len(self.dct)

    def __iter__(self):
        return iter(self.dct)

    def __contains__(self, key):
        return normalize_type(key) in self.dct

    def addHeader(self, header):
        if header in self.headers:
            return False
        self.headers.add(header)
        return True

    def __setitem__(self, key, item):
        # allow updates from a type hint file
        if key == '%% HEADERS %%':
            try:
                self.dct[key].update(item)
            except KeyError:
                self.dct[key] = set(item)
            return
        key = normalize_type(key)
        self.dct[key] = item
        #print '[type] %s -> %s' % (key, item)

    def __getitem__(self, key):
        key = normalize_type(key)
        return self.dct[key]

    def get(self, key, default=None):
        key = normalize_type(key)
        return self.dct.get(key, default)


def update_fallback(env, framework):
    frameworks = os.path.join(framework, 'Frameworks')
    if os.path.exists(frameworks):
        fallback = env.get('DYLD_FALLBACK_FRAMEWORK_PATH')
        if fallback is None:
            fallback = frameworks
        else:
            fallback += ':' + frameworks
        env['DYLD_FALLBACK_FRAMEWORK_PATH'] = fallback

def framework_header(f, known={}, env=dict(os.environ)):
    headers = known.get(f)
    if headers is not None:
        return headers
    dylib = locate_framework(f, env=env)
    framework = os.path.dirname(dylib)
    update_fallback(env, framework)
    headers = known[f] = os.path.join(framework, 'Headers')
    return headers

def link_flag_for_framework(name):
    try:
        framework_find(name)
        return name

    except ValueError:
        subpath = 'Frameworks/%s.framework'%(name,)
        for basedir in '/Library/Frameworks', '/System/Library/Frameworks':
            for dn in os.listdir(basedir):
                possibleMatch = os.path.join(basedir, dn, subpath)
                if os.path.exists(possibleMatch):
                    return os.path.splitext(dn)[0]
        raise

def locate_framework(name, **kwds):
    try:
        return framework_find(name, **kwds)
    except ValueError:
        # Framework wasn't found directly, it might be a subframework
        if name.endswith('.framework'):
            subpath = 'Frameworks/%s'%(name,)
        else:
            subpath = 'Frameworks/%s.framework'%(name,)

        for basedir in '/Library/Frameworks', '/System/Library/Frameworks':
            for dn in os.listdir(basedir):
                possibleMatch = os.path.join(basedir, dn, subpath)
                if os.path.exists(possibleMatch):
                    return os.path.join(possibleMatch, os.path.splitext(name)[0])

        # Not found after all.
        raise




def locate_header(f):
    framework, header = os.path.split(f)
    return os.path.join(framework_header(framework + '.framework'), header)
    
class Dependency(object):
    def __init__(self, header):
        self.header = header

    def infoTuple(self):
        return (self.header,)

    def __repr__(self):
        return '%s%r' % (type(self).__name__, self.infoTuple())



    

class FrameworkScanner(object):
    def __init__(self, additional=None):
        self._scanner = None
        if additional is not None:
            self._additionalHeaders = additional
        else:
            self._additionalHeaders = []

    def scanframework(self, name, sub=None):
        if sub is None:
            sub = name
        start = '%s/%s.h' % (name, sub)
        startfile = locate_header(start)
        startframework = os.path.join(os.path.dirname(locate_framework(name)), '')
        self.seen = seen = []
        scanners = []
        if os.path.exists(startfile):
            seen.append(start)
            scanners.append(self.scanfile(startfile))
            for item in self._additionalHeaders:
                headers = glob.glob(locate_header('%s/%s.h' % (name, item)))
                for header in headers:
                    seen.append(name + '/' + os.path.basename(header))
                    scanners.append(self.scanfile(header))

        else:
            headers = glob.glob(locate_header('%s/*.h' % (name,)))
            for header in headers:
                seen.append(name + '/' + os.path.basename(header))
                scanners.append(self.scanfile(header))
        while scanners:
            try:
                token = scanners[-1].next()
            except StopIteration:
                scanners.pop()

                if not scanners:
                    # We're done with all regular headers, check if we missed
                    # some optional headers:
                    all_headers = glob.glob(locate_header('%s/*.h' % (name,)))
                    for header in all_headers:
                        p = name + '/' + os.path.basename(header)
                        if p not in seen:
                            seen.append(p)
                            scanners.append(self.scanfile(header))

                continue
            if isinstance(token, (AngleImport, StringImport)):
                fn = token['import_file']
                if fn in seen:
                    pass
                else:
                    try:
                        header = locate_header(fn)
                    except ValueError:
                        pass
                    else:
                        seen.append(fn)
                        if header.startswith(startframework):
                            hfn = locate_header(fn)
                            if os.path.exists(hfn):
                                scanners.append(self.scanfile(hfn))
                        else:
                            yield Dependency(fn)
                continue
            yield token
    
    def scanfile(self, fn):
        if self._scanner is None:
            self._scanner = Scanner(LEXICON)
        def deadraise(string, i, j):
            print '-' * len(fn)
            print fn
            print '-' * len(fn)
            s = string[i:].split('\n',1)[0]
            print s
            print
            import pdb
            pdb.Pdb().set_trace()

        if fn.lower().endswith('obsolete.h'):
            return iter(())

        logging.info("scanning %s", fn)
        return self._scanner.iterscan(file(fn).read(), dead=deadraise)

def contains_instances_of(iterator, types):
    for i in iterator:
        if isinstance(i, types):
            return True
    return False


def normalize_typename(value):
    value = value.strip().replace('\t', ' ')
    while '  ' in value:
        value = value.replace('  ', ' ')
    value = value.replace(' *', '*')

    if value.endswith('*'):
        try:
            objc.lookUpClass(value[:-1])
            return 'id'
        except objc.error:
            pass
    return value




class FrameworkMetadata (object):

    def __init__(self, framework, types=None, types64=None, dependencies=None):
        self.link_framework = link_flag_for_framework(framework)
        assert self.link_framework is not None

        if framework not in  ('Foundation', 'AppKit'):
            self.CFLAGS='-pipe -framework %s -framework AppKit -framework Foundation'%(self.link_framework,)
        else:
            self.CFLAGS='-framework %s'%(framework,)

        if sys.byteorder == 'little':
            self.CFLAGS64='-arch x86_64 '
        else:
            self.CFLAGS64='-arch ppc64 '

        self.framework = framework

        if types is None:
            self.types = typedict()
        else:
            self.types = types

        if types64 is None:
            self.types64 = typedict()
        else:
            self.types64 = types

        if dependencies is None:
            self.dependencies = set()
        else:
            self.dependencies = dependencies

        self.globthings = []
        self.enums = []
        self.strvals = []
        self.imports = []
        self.structs = []
        self.plain_structs = {}
        self.opaque_structs = {}
        self.opaque_pointers = []
        self.cftypes = []
        self.functions = []
        self.inline_functions = []
        self.informal_protocols = []
        self.classes = {}
        self.null_const = []
        self.static_inlines = []

        self.special_type_encodings = set()
        self.special_type_encodings.add(objc._C_BOOL)
        self.special_type_encodings.add(objc._C_PTR+objc._C_BOOL)

        if hasattr(objc, '_C_UNICHAR'):
            self.special_type_encodings.add(objc._C_UNICHAR)
            self.special_type_encodings.add(objc._C_PTR+objc._C_UNICHAR)
            self.special_type_encodings.add(objc._C_PTR+objc._C_PTR+objc._C_UNICHAR)
            self.special_type_encodings.add(objc._C_CONST+objc._C_PTR+objc._C_UNICHAR)
        else:
            objc._C_UNICHAR = self.encodedType('unichar')[0]

        if hasattr(objc, '_C_CHAR_AS_TEXT'):
            self.special_type_encodings.add(objc._C_CHAR_AS_TEXT)
            self.special_type_encodings.add(objc._C_PTR+objc._C_CHAR_AS_TEXT)
            self.special_type_encodings.add(objc._C_PTR+objc._C_PTR+objc._C_CHAR_AS_TEXT)
            self.special_type_encodings.add(objc._C_CONST+objc._C_PTR+objc._C_CHAR_AS_TEXT)

        if hasattr(objc, '_C_CHAR_AS_INT'):
            self.special_type_encodings.add(objc._C_CHAR_AS_INT)
            self.special_type_encodings.add(objc._C_PTR+objc._C_CHAR_AS_INT)
            self.special_type_encodings.add(objc._C_PTR+objc._C_PTR+objc._C_CHAR_AS_INT)
            self.special_type_encodings.add(objc._C_CONST+objc._C_PTR+objc._C_CHAR_AS_INT)

        if hasattr(objc, '_C_CPPBOOL'):
            self.special_type_encodings.add(objc._C_CPPBOOL)
            self.special_type_encodings.add(objc._C_PTR+objc._C_CPPBOOL)
            self.special_type_encodings.add(objc._C_PTR+objc._C_PTR+objc._C_CPPBOOL)
            self.special_type_encodings.add(objc._C_CONST+objc._C_PTR+objc._C_CPPBOOL)

        # Due to a bug in the compiler 'unsigned char*' gets @encode-d into
        # the wrong value, try to compensate for that.
        self.special_type_encodings.add(objc._C_PTR+objc._C_UCHR)

        self.cfstringtype = self.encodedType('CFStringRef')[0]
        self.unichartype = self.encodedType('UniChar')[0]

        self.exceptions = None

        # Type information from dependencies:
        self._dep_cftypes = []
        self._dep_opaque = []

        # This is rather jucky, for some reason webkit uses an #ifdef for
        # WebNSInteger and undefines this at the end of include files instead
        # of using typedefs.
        # This is a workaround to ensure that webkit will work with this tool.
        if os.uname()[2] < '9.':
            WebNSInteger='int'
            WebNSUInteger='unsigned int'
        else:
            WebNSInteger='NSInteger'
            WebNSUInteger='NSUInteger'

        self.types['WebNSInteger'], self.types64['WebNSInteger'] = self.encodedType(WebNSInteger)
        self.types['WebNSUInteger'], self.types64['WebNSUInteger'] = self.encodedType(WebNSUInteger)

        self.loadedMetaData = set()

        if framework != 'CoreFoundation':
            # Dependences aren't always explicit
            self.tryLoadMetaData('CoreFoundation')

        if framework == 'CoreVideo':
            # Pseudo framework with OpenGL related definitions
            self.tryLoadMetaData('CGL')
            self.tryLoadMetaData('CoreGraphics')

    def extractTypes(self, framework):
        """
        Extract type definitions from a framework. 

        This function only parses type definitions and updates the type table.
        """
        return

        if not self.types.addHeader(framework):
            return

        logging.info("extract types from: %s", framework)

        return;

        f = FrameworkMetadata(framework, 
                self.types, self.types64, self.dependencies)
        f.scan()

    def encodedType(self, ctype, _framework=None):
        ctype = normalize_typename(ctype)
        if not ctype:
            raise RuntimeError, "No type??"

        if ctype in self.types:
            # XXX: the types64 one isn't fully correct
            return self.types[ctype], self.types64.get(ctype, '')

        _ctype = ctype

        if ctype.startswith('in '):
            prefix = objc._C_IN
            ctype = ctype[3:]

        elif ctype.startswith('inout '):
            prefix = objc._C_INOUT
            ctype = ctype[6:]

        elif ctype.startswith('out '):
            prefix = objc._C_OUT
            ctype = ctype[4:]

        elif ctype.startswith('oneway '):
            prefix = objc._C_ONEWAY
            ctype = ctype[7:]

        else:
            prefix = ''

        data, data2 = self._compileAndRun(
                r'printf("%%s\n", @encode(%s));'%(ctype), additionalFramework=_framework)
        data = data.strip()
        data2 = data2.strip()

        # Strip const label to avoid confusion
        if data.startswith(objc._C_CONST):
            data = data[1:]
        if data2.startswith(objc._C_CONST):
            data2 = data2[1:]

        if data == '*':
            # Due to a bug in the objective-C compiler both 'char*' and 'unsigned char*'
            # get compiled into '*' (the later should be '^C').
            d, d2 = self._compileAndRun(
                    r'%s x; printf("%%s\n", @encode(*x));'%(ctype), additionalFramework=_framework)
            d = d.strip()
            d2 = d2.strip()
            if d.startswith(objc._C_CONST):
                d = d[1:]
            if d2.startswith(objc._C_CONST):
                d2 = d2[1:]
            if d == objc._C_UCHR:
                data = objc._C_PTR + objc._C_UCHR
            if d2 == objc._C_UCHR:
                data2 = objc._C_PTR + objc._C_UCHR

        # Make up a struct tag if a struct definition doesn't have one
        if data and data.startswith('{?'):
            if ' ' not in ctype:
                data = data[0] + ctype + data[2:]

        if data2 and data2.startswith('{?'):
            if ' ' not in ctype:
                data2 = data2[0] + ctype + data2[2:]


        if data:
            self.types[_ctype] = prefix + data
        if data2:
            self.types64[_ctype] = prefix + data2

        if data:
            return (prefix + data, prefix+data2)

        return None, None


    def exceptionNodes(self, cls, exceptions=None):
        if exceptions is None:
            exceptions = self.exceptions

            if exceptions is None:
                return

        for node in exceptions.findall(cls):
            yield node

    def find_exception(self, cls, name, child_tag=None, child_index=None, exceptions=None, nameattr='name', indexattr='index'):

        if exceptions is None:
            if self.exceptions is None:
                return

            exceptions = self.exceptions.getroot()

        for elem in exceptions.findall(cls):
            if elem.get(nameattr, None) == name:
                if child_tag is None:
                    return elem

                else:
                    if child_index is not None:
                        for child in elem:
                            if child.tag != child_tag:
                                continue
                            
                            if child.get(indexattr) == str(child_index):
                                return child
                    else:
                        for child in elem.getchildren():
                            if unicode(child.tag) == unicode(child_tag):
                                return child

        return None

    def haveFunction(self, name):
        for item in self.functions:
            if item[0] == name:
                return True
        return False

    def isStringyType(self, encoded, typestr):
        # Return True if the type is obviously textual.
        # Note that we can only deduce this for unicode characters/strings,
        # although I'm returning True for all char's as well.
        if typestr is None:
            return False

        typestr = normalize_type(typestr)
        if encoded in (
                objc._C_CHR, objc._C_CHARPTR, objc._C_PTR+objc._C_CHR,
                objc._C_PTR+objc._C_CHARPTR, 
                objc._C_PTR+objc._C_PTR+objc._C_CHR,
                ):
            if typestr in ('char', 'char*', 'char**'):
                return True
            return False

        if encoded != self.unichartype:
            return False

#        if typestr in ('unichar', 'UniChar', 'unichar*', 'UniChar*'):
#            return True
#
#        elif typestr in ('unichar**', 'UniChar**'):
#            return True

        return False


    def isCFType(self, encoded):
        # XXX: Need to load data for dependend frameworks as well.
        while encoded and encoded[0] in (
                objc._C_IN, objc._C_OUT, objc._C_INOUT, objc._C_CONST):
            encoded = encoded[1:]

        for nm, tp, tp64 in self.cftypes:
            if tp == encoded:
                return True

        for nm, tp, tp64 in self._dep_cftypes:
            if tp == encoded:
                return True

        return False

    def isOpaquePointerType(self, encoded):
        while encoded and encoded[0] in (
                objc._C_IN, objc._C_OUT, objc._C_INOUT, objc._C_CONST):
            encoded = encoded[1:]

        for name, tp, tp64 in self.opaque_pointers:
            if tp == encoded:
                return True

        for name, tp, tp64 in self._dep_opaque:
            if tp == encoded:
                return True

        return False


    def hasModifier(self, encoded):
        return encoded and encoded[0] in (
            objc._C_IN, objc._C_OUT, objc._C_INOUT) #, objc._C_CONST)

    def isPointerType(self, encoded):
        if encoded is None:
            return False

        # First strip type qualifiers:
        while encoded and encoded[0] in (
                objc._C_IN, objc._C_OUT, objc._C_INOUT, objc._C_CONST):
            encoded = encoded[1:]

        if encoded == objc._C_CHARPTR:
            return True

        if not encoded.startswith(objc._C_PTR):
            return False

        if self.isCFType(encoded) or self.isOpaquePointerType(encoded):
            return False

        return True
    
    def emitDependecyList(self, fp):
        for k in sorted(self.dependencies):
            print >>fp, k

    def emitMetaDataXML(self, fp):
        """
        Write the XML file with metadata information.
        """

        # Note: the code below needs to ensure that data will be written out
        # in a stable order to ensure that it is possible to compare the output
        # of two runs without special tools. I've chosen alphabetical order here.
        root = ET.Element('signatures', version='1.0')

        for dep in self.dependencies:
            path = locate_framework(dep)
            exc = self.find_exception('depends_on',  path, nameattr='path')
            if exc is not None and exc.get('ignore') == 'true':
                continue

            e = ET.SubElement(root, 'depends_on', path=path)
            self.copyExceptionData(e, exc)
            self.pruneComment(e)

        for name, encoding, encoding64 in sorted(self.structs):
            exc = self.find_exception('struct', name)
            if exc is not None and exc.get('ignore') == 'true':
                continue
        
            if exc is None and name.startswith('_'):
                continue

            e = ET.SubElement(root, 'struct', name=name, type=encoding)
            if encoding64:
                e.set('type64', encoding64)

            self.copyExceptionData(e, exc)
            self.pruneComment(e)


        for name, encoding, encoding64 in sorted(self.opaque_pointers):
            exc = self.find_exception('opaque', name)
            if exc is not None and exc.get('ignore') == 'true':
                continue

            if exc is None and name.startswith('_'):
                continue

            e = ET.SubElement(root, 'opaque', name=name, type=encoding)
            if encoding64:
                e.set('type64', encoding64)

            self.copyExceptionData(e, exc)
            self.pruneComment(e)

        for name, encoding, encoding64 in sorted(self.cftypes):
            exc = self.find_exception('cftype', name)
            if exc is not None and exc.get('ignore') == 'true':
                continue

            e = ET.SubElement(root, 'cftype', name=name, type=encoding)
            if encoding64:
                e.set('type64', encoding64)

            self.copyExceptionData(e, exc)
            self.pruneComment(e)

        lastName = None
        for name, type, type64 in sorted(self.globthings):

            if name == lastName:
                # Some frameworks offer multiple definitions for global thinks,
                # AddressBook is a prime example of this. This code avoids
                # duplicate definitions in the metadata.
                continue

            lastName = name

            exc = self.find_exception('constant', name)
            if exc is not None and exc.get('ignore') == 'true':
                continue

            e = ET.SubElement(root, 'constant', name=name, type=type)
            if type64 and type64 != type:
                e.set('type64', type64)

            self.copyExceptionData(e, exc)
            self.pruneComment(e)

        for name, value, value64, valuePPC in sorted(self.enums):
            exc = self.find_exception('enum', name)
            if exc is not None and exc.get('ignore') == 'true':
                continue

            if name.startswith('_'):
                # Ignore private names unless explicitly told otherwise
                if exc is None or exc.get('ignore') != 'false':
                    continue

            e = ET.SubElement(root, 'enum', name=name)

            if value and valuePPC and (value != valuePPC):
                e.set('be_value', valuePPC)
                e.set('le_value', value)

            elif value:
                e.set('value', value)

            if value64 and value64 != value:
                e.set('value64', value64)

            self.copyExceptionData(e, exc)
            self.pruneComment(e)

        for name, tp, value, value64 in sorted(self.strvals):
            exc = self.find_exception('string_constant', name)
            if exc is not None and exc.get('ignore') == 'true':
                continue

            # Maybe stuff the data into the text?
            e = ET.SubElement(root, 'string_constant', name=name)
            if value:
                if isinstance(value, str):
                    e.set('value', value.decode('utf-8'))
                else:
                    e.set('value', value)
            if value64 and value64 != value:
                if isinstance(value64, str):
                    e.set('value64', value64.decode('utf-8'))
                else:
                    e.set('value64', value64)

            if tp == objc._C_ID:
                e.set('nsstring', 'true')

            self.copyExceptionData(e, exc)
            self.pruneComment(e)

        for name in sorted(self.null_const):
            exc = self.find_exception('null_const', name)
            if exc is not None and exc.get('ignore') == 'true':
                continue

            e =  ET.SubElement(root, 'null_const', name=name)
            self.copyExceptionData(e, exc)
            self.pruneComment(e)


        for nm, (retType, retType64, returnMeta), arginfo, variadic in sorted(self.functions):
            exc = self.find_exception('function', nm)
            if exc is not None and exc.get('ignore') == 'true':
                continue

            func = ET.SubElement(root, 'function')

            if variadic:
                func.set('variadic', 'true')

            func.set('name', nm)
            self.copyExceptionData(func, exc)

            retexc = self.find_exception('function', nm, 'retval')

            if retexc is not None or retType != objc._C_VOID or returnMeta:
                e = ET.SubElement(func, 'retval', type=retType)
                if retType64 and retType64 != retType:
                    e.set('type64', retType64)

                for k, v in returnMeta.items():
                    e.set(k, v)

                self.copyExceptionData(e, retexc, copyChildren=True)
                self.pruneComment(e)

            for idx, arg in enumerate(arginfo):
                exc = self.find_exception('function', nm, 'arg', idx)
                e = ET.SubElement(func, 'arg')

                e.set('type', arg['encoded'])
                if arg['encoded64'] and arg['encoded64'] != arg['encoded']:
                    e.set('type64', arg['encoded'])

                if 'numeric' in arg:
                    e.set('numeric', arg['numeric'])

                self.copyExceptionData(e, exc, copyChildren=True)
                self.pruneComment(e)

        for nm, (retType, retType64), arginfo, variadic in sorted(self.inline_functions):
            exc = self.find_exception('function', nm)
            if exc is not None and exc.get('ignore') == 'true':
                continue

            func = ET.SubElement(root, 'function', inline='true')

            if variadic:
                func.set('variadic', 'true')

            func.set('name', nm)

            retexc = self.find_exception('function', nm, 'retval')

            if True: # retexc or (retType != objc._C_VOID):
                e = ET.SubElement(func, 'retval', type=retType)
                if retType64 and retType64 != retType:
                    e.set('type64', retType64)

                self.copyExceptionData(e, retexc, copyChildren=True)
                self.pruneComment(e)

            for idx, arg in enumerate(arginfo):
                exc = self.find_exception('function', nm, 'arg', idx)
                e = ET.SubElement(func, 'arg')

                e.set('type', arg['encoded'])
                if arg['encoded64'] and arg['encoded64'] != arg['encoded']:
                    e.set('type64', arg['encoded'])

                self.copyExceptionData(e, exc, copyChildren=True)
                self.pruneComment(e)

        for nm, methods in sorted(self.informal_protocols):
            protoexc = self.find_exception('informal_protocol', nm)
            if protoexc is not None and protoexc.get('ignore') == 'true':
                continue

            proto = ET.SubElement(root, 'informal_protocol')
            proto.set('name', nm)
            self.copyExceptionData(proto, protoexc)
            self.pruneComment(proto)

            for m in sorted(methods, key=lambda item: item['selector']):
                exc = self.find_exception('method', nm, m['selector'], nameattr='selector', exceptions=protoexc)
                if exc is not None and exc.get('ignore') == 'true': 
                    continue

                e = ET.SubElement(proto, 'method')
                for k, v in sorted(m.items()):
                    if isinstance(v, bool):
                        if v:
                            e.set(k, 'true')
                        else:
                            e.set(k, 'false')
                    else:
                        e.set(k, str(v))
                self.copyExceptionData(e, exc)
                self.pruneComment(e)

        for classname in sorted(self.classes):
            clsexc = self.find_exception('class', classname)
            if clsexc and clsexc.get('ignore') == 'true':
                continue

            cls = ET.SubElement(root, 'class', name=classname)
            self.copyExceptionData(cls, clsexc)
            self.pruneComment(cls)


            for method in sorted(self.classes[classname], key=lambda x: x['selector']):

                methodExc = self.find_exception(
                        'method', method['selector'],
                        exceptions=clsexc, nameattr='selector')

                # The 'ignore' atribute on methods is slight different than
                # on other elements: copy to the metadata file.
                #if methodExc and methodExc.get('ignore') == 'true':
                #    continue

                meth = ET.SubElement(cls, 'method', selector=method['selector'])

                if method['class_method']:
                    meth.set('class_method', 'true')
                if method['variadic']:
                    meth.set('variadic', 'true')
                if method.get('comment'):
                    meth.set('comment', method['comment'])

                self.copyExceptionData(meth, methodExc)
                self.pruneComment(meth)


                if len(method['returns']) == 2:
                    ret, ret64 = method['returns']
                    hints = {}
                else:
                    ret, ret64, hints = method['returns']
                exc = self.find_exception(
                        'retval', None, exceptions = methodExc)

                if self.isPointerType(ret) or (ret64 and self.isPointerType(ret64)) or (ret in self.special_type_encodings):
                    e = ET.SubElement(meth, 'retval', type=ret)
                    if ret64 and ret64 != ret:
                        e.set('type64', ret64)
                    for k, v in hints.items():
                        e.set(k, v)
                    self.copyExceptionData(e, exc, copyChildren=True)
                    self.pruneTypeInfo(e, 'type', ret, ret64)
                    self.pruneComment(e)

                elif exc is not None or hints:
                    e = ET.SubElement(meth, 'retval')
                    for k, v in hints.items():
                        e.set(k, v)
                    self.copyExceptionData(e, exc, copyChildren=True)
                    self.pruneTypeInfo(e, 'type', ret, ret64)
                    self.pruneComment(e)

                for argidx in sorted(method['arguments']):
                    if len(method['arguments'][argidx]) == 2:
                        arg, arg64 = method['arguments'][argidx]
                        meta = None
                    else:
                        arg, arg64, meta = method['arguments'][argidx]

                    exc = self.find_exception(
                            'method', method['selector'],
                            child_tag='arg', child_index=argidx,
                            exceptions=clsexc, nameattr='selector')

                    e = ET.SubElement(meth, 'arg', index=str(argidx), type=arg)
                    if arg64 and arg64 != arg:
                        e.set('type64', arg64)

                    if meta is not None:
                        for k, v in meta.items():
                            e.set(k, v)

                    self.copyExceptionData(e, exc, copyChildren=True)
                    self.pruneTypeInfo(e, 'type', arg, arg64)
                    self.pruneComment(e)

            if clsexc is not None:
                self.copyUnhandledNodes(clsexc, 'method', 
                        self.classes[classname],
                        nameAttr='selector', getName=lambda x:x['selector'])

        print >>fp, HEADER
        indentET(root)
        tree = ElementTree(root)
        tree.write(fp)
        fp.write('\n')

    def copyUnhandledNodes(self, root, cls, items, 
                                getName=lambda node: node[0],
                                nameAttr='name'):
        """
        Copy exception nodes that weren't used yet.
        
        Used to avoid loosing information when updating the metadata on
        an older OS-release.
        """

        for node in self.exceptionNodes(cls):
            nm = node.get(nameAttr)
            for cur in items:
                name = getName(cur)
                if nm == name:
                    break
            else:
                e = ET.SubElement(root, node.tag, name=nm)
                self.copyExceptionData(e, node)
                if node is not None:
                    for child in node:
                        e.append(child)

    def emitExceptionsXML(self, fp):

        root = ET.Element('signatures', version='1.0')

        for dep in self.dependencies:
            path = locate_framework(dep)
            exc = self.find_exception('depends_on',  path, nameattr='path')
            if exc is None:
                continue

            e = ET.SubElement(root, 'depends_on', path=path)
            self.copyExceptionData(e, exc)
            self.pruneComment(e)

        for name, encoded, encoded64 in sorted(self.structs):
            exc = self.find_exception('struct', name)

            if name.startswith('_') and exc is None:
                continue

            e = ET.SubElement(root, 'struct', name=name)
            if exc is not None and exc.get('ignore') == 'true':
                e.set('ignore', 'true')

            self.copyExceptionData(e, exc)

        self.copyUnhandledNodes(root, 'struct', self.structs)

        for name, encoded, encoded64 in sorted(self.opaque_pointers):
            exc = self.find_exception('opaque', name)
            if exc is None and name.startswith('_'):
                continue

            e = ET.SubElement(root, 'opaque', name=name)

            if exc is not None and exc.get('ignore') == 'true':
                e.set('ignore', 'true')

            self.copyExceptionData(e, exc)

        self.copyUnhandledNodes(root, 'opaque', self.opaque_pointers)

        for name, encoded, encoded64 in sorted(self.cftypes):
            e = ET.SubElement(root, 'cftype', name=name)

            exc = self.find_exception('cftype', name)
            if exc is not None and exc.get('ignore') == 'true':
                e.set('ignore', 'true')

            if name.endswith('Ref'):
                fn = name[:-3] + 'GetTypeID'
                if self.haveFunction(fn):
                    e.set('gettypeid_func', fn)

            self.copyExceptionData(e, exc)

        self.copyUnhandledNodes(root, 'cftype', self.cftypes)

        for name, encoded, encoded64 in sorted(self.globthings):
            exc = self.find_exception('constant', name)
            if exc is not None:
                e = ET.SubElement(root, 'constant', name=name)

                if exc.get('ignore') == 'true':
                    e.set('ignore', 'true')

                self.copyExceptionData(e, exc)

        self.copyUnhandledNodes(root, 'constant', self.globthings)

        for item in sorted(self.enums):
            name = item[0]
            exc = self.find_exception('enum', name)
            if exc is not None:
                e = ET.SubElement(root, 'enum', name=name)

                if exc.get('ignore') == 'true':
                    e.set('ignore', 'true')

                self.copyExceptionData(e, exc)

        self.copyUnhandledNodes(root, 'constant', self.enums)

        for name, tp, value, value64 in sorted(self.strvals):
            exc = self.find_exception('string_constant', name)
            if exc is not None:
                e = ET.SubElement(root, 'string_constant', name=name)

                if exc.get('ignore') == 'true':
                    e.set('ignore', 'true')

                self.copyExceptionData(e, exc)

        self.copyUnhandledNodes(root, 'string_constant', self.strvals)

        for name in sorted(self.null_const):
            exc = self.find_exception('null_const', name)
            if exc is not None:
                e =  ET.SubElement(root, 'null_const', name=name)
                self.copyExceptionData(e, exc)
                if exc.get('ignore') == 'true':
                    e.set('ignore', 'true')

        self.copyUnhandledNodes(root, 'null_const', self.null_const)

        for nm, (retType, retType64), arginfo, variadic in sorted(self.inline_functions):
            exc = self.find_exception('function', nm)
            if exc is not None and exc.get('ignore') == 'true':
                e = ET.SubElement(root, 'function', name=nm, ignore='true')
                continue

            func = None

            def makeFunction():
                if func is not None: return func

                f = ET.SubElement(root, 'function', name=nm, inline='true')
                if variadic:
                    f.set('variadic', 'true')

                return f

            if exc:
                func = makeFunction()
                self.copyExceptionData(func, exc)

            retexc = self.find_exception('function', nm, 'retval')

            isCreateOrCopy = False
            if self.isCFType(retType) and ('Create' in nm or 'Copy' in nm):
                isCreateOrCopy = True

            if retexc or self.isPointerType(retType) or isCreateOrCopy:
                func = makeFunction()
                e = ET.SubElement(func, 'retval', type=retType)
                if retType64:
                    e.set('type64', retType64)

                # Some heuristics, to be done before merging the exception
                # data
                if isCreateOrCopy:
                    if self.isCFType(retType):
                        e.set('already_cfretained', 'true')
                    else:
                        e.set('already_retained', 'true')

                    # This sucks, need to refactor...
                    del e.attrib['type']
                    if 'type64' in e.attrib:
                        del e.attrib['type64']

                self.copyExceptionData(e, retexc, copyChildren=True)
                self.pruneTypeInfo(e, 'type', retType, retType64)


            for idx, arg in enumerate(arginfo):
                exc = self.find_exception('function', nm, 'arg', idx)

                if exc or self.isPointerType(arg['encoded']):
                    func = makeFunction()
                    e = ET.SubElement(func, 'arg', index=str(idx))
                    e.set('type', arg['encoded'])
                    if arg.get('encoded64'):
                        e.set('type64', arg['encoded64'])

                    self.copyExceptionData(e, exc, copyChildren=True)
                    self.pruneTypeInfo(e, 'type', arg['encoded'], arg.get('encoded64'))

        for nm, (retType, retType64, retMeta), arginfo, variadic in sorted(self.functions):
            exc = self.find_exception('function', nm)
            if exc is not None and exc.get('ignore') == 'true':
                e = ET.SubElement(root, 'function', name=nm, ignore='true')
                continue

            func = None

            def makeFunction():
                if func is not None: return func

                f = ET.SubElement(root, 'function', name=nm)
                if variadic:
                    f.set('variadic', 'true')

                return f

            if variadic:
                func = makeFunction()

            if exc is not None:
                func = makeFunction()
                self.copyExceptionData(func, exc)

            retexc = self.find_exception('function', nm, 'retval')

            isCreateOrCopy = False
            if self.isCFType(retType) and ('Create' in nm or 'Copy' in nm):
                isCreateOrCopy = True

            if retexc is not None or self.isPointerType(retType) or isCreateOrCopy or retMeta:
                func = makeFunction()
                e = ET.SubElement(func, 'retval', type=retType)
                if retType64:
                    e.set('type64', retType64)

                for k, v in retMeta.items():
                    e.set(k, v)

                # Some heuristics, to be done before merging the exception
                # data
                if isCreateOrCopy:
                    if self.isCFType(retType):
                        e.set('already_cfretained', 'true')
                    else:
                        e.set('already_retained', 'true')

                    # This sucks, need to refactor...
                    del e.attrib['type']
                    if 'type64' in e.attrib:
                        del e.attrib['type64']

                self.copyExceptionData(e, retexc, copyChildren=True)
                self.pruneTypeInfo(e, 'type', retType, retType64)


            for idx, arg in enumerate(arginfo):
                exc = self.find_exception('function', nm, 'arg', idx)

                if exc is not None or self.isPointerType(arg['encoded']) or 'numeric' in arg:
                    func = makeFunction()
                    e = ET.SubElement(func, 'arg', index=str(idx))
                    e.set('type', arg['encoded'])
                    if arg.get('encoded64'):
                        e.set('type64', arg['encoded64'])

                    if 'numeric' in arg:
                        e.set('numeric', arg['numeric'])

                    self.copyExceptionData(e, exc, copyChildren=True)
                    self.pruneTypeInfo(e, 'type', arg['encoded'], arg.get('encoded64'))

        self.copyUnhandledNodes(root, 'function', self.functions + self.inline_functions)

        for nm, methods in sorted(self.informal_protocols):
            protoexc = self.find_exception('informal_protocol', nm)
            if protoexc is not None and protoexc.get('ignore') == 'true':
                e = ET.SubElement(root, 'informal_protocol', name=nm, ignore='true')
                continue

            if protoexc is None:
                continue

            # Need to check what exceptions there can be for informal 
            # protocols.
           
            proto = None
            def makeProto():
                if proto is not None:
                    return proto

                result =  ET.SubElement(root, 'informal_protocol', name, nm)
                self.copyExceptionData(result, protoexc)
                return result

            for m in sorted(methods, key=lambda item: item['selector']):
                exc = self.find_exception('method', nm, m['selector'], nameattr='selector', exceptions=protoexc)
                if exc is not None:
                    proto = makeProto()
                    e = ET.SubElement(proto, 'method')
                    self.copyExceptionData(e, exc)

        # FIXME: copy unhandled informal protocol metadata

        for classname in sorted(self.classes):
            clsexc = self.find_exception('class', classname)

            cls = None
            def getClass():
                if cls:
                    return cls
                r  = ET.SubElement(root, 'class', name=classname)
                self.copyExceptionData(r, clsexc)
                return r

            if clsexc and clsexc.get('ignore') == 'true':
                cls = getClass()
                continue

            for method in sorted(self.classes[classname], key=lambda x: x['selector']):

                methodExc = self.find_exception(
                        'method', method['selector'],
                        exceptions=clsexc, nameattr='selector')

                meth = None

                def getMethod():
                    if meth is not None:
                        return cls, meth
                    c = getClass()
                    m = ET.SubElement(c, 'method', selector=method['selector'])
                    self.copyExceptionData(m, methodExc)
                    return c, m


                if methodExc:
                    cls, meth = getMethod()
                    if methodExc.get('ignore') == 'true':
                        continue

                if len(method['returns']) == 2:
                    ret, ret64 = method['returns']
                    hints = {}
                else:
                    ret, ret64, hints = method['returns']

                exc = self.find_exception(
                        'retval', None, exceptions = methodExc)

                if self.isPointerType(ret) or (ret64 and self.isPointerType(ret64)) or ret == objc._C_SEL: 
                    # Ignore special_encodings for the exceptions file:
                    # or ret in self.special_type_encodings:
                    if meth is None:
                        cls, meth = getMethod()
                    e = ET.SubElement(meth, 'retval', type=ret)
                    if ret64 and ret64 != ret:
                        e.set('type64', ret64)
                    for k, v in hints.items():
                        e.set(k, v)
                    self.copyExceptionData(e, exc, copyChildren=True)
                    self.pruneTypeInfo(e, 'type', ret, ret64)

                elif exc is not None or hints:
                    cls, meth = getMethod()
                    e = ET.SubElement(meth, 'retval')
                    for k, v in hints.items():
                        e.set(k, v)
                    self.copyExceptionData(e, exc, copyChildren=True)
                    self.pruneTypeInfo(e, 'type', ret, ret64)

                for argidx in sorted(method['arguments']):
                    if len(method['arguments'][argidx]) == 2:
                        arg, arg64 = method['arguments'][argidx]
                        meta = None
                    else:
                        arg, arg64, meta = method['arguments'][argidx]


                    exc = self.find_exception(
                            'method', method['selector'],
                            child_tag='arg', child_index=argidx,
                            exceptions=clsexc, nameattr='selector')

                    if arg in self.special_type_encodings:
                        # Don't add these to the exceptions file unless there
                        # is other metadata.
                        if exc is not None:
                            cls, meth = getMethod()
                            e = ET.SubElement(meth, 
                                    'arg', index=str(argidx))

                            # First set heuristic  metadata
                            if meta is not None:
                                for k, v in meta.items():
                                    e.set(k, v)
                            
                            # Then the values from the metadat file
                            self.copyExceptionData(e, exc, copyChildren=True)
                            self.pruneTypeInfo(e, 'type', arg, arg64)
                        continue

                    cls, meth = getMethod()
                    e = ET.SubElement(meth, 'arg', index=str(argidx), type=arg)
                    if arg64 and arg64 != arg:
                        e.set('type64', arg64)
                    if meta is not None:
                        for k, v in meta.items():
                            e.set(k, v)

                    self.copyExceptionData(e, exc, copyChildren=True)
                    self.pruneTypeInfo(e, 'type', arg, arg64)

                if meth and method['class_method']:
                        meth.set('class_method', 'true')

                if method['variadic']:
                    cls, meth = getMethod()
                    meth.set('variadic', 'true')

                if method.get('comment'):
                    cls, meth = getMethod()
                    meth.set('comment', method['comment'])

            if clsexc is not None:
                self.copyUnhandledNodes(clsexc, 'method', 
                        self.classes[classname],
                        nameAttr='selector', getName=lambda x:x['selector'])

        self.copyUnhandledNodes(root, 'class', self.classes)

        print >>fp, HEADER
        indentET(root)
        tree = ElementTree(root)
        tree.write(fp)

    def stripStructFieldNames(self, encoding):
        return gStructFieldNameRe.sub('', encoding)

    def loadExceptionsXML(self, fname):
        self.exceptions = ET.parse(fname)

        # On Leopard Apple has started removing struct tags from some typedef-ed
        # definitions. This means the @encode-d value no longer uniquely 
        # identifies said type. 
        # The workaround for this is to add our own, made-up, encoding to the
        # exception file and use that instead of the real one. Because we use
        # a made-up encoding we must also create metadata nodes for all methods
        # that have such types as a return or argument value.
        for node in self.exceptions.getroot().findall('struct'):
            if node.get('type'):
                # Ensure that this type gets used throughout: add the type
                # to the encodings dict and to special_type_encodings
                self.special_type_encodings.add(node.get('type'))

                nm = node.get('name')
                tp = self.stripStructFieldNames(node.get('type'))
                tp64 = self.stripStructFieldNames(node.get('type64'))

                self.types[nm] = tp
                self.types[nm + '*'] = objc._C_PTR + tp
                self.types64[nm] = tp64
                self.types64[nm + '*'] = objc._C_PTR + tp64

    def pruneComment(self, node):
        if 'comment' in node.attrib:
            del node.attrib['comment']

        for nm in gBooleanAttributesDefaultingFalse:
            if node.attrib.get(nm) == 'false':
                del node.attrib[nm]

        for nm in gBooleanAttributesDefaultingTrue:
            if node.attrib.get(nm) == 'true':
                del node.attrib[nm]

        # XXX: needed for migration:
        if 'already_retained' in node.attrib and 'already_cfretained' in node.attrib:
            del node.attrib['already_retained']

    def pruneTypeInfo(self, node, typeAttr, type, type64):
        """
        Remove the type attributes from an exception node when they aren't
        actually necessary, this keeps the metadata clean.
        """

        attrs = node.attrib

        for nm in gBooleanAttributesDefaultingFalse:
            if attrs.get(nm) == 'false':
                del node.attrib[nm]

        if typeAttr not in node.attrib and typeAttr + '64' not in node.attrib:
            return

        if typeAttr in attrs and attrs[typeAttr] is None:
            del node.attrib[typeAttr]

        if typeAttr + '64' in attrs and attrs[typeAttr + '64'] is None:
            del node.attrib[typeAttr]

        if attrs.get(typeAttr) != type:
            return

        elif self.isCFType(type) or self.isOpaquePointerType(type):
            # No need to the type info when it's already handled.
            pass

        elif type in self.special_type_encodings:
            # Type info cannot be stripped
            return

        elif typeAttr + '64' in attrs:
            if attrs[typeAttr + '64'] != type64:
                return

        for attr in gTypeModifierAttributes:
            if attr in attrs:
                break
        else:
            # We don't have real metadata, keep the types to make the work
            # of the metadata-maintainer easier.

            if typeAttr not in node.attrib or not self.hasModifier(node.attrib[typeAttr]):
                return

        # There doesn't seem to be a public API for this??
        if typeAttr in attrs:
            del node.attrib[typeAttr]
        if typeAttr + '64' in attrs:
            del node.attrib[typeAttr + '64']


    def copyExceptionData(self, node, exceptionNode, copyChildren=False):
        """
        Copy exception data for this node
        """
        if exceptionNode is None:
            return

        for attrname in gExceptionAttributes.get(None, ()):
            value = exceptionNode.get(attrname)
            if value:
                node.set(attrname, value)

        for attrname in gExceptionAttributes.get(node.tag, ()):
            value = exceptionNode.get(attrname)
            if value:
                node.set(attrname, value)

            if value and (attrname == 'type' or attrname == 'type64'):
                if value.startswith('@encode'):
                    value, value64 = self.encodedType(value[7:-1])
                    if attrname.endswith('64'):
                        node.set(attrname, value64)
                    else:
                        node.set(attrname, value)

        if copyChildren:
            for child in exceptionNode.getchildren():
                attrib = dict(child.attrib)
                if 'comment' in attrib:
                    del attrib['comment']

                ET.SubElement(node, child.tag, **attrib)


    def _initTypes(self):

        # The type 'BOOL' is an alias for one of the small integer types,
        # expecitly covert to objc._C_BOOL to allow us to emit this into
        # the metadata
        for tp in ('BOOL', 'Boolean', 'CGPDFBoolean' ):
            self.types[tp] = objc._C_BOOL
            self.types64[tp] = objc._C_BOOL
            self.types[tp+'*'] = objc._C_PTR + objc._C_BOOL
            self.types64[tp+'*'] = objc._C_PTR + objc._C_BOOL
            self.types[tp+' *'] = objc._C_PTR + objc._C_BOOL
            self.types64[tp+' *'] = objc._C_PTR + objc._C_BOOL


        if hasattr(objc, '_C_CPPBOOL'):
            self.types['bool'] = objc._C_CPPBOOL
            self.types['bool*'] = objc._C_PTR + objc._C_CPPBOOL
            self.types['bool *'] = objc._C_PTR + objc._C_CPPBOOL

        for tp in ('unichar', 'UniChar'):
            for col in (self.types, self.types64):
                col[tp] = objc._C_UNICHAR
                col[tp+'*'] = objc._C_PTR + objc._C_UNICHAR
                col[tp+' *'] = objc._C_PTR + objc._C_UNICHAR
                col[tp+'**'] = objc._C_PTR + objc._C_PTR + objc._C_UNICHAR
                col[tp+' **'] = objc._C_PTR + objc._C_PTR + objc._C_UNICHAR
                col[tp+'* *'] = objc._C_PTR + objc._C_PTR + objc._C_UNICHAR
                col[tp+' * *'] = objc._C_PTR + objc._C_PTR + objc._C_UNICHAR

                col['const ' + tp] = objc._C_CONST + objc._C_UNICHAR
                col['const ' + tp + '*' ] = objc._C_CONST + objc._C_PTR + objc._C_UNICHAR
                col['const ' + tp + ' *' ] = objc._C_CONST + objc._C_PTR + objc._C_UNICHAR

        if hasattr(objc, '_C_CHAR_AS_INT'):
            for tp in ('int8_t',):
                for col in self.types, self.types64:
                    col[tp] = objc._C_CHAR_AS_INT
                    col[tp + '*'] = objc._C_PTR + objc._C_CHAR_AS_INT
                    col[tp + ' *'] = objc._C_PTR + objc._C_CHAR_AS_INT
                    col[tp + '**'] = objc._C_PTR + objc._C_PTR + objc._C_CHAR_AS_INT
                    col[tp + '* *'] = objc._C_PTR + objc._C_PTR + objc._C_CHAR_AS_INT
                    col[tp + ' **'] = objc._C_PTR + objc._C_PTR + objc._C_CHAR_AS_INT
                    col[tp + ' * *'] = objc._C_PTR + objc._C_PTR + objc._C_CHAR_AS_INT
                    col['const ' + tp] = objc._C_CONST + objc._C_CHAR_AS_INT
                    col['const ' + tp + '*'] = objc._C_CONST + objc._C_PTR + objc._C_CHAR_AS_INT
                    col['const ' + tp + ' *'] = objc._C_CONST + objc._C_PTR + objc._C_CHAR_AS_INT


        # CFTypeRef is a typedef for 'void*', which isn't exactly useful for
        # the metadata files.
        self.types['CFTypeRef'] = objc._C_ID
        self.types64['CFTypeRef'] = objc._C_ID
        self.types['CFTypeRef*'] = objc._C_PTR + objc._C_ID
        self.types64['CFTypeRef*'] = objc._C_PTR + objc._C_ID

    def scanClasses(self):
        """
        Load the framework and look for difficult methods in said framework.

        This is crude as hell, but helps in 
        """
        def haveMeta(cls, sel):
            for info in self.classes.get(cls.__name__, ()):
                if info['selector'] == sel:
                    return True

            return False

        framework_name = filter(None, os.path.split(self.framework))[0]
        framework_path = unicode(
                os.path.dirname(locate_framework(framework_name)), 
                sys.getfilesystemencoding())

        NSBundle = objc.lookUpClass('NSBundle')
        bundle = NSBundle.bundleWithPath_(framework_path)
        bundle.load()
        for cls in objc.getClassList():
            if NSBundle.bundleForClass_(cls) is not bundle:
                continue

            for methName in dir(cls):
                try:
                    meth = getattr(cls, methName)
                except AttributeError:
                    continue

                if not isinstance(meth, objc.selector):
                    continue

                selector = meth.selector

                if haveMeta(cls, selector):
                    continue

                meta = {}

                parts = objc.splitSignature(meth.native_signature)
                changed_parts = objc.splitSignature(meth.signature)
                if parts[0].startswith('^'):
                    # This is not quite true, but not really a problem either...
                    meta['returns'] = (parts[0], parts[0])
                    meta['arguments'] = {}
                    if changed_parts[0] != parts[0]:
                        if changed_parts[0].endswith(parts[0]):
                            meta['returns'] = meta['returns'] + ({
                                    'type_modifier': changed_parts[0][:len(changed_parts[0])-len(parts[0])],
                            },)
                        else:
                            meta['returns'] = changed_parts[0], changed_parts[0]

                for idx, (p, cp) in enumerate(zip(parts[1:], changed_parts[1:])):
                    if p.startswith('^'):
                        meta.setdefault('arguments', {})[idx] = (p, p, {})
                        if p != cp:
                            if cp.endswith(p):
                                meta['arguments'][idx] = (p, p, {
                                    'type_modifier': cp[:len(cp)-len(p)]
                                })
                            else:
                                meta['arguments'][idx] = (cp, cp, {})




                if meta:
                    meta['selector'] = selector
                    meta['class_method'] = meth.isClassMethod
                    meta['variadic'] = False
                    meta['comment'] = "framework scan"

                    self.classes.setdefault(cls.__name__, []).append(meta)

    def scan(self):
        """
        Scan framework headers.
        """

        framework_name = filter(None, os.path.split(self.framework))[0]
        framework_path = unicode(
                os.path.dirname(locate_framework(framework_name)), 
                sys.getfilesystemencoding())

    
        scanner = self.scanner = FrameworkScanner()

        if self.types is None:
            self.types = typedict()
        self._initTypes()

        self.ignores = set([
            CompilerDirective,
            BlockComment,
            SingleLineComment,
            CPPDecls,
            StaticInlineFunctionPrototype,
            SC_SCHEMA_DECLARATION,

            # Stuff below here might be interesting
            UninterestingStruct,
            MacroDefine,
            AttributeCrap,
        ])

        self.processTokens(scanner.scanframework(self.framework))


    def _processGlobalThing(self, token):
        name = token['name'].strip()

        if ',' in name:
            names = name.split(',')
            name = names[0]
            names = names[1:]
        else:
            names = []
            
        if name[0] == '_': 
            # Skip private variables
            return

        tp, tp64 = self.encodedType(token['type'])
        if not tp:
            return

        while tp and tp[0] == objc._C_CONST:
            tp = tp[1:]

        while tp64 and tp64[0] == objc._C_CONST:
            tp64 = tp64[1:]

        self.globthings.append((unicode(name), tp, tp64))


        # C's type rules are quaint(sp?), strip indirection
        # from the type we have now.
        type = token['type'].strip()
        while type.endswith('*'):
            type = type[:-1]

        for nm in names:
            nm = nm.strip()
            indirection = ''
            while nm[0] == '*':
                indirection += '*'
                nm = nm[1:].strip()

            tp, tp64 = self.encodedType(type + indirection)
            self.globthings.append((unicode(nm), tp, tp64))




    def _processNamedEnum(self, token):
        nm = token.matches()[-1]['name'].strip()

        self._processEnum(token)


    def _processEnum(self, enum):
        i = -1
        for token in enum.matches():
            if isinstance(token, (EnumValueMember, EnumBareMember)):
                    name = token['name']

                    # Need to compile 3-way (intel-32, ppc-32, and something-64-bit) to
                    # get all possible variations of values. Compiling multiple times is
                    # expensive, therefore avoid cross-architecture compiling when the
                    # value is obviously a plain integer or has an implicit value.
                    if isinstance(token, EnumValueMember) and not simpleValue(token['value']):
                        data, data64, dataPPC = self._compileAndRun(
                            ENUM_MAIN % locals(), ENUM_DEFINITIONS, 

                            # I have no idea why, but at least some system
                            # headers contain '#if 0'-ed out code...
                            allowFailure=True, 
                            ppcAndIntel=True)
                    else:
                        data, data64 = self._compileAndRun(
                            ENUM_MAIN % locals(), ENUM_DEFINITIONS, 

                            # I have no idea why, but at least some system
                            # headers contain '#if 0'-ed out code...
                            allowFailure=True, 
                            ppcAndIntel=False)
                        dataPPC = ''

                    if data:
                        tp, value = data.split('\n', 1)
                        value = value
                    else:
                        tp = None
                        value = ''

                    if data64 and '\n' in data64:
                        tp64, value64 = data64.split('\n', 1)
                        value64 = value64
                    else:
                        tp64 = None
                        value64 = ''

                    if tp is None:
                        tp = tp64

                    if tp is None:
                        continue

                    if dataPPC:
                        try:
                            tpPPC, valuePPC = dataPPC.split('\n', 1)
                        except ValueError:
                            print "tpPPC", `dataPPC`
                            tpPPC = valuePPC = None

                        if tp is None:
                            tp = tpPPC
                    else:
                        tpPPC = None
                        valuePPC = None
                
                    if name.endswith('FunctionKey'):
                        # Special casing for for keycode definitions in AppKit
                        if value is not None:
                            value = unichr(int(value))
                        if value64 is not None:
                            value64 = unichr(int(value64))

                        self.strvals.append((name, objc._C_ID, value, value64))
                    elif tp in [ objc._C_ID, objc._C_CHARPTR ]:
                        self.strvals.append((name, tp, value, value64))
                    else:
                        self.enums.append((name, value, value64, valuePPC))
                        
            elif isinstance(token, (EnumEnd, NamedEnumEnd)):
                pass

            elif type(token) in self.ignores:
                pass

            else:
                raise RuntimeError, "Unhandled token in Enum definition: %r"%(
                        token,)

    def _processFunctionCallDefine(self, token):
        if token['name'].startswith('_'): return

        name = token['name']
        body = token['body'].strip()
        if not body.startswith('CFSTR("'):
            return

        name = token['name'].strip()
        data, data64, dataPPC = self._compileAndRun(
                ENUM_MAIN % locals(), ENUM_DEFINITIONS, allowFailure=1, ppcAndIntel=1)

        if data:
            if '\n' in data:
                tp, value = data.split('\n', 1)

            else:
                logging.warning("ignore hard define %s", name)
                return

        else:
            tp = None
            value=None

        if data64:
            tp64, value64 = data64.split('\n', 1)
            value64 = value64

            if tp is None:
                tp = tp64
        else:
            tp64 = None
            value64 = None

        if dataPPC:
            tpPPC, valuePPC = dataPPC.split('\n', 1)

            if tp is None:
                tp = tpPPC
        else:
            tpPPC = None
            valuePPC = None


        if tp in [ objc._C_FLT, objc._C_DBL]:

            # Printf's '%g' might print a value that's not clearly recognizable
            # as float. Compensate for that.
            for c in value:
                if not c.isdigit():
                    break
            else:
                value = value + '.0'

            for c in value64:
                if not c.isdigit():
                    break
            else:
                value64 = value64 + '.0'

            for c in valuePPC:
                if not c.isdigit():
                    break
            else:
                valuePPC = valuePPC + '.0'

        if not value and not value64 and not valuePPC:
            logging.info("No value for enum label %s", name)
            return
            return

        if tp in [ objc._C_ID, objc._C_CHARPTR, self.cfstringtype, objc._C_CONST + self.cfstringtype ]:
            if tp == objc._C_CHARPTR:
                self.strvals.append((name, objc._C_CHARPTR, value, value64))
            else:
                self.strvals.append((name, objc._C_ID, value, value64))

        else:
            self.enums.append((name, value, value64, valuePPC))

    

        
    def _processSimpleDefine(self, token):
        # XXX: Hardcoded list, move to exceptions file?
        logging.debug("Simple define %s", token['name'])
        if token['name'].startswith('_'): return
        if token['name'] in ('NULL',): return
        if token['value'].strip().startswith('AVAILABLE_MAC_OS_X_VERSION_'): return
        if token['value'].strip().startswith('DEPRECATED_'): return
        if token['value'] in ('SHRT_MAX',): return

        if token['value'] == 'nil':
            self.null_const.append(token['name'])
            return

        # Note: we pick up some definitions in #ifdef-out parts of the code
        # (such as 64-bit only definition on a 32-bit build, therefore allow
        # compilation to fail).
        name = token['name'].strip()
        if name == 'kCGNotifyEventTapRemoved':
            allowFailure=False
        else:
            allowFailure=True
        data, data64, dataPPC = self._compileAndRun(
                ENUM_MAIN % locals(), ENUM_DEFINITIONS, allowFailure=allowFailure, ppcAndIntel=1)

        if data:
            if '\n' in data:
                tp, value = data.split('\n', 1)

            else:
                tp = data
                if tp == objc._C_PTR + objc._C_VOID and token['value'] == 'NULL':
                    self.null_const.append(name)

                else:
                    logging.warning("ignore hard define %s", name)

                return

        else:
            tp = None
            value=None

        if data64:
            tp64, value64 = data64.split('\n', 1)
            value64 = value64

            if tp is None:
                tp = tp64
        else:
            tp64 = None
            value64 = None

        if dataPPC:
            if '\n' in dataPPC:
                tpPPC, valuePPC = dataPPC.split('\n', 1)
            else:
                logging.info("Corrupt output on PPC for %s for %s", name, dataPPC)
                tpPPC, valuePPC = dataPPC, ''
            if tp is None:
                tp = tpPPC
        else:
            tpPPC = None
            valuePPC = None

        if not value and not value64 and not valuePPC:
            logging.warning("No value for #define %s %r %r %r", name, value, value64, valuePPC)
            logging.warning("data: %r %r %r", data, data64, dataPPC)
            return

        if tp in [ objc._C_FLT, objc._C_DBL]:

            # Printf's '%g' might print a value that's not clearly recognizable
            # as float. Compensate for that.
            for c in value:
                if not c.isdigit():
                    break
            else:
                value = value + '.0'

            if value64:
                for c in value64:
                    if not c.isdigit():
                        break
                else:
                    value64 = value64 + '.0'

            if valuePPC:
                for c in valuePPC:
                    if not c.isdigit():
                        break
                else:
                    valuePPC = valuePPC + '.0'

        if not value and not value64 and not valuePPC:
            logging.info("No value for #define %s", name)
            return
    
        if tp in [ objc._C_ID, objc._C_CHARPTR, self.cfstringtype, objc._C_CONST + self.cfstringtype ]:
            if tp == objc._C_CHARPTR:
                self.strvals.append((name, objc._C_CHARPTR, value, value64))
            else:
                self.strvals.append((name, objc._C_ID, value, value64))

        else:
            self.enums.append((name, value, value64, valuePPC))

    def _processDependencies(self, token):
        dep = os.path.dirname(token.infoTuple()[0])
        if dep and dep not in self.dependencies:
            self.dependencies.add(dep)
            self.extractTypes(dep)
            self.imports.append(dep)
            self.tryLoadMetaData(dep)

    def tryLoadMetaData(self, framework):
        """
        Try to load metadata for a framework we're depending on, this is
        needed to correctly recognize opaque pointers and CF-types that are
        defined in that framework.
        """
        if framework in self.loadedMetaData:
            return

        self.loadedMetaData.add(framework)
        logging.info('Try loading metadata for %s', framework)


        # NOTE: This will require some changes once the system's metadata is
        # useful.

        # Need to find bug that causes this to fail...
        #return

        try:
            xml = pkg_resources.resource_string(framework, 'PyObjC.bridgesupport') 
        except:
            
            # XXX: to be removed
            pth = os.path.join(
                        '..', 
                        'pyobjc-framework-%s'%(framework,),
                        'Lib',
                        framework,
                        'PyObjC.bridgesupport')
            if not os.path.exists(pth):
                if framework == 'CoreServices' and self.framework != 'CoreFoundation':
                    # CoreServices is an umbrella framework and the interesting
                    # info is in CoreFoundation
                    self.tryLoadMetaData('CoreFoundation')
                    for fn in os.listdir('/System/Library/Frameworks/CoreServices.framework/Frameworks'):
                        self.tryLoadMetaData(fn.split('.')[0])
                    return

                elif framework == 'Cocoa':
                    # Cocoa is a convenience framework that just links to these
                    # two:
                    self.tryLoadMetaData('Foundation')
                    self.tryLoadMetaData('AppKit')
                    return

                elif framework == 'ApplicationServices':
                    self.tryLoadMetaData('CoreFoundation')
                    for fn in os.listdir('/System/Library/Frameworks/ApplicationServices.framework/Frameworks'):
                        self.tryLoadMetaData(fn.split('.')[0])
                        return

                elif framework == 'Quartz':
                    self.tryLoadMetaData('CoreFoundation')
                    for fn in os.listdir('/System/Library/Frameworks/Quartz.framework/Frameworks'):
                        self.tryLoadMetaData(fn.split('.')[0])
                        return


                else:
                    for meta in ('Cocoa', 'Quartz'):
                        pth = os.path.join(
                            '..', 
                            'pyobjc-framework-%s'%(meta,),
                            'Lib',
                            framework,
                            'PyObjC.bridgesupport')
                        if os.path.exists(pth):
                            break

                    else:
                        logging.info('Failed loading metadata for %s', framework)
                        return

            xml = open(pth, 'rb').read()

        logging.debug("Loading metadata for %s", framework)

        meta = ET.parse(StringIO.StringIO(xml)).getroot()
        for node in meta.findall('cftype'):
            self._dep_cftypes.append(
                    (node.get('name'), node.get('type'), node.get('type64')))

        for node in meta.findall('opaque'):
            self._dep_opaque.append(
                    (node.get('name'), node.get('type'), node.get('type64')))

        # Deal with structs that have a custom encoding:
        for node in meta.findall('struct'):
            nm = node.get('name')
            tp = self.stripStructFieldNames(node.get('type', ''))
            tp64 = self.stripStructFieldNames(node.get('type64', ''))

            try:
                realTp, _ = self.encodedType(nm, framework)
            except:
                logging.debug("Cannot get encoded struct %s", nm) 
                continue

            if realTp != tp:
                self.special_type_encodings.add(tp)
                self.types[nm] = tp
                self.types[nm + '*'] = objc._C_PTR + tp
                self.types64[nm] = tp64
                self.types64[nm + '*'] = objc._C_PTR + tp64

        for node in meta.findall('depends_on'):
            path = node.get('path')
            if path is None: continue
            if not os.path.exists(path): continue

            # Some day this code will use the framework paths instead of 
            # plain framework names...
            frameworkName = os.path.split(path)[1]
            frameworkName = os.path.splitext(frameworkName)[0]
            self.tryLoadMetaData(frameworkName)

        logging.info('Done loading metadata for %s', framework)

    def _processStruct(self, token):
        tag = token['structname']
        self.plain_structs[tag] = token

        if tag in self.opaque_structs:
            # Whoops, it is a struct definition after all.
            name = self.opaque_structs[tag]
            if name.endswith('*'):
                name = name[:-1]
            self._processNamedStruct(token, name)
            opaques = []

            name = self.opaque_structs[tag]
            for entry in self.opaque_pointers:
                if entry[0] == name:
                    continue
                opaques.append(entry)
            self.opaque_pointers = opaques

            cfs = []
            for entry in self.cftypes:
                if entry[0] == name:
                    continue
                cfs.append(entry)
            self.cftypes = cfs


    def _processNamedStruct(self, token, name=None):
        # Skip structs containing function pointers, those cannot be
        # wrapped automaticly (yet?)
        if isinstance(token, Struct):
            externalname = name

        elif isinstance(token, NamedStruct):
            if contains_instances_of(token.matches(), FunctionStructMember): return

            externalname = token.matches()[-1]['name']
        else:
            externalname = token['name']

        ivarType = externalname
        data, data64 = self._compileAndRun(
                    IVAR_TYPE_MAIN, IVAR_TYPE_DEFINITIONS % locals(), 
                    allowFailure=True)

        # Found a struct without a struct tag. That's rather useless because
        # two different types may have the same structure (excluding field *names*)
        # Therefore make up a struct tag.
        if data and data[1] == '?':
            data = data[0] + '_' + externalname + data[2:]

        if data64 and data64[1] == '?':
            data64 = data64[0] + '_' + externalname + data64[2:]

        self.structs.append((externalname, data, data64))
        logging.debug("Struct definition for %s", externalname)


    def _processOpaqueNamedStruct(self, token):
        name = token['name']
        tag = token['label']
        const = token['const']
        indirect = normalize_type(token['indirection'])

        if not indirect and tag in self.plain_structs:
            self._processNamedStruct(token)
            return

        logging.debug("Process opaque struct: %(name)s"% token)

        if indirect:
            ivarType = name
            name = name 
        else:
            ivarType = name + '*'
            name = name + '*'

        data, data64 = self._compileAndRun(
                IVAR_TYPE_MAIN, IVAR_TYPE_DEFINITIONS % locals() )

        self.types[ivarType] = data

        exc = self.find_exception('cftype', ivarType)
        if exc is not None:
            self.cftypes.append((name, data, data64))
            return

        exc = self.find_exception('opaqaue', ivarType)
        if exc is not None:
            self.opaque_pointers.append((name, data, data64))
            return

        # Do a guestimate...
        if name.endswith('Ref') and tag.startswith('__'):
            # This is probably a CF-basd type
            self.cftypes.append((name, data, data64))

        else:
            self.opaque_pointers.append((name, data, data64))

        self.opaque_structs[tag] = name


    def _processUninterestingTypedef(self, token):
        # XXX: drop?
        if ',' in token['body']: return
        ptr = 0
        body = token['body'].split()

        alias = normalize_type(' '.join(body[:-1]))
        target = body[-1]

        if target in self.types:
            return


        if alias == 'CFTypeRef':
            self.cftypes.append((target, '@', '@'))

            # Also override the encoded type, for easier wrapping
            self.types[target] = '@'
            self.types64[target] = '@'
            return
       
        while alias[-1] == '*':
            alias = alias[:-1]
            ptr += 1
        while target[0] == '*':
            target = target[1:]
            ptr += 1
        if alias in self.types:
            if ptr == 1:
                prefix = objc._C_PTR
            elif ptr > 1:
                prefix = objc._C_PTR*ptr
            else:
                prefix = ''
            self.types[target] = prefix + self.types[alias]

        else:
            logging.info("Ignore simple typedef: %s -> %s", target, alias)


    def _processProtocol(self, token):
        # XXX: maybe collect these as informal protocols
        logging.info("Protocol: %s", token['name'])

        # Process nested definitions
        self.processTokens([ 
            t for t in token.matches()
                if type(t) not in (ProtocolEnd, SimpleMethodDef, SegmentedMethodDef)])

        clsexc = self.find_exception('class', 'NSObject')

        # Look for exceptions
        # XXX: refactor this loop, its the same as in _processInterface
        methods = []
        for t in token.matches():
            if isinstance(t, SimpleMethodDef):
                if t['kind'] == '-':
                    class_method=False
                else:
                    class_method=True

                returnType, returnType64 = self.encodedType(t['returntype'] or 'id')
                if self.isPointerType(returnType) or returnType in self.special_type_encodings:
                    methods.append(
                        dict(
                            selector=t['name'],
                            class_method=class_method,
                            returns=(returnType, returnType64),
                            arguments={},
                            variadic=False,
                        )
                )

            elif isinstance(t, SegmentedMethodDef):
                if t['kind'] == '-':
                    class_method=False
                else:
                    class_method=True

                isVariadic = False
               
                returnType, returnType64 = self.encodedType(t['returntype'] or 'id')
                haveSpecial = self.isPointerType(returnType) or returnType in self.special_type_encodings
                arguments = {}
                segs = []

                for idx, s in enumerate(t.matches()):
                    if isinstance(s, FunctionElipsisParameter):
                        isVariadic = True

                    if isinstance(s, MethodSegment):
                        segs.append(s['name'])
                        argType, argType64 = self.encodedType(s['type'] or 'id')
                        if argType is None:
                            # Compiler problems...
                            pass
                        elif self.isPointerType(argType) and normalize_type(s['type']) == 'NSError**':
                            # An NSError** argument, probably an output 
                            # argument
                            arguments[idx] = (argType, argType64, {
                                'type_modifier': 'o',
                                'null_accepted': 'true',
                            })
                            haveSpecial = True

                        elif self.isPointerType(argType) and normalize_type(s['type']) == 'CFErrorRef*':
                            # An NSError** argument, probably an output 
                            # argument
                            arguments[idx] = (argType, argType64, {
                                'type_modifier': 'o',
                                'null_accepted': 'true',
                            })
                            haveSpecial = True
                        elif (self.isPointerType(argType) and not self.hasModifier(argType)) or argType in self.special_type_encodings:
                            haveSpecial = True
                            arguments[idx] = (argType, argType64, None)


                selector = ''.join(segs)


                for i in range(len(segs)+1):
                    exc = self.find_exception(
                        'method', selector,
                        child_tag='arg', child_index=i,
                        exceptions=clsexc, nameattr='selector')
                    if exc is not None:
                        haveSpecial = True
                        if i not in arguments:
                            arguments[i] = (None, None, None)
                            haveSpecial = True


                if haveSpecial or isVariadic:
                    methods.append(
                        dict(
                            selector=''.join(segs),
                            class_method=class_method,
                            returns=(returnType, returnType64),
                            arguments=arguments,
                            variadic=isVariadic,
                        )
                    )


        if methods:
            # Always add to 'NSObject', that way all classes implementing this
            # protocol will see these exceptions.
            if 'NSObject' in self.classes:
                self.classes['NSObject'].extend(methods)
            else:
                self.classes['NSObject'] = methods




    def _processInterface(self, token):
        # Process nested definitions
        self.processTokens([ 
            t for t in token.matches()
                if type(t) not in (InterfaceEnd, SimpleMethodDef, SegmentedMethodDef, PropertyDefinition)])

        self.types[token['name'] + '*'] = objc._C_ID
        self.types64[token['name'] + '*'] = objc._C_ID
        self.types[token['name'] + '**'] = objc._C_PTR + objc._C_ID
        self.types64[token['name'] + '**'] = objc._C_PTR + objc._C_ID

        if token['name'] == 'NSObject' and token['category']:
            self._processInformalProtocol(token)
        
        logging.info("Class: %s (%s)", token['name'], token['category'])
        clsexc = self.find_exception('class', token['name'])

        methods = []
        for t in token.matches():
            if isinstance(t, PropertyDefinition):
                # @property
                typestr = t['type']
                options = t['options']
                if options is None:
                    options = []
                else:
                    options = [ v.strip() for v in options.split(',') ]

                haveSetter = True
                if 'readonly' in options:
                    haveSetter = False

                

                first = True


                for nm in t.matches():
                    if isinstance(nm, PropertyName):
                        nm = nm['name']
                    else:
                        continue

                    getterName = nm
                    setterName = 'set%s:'%(nm[0].upper() + nm[1:],)
                    for opt in options:
                        if opt.startswith('getter='):
                            getterName = opt.split('=', 1)[-1]
                        elif opt.startswith('setter='):
                            setterName = opt.split('=', 1)[-1]

                    curtype = typestr
                    while nm.startswith('*'):
                        curtype += '*'
                        nm = nm[1:].strip()


                    tp, tp64 = self.encodedType(curtype)

                    # First try to tell about the propertygetter
                    returnsMeta = {}
                    if self.isStringyType(tp, curtype):
                        returnsMeta['numeric'] = 'false'
                    
                    if self.isPointerType(tp) or tp in self.special_type_encodings or returnsMeta:
                        methods.append(
                            dict(
                                selector=getterName,
                                class_method=False,
                                returns=(tp, tp64, returnsMeta),
                                arguments={},
                                variadic=False,
                            )
                    )

                    # Then try to tell about the setter
                    if haveSetter:
                        if self.isPointerType(tp) or tp in self.special_type_encodings or returnsMeta:
                            methods.append(
                                dict(
                                    selector=setterName,
                                    class_method=False,
                                    returns=(objc._C_VOID, objc._C_VOID, {}),
                                    arguments={
                                        0: (tp, tp64, returnsMeta),
                                    },
                                    variadic=False,
                                )
                        )


                    if first:
                        # Strip indirection, pointer indirection only applies to the first name in 
                        # a list.
                        while typestr.endswith('*'):
                            typestr = typestr[:-1]
                        first = False




            elif isinstance(t, SimpleMethodDef):
                if t['kind'] == '-':
                    class_method=False
                else:
                    class_method=True

                returnType, returnType64 = self.encodedType(t['returntype'] or 'id')
                returnsMeta = {}
                if self.isStringyType(returnType, t['returntype'] or 'id'):
                    returnsMeta['numeric'] = 'false'

                if self.isPointerType(returnType) or returnType in self.special_type_encodings or returnsMeta:
                    methods.append(
                        dict(
                            selector=t['name'],
                            class_method=class_method,
                            returns=(returnType, returnType64, returnsMeta),
                            arguments={},
                            variadic=False,
                        )
                )

            elif isinstance(t, SegmentedMethodDef):
                if t['kind'] == '-':
                    class_method=False
                else:
                    class_method=True

                isVariadic = False
               
                returnType, returnType64 = self.encodedType(t['returntype'] or 'id')
                returnsMeta = {}
                if self.isStringyType(returnType, t['returntype'] or 'id'):
                    returnsMeta['numeric'] = 'false'

                haveSpecial = self.isPointerType(returnType) or returnType in self.special_type_encodings
                arguments = {}
                segs = []

                for idx, s in enumerate(t.matches()):
                    if isinstance(s, FunctionElipsisParameter):
                        isVariadic = True

                    if isinstance(s, MethodSegment):
                        segs.append(s['name'])
                        argType, argType64 = self.encodedType(s['type'] or 'id')
                        if argType is None:
                            # Compiler problems...
                            pass

                        elif self.isPointerType(argType) and normalize_type(s['type']) == 'NSError**':
                            # An NSError** argument, probably an output 
                            # argument
                            arguments[idx] = (argType, argType64, {
                                'type_modifier': 'o',
                                'null_accepted': 'true',
                            })
                            haveSpecial = True

                        elif (self.isPointerType(argType) and not self.hasModifier(argType)) or argType in self.special_type_encodings or argType == objc._C_SEL:
                            haveSpecial = True
                            arguments[idx] = (argType, argType64, None)

                        elif self.isStringyType(argType, s['type']):
                            haveSpecial = True
                            arguments[idx] = (argType, argType64, {
                                'numeric': 'false'})


                selector = ''.join(segs)


                for i in range(len(segs)+1):
                    exc = self.find_exception(
                        'method', selector,
                        child_tag='arg', child_index=i,
                        exceptions=clsexc, nameattr='selector')
                    if exc is not None:
                        haveSpecial = True
                        if i not in arguments:
                            arguments[i] = (None, None, None)
                            haveSpecial = True


                if haveSpecial or isVariadic:
                    methods.append(
                        dict(
                            selector=''.join(segs),
                            class_method=class_method,
                            returns=(returnType, returnType64, returnsMeta),
                            arguments=arguments,
                            variadic=isVariadic,
                        )
                    )


        if methods:
            if token['name'] in self.classes:
                self.classes[token['name']].extend(methods)
            else:
                self.classes[token['name']] = methods

    def _processInformalProtocol(self, token):
        logging.info("Informal protocol: %s", token['category'])
        methods = []
        for t in token.matches():
            # Add dict(selector=, encoding=, ...) to methods
            if isinstance(t, SimpleMethodDef):
                if t['kind'] == '-':
                    class_method = False
                else:
                    class_method = True

                returnType, returnType64 = self.encodedType(t['returntype'] or 'id')
                methods.append(
                    dict(
                        selector=t['name'],
                        class_method=class_method,
                        type=returnType + '@:',
                    )
                )

                if returnType64 and returnType64 != returnType:
                    methods[-1]['type64'] = returnType64 + '@:',

            elif isinstance(t, SegmentedMethodDef):
                if t['kind'] == '-':
                    class_method=False
                else:
                    class_method=True
        
                returnType, returnType64 = self.encodedType(t['returntype'] or 'id')
                types = [
                    returnType,
                    objc._C_ID,
                    objc._C_SEL,
                ]
                have64 = bool(returnType64)
                types64 = [
                    returnType64,
                    objc._C_ID,
                    objc._C_SEL,
                ]
                segs = []

                for s in t.matches():
                    if isinstance(s, MethodSegment):
                        segs.append(s['name'])
                        argType, argType64 = self.encodedType(s['type'] or 'id')
                        types.append(argType)
                        if not argType64:
                            have64 = False
                        types64.append(argType64)

                if None in types:
                    logging.warning("Cannot calcultate types for %s %s",
                            token['category'],
                            ''.join(segs))

                    continue


                methods.append(
                    dict(
                        selector=''.join(segs),
                        class_method=class_method,
                        type=''.join(types),
                    )
                )
                if have64 and types64 != types:
                    methods[-1]['type64'] = ''.join(types64)


        self.informal_protocols.append((token['category'], methods))

    def _processForwardClassReference(self, token):
        pass

    def _processForwardProtocolReference(self, token):
        pass

    def _processExportFunction(self, token):
        logging.debug('ExportFunction %s', token['name'])
        returns = token['returns']
        name = token['name'].strip()

        for item in self.functions:
            if item[0] == name:
                return

        if name.startswith('_'): 
            # Ignore  private functions, but have a hook to surpress
            # this behaviour
            exc = self.find_exception('function', name)
            if exc is None or exc.get('ignore', 'false') == 'true':
                return

        if isinstance(token, ExportVoidFunction):
            returnType, returnType64 = self.encodedType(returns)
            if returnType is None:
                logging.warning("Ignore function %s: cannot encode type %r",
                        name, returns)
                return
            returnMeta = {}
            if self.isStringyType(returnType, returns):
                returnMeta['numeric'] = 'false'

            self.functions.append((name, (returnType,returnType64, returnMeta), [], False))
            return


        variadic = False

        returnType, returnType64 = self.encodedType(returns)
        if returnType is None:
            logging.warning("Ignore function %s: cannot encode type %r",
                    name, returns)
            return

        returnMeta = {}
        if self.isStringyType(returnType, returns):
            returnMeta['numeric'] = 'false'

        arginfo = []
        for idx, arg in enumerate([ x for x in token.matches()[:-1] if not isinstance(x, BlockComment)]):
            if isinstance(arg, FunctionElipsisParameter):
                variadic = True
                continue

            nm = arg['name']
            tp = arg['type'].strip()

            if nm is None:
                # Sigh, getting the function parameter scanner correct is
                # a hopeless task, work around the problems here.
                m = re.match('(.*?)([A-Za-z_][A-Za-z0-9_]*)$', tp)
                if m:
                    tp = m.group(1).strip()
                    nm = m.group(2).strip()
                    if not tp:
                        tp = nm
                        nm = ''


            array = arg['array']
            if array:
                tp = tp + array
            arg = {}
            arginfo.append(arg)

            if nm is None:
                arg['type'] = tp
            else:
                arg['type'] = tp
                arg['name'] = nm.strip()


            try:
                arg['encoded'], arg['encoded64'] = self.encodedType(tp)
            except:
                print token
                raise

            if arg['encoded'] is None:
                logging.warning(
                    "Ignore function %s: cannot encode type %r for argument %d",
                    name, tp, idx)
                return

            if self.isStringyType(arg['encoded'], tp):
                arg['numeric'] = 'false'

        if isinstance(token, StaticInlineFunction):
            self.inline_functions.append((name, (returnType, returnType64), arginfo, variadic))
        else:
            self.functions.append((name, (returnType, returnType64, returnMeta), arginfo, variadic))


    def processTokens(self, tokenList):
        for token in ifilter(None, tokenList):
            if isinstance(token, CPPCrap):
                # Try to extract as much info as possible from CPPCrap
                if '#else' in token['body']:
                    text = token['body']
                    text = text[text.index('#else'):]
                    scn = Scanner(LEXICON)
                    self.processTokens(scn.iterscan(text))

            elif isinstance(token, GlobalThing):
                self._processGlobalThing(token)

            elif isinstance(token, Enum):
                self._processEnum(token)
            
            elif isinstance(token, NamedEnum):
                self._processNamedEnum(token)

            elif isinstance(token, Dependency):
                self._processDependencies(token)

            elif isinstance(token, SimpleDefine):
                self._processSimpleDefine(token)

            elif isinstance(token, FunctionCallDefine):
                self._processFunctionCallDefine(token)

            elif isinstance(token, NamedStruct):
                self._processNamedStruct(token)

            elif isinstance(token, Struct):
                self._processStruct(token)

            elif isinstance(token, OpaqueNamedStruct):
                self._processOpaqueNamedStruct(token)

            elif isinstance(token, UninterestingTypedef):
                self._processUninterestingTypedef(token)

            elif isinstance(token, Interface):
                self._processInterface(token)

            elif isinstance(token, Protocol):
                self._processProtocol(token)

            elif isinstance(token, ForwardClassReference):
                self._processForwardClassReference(token)

            elif isinstance(token, ForwardProtocolReference):
                self._processForwardProtocolReference(token)

            elif isinstance(token, (ExportFunction, ExportVoidFunction, StaticInlineFunction)):
                self._processExportFunction(token)

            else:
                if type(token) not in self.ignores:
                    print token
                    import pdb
                    pdb.Pdb().set_trace()



    def _compileAndRun(self, mainBody, globalDefinitions='', allowFailure=True, ppcAndIntel=False, additionalFramework=None):
        """Returns output, inserts 'mainBody' as the main body"""

        # Insert all include files we've seen so far instead of just
        # <framework/framework.h> because some frameworks don't have that
        # file.
        if not hasattr(self, 'scanner'):
            include_files = []
        else:
            include_files = self.scanner.seen

        # FSEvents is a separate framework, but also part of CarbonCore
        # which is the real version?
        include_files = [fn for fn in include_files if fn != 'FSEvents/FSEvents.h' ]

        if self.framework == self.link_framework:
            includes = '\n'.join(["#import <%s>"%(fn,) for fn in include_files])
        else:
            includes = '#import <%s/%s.h>'%(self.link_framework, self.link_framework)

        if additionalFramework:
            if os.path.exists('/System/Library/Frameworks/CoreServices.framework/Frameworks/%s.framework'%(additionalFramework)):
                pass
            elif os.path.exists('/System/Library/Frameworks/ApplicationServices.framework/Frameworks/%s.framework'%(additionalFramework)):
                pass
            else:
                includes += '\n#import <%s/%s.h>'%(additionalFramework, additionalFramework)

        contents = COMPILE_FILE % locals()

        fp = open('_scanframework.m', 'w')
        fp.write(contents)
        fp.close()

        try:
            # XXX: add redirection of stderr to /dev/null
            xit = subprocess.call('cc -pipe -o _scanframework _scanframework.m %s 2>/dev/null'%(
                self.CFLAGS), shell=True)

            if xit != 0:
                # Some frameworks, such as SyncServices contain some code that will only
                # work when the deployment target is at least 10.5...
                os.environ['MACOSX_DEPLOYMENT_TARGET']='10.5'
                xit = subprocess.call('cc -pipe -o _scanframework _scanframework.m %s 2>/dev/null'%(
                    self.CFLAGS), shell=True)
                del os.environ['MACOSX_DEPLOYMENT_TARGET']

            if xit != 0:
                logging.debug(
                    "Compilation failed for file contents\n---\n%s\n---",
                    contents)
                if allowFailure:
                    data = ''

                else:
                    raise RuntimeError("Compilation failed")

            else:

                data = subprocess.Popen(['./_scanframework'], stdout=subprocess.PIPE
                    ).communicate()[0]
                data = data.strip()

            if int(os.uname()[2].split('.')[0]) <= 8:
                data64 = ''

            else:
                os.environ['MACOSX_DEPLOYMENT_TARGET']='10.5'
                xit = subprocess.call(
                    'cc -pipe -o _scanframework _scanframework.m %s %s 2>/dev/null'%(
                    self.CFLAGS, self.CFLAGS64), shell=True)
                del os.environ['MACOSX_DEPLOYMENT_TARGET']
                if xit != 0:
                    logging.debug(
                        "Compilation-64 failed for file contents\n---\n%s\n---",
                        contents)

                    # Some datatypes are only available in 32-bit mode,
                    # such as type 'Movie' (found in QTKit/Quicktime). Not sure
                    # if this will change before Leopard is out. 
                    # Just ignore compile errors for now...
                    data64 = ''
                    #if allowFailure:
                    #    data64 = ''
                    #else:
                    #    raise RuntimeError("Compilation-64 failed")

                else:
                    data64 = subprocess.Popen(['./_scanframework'], 
                            stdout=subprocess.PIPE).communicate()[0]
                    data64 = data64.strip()

            if ppcAndIntel:
                if sys.byteorder != 'little':
                    raise RuntimeError("Sorry, must run on an intel system")

                xit = subprocess.call(
                    'cc -arch ppc -pipe -o _scanframework _scanframework.m %s 2>/dev/null'%(
                    self.CFLAGS), shell=True)
                if xit != 0:
                    os.environ['MACOSX_DEPLOYMENT_TARGET']='10.5'
                    xit = subprocess.call(
                        'cc -arch ppc -pipe -o _scanframework _scanframework.m %s 2>/dev/null'%(
                        self.CFLAGS), shell=True)
                    del os.environ['MACOSX_DEPLOYMENT_TARGET']
                if xit != 0:
                    logging.debug(
                        "Compilation-PPC failed for file contents\n---\n%s\n---",
                        contents)

                    if allowFailure:
                        dataPPC = ''
                    else:
                        raise RuntimeError("Compilation-PPC failed")

                else:
                    dataPPC = subprocess.Popen(['./_scanframework'], 
                            stdout=subprocess.PIPE).communicate()[0]
                    dataPPC = dataPPC.strip()

                return data, data64, dataPPC

        finally:
            if os.path.exists('_scanframework'):
                os.unlink('_scanframework')

            if os.path.exists('_scanframework.m'):
                os.unlink('_scanframework.m')




        return data, data64


def _main():
    
    #  Handle command-line arguments.
    parser = optparse.OptionParser(version="%prog 0.1")
    parser.add_option("-f", "--framework", dest="framework", 
        metavar="FRAMEWORK",
        help="Extra metadata from the given framework") 
    parser.add_option("-o", "--output", dest="outfile", metavar="FILE",
        help="Write the metadata to the given file (defaults to stdout)")
    parser.add_option("-O", "--output-exception", dest="outmeta", metavar="FILE",
        help="Write the exception to the given file (defaults to stdout)")
    parser.add_option("-e", "--exception", dest="exceptionfile", metavar="FILE",
        help="Use the given exception file when generating the output")
    parser.add_option("-F", "--format", dest="format", metavar="FORMAT",
        help="Select metadata format ('final-md' (default) or 'excp-templ-md')",
        default="final-md", 
        type="choice", choices=('final-md', 'excp-templ-md', 'both'))
    parser.add_option("--type_cache", dest="typecache", metavar="FILE")
    #parser.add_option("-c", "--compiler-flags", dest="cflags", metavar="CFLAGS",
    #    help="Specify custom compiler flags")
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose", 
        default=False, help="Be more verbose during generation")
    parser.add_option("-d", "--dependencies", dest="dependencies_file",
        help="Write a list of dependency to the specified file " +
             "(use '-' for stdout)", metavar="FILE")

    options, args = parser.parse_args()
    if args:
        parser.error("incorrect number of arguments")

    if options.framework is None:
        parser.error("You must specify the framework to parse")

    logging.basicConfig(
        format="%(levelname)s: %(message)s",
        stream=sys.stderr,
        level=(
            {
                True: logging.DEBUG, 
                False:logging.WARNING
            }[options.verbose])
    )

    
    if options.outfile is None:
        outfp = sys.stdout

    else:
        outfp = open(options.outfile + '~', 'w')

    try:
        types = types64 = None
        if options.typecache:
            if os.path.exists(options.typecache):
                fp = open(options.typecache, 'rb')
                try:
                    types, types64 = pickle.load(fp)
                except:
                    pass

        meta = FrameworkMetadata(options.framework, types, types64)

        if options.exceptionfile:
            meta.loadExceptionsXML(options.exceptionfile)

        meta.scan()
        #meta.scanClasses()

        if options.format == 'final-md':
            meta.emitMetaDataXML(outfp)

        elif options.format == 'excp-templ-md':
            meta.emitExceptionsXML(outfp)

        elif options.format == 'both':
            meta.emitMetaDataXML(outfp)

        outfp.close()
        if options.outfile:
            os.rename(options.outfile + '~', options.outfile)

        if options.format == 'both':

            if options.outmeta is None:
                outfp = sys.stdout

            else:
                outfp = open(options.outmeta + '~', 'w')

            meta.emitExceptionsXML(outfp)

            if options.outmeta:
                os.rename(options.outmeta + '~', options.outmeta)

    except:
        if options.outfile is not None:
            if os.path.exists(options.outfile + '~'):
                os.unlink(options.outfile + '~')

        if options.outmeta is not None:
            if os.path.exists(options.outmeta + '~'):
                os.unlink(options.outmeta + '~')
        raise

    if options.dependencies_file:
        if options.dependencies_file == '-':
            fp = sys.stdout
        else:
            fp = open(dependencies_file, 'w')
        meta.emitDependecyList(fp)
        del fp

    if options.typecache:
        types, types64 = meta.types, meta.types64
        fp = open(options.typecache, 'wb')
        pickle.dump((types, types64), fp)
        fp.close()


def main():
    # Some frameworks, such as SyncServices contain some code that will only
    # work when the deployment target is at least 10.5...
    #os.environ['MACOSX_DEPLOYMENT_TARGET']='10.5'

    try:
        _main()

    except KeyboardInterrupt:
        print "Interrupted"

    except:
        raise

    return 0


if __name__ == "__main__":
    main()
