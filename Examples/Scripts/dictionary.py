#!/usr/bin/env python
# This is a doctest
"""
==============================
Using Cocoa collection classes
==============================

Cocoa contains a number of collection classes, including dictionaries and
arrays (like python lists) in mutable and immutable variations. We'll 
demonstrate their usage using the ``NSMutableDictonary`` class.

We'll start by importing everything we need::

    >>> from Foundation import *

Then create an empty dictionary::

    >>> d = NSMutableDictionary.dictionary()
    >>> d
    {}
    >>> isinstance(d, dict)
    False
    >>> isinstance(d, NSMutableDictionary)
    True

You can add a new value using the Objective-C API::

    >>> d.setObject_forKey_(42, 'key2')
    >>> d
    {key2 = 42; }

But can also use the familiar python interface:

    >>> d['key1'] = u'hello'
    >>> d
    {key1 = hello; key2 = 42; }

The same is true for fetching elements::

    >>> d['key2']
    42
    >>> d.objectForKey_('key1')
    u'hello'
"""
import doctest
import __main__
doctest.testmod(__main__, verbose=1)
