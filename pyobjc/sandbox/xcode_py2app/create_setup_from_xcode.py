#
# Assume that most lines in this file are preceded by an XXX.
# This is some seriously ugly shit.
#
# Written for ReSTEdit's Xcode project.
#
import sys
import os
import glob
from altgraph.compat import *
from Foundation import *
from altgraph.ObjectGraph import ObjectGraph

class attrdict(dict):
    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError, e:
            raise AttributeError(*e.args)

class Object(object):
    def __init__(self, guid, dct):
        self.graphident = self._guid = guid
        self._prototype = dct

    def __repr__(self):
        return "<%s guid=%s>" % (type(self).__name__, self._guid)

    def __hash__(self):
        return hash(self._guid)

    def __eq__(self, other):
        return self._guid == other._guid

class ArchiveGraph(ObjectGraph):
    def __init__(self, graph=None, debug=0):
        super(ArchiveGraph, self).__init__(graph=graph, debug=debug)
        self.root = None
        self.classes = attrdict()
        self.classbuckets = attrdict()

    def parseDict(self, d):
        newobjects = []
        for guid, dct in d[u'objects'].iteritems():
            isa = dct[u'isa']
            cls = self.getClass(isa)
            node = self.createNode(cls, guid, dct)
            self.classbuckets[isa].append(node)
            newobjects.append(node)
        self.root = self.findNode(d[u'rootObject'])
        self.createReference(None, self.root, 'root')
        for obj in newobjects:
            self.resolveObject(obj)
            
    def resolveObject(self, obj):
        d = self.resolveItem(obj._prototype, caller=obj)
        ident = d.get('path') or d.get('name')
        if ident:
            obj.identifier = '%s(%s)' % (type(obj).__name__, ident)
        else:
            obj.identifier  = repr(obj)
        for key, value in d.iteritems():
            setattr(obj, str(key), value)

    def resolveItem(self, item, caller=None, edge_data='unknown'):
        if isinstance(item, (dict, NSDictionary)):
            d = attrdict()
            for key, value in item.iteritems():
                key = self.resolveItem(key, caller=caller, edge_data=edge_data)
                value = self.resolveItem(value, caller=caller, edge_data=str(key))
                d[key] = value
            item = d
        elif isinstance(item, (unicode, NSString)):
            ref = self.findNode(item)
            if ref is not None:
                self.createReference(caller, ref, edge_data=edge_data)
                item = ref
        elif isinstance(item, (list, tuple, NSArray)):
            edge_data = '[%s]' % (edge_data,)
            item = [self.resolveItem(i, caller=caller, edge_data=edge_data) for i in item]
        return item
    
    def getClass(self, isa):
        cls = self.classes.get(isa)
        if cls is None:
            cls = self.classes[isa] = type(str(isa), (Object,), {})
            self.classbuckets[isa] = []
        return cls

    def __getitem__(self, item):
        return self.findNode(item)

    def fromPath(cls, fn):
        self = cls()
        self.parseDict(openDict(fn))
        return self
    fromPath = classmethod(fromPath)

    def itergraphreport(self, name='G'):
        nodes = map(self.graph.describe_node, self.graph.iterdfs(self))
        describe_edge = self.graph.describe_edge
        return itergraphreport(nodes, describe_edge, name=name)

    def graphreport(self, fileobj=None):
        if fileobj is None:
            fileobj = sys.stdout
        fileobj.writelines(self.itergraphreport())

def itergraphreport(nodes, describe_edge, name='G'):
    edges = deque()

    def nodevisitor(node, data, outgoing, incoming):
        if data is None:
            data = node
        ident = getattr(data, 'identifier', None)
        if ident is None:
            ident = repr(data)
        return {'label': ident}

    def edgevisitor(edge, data, head, tail):
        return {'label': str(data)}

    yield 'digraph %s {\n' % (name,)
    attr = dict(rankdir='LR', concentrate='true')
    cpatt  = '%s="%s"'
    for item in attr.iteritems():
        yield '\t%s;\n' % (cpatt % item,)

    # create sets for subgraph, write out descriptions
    for (node, data, outgoing, incoming) in nodes:
        # update edges
        for edge in imap(describe_edge, outgoing):
            edges.append(edge)

        # describe node
        yield '\t"%s" [%s];\n' % (
            node,
            ','.join([
                (cpatt % item) for item in
                nodevisitor(node, data, outgoing, incoming).iteritems()
            ]),
        )

    def do_graph(edges, tabs):
        edgestr = tabs + '"%s" -> "%s" [%s];\n'
        # describe edge
        for (edge, data, head, tail) in edges:
            attribs = edgevisitor(edge, data, head, tail)
            yield edgestr % (
                head,
                tail,
                ','.join([(cpatt % item) for item in attribs.iteritems()]),
            )

    for s in do_graph(edges, '\t'):
        yield s

    yield '}\n'

def openDict(fn):
    if not isinstance(fn, unicode):
        fn = unicode(fn, 'utf-8')
    return NSDictionary.dictionaryWithContentsOfFile_(fn)

def main():
    fn = (sys.argv[1:2] or glob.glob('*.xcode/project.pbxproj'))[0]
    o = ArchiveGraph.fromPath(fn)
    #o.graphreport()
    return o

def isPythonResource(fn):
    return fn.endswith(u'.py')

def allFiles(phase):
    for buildFile in phase.files:
        ref = buildFile.fileRef
        for ref in getattr(ref, 'children', (ref,)):
            yield unicode(ref.path).encode('utf-8')

def collectResources(paths, py, res):
    for path in paths:
        if isPythonResource(path):
            py.append(path)
        else:
            res.append(path)

C_TEMPLATE = """
/* 
    XXX - THIS IS A GENERATED FILE - DO NOT MODIFY - XXX
*/

#import "Python.h"
PyMODINIT_FUNC
init__py2app_xcode__(void)
{
    (void)Py_InitModule("__py2app_xcode__", NULL);
}
"""

TEMPLATE = """
#
# XXX - THIS IS A GENERATED FILE - DO NOT MODIFY - XXX
#
from distutils.core import setup, Extension
import py2app
import py2app.recipes
from StringIO import StringIO
import plistlib
import os

plist = plistlib.Plist.fromFile(%(plist)r)
del plist[u'PyRuntimeLocations']

sources = %(sources)r
kw = dict(options = dict(py2app=dict(
    plist=plist,
    compressed=True,
    strip=True,
)))
if sources:
    sources.insert(0, '__py2app_xcode__.c')
    extra_link_args = []
    for framework in %(frameworks)r:
        if framework.endswith('.framework'):
            base = os.path.basename(framework)[:-len('.framework')]
            framework = os.path.join(framework, base)
        extra_link_args.append(framework)
    kw['ext_modules'] = [
        Extension('__py2app_xcode__',
            sources,
            extra_compile_args=['-F.', '-I.', '-L.'],
            extra_link_args=extra_link_args,
        ),
    ]
    kw['options']['py2app']['includes'] = ['__py2app_xcode__']

    class py2app_xcode_recipe(object):
        def check(self, dist, mf):
            return dict(prescripts=[StringIO("import __py2app_xcode__")])
    import py2app.recipes
    py2app.recipes.py2app_xcode = py2app_xcode_recipe()
    

setup(
    data_files = [(os.path.dirname(rsrc), [rsrc]) for rsrc in %(resources)r],
    app = [%(app)r],
    **kw
)
"""

def parse(o):
    root = o.root
    if not root.targets:
        raise ValueError, "No targets"
    if len(root.targets) > 1:
        print "Warning, multiple targets, using the first"
    target = root.targets[0]
    assert len(root.targets) == 1
    b = target.buildSettings
    plist = unicode(b.INFOPLIST_FILE).encode('utf-8')
    c = o.classes
    resources = []
    sources = []
    frameworks = []
    copyfiles = []
    python = []
    for phase in target.buildPhases:
        if isinstance(phase, c.PBXHeadersBuildPhase):
            # don't care about these!
            pass
        elif isinstance(phase, c.PBXResourcesBuildPhase):
            collectResources(allFiles(phase), python, resources),
        elif isinstance(phase, c.PBXSourcesBuildPhase):
            sources.extend(allFiles(phase))
        elif isinstance(phase, c.PBXFrameworksBuildPhase):
            frameworks.extend(allFiles(phase))
        elif isinstance(phase, c.PBXCopyFilesBuildPhase):
            # external references to python junk
            pass
    app = '__main__.py'
    python.remove(app)
    sources.remove('main.m')
    resources.remove(plist)

    if sources and not os.path.exists('__py2app_xcode__.c'):
        file('__py2app_xcode__.c', 'w').write(C_TEMPLATE)
    return TEMPLATE % locals()
    
if __name__ == '__main__':
    o = main()
    file('setup.py', 'w').write(parse(o))
