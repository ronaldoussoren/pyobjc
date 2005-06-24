#!/usr/bin/env python
"""
Script for checking if scanframeworks creates wrappers for at least as much
stuff as the old scripts.
"""
import sys

if len(sys.argv) != 3:
    print "Usage: diffWrappers.py Foundation.old Foundation.new"
    sys.exit(1)

old = __import__(sys.argv[1])
new = __import__(sys.argv[2])

for k, v_old in old.__dict__.iteritems():
    if not hasattr(new, k):
        print "In OLD but not in NEW: %s (%r)" % (k, v_old)
        continue

    v_new = getattr(new, k)

    if isinstance(v_old, (str, int, unicode)):
        if v_old != v_new:
            print v_new
            print "OLD != NEW for %s (%r != %r)" % (k, v_old, v_new)

    elif callable(v_old):
        if not callable(v_new):
            print "OLD is callable, NEW isn't for %s (%r, %r)" % (
                    k, v_old, v_new)

    elif callable(v_new):
        if not callable(v_old):
            print "OLD isn't callable, NEW is for %s (%r, %r)" % (
                    k, v_old, v_new)

    elif isinstance(v_old, (tuple, list)):
        if v_old != v_new:
            print "OLD != NEW for %s (%r != %r)"%(k, v_old, v_new)

    elif v_old is None:
        if v_new is not None:
            print "OLD != NEW for %s (%r != %r)"%(k, v_old, v_new)

    else:
        print "FIXME!", k, type(v_old), type(v_new)

for k, v in new.__dict__.iteritems():
    if k.startswith('_') and k.endswith('_encoded'):
        # Most likely '_SOMESTRUCT_encoded', these are introduced by 
        # the wrapper generator and are not interesting at all.
        continue

    if not hasattr(old, k):
        print "Not in OLD: %s (%r)" % (k, v)
