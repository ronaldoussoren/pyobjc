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

class EnumCollector(object):
    def __init__(self):
        self.seen = []
        self.code = []

    def add(self, enum):
        value = -1
        for token in enum.matches():
            if isinstance(token, EnumValueMember):
                value = token['value']

def do_enum(enum):
    if isinstance(enum, NamedEnum):
        yield '\n# ' + enum.matches()[-1]['name']
    i = -1
    for token in enum.matches():
        if isinstance(token, EnumValueMember):
            name = token['name']
            value = token['value']
            i = int(value) + 1
            yield '\n%s = %s' % (name, value)
        elif isinstance(token, EnumBareMember):
            name = token['name']
            i += 1
            value = i
            yield '\n%s = %s' % (name, value)
        elif isinstance(token, (EnumEnd, NamedEnumEnd)):
            yield '\n'
        elif isinstance(token, SingleLineComment):
            yield ' # ' + token['comment']

def makeInit(framework, out):
    framework_name = filter(None, os.path.split(framework))[0]
    framework_path = unicode(os.path.dirname(framework_find(framework_name)), sys.getfilesystemencoding())
    f = FrameworkScanner()
    types = {
        'id': 'objc._C_ID',
        'NSString *': 'objc._C_ID',
        'double': 'objc._C_DBL',
    }
    ignores = set([
        CompilerDirective,
        BlockComment,
        SingleLineComment,
        CPPCrap,
        ForwardClassReference,
        Interface,
    ])
    dependencies = set()
    globthings = []
    enums = []
    imports = []
    for token in ifilter(None, f.scanframework(framework)):
        if isinstance(token, GlobalThing):
            globthings.append('        (%r, %s),\n' % (unicode(token['name']), types[token['type']]))
        elif isinstance(token, (Enum, NamedEnum)):
            for s in do_enum(token):
                enums.append(s)
        elif isinstance(token, Dependency):
            dep = os.path.dirname(token.infoTuple()[0])
            if dep and dep not in dependencies:
                dependencies.add(dep)
                imports.append('\ntry:\n    from %s import *\nexcept ImportError:\n    pass\n' % (dep,))
        else:
            if type(token) not in ignores:
                print token
                import pdb
                pdb.Pdb().set_trace()
    print >>out, '# Imports'
    out.writelines(imports)
    print >>out, '\n# Enumerations'
    out.writelines(enums)
    bundle_variables = ''.join(globthings)
    print >>out, """

def _initialize():
    from Foundation import NSBundle
    import objc
    p = objc.pathForFramework(%(framework_path)r)
    objc.loadBundle(%(framework_name)r, globals(), bundle_path=p)
    b = NSBundle.bundleWithPath_(p)
    objc.loadBundleVariables(b, globals(), [
%(bundle_variables)s
    ])

    # XXX - hack to fix-up NSError** args
    #for cls in globals().values():
    #    if not isinstance(cls, objc.objc_class):
    #        continue
    #    for selname in dir(cls):
    #        if selname.startswith('_'):
    #            continue
    #        o = getattr(cls, selname, None)
    #        if not isinstance(o, objc.selector):
    #            continue
    #        if o.selector.endswith(':error:') and o.signature.endswith('^@'):
    #            if o.signature[-3] in 'onN':
    #                continue
    #            sel = objc.selector(None,
    #                selector=o.selector,
    #                o.signature[:-2] + 'n^@')
    #            setattr(cls, selname, sel)
_initialize()
    """ % locals()

def makeWrapper(fmwk):
    try:
        os.makedirs(fmwk)
    except OSError:
        pass
    makeInit(fmwk, file(os.path.join(fmwk, '__init__.py'), 'w'))

if __name__ == '__main__':
    fmwk = (sys.argv[1:] or ['PreferencePanes'])[0]
    makeWrapper(fmwk)
