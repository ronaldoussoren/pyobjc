
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

        cleanup = []
        try:
            self.assertEqual(len(o.aDict), 0)
            self.assertEqual(o.aDict, {})

            seen = { v[1]: v[2]['new'] for v in observer.values }
            self.assertEqual(seen, {'aDict': {}})

            o.aDict['key'] = 42
            seen = { v[1]: v[2]['new'] for v in observer.values }
            self.assertEqual(seen, {'aDict': { 'key': 42}})

            observer.register(o, 'aDict.key')
            cleanup.append(lambda: observer.unregister(o, 'aDict.key'))

            o.aDict['key'] = 43
            seen = { v[1]: v[2]['new'] for v in observer.values }
            self.assertEqual(seen, {'aDict': { 'key': 43}, 'aDict.key': 43})

            self.assertNotIn('indexes', observer.values[-1][-1])
            self.assertEqual(observer.values[-1][-1]['old'], 42)
            self.assertEqual(observer.values[-1][-1]['new'], 43)

            del o.aDict['key']

            seen = { v[1]: v[2]['new'] for v in observer.values }
            self.assertEqual(seen, {'aDict': {}, 'aDict.key': None})
            self.assertNotIn('indexes', observer.values[-1][-1])
            self.assertEqual(observer.values[-1][-1]['old'], 43)
            self.assertEqual(observer.values[-1][-1]['new'], None)

        finally:
            observer.unregister(o, 'aDict')
            for func in cleanup[::-1]:
                func()

if __name__ == "__main__":
    main()
