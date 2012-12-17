"""
Test cases for testing if it is possible to pickle
Objective-C objects
"""
from PyObjCTools.TestSupport import *


# Test cases for pickling ObjC objects
class TestPickleObjC (TestCase):
    pass


# Test cases for pickling mixed Python/ObjC
# object graphs
class TestPickleMixedGraph (TestCase):
    pass


# Test cases for pickling Python subclasses
# of NSObject
class TestPicklePythonNSObject (TestCase):
    pass

if __name__ == "__main__":
    main()
