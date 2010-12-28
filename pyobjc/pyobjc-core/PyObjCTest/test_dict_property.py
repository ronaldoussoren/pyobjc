
from PyObjCTools.TestSupport import *
from PyObjCTest.test_object_property import OCObserve
import objc

NSObject = objc.lookUpClass('NSObject')

class TestDictPropertyHelper (NSObject):
    aDict = objc.dict_property()

class TestDictProperty (TestCase):
    # objc.dict_property is currently just an object_property with a default value

    def testDefault(self):
        observer = OCObserve.alloc().init()

        o = TestDictPropertyHelper.alloc().init()
        observer.register(o, 'aDict')
        try:
            self.assertEqual(len(o.aDict), 0)
            self.assertEqual(o.aDict, {})
            self.assertEqual(len(observer.values), 0)

            o.aDict['key'] = 42
            self.assertEqual(len(observer.values), 0)

            observer.register(o, 'aDict.key')

            o.aDict['key'] = 43
            self.assertEqual(len(observer.values), 1)

            self.assertNotIn('indexes', observer.values[-1][-1])
            self.assertEqual(observer.values[-1][-1]['old'], 42)
            self.assertEqual(observer.values[-1][-1]['new'], 43)

            del o.aDict['key']

            self.assertEqual(len(observer.values), 2)
            self.assertNotIn('indexes', observer.values[-1][-1])
            self.assertEqual(observer.values[-1][-1]['old'], 43)
            self.assertEqual(observer.values[-1][-1]['new'], None)

        finally:
            observer.unregister(o, 'aDict')
            observer.unregister(o, 'aDict.key')

if __name__ == "__main__":
    main()
