import unittest
from CoreFoundation import *

class TestCFBag (unittest.TestCase):
    def dont_testCreation(self):
        bag = CFBagCreate(None, [1,1,2,3,4], 5, kCFTypeBagCallBacks)
        self.assert_(isinstance(bag, CFBagRef))
        self.assertEquals(GetCountOfValue(bag, 1), 2)
        self.assertEquals(GetCountOfValue(bag, 3), 1)

        bag = CFBagCreateMutable(None, 0, kCFTypeBagCallbacks)
        self.assert_(isinstance(bag, CFBagRef))
        CFBagSetValue(bag, 9)
        CFBagSetValue(bag, 8)
        CFBagSetValue(bag, 9)
        self.assertEquals(GetCountOfValue(bag, 9), 2)
        self.assertEquals(GetCountOfValue(bag, 8), 1)
    
    def dont_testApplyFunction(self):
        items = []
        contexts = []

        bag = CFBagCreate(None, [1,1,2,3,4], 5, kCFTypeBagCallBacks)

        def func(item, context):
            items.append(item*item)
            contexts.append(context)

        CFBagApplyFunction(bag, func, 99)
        items.sort()
        self.assertEquals(items, [1,1,4,9,16])
        self.assertEquals(contexts, [99,99,99,99,99])

if __name__ == "__main__":
    unittest.main()
