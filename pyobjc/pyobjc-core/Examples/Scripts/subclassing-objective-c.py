#!/usr/bin/env python
# This is a doctest
"""
=========================================
Subclassing Objective-C classes in Python
=========================================

It is possible to subclass any existing Objective-C class in python.

We start by importing the interface to the Objective-C runtime, although
you'd normally use wrappers for the various frameworks, and then locate
the class we'd like to subclass::

    >>> import objc
    >>> NSEnumerator = objc.lookUpClass('NSEnumerator')
    >>> NSEnumerator
    <objective-c class NSEnumerator at 0xa0a039a8>

You can then define a subclass of this class using the usual syntax::

    >>> class MyEnumerator (NSEnumerator):
    ...    __slots__ = ('cnt',)
    ...    #
    ...    # Start of the method definitions:
    ...    def init(self):
    ...        self.cnt = 10
    ...        return self
    ...    #
    ...    def nextObject(self):
    ...        if self.cnt == 0:
    ...            return None
    ...        self.cnt -= 1
    ...        return self.cnt
    ...    #
    ...    def __del__(self):
    ...        global DEALLOC_COUNT
    ...        DEALLOC_COUNT = DEALLOC_COUNT + 1


To check that our instances our deallocated we maintain a ``DEALLOC_COUNT``::

    >>> DEALLOC_COUNT=0

As always, the creation of instances of Objective-C classes looks a bit odd
for Python programs:

    >>> obj = MyEnumerator.alloc().init()
    >>> obj.allObjects()
    (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)

Destroy our reference to the object, to check if it will be deallocated::

   >>> del obj
   >>> DEALLOC_COUNT
   1

"""
import doctest
import __main__
doctest.testmod(__main__, verbose=1)
