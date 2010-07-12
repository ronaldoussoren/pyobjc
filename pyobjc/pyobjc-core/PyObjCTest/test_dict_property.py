
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
            self.assertEquals(len(o.aDict), 0)
            self.assertEquals(o.aDict, {})
            self.assertEquals(len(observer.values), 0)

            o.aDict['key'] = 42
            self.assertEquals(len(observer.values), 0)

            observer.register(o, 'aDict.key')

            o.aDict['key'] = 43
            self.assertEquals(len(observer.values), 1)

            self.assertNotIn('indexes', observer.values[-1][-1])
            self.assertEquals(observer.values[-1][-1]['old'], 42)
            self.assertEquals(observer.values[-1][-1]['new'], 43)

            del o.aDict['key']

            self.assertEquals(len(observer.values), 2)
            self.assertNotIn('indexes', observer.values[-1][-1])
            self.assertEquals(observer.values[-1][-1]['old'], 43)
            self.assertEquals(observer.values[-1][-1]['new'], None)

        finally:
            observer.unregister(o, 'aDict')
            observer.unregister(o, 'aDict.key')

if __name__ == "__main__":
    main()
