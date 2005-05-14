# TODO
# - documentation
# - scan headers outsite of frameworks (/usr/include/foo.h)
# - generate wrappers for 'static inline' functions
# - parse protocols and categories -> generate informal_protocol definitions
# - deal with embedded frameworks
# - compare results of scanframeworks with those of the 'old' generator
#   scripts
# - test, test and even more testing
# - refactor script: make it possible to create wrappers for multiple 
#   frameworks in one go, without rescanning headers over and over again.
# - integrate into build process
# - Scanframework of CoreFoundation seems to indicate that the tokenizer 
#   isn't good enough yet (or that I broke it).
# - How can we wrap CoreFoundation types (e.g. CFURLRef)? How can we 
#   find CFRef-style types?
import os
try:
    set
except NameError:
    from sets import Set as set
import glob
import sys
from tokenize_header import *
from macholib.dyld import framework_find
from itertools import *
from textwrap import dedent

class Hinter (object):
    """
    A hinter can be used to specify additional information about
    a framework. 

    NOTE: The hinter should only be used to insert information that
    cannot be deduced from the header files, don't use the hinter to
    work around limitations in the scanner!
    """
    def __init__(self, path):
        self._globals = {}
        execfile(path, self._globals)
    
        self._ignores = self._globals.get('IGNORES', {})
        self._ignorefunc = self._globals.get('should_ignore', None)

    def should_ignore(self, name):
        if name in self._ignores:
            return True
        elif self._ignorefunc is not None and self._ignorefunc(name):
            return True

        return False

    def write_additional_imports(self, fp):
        """
        Write additional import statements in the __init__.py. This
        uses the 'ADDITIONAL_IMPORTS' in the hints file, if that exists.
        """
        imports = self._globals.get('ADDITIONAL_IMPORTS', ())

        for imp in imports:
            print >>fp, dedent("""\
                    try:
                        import %(imp)s
                    except ImportError:
                        pass
                    """%locals())

    def argument_kind(self, name, idx, nm, tp):
        """
        Determine the kind (in, out or inout) of an argument, using
        the argument_kind function in the hints file. 
        
        The hint function should return None if it doesn't know the kind
        of the argument.
        """
        fun = self._globals.get('argument_kind', None)
        if fun is None:
            return None

        return fun(name, idx, nm, tp)

    def should_create_struct_wrapper(self, name, fieldnames, fieldtypes):
        fun = self._globals.get('should_create_struct_wrapper', None)
        if fun is None:
            return None

        return fun(name, fieldnames, fieldtypes)




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
    dylib = framework_find(f, env=env)
    framework = os.path.dirname(dylib)
    update_fallback(env, framework)
    headers = known[f] = os.path.join(framework, 'Headers')
    return headers

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
    def __init__(self):
        self._scanner = None

    def scanframework(self, name, sub=None):
        if sub is None:
            sub = name
        start = '%s/%s.h' % (name, sub)
        startfile = locate_header(start)
        startframework = os.path.join(os.path.dirname(framework_find(name)), '')
        seen = set()
        scanners = []
        if os.path.exists(startfile):
            seen.add(start)
            scanners.append(self.scanfile(startfile))
        else:
            headers = glob.glob(locate_header('%s/*.h' % (name,)))
            for header in headers:
                seen.add(name + '/' + os.path.basename(header))
                scanners.append(self.scanfile(header))
        while scanners:
            try:
                token = scanners[-1].next()
            except StopIteration:
                scanners.pop()
                continue
            if isinstance(token, (AngleImport, StringImport)):
                fn = token['import_file']
                if fn in seen:
                    pass
                else:
                    seen.add(fn)
                    try:
                        header = locate_header(fn)
                    except ValueError:
                        pass
                    else:
                        if header.startswith(startframework):
                            scanners.append(self.scanfile(locate_header(fn)))
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
        return self._scanner.iterscan(file(fn).read(), dead=deadraise)

def contains_instances_of(iterator, types):
    for i in iterator:
        if isinstance(i, types):
            return True
    return False

def do_enum(enum):
    if isinstance(enum, NamedEnum):
        yield '\n# ' + enum.matches()[-1]['name']
    i = -1
    for token in enum.matches():
        if isinstance(token, EnumValueMember):
            name = token['name']
            value = token['value']

            try:
                i = int(value)
            except ValueError:
                i = (value, 0)

            if hinter is not None and hinter.should_ignore(name):
                continue

            yield '\n%s = %s' % (name, value)
        elif isinstance(token, EnumBareMember):
            name = token['name']
            if isinstance(i, tuple):
                i = (i[0], i[1] + 1)

                if hinter is not None and hinter.should_ignore(name):
                    continue

                yield '\n%s = %s + %s'%(name, i[0], i[1])

            else:
                i += 1
                value = i

                if hinter is not None and hinter.should_ignore(name):
                    continue

                yield '\n%s = %s' % (name, value)
        elif isinstance(token, (EnumEnd, NamedEnumEnd)):
            yield '\n'
        elif isinstance(token, SingleLineComment):
            yield ' # ' + token['comment']

def do_opaque_struct(token, types, opaque_pointers, hinter):
    name = token['name']
    tag = token['label']
    indirect = token['indirection'].strip() == '*'

    if hinter is not None and hinter.should_ignore(name):
        return

    encoded = 'objc._C_PTR + objc._C_STRUCT_B + %r + objc._C_STRUCT_E'%(tag,)
    types[name +  '*'] = encoded

    if not indirect:
        name += 'Ptr'

    opaque_pointers.append(
        '%(name)s = objc.createOpaquePointerType(%(name)r, %(encoded)r, "typedef struct %(tag)s* %(name)s")\n'% locals() )


def do_struct(token, types, structs, hinter):
    # Skip structs containing function pointers, those cannot be
    # wrapped automaticly (yet?)
    if contains_instances_of(token.matches(), FunctionStructMember): return

    externalname = token.matches()[-1]['name']

    if hinter is not None and hinter.should_ignore(externalname):
        return

    structname = token['structname']
    body = token.matches()[:-1]
    fieldnames = []
    fields = []
    elems = [
        'objc._C_STRUCT_B',
    ]
    if structname:
        elems.append('"%s"'%(structname,))
    if body:
        elems.append('"="')
        for tk in body:
            if isinstance(tk, StructMember):
                tp = normalize_typename(tk['type'])
                nm = tk['name']
                nm = [ n.strip() for n in nm.split(',') ]
                fieldnames.extend(nm)
                for x in nm:
                    fields.append('    %s\t%s;'%(tp, x))

                try:
                    etp = types[tp]
                except KeyError:
                    return

                elems.extend([types[tp]]*len(nm))

            elif isinstance(tk, NestedStructMember):
                print "Ignore hard struct", token
                return
        
    elems.append('objc._C_STRUCT_E')
    encoded = "''.join(("+ ', '.join(elems) + ",))"
    types[externalname] = '_%s_encoded'%(externalname,)

    doc = 'typedef struct {\n%s\n} %s;'%('\n'.join(fields), externalname)

    structs.append('_%s_encoded = %s\n'%(externalname, encoded))

    if hinter is not None and not hinter.should_create_struct_wrapper(
            externalname, fieldnames, fields):
        return

    structs.append('%s = objc.createStructType("%s", _%s_encoded, %s, %r)\n'%(
        externalname, externalname, externalname, fieldnames, doc))

def normalize_typename(value):
    value = value.strip().replace('\t', ' ')
    while '  ' in value:
        value = value.replace('  ', ' ')
    value = value.replace(' *', '*')
    return value

def do_function(token, types, functions, hinter=None):
    returns = normalize_typename(token['returns'])
    name = token['name'].strip()

    # Ignore  private functions
    if name.startswith('_'): return

    if hinter is not None and hinter.should_ignore(name):
        return

    if isinstance(token, ExportVoidFunction):
        if returns in types:
            functions.append("\n        (%r, %s, '%s %s(void)'),"%(
                    name, 
                    types[returns],
                    returns, name))
        else:
            print "Ignore function %s (retval) %r"%(name, returns)
        return

    if contains_instances_of(token.matches(), FunctionElipsisParameter):
        print "Ignore varargs function %s"%(name,)
        return

    if returns not in types and returns != 'void':
        print "Ignore function %s (retval) %r"%(name, returns)
        return

    arglist = []
    if returns == 'void':
        argtypes = ['objc._C_VOID',]
    else:
        argtypes = [types[returns],]

    for idx, arg in enumerate(token.matches()[:-1]):
        tp = normalize_typename(arg['type'])
        nm = arg['name']
        if nm is None:
            arglist.append('%s'%(tp,))
        else:
            nm = nm.strip()
            arglist.append('%s %s'%(tp, nm))

        if tp in types:
            encoded = types[tp]
        elif tp[-1] == '*':
            kind = None
            if tp.startswith('const '):
                kind = 'objc._C_IN'
                c = tp[5:].strip()
            else:
                c = tp


            ptr = 0
            while c[-1] == '*':
                c = c[:-1]
                ptr += 1
            if c not in types:
                print 'Ignore function %s (arg) nm: %r, tp: %r'%(name, nm, tp)
                return
            
            # XXX: we really need a hinting mechanism here: someone needs to
            # tell us if the argument is an input or output argument.
            if kind is None:
                if hinter is not None:
                    kind = hinter.argument_kind(name, idx, nm, tp)
                    if kind is None:
                        print 'Ignore function %s (arg) nm: %r, tp: %r'%(
                            name, nm, tp)
                        return
                else:
                    print 'Ignore function %s (arg) nm: %r, tp: %r'%(
                        name, nm, tp)
                    return

            if ptr != 1:
                print 'Ignore function %s (arg) nm: %r, tp: %r'%(name, nm, tp)
                return
                #encoded = kind + ' + (objc._C_PTR * %d ) + '%(ptr,) + types[c]
            else:
                encoded = kind + ' + objc._C_PTR + ' + types[c]
        else:
            print 'Ignore function %s (arg) nm: %r, tp: %r'%(name, nm, tp)
            return

        argtypes.append(encoded)

    encoded = "''.join(("+ ', '.join(argtypes) + ",))"
    functions.append("\n        (%r, %s, '%s %s(%s)'),"%(
        name, encoded, returns, name, ', '.join(arglist)))

def do_uninteresting_typedef(token, types):
    if ',' in token['body']: return
    ptr = 0
    body = token['body'].split()

    alias = ' '.join(body[:-1])
    target = body[-1]

    if hinter is not None and hinter.should_ignore(target):
        return

    while alias[-1] == '*':
        alias = alias[:-1]
        ptr += 1
    while target[0] == '*':
        target = target[1:]
        ptr += 1
    if alias in types:
        if ptr == 1:
            prefix = 'objc._C_PTR+'
        elif ptr > 1:
            prefix = '(objc._C_PTR*%s)+'%(ptr,)
        else:
            prefix = ''
        types[target] = prefix + types[alias]
    else:
        print "Ignore simple typedef: %s"%(target,)

def extractTypes(framework, types, dependencies):
    """
    Extract type definitions from a framework. 

    This function only parses type definitions and updates the type table.
    """
    f = FrameworkScanner()

    for token in ifilter(None, f.scanframework(framework)):
        if isinstance(token, NamedEnum):
            nm = token.matches()[-1]['name'].strip()
            types[nm] = types['int']

        elif isinstance(token, Dependency):
            # TODO: also parse system headers
            dep = os.path.dirname(token.infoTuple()[0])
            if dep and dep not in dependencies:
                dependencies.add(dep)
                extractTypes(dep, types, dependencies)

        elif isinstance(token, NamedStruct):
            do_struct(token, types, [], None)

        elif isinstance(token, OpaqueNamedStruct):
            do_opaque_struct(token, types, [], None)

        elif isinstance(token, UninterestingTypedef):
            do_uninteresting_typedef(token, types)

        elif isinstance(token, (Interface, ForwardClassReference)):
            types[token['name'] + '*'] = types['id']

def makeInit(framework, out, hinter = None):
    framework_name = filter(None, os.path.split(framework))[0]
    framework_path = unicode(os.path.dirname(framework_find(framework_name)), sys.getfilesystemencoding())
    f = FrameworkScanner()
    types = {
        'id': 'objc._C_ID',
        'NSString *': 'objc._C_ID',
        'NSString*': 'objc._C_ID',
        'CFStringRef': 'objc._C_ID',
        'SEL': 'objc._C_SEL',
        'BOOL': 'objc._C_NSBOOL',
        'bool': 'objc._C_BOOL',
        'Class': 'objc._C_CLASS',

        'char': 'objc._C_CHR',
        'unsigned char': 'objc._C_UCHR',

        'int': 'objc._C_INT',
        'signed int': 'objc._C_INT',
        'signed': 'objc._C_INT',
        'unsigned int': 'objc._C_UINT',
        'unsigned': 'objc._C_UINT',

        'short': 'objc._C_SHT',
        'signed short': 'objc._C_SHT',
        'unsigned short': 'objc._C_USHT',

        'long': 'objc._C_LNG',
        'signed long': 'objc._C_LNG',
        'unsigned long': 'objc._C_ULNG',

        'long long': 'objc._C_LNGLNG',
        'signed long long': 'objc._C_LNGLNG',
        'unsigned long long': 'objc._C_ULNGLNG',

        'float': 'objc._C_FLT',
        'double': 'objc._C_DBL',
        
        'char*': 'objc._C_CHARPTR',
    }

    # Some aliases
    # XXX: need to improve this script, this information can be 
    # extracted from system headers
    types['int8_t'] = types['char']
    types['uint8_t'] = types['unsigned char']
    types['int16_t'] = types['short']
    types['uint16_t'] = types['unsigned short']
    types['int32_t'] = types['long']
    types['uint32_t'] = types['unsigned long']
    types['int64_t'] = types['long long']
    types['uint64_t'] = types['unsigned long long']
    types['const char*'] = types['char*']

    ignores = set([
        CompilerDirective,
        BlockComment,
        SingleLineComment,
        CPPCrap,

        # Stuff below here might be interesting
        UninterestingStruct, 
        MacroDefine,
    ])
    dependencies = set()
    globthings = []
    enums = []
    simple_defines=[]
    imports = []
    structs = []
    functions = []
    opaque_pointers = []
    for token in ifilter(None, f.scanframework(framework)):
        if isinstance(token, GlobalThing):
            name = token['name'].strip()

            if hinter and hinter.should_ignore(name):
                continue

            # Skip private variables
            if name[0] == '_': continue

            tp = normalize_typename(token['type'])
            if tp not in types:
                print 'ignore', token
                continue

            globthings.append('\n        (%r, %s),' %(unicode(name), types[tp]))
        elif isinstance(token, (Enum, NamedEnum)):
            if isinstance(token, NamedEnum):
                nm = token.matches()[-1]['name'].strip()
                types[nm] = types['int']

            for s in do_enum(token):
                enums.append(s)
        elif isinstance(token, Dependency):
            dep = os.path.dirname(token.infoTuple()[0])
            if dep and dep not in dependencies:
                dependencies.add(dep)
                extractTypes(dep, types, dependencies)
                imports.append('\ntry:\n    from %s import *\nexcept ImportError:\n    pass\n' % (dep,))
        elif isinstance(token, SimpleDefine):
            if token['name'].startswith('_'): continue
            if token['name'] in ('NULL',): continue
            if token['value'].startswith('AVAILABLE_MAC_OS_X_VERSION_'): continue
            if token['value'] in ('SHRT_MAX',): continue # XXX
            simple_defines.append('%s=%s\n'%(token['name'], token['value']))

        
        elif isinstance(token, NamedStruct):
            do_struct(token, types, structs, hinter)

        elif isinstance(token, OpaqueNamedStruct):
            do_opaque_struct(token, types, opaque_pointers, hinter)

        elif isinstance(token, UninterestingTypedef):
            do_uninteresting_typedef(token, types)

        elif isinstance(token, Protocol):
            # TODO: generate informal-protocol definition. 
            # Need to enhance the tokenizer for that
            pass

        elif isinstance(token, (Interface, ForwardClassReference)):
            # Class definition: make the type known to the type table
            types[token['name'] + '*'] = types['id']

        elif isinstance(token, (ExportFunction, ExportVoidFunction)):
            do_function(token, types, functions, hinter)

        elif isinstance(token, StaticInlineFunction):
            # TODO: emit wrapper inside a C file.
            pass

        else:
            if type(token) not in ignores:
                print token
                import pdb
                pdb.Pdb().set_trace()
    print >>out, '# Imports'
    out.write('import objc\n')
    out.writelines(imports)
    if hinter is not None:
        hinter.write_additional_imports(out)
        
    if enums:
        print >>out, '\n# Enumerations'
        out.writelines(enums)

    if simple_defines:
        print >>out, '\n# Simple defines'
        out.writelines(simple_defines)

    if structs:
        print >>out, '\n# struct definitions'
        out.writelines(structs)

    if opaque_pointers:
        print >>out, '\n# opaque pointers'
        out.writelines(opaque_pointers)

    bundle_variables = ''.join(globthings)
    bundle_functions = ''.join(functions)
    print >>out, """

def _initialize():
    import objc
    p = objc.pathForFramework(%(framework_path)r)
    objc.loadBundle(%(framework_name)r, globals(), bundle_path=p)
    """ % locals()

    if bundle_variables or bundle_functions:
        print >>out, """\
    b = objc.lookUpClass('NSBundle').bundleWithPath_(p)
"""

    if bundle_variables:
        print >>out, """\
    objc.loadBundleVariables(b, globals(), [%(bundle_variables)s
    ])
""" % locals()

    if bundle_functions:
        print >>out, """\
    objc.loadBundleFunctions(b, globals(), [%(bundle_functions)s
    ])
""" % locals()
    print >>out, """
_initialize()
del objc
"""

def makeWrapper(fmwk, hinter):
    try:
        os.makedirs(fmwk)
    except OSError:
        pass
    makeInit(fmwk, file(os.path.join(fmwk, '__init__.py'), 'w'), hinter)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        fmwk = 'PreferencePanes'
        hinter = None
    elif len(sys.argv) == 2:
        fmwk = sys.argv[1]
        hinter = None
    elif len(sys.argv) == 3:
        fmwk = sys.argv[1]
        hinter = Hinter(sys.argv[2])
    else:
        print >> sys.stderr, "Usage: scanframeworks [Framework [hinter]]"
        sys.exit(1)

    makeWrapper(fmwk, hinter)
