"""
Some testcases for archiving basic python types.

Note that archiving isn't supported in the general case,
just for basic python types (dict, list, tuple, int, float)

XXX: this doesn't work correctly, both cyclic tests fail badly.
"""
import objc.test
import objc
import sys

NSObject = objc.lookUpClass('NSObject')
NSArchiver = objc.lookUpClass('NSArchiver')
NSUnarchiver = objc.lookUpClass('NSUnarchiver')
NSArray = objc.lookUpClass('NSArray')
NSDictionary = objc.lookUpClass('NSDictionary')

class TestArchivingPythonBasicTypes (objc.test.TestCase):
    def testFloat(self):
        for value in [-1.0, -42432.9, 5.4, 643e99, 1.0e180 * 1.0e180 ]:
            dt = NSArchiver.archivedDataWithRootObject_(value)
            self.assert_( dt is not None )

            newVal = NSUnarchiver.unarchiveObjectWithData_(dt)
            self.assert_( isinstance(newVal, float) )

            self.assertEquals(value, newVal)

    def testInt(self):
        if sys.maxint > 2 * 32:
            VALS = [sys.maxint,  -sys.maxint - 1, 5, 5325 ]
        else:
            VALS = [sys.maxint,  -sys.maxint - 1, sys.maxint + 10 , -sys.maxint - 20, 5, 5325 ]
        for value in VALS:
            dt = NSArchiver.archivedDataWithRootObject_(value)
            self.assert_( dt is not None )

            newVal = NSUnarchiver.unarchiveObjectWithData_(dt)

            self.assert_( isinstance(newVal, (int, long)) )

            self.assertEquals(value, newVal)

    def testStr(self):
        for value in [ 'aap', 'noot', '',  'mies' ]:
            dt = NSArchiver.archivedDataWithRootObject_(value)
            self.assert_( dt is not None )

            newVal = NSUnarchiver.unarchiveObjectWithData_(dt)
            self.assert_( isinstance(newVal, unicode) )
            self.assertEquals(value, newVal)

    def testUnicode(self):
        for value in [ u'aap', u'noot', u'',  u'mies', unichr(4000) ]:
            dt = NSArchiver.archivedDataWithRootObject_(value)
            self.assert_( dt is not None )

            newVal = NSUnarchiver.unarchiveObjectWithData_(dt)
            self.assert_( isinstance(newVal, unicode) )
            self.assertEquals(value, newVal)


    def testTuple(self):
        for value in [ (1,2,3), ('a', 4, 'd') ]:
            self.assertRaises(ValueError, NSArchiver.archivedDataWithRootObject_, value)
            """ These would be nice, but are non-trivial:
            dt = NSArchiver.archivedDataWithRootObject_(value)
            self.assert_( dt is not None )

            newVal = NSUnarchiver.unarchiveObjectWithData_(dt)
            self.assert_( isinstance(newVal, NSArray) )
            self.assertEquals(value, newVal)
            """

    def testList(self):
        for value in [ [1,2,3], ['a', 4, 'd'] ]:
            self.assertRaises(ValueError, NSArchiver.archivedDataWithRootObject_, value)
            """ These would be nice, but are non-trivial:
            dt = NSArchiver.archivedDataWithRootObject_(value)
            self.assert_( dt is not None )

            newVal = NSUnarchiver.unarchiveObjectWithData_(dt)
            self.assert_( isinstance(newVal, NSArray) )
            self.assertEquals(value, newVal)
            """

    def testDictionary(self):
        for value in [ dict(a='b', b=42), {1:99, 2:'a'} ]:
            self.assertRaises(ValueError, NSArchiver.archivedDataWithRootObject_, value)
            """ These would be nice, but are non-trivial:
            dt = NSArchiver.archivedDataWithRootObject_(value)
            self.assert_( dt is not None )

            newVal = NSUnarchiver.unarchiveObjectWithData_(dt)
            self.assert_( isinstance(newVal, NSDictionary) )
            self.assertEquals(value, newVal)
            """

    def testComplex(self):
        value = {
            'a': 99,
            'b': [1, 2, 3, 4],
            'c': { 1: 99, 2:44 },
            (1,2,3): ['a', {'b':'c'}, 99],
        }

        self.assertRaises(ValueError, NSArchiver.archivedDataWithRootObject_, value)
        """ These would be nice, but are non-trivial:

        dt = NSArchiver.archivedDataWithRootObject_(value)
        self.assert_( dt is not None )

        newVal = NSUnarchiver.unarchiveObjectWithData_(dt)
        self.assert_( isinstance(newVal, NSDictionary) )
        self.assertEquals(value, newVal)

        value = NSDictionary.dictionaryWithDictionary_({
                'a': NSArray.arrayWithArray_([{'a': 'b'}])
            })

        dt = NSArchiver.archivedDataWithRootObject_(value)
        self.assert_( dt is not None )

        newVal = NSUnarchiver.unarchiveObjectWithData_(dt)
        self.assert_( isinstance(newVal, NSDictionary) )
        self.assertEquals(value, newVal)
        """

    def testCyclicList(self):
        value = [ 1, 2 ]
        value.append(value)

        self.assertRaises(ValueError, NSArchiver.archivedDataWithRootObject_, value)
        """ These would be nice, but are non-trivial:
        dt = NSArchiver.archivedDataWithRootObject_([value])
        self.assert_( dt is not None )

        newVal = NSUnarchiver.unarchiveObjectWithData_(dt)
        self.assert_( isinstance(newVal, NSArray) )
        self.assertEquals(value, newVal)
        """

    def testCyclicDictionary(self):
        value = {'a': 'b'}
        value['c'] = value

        self.assertRaises(ValueError, NSArchiver.archivedDataWithRootObject_, value)
        """ These would be nice, but are non-trivial:
        dt = NSArchiver.archivedDataWithRootObject_(value)
        self.assert_( dt is not None )

        newVal = NSUnarchiver.unarchiveObjectWithData_(dt)
        self.assert_( isinstance(newVal, NSDictionary) )
        self.assertEquals(value, newVal)
        """



if __name__ == "__main__":
    objc.test.main()
