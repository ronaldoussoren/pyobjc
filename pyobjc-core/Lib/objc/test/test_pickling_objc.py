"""
Test cases for testing if it is possible to pickle
Objective-C objects
"""
import objc.test


# Test cases for pickling ObjC objects 
class TestPickleObjC (objc.test.TestCase):
    pass


# Test cases for pickling mixed Python/ObjC 
# object graphs
class TestPickleMixedGraph (objc.test.TestCase):
    pass


# Test cases for pickling Python subclasses
# of NSObject
class TestPicklePythonNSObject (objc.test.TestCase):
    pass

if __name__ == "__main__":
    objc.test.main()
