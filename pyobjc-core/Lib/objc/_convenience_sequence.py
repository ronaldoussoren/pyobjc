"""
This module implements a callback function that is used by the C code to
add Python special methods to Objective-C classes with a suitable interface.
"""
from objc._convenience import addConvenienceForClass

__all__ = ('addConvenienceForBasicSequence',)

def collection_iter(self):
    for idx in range(len(self)):
        yield self[idx]

def addConvenienceForBasicSequence(classname, readonly=True):
    addConvenienceForClass(classname, (
        ('__len__',  lambda self: self.count()),
        ('__getitem__', lambda self, idx: self.objectAtIndex_(idx)),
        ('__iter__', collection_iter),
    ))

    if not readonly:
        addConvenienceForClass(classname, (
            ('__setitem__', lambda self, idx, value: self.setObject_atIndex_(value, idx)),
        ))


# XXX: Move these to another file
addConvenienceForBasicSequence('WebScriptObject', True)
addConvenienceForClass('WebScriptObject', (
    ('count',    lambda self: self.lenght()),
))
addConvenienceForBasicSequence('QCStructure', True)
