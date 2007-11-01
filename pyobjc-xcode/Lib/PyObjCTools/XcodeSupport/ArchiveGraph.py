#!/usr/bin/env python

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

XCODE_20 = 1000
XCODE_21 = 999

def _xcodeFiles(base):
    for fn in os.listdir(base):
        ext = os.path.splitext(fn)[1]
        if ext == '.xcode':
            yield XCODE_20, os.path.join(base, fn, 'project.pbxproj')
        elif ext == '.xcodeproj':
            yield XCODE_21, os.path.join(base, fn, 'project.pbxproj')

def xcodeFiles(base):
    lst = list(_xcodeFiles(base))
    lst.sort()
    return [path for (ver, path) in lst]
        
def main():
    fn = (sys.argv[1:2] or xcodeFiles('.'))[0]
    o = ArchiveGraph.fromPath(fn)
    o.graphreport()
    return o

if __name__ == '__main__':
    o = main()
