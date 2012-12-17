from PyObjCTools.TestSupport import *

import objc
import sys

try:
    from  Foundation import NSRange

    _C_NSRange = NSRange.__typestr__

except ImportError:
    if sys.maxsize > 2 ** 32:
        _C_NSRange = b"{_NSRange=QQ}"
    else:
        _C_NSRange = b"{_NSRange=II}"


NSObject = objc.lookUpClass("NSObject")

class TestBasicDescriptors (TestCase):

    # IBOutlet is tested in test_ivar

    def test_ibaction(self):

        @objc.IBAction
        def myAction_(self, sender):
            return 1

        self.assertIsInstance(myAction_, objc.selector)
        self.assertEqual(myAction_.signature, b'v@:@')
        self.assertEqual(myAction_.selector, b'myAction:')
        self.assertFalse(myAction_.isClassMethod)


        self.assertRaises(TypeError, objc.IBAction, None)
        self.assertRaises(TypeError, objc.IBAction, 42)

    def test_instancemethod(self):
        class TestDescriptorsClass1 (NSObject):
            @objc.instancemethod
            def new(self):
                pass

        o = NSObject.alloc().init()
        self.assertFalse(hasattr(o, 'new'))
        self.assertTrue(hasattr(NSObject, 'new'))
        self.assertTrue(NSObject.new.isClassMethod)

        o = TestDescriptorsClass1.alloc().init()
        m = o.new
        self.assertIsInstance(m, objc.selector)
        self.assertFalse(m.isClassMethod)


        self.assertRaises(TypeError, objc.instancemethod, None)
        self.assertRaises(TypeError, objc.instancemethod, 42)

    def test_typedSelector(self):

        @objc.typedSelector(b"I@:qq")
        def mySelector_arg_(self, a, b):
            return 4

        self.assertIsInstance(mySelector_arg_, objc.selector)
        self.assertEqual(mySelector_arg_.signature, b"I@:qq")
        self.assertEqual(mySelector_arg_.selector, b"mySelector:arg:")

        self.assertRaises(TypeError, objc.typedSelector(b"v@:i"), None)
        self.assertRaises(TypeError, objc.typedSelector(b"v@:i"), 42)

    def testNamedSelector(self):
        @objc.namedSelector(b'foo:bar:')
        def mymethod(self, a, b):
            pass

        self.assertIsInstance(mymethod, objc.selector)
        self.assertEqual(mymethod.signature, b"v@:@@")
        self.assertEqual(mymethod.selector, b"foo:bar:")

        self.assertRaises(TypeError, objc.namedSelector(b"foo:bar:"), None)
        self.assertRaises(TypeError, objc.namedSelector(b"foo:bar:"), 42)

        @objc.namedSelector(b'foo:bar:', signature=b"q@:qq")
        def mymethod(self, a, b):
            pass

        self.assertIsInstance(mymethod, objc.selector)
        self.assertEqual(mymethod.signature, b"q@:qq")
        self.assertEqual(mymethod.selector, b"foo:bar:")

        self.assertRaises(TypeError, objc.namedSelector(b"foo:bar:", b"q@:qq"), None)
        self.assertRaises(TypeError, objc.namedSelector(b"foo:bar:", b"q@:qq"), 42)

    def testNamedselector(self):
        with filterWarnings("ignore", RuntimeWarning):
            @objc.namedselector(b'foo:bar:')
            def mymethod(self, a, b):
                pass

            self.assertIsInstance(mymethod, objc.selector)
            self.assertEqual(mymethod.signature, b"v@:@@")
            self.assertEqual(mymethod.selector, b"foo:bar:")

            self.assertRaises(TypeError, objc.namedselector(b"foo:bar:"), None)
            self.assertRaises(TypeError, objc.namedselector(b"foo:bar:"), 42)

            @objc.namedselector(b'foo:bar:', signature=b"q@:qq")
            def mymethod(self, a, b):
                pass

            self.assertIsInstance(mymethod, objc.selector)
            self.assertEqual(mymethod.signature, b"q@:qq")
            self.assertEqual(mymethod.selector, b"foo:bar:")

            self.assertRaises(TypeError, objc.namedselector(b"foo:bar:", b"q@:qq"), None)
            self.assertRaises(TypeError, objc.namedselector(b"foo:bar:", b"q@:qq"), 42)

    # synthesize is tested in test_synthesize

    def test_accessor(self):
        # NOTE: the optional type argument is tested through the typedAccessor function

        # Basic properties:

        @objc.accessor
        def color(self):
            return 42

        @objc.accessor
        def isColor(self):
            return 42

        @objc.accessor
        def setColor_(self, value):
            pass

        self.assertIsInstance(color, objc.selector)
        self.assertIsInstance(isColor, objc.selector)
        self.assertIsInstance(setColor_, objc.selector)

        self.assertEqual(color.signature, b"@@:")
        self.assertEqual(isColor.signature, b"@@:")
        self.assertEqual(setColor_.signature, b"v@:@")


        # Indexed accessors

        @objc.accessor
        def countOfFlavors(self):
            return 2

        @objc.accessor
        def objectInFlavorsAtIndex_(self, idx):
            return "sour"

        @objc.accessor
        def flavorsAtIndexes_(sef, indices):
            return ["sour", "sweet"]

        @objc.accessor
        def getFlavors_range_(self, buffer, range):
            return ["sour", "sweet"]


        self.assertIsInstance(countOfFlavors, objc.selector)
        self.assertIsInstance(objectInFlavorsAtIndex_, objc.selector)
        self.assertIsInstance(flavorsAtIndexes_, objc.selector)
        self.assertIsInstance(getFlavors_range_, objc.selector)

        self.assertEqual(countOfFlavors.signature, objc._C_NSUInteger + b"@:")
        self.assertEqual(objectInFlavorsAtIndex_.signature, b"@@:" + objc._C_NSUInteger)
        self.assertEqual(flavorsAtIndexes_.signature, b"@@:@")

        # XXX: This needs even more work: also have to add custom metadata!
        self.assertEqual(getFlavors_range_.signature, b"v@:o^@" + _C_NSRange)

        # Mutable Indexed Accessors

        @objc.accessor
        def insertObject_inFlavorsAtIndex_(self, value, idx):
            pass

        @objc.accessor
        def insertFlavors_atIndexes_(self, values, indices):
            pass

        @objc.accessor
        def removeObjectFromFlavorsAtIndex_(self, index):
            pass

        @objc.accessor
        def removeFlavorsAtIndexes_(self, indices):
            pass

        @objc.accessor
        def replaceObjectInFlavorsAtIndex_withObject_(self, value, idx):
            pass

        @objc.accessor
        def replaceFlavorsAtIndexes_withFlavors_(self, indices, values):
            pass


        self.assertIsInstance(insertObject_inFlavorsAtIndex_, objc.selector)
        self.assertIsInstance(insertFlavors_atIndexes_, objc.selector)
        self.assertIsInstance(removeObjectFromFlavorsAtIndex_, objc.selector)
        self.assertIsInstance(removeFlavorsAtIndexes_, objc.selector)
        self.assertIsInstance(replaceObjectInFlavorsAtIndex_withObject_, objc.selector)
        self.assertIsInstance(replaceFlavorsAtIndexes_withFlavors_, objc.selector)

        self.assertEqual(insertObject_inFlavorsAtIndex_.signature, b"v@:@" + objc._C_NSUInteger)
        self.assertEqual(insertFlavors_atIndexes_.signature, b"v@:@@")
        self.assertEqual(removeObjectFromFlavorsAtIndex_.signature, b"v@:" + objc._C_NSUInteger)
        self.assertEqual(removeFlavorsAtIndexes_.signature, b"v@:@")
        self.assertEqual(replaceObjectInFlavorsAtIndex_withObject_.signature, b"v@:" + objc._C_NSUInteger + b"@")
        self.assertEqual(replaceFlavorsAtIndexes_withFlavors_.signature, b"v@:@@")


        # Getter Unordered Accessors
        @objc.accessor
        def countOfLanguages(self):
            pass

        @objc.accessor
        def enumeratorOfLanguages(self):
            pass

        @objc.accessor
        def memberOfLanguages_(self, value):
            return False

        self.assertIsInstance(countOfLanguages, objc.selector)
        self.assertIsInstance(enumeratorOfLanguages, objc.selector)
        self.assertIsInstance(memberOfLanguages_, objc.selector)

        self.assertEqual(countOfLanguages.signature, objc._C_NSUInteger + b"@:")
        self.assertEqual(enumeratorOfLanguages.signature, b"@@:")
        self.assertEqual(memberOfLanguages_.signature, objc._C_NSBOOL + b"@:@")

        # Mutable Unordered Accessors

        @objc.accessor
        def addLanguagesObject_(self, value):
            pass

        @objc.accessor
        def addLanguagues_(self, values):
            pass

        @objc.accessor
        def intersectLanguagues_(self, values):
            pass

        self.assertIsInstance(addLanguagesObject_, objc.selector)
        self.assertIsInstance(addLanguagues_, objc.selector)
        self.assertIsInstance(intersectLanguagues_, objc.selector)

        self.assertEqual(addLanguagesObject_.signature, b"v@:@")
        self.assertEqual(addLanguagues_.signature, b"v@:@")
        self.assertEqual(intersectLanguagues_.signature, b"v@:@")

        # Validation
        @objc.accessor
        def validateColor_error_(self, value, error):
            return (False, None)

        self.assertIsInstance(validateColor_error_, objc.selector)
        self.assertEqual(validateColor_error_.signature, objc._C_NSBOOL + b'@:N^@o^@')



        # Keyword arguments (**kwds) and varargs (*args) are
        # not supported:

        def attrib(self, *args):
            pass
        self.assertRaises(TypeError, objc.accessor, attrib)

        def attrib(self, **kwds):
            pass
        self.assertRaises(TypeError, objc.accessor, attrib)

        # Not really an accessor
        def attrib_error_(self, a, b):
            pass
        self.assertRaises(TypeError, objc.accessor, attrib_error_)

        # Argument counts that don't match
        def validateObject_error_(self, a):
            pass
        self.assertRaises(TypeError, objc.accessor, validateObject_error_)

        def validateObject_error_(self, a, b, c):
            pass
        self.assertRaises(TypeError, objc.accessor, validateObject_error_)

        def validateObject_error_(self, a, b, c, d=1, e=2):
            pass
        self.assertRaises(TypeError, objc.accessor, validateObject_error_)

        @objc.accessor
        def validateObject_error_(self, a, b, c=1):
            pass




    def test_typedAccessor(self):
        # NOTE: the optional type argument is tested through the typedAccessor function

        # Basic properties:

        mytype = b"{Struct=qq}"

        @objc.typedAccessor(mytype)
        def color(self):
            return 42

        @objc.typedAccessor(mytype)
        def isColor(self):
            return 42

        @objc.typedAccessor(mytype)
        def setColor_(self, value):
            pass

        self.assertIsInstance(color, objc.selector)
        self.assertIsInstance(isColor, objc.selector)
        self.assertIsInstance(setColor_, objc.selector)

        self.assertEqual(color.signature, mytype + b"@:")
        self.assertEqual(isColor.signature, mytype + b"@:")
        self.assertEqual(setColor_.signature, b"v@:" + mytype)


        # Indexed accessors

        @objc.typedAccessor(mytype)
        def countOfFlavors(self):
            return 2

        @objc.typedAccessor(mytype)
        def objectInFlavorsAtIndex_(self, idx):
            return "sour"

        @objc.typedAccessor(mytype)
        def flavorsAtIndexes_(sef, indices):
            return ["sour", "sweet"]

        @objc.typedAccessor(mytype)
        def getFlavors_range_(self, buffer, range):
            return ["sour", "sweet"]


        self.assertIsInstance(countOfFlavors, objc.selector)
        self.assertIsInstance(objectInFlavorsAtIndex_, objc.selector)
        self.assertIsInstance(flavorsAtIndexes_, objc.selector)
        self.assertIsInstance(getFlavors_range_, objc.selector)

        self.assertEqual(countOfFlavors.signature, objc._C_NSUInteger + b"@:")
        self.assertEqual(objectInFlavorsAtIndex_.signature, mytype + b"@:" + objc._C_NSUInteger)
        self.assertEqual(flavorsAtIndexes_.signature, b"@@:@") #XXX: is this correct?

        # XXX: This needs even more work: also have to add custom metadata!
        self.assertEqual(getFlavors_range_.signature, b"v@:o^@" + _C_NSRange)

        # Mutable Indexed Accessors

        @objc.typedAccessor(mytype)
        def insertObject_inFlavorsAtIndex_(self, value, idx):
            pass

        @objc.typedAccessor(mytype)
        def insertFlavors_atIndexes_(self, values, indices):
            pass

        @objc.typedAccessor(mytype)
        def removeObjectFromFlavorsAtIndex_(self, index):
            pass

        @objc.typedAccessor(mytype)
        def removeFlavorsAtIndexes_(self, indices):
            pass

        @objc.typedAccessor(mytype)
        def replaceObjectInFlavorsAtIndex_withObject_(self, value, idx):
            pass

        @objc.typedAccessor(mytype)
        def replaceFlavorsAtIndexes_withFlavors_(self, indices, values):
            pass


        self.assertIsInstance(insertObject_inFlavorsAtIndex_, objc.selector)
        self.assertIsInstance(insertFlavors_atIndexes_, objc.selector)
        self.assertIsInstance(removeObjectFromFlavorsAtIndex_, objc.selector)
        self.assertIsInstance(removeFlavorsAtIndexes_, objc.selector)
        self.assertIsInstance(replaceObjectInFlavorsAtIndex_withObject_, objc.selector)
        self.assertIsInstance(replaceFlavorsAtIndexes_withFlavors_, objc.selector)

        self.assertEqual(insertObject_inFlavorsAtIndex_.signature, b"v@:" + mytype + objc._C_NSUInteger)
        self.assertEqual(insertFlavors_atIndexes_.signature, b"v@:@@") # XXX: is this correct?
        self.assertEqual(removeObjectFromFlavorsAtIndex_.signature, b"v@:" + objc._C_NSUInteger)
        self.assertEqual(removeFlavorsAtIndexes_.signature, b"v@:@")
        self.assertEqual(replaceObjectInFlavorsAtIndex_withObject_.signature, b"v@:" + objc._C_NSUInteger + mytype)
        self.assertEqual(replaceFlavorsAtIndexes_withFlavors_.signature, b"v@:@@") # XXX: is this correct?


        # Getter Unordered Accessors
        @objc.typedAccessor(mytype)
        def countOfLanguages(self):
            pass

        @objc.typedAccessor(mytype)
        def enumeratorOfLanguages(self):
            pass

        @objc.typedAccessor(mytype)
        def memberOfLanguages_(self, value):
            return False

        self.assertIsInstance(countOfLanguages, objc.selector)
        self.assertIsInstance(enumeratorOfLanguages, objc.selector)
        self.assertIsInstance(memberOfLanguages_, objc.selector)

        self.assertEqual(countOfLanguages.signature, objc._C_NSUInteger + b"@:")
        self.assertEqual(enumeratorOfLanguages.signature, b"@@:")
        self.assertEqual(memberOfLanguages_.signature, objc._C_NSBOOL + b"@:" + mytype)

        # Mutable Unordered Accessors

        @objc.typedAccessor(mytype)
        def addLanguagesObject_(self, value):
            pass

        @objc.typedAccessor(mytype)
        def addLanguagues_(self, values):
            pass

        @objc.typedAccessor(mytype)
        def intersectLanguagues_(self, values):
            pass

        self.assertIsInstance(addLanguagesObject_, objc.selector)
        self.assertIsInstance(addLanguagues_, objc.selector)
        self.assertIsInstance(intersectLanguagues_, objc.selector)

        self.assertEqual(addLanguagesObject_.signature, b"v@:" + mytype)
        self.assertEqual(addLanguagues_.signature, b"v@:@") # XXX: is this correct?
        self.assertEqual(intersectLanguagues_.signature, b"v@:@")

        # Validation
        @objc.typedAccessor(mytype)
        def validateColor_error_(self, value, error):
            return (False, None)

        self.assertIsInstance(validateColor_error_, objc.selector)
        self.assertEqual(validateColor_error_.signature, objc._C_NSBOOL + b'@:N^@o^@')

    def test_Accessor(self):
        with filterWarnings("ignore", DeprecationWarning):
            # NOTE: the optional type argument is tested through the typedAccessor function

            # Basic properties:

            @objc.Accessor
            def color(self):
                return 42

            @objc.Accessor
            def isColor(self):
                return 42

            @objc.Accessor
            def setColor_(self, value):
                pass

            self.assertIsInstance(color, objc.selector)
            self.assertIsInstance(isColor, objc.selector)
            self.assertIsInstance(setColor_, objc.selector)

            self.assertEqual(color.signature, b"@@:")
            self.assertEqual(isColor.signature, b"@@:")
            self.assertEqual(setColor_.signature, b"v@:@")


            # Indexed accessors

            @objc.Accessor
            def countOfFlavors(self):
                return 2

            @objc.Accessor
            def objectInFlavorsAtIndex_(self, idx):
                return "sour"

            @objc.Accessor
            def flavorsAtIndexes_(sef, indices):
                return ["sour", "sweet"]

            @objc.Accessor
            def getFlavors_range_(self, buffer, range):
                return ["sour", "sweet"]


            self.assertIsInstance(countOfFlavors, objc.selector)
            self.assertIsInstance(objectInFlavorsAtIndex_, objc.selector)
            self.assertIsInstance(flavorsAtIndexes_, objc.selector)
            self.assertIsInstance(getFlavors_range_, objc.selector)

            self.assertEqual(countOfFlavors.signature, objc._C_NSUInteger + b"@:")
            self.assertEqual(objectInFlavorsAtIndex_.signature, b"@@:" + objc._C_NSUInteger)
            self.assertEqual(flavorsAtIndexes_.signature, b"@@:@")

            # XXX: This needs even more work: also have to add custom metadata!
            self.assertEqual(getFlavors_range_.signature, b"v@:o^@" + _C_NSRange)

            # Mutable Indexed Accessors

            @objc.Accessor
            def insertObject_inFlavorsAtIndex_(self, value, idx):
                pass

            @objc.Accessor
            def insertFlavors_atIndexes_(self, values, indices):
                pass

            @objc.Accessor
            def removeObjectFromFlavorsAtIndex_(self, index):
                pass

            @objc.Accessor
            def removeFlavorsAtIndexes_(self, indices):
                pass

            @objc.Accessor
            def replaceObjectInFlavorsAtIndex_withObject_(self, value, idx):
                pass

            @objc.Accessor
            def replaceFlavorsAtIndexes_withFlavors_(self, indices, values):
                pass


            self.assertIsInstance(insertObject_inFlavorsAtIndex_, objc.selector)
            self.assertIsInstance(insertFlavors_atIndexes_, objc.selector)
            self.assertIsInstance(removeObjectFromFlavorsAtIndex_, objc.selector)
            self.assertIsInstance(removeFlavorsAtIndexes_, objc.selector)
            self.assertIsInstance(replaceObjectInFlavorsAtIndex_withObject_, objc.selector)
            self.assertIsInstance(replaceFlavorsAtIndexes_withFlavors_, objc.selector)

            self.assertEqual(insertObject_inFlavorsAtIndex_.signature, b"v@:@" + objc._C_NSUInteger)
            self.assertEqual(insertFlavors_atIndexes_.signature, b"v@:@@")
            self.assertEqual(removeObjectFromFlavorsAtIndex_.signature, b"v@:" + objc._C_NSUInteger)
            self.assertEqual(removeFlavorsAtIndexes_.signature, b"v@:@")
            self.assertEqual(replaceObjectInFlavorsAtIndex_withObject_.signature, b"v@:" + objc._C_NSUInteger + b"@")
            self.assertEqual(replaceFlavorsAtIndexes_withFlavors_.signature, b"v@:@@")


            # Getter Unordered Accessors
            @objc.Accessor
            def countOfLanguages(self):
                pass

            @objc.Accessor
            def enumeratorOfLanguages(self):
                pass

            @objc.Accessor
            def memberOfLanguages_(self, value):
                return False

            self.assertIsInstance(countOfLanguages, objc.selector)
            self.assertIsInstance(enumeratorOfLanguages, objc.selector)
            self.assertIsInstance(memberOfLanguages_, objc.selector)

            self.assertEqual(countOfLanguages.signature, objc._C_NSUInteger + b"@:")
            self.assertEqual(enumeratorOfLanguages.signature, b"@@:")
            self.assertEqual(memberOfLanguages_.signature, objc._C_NSBOOL + b"@:@")

            # Mutable Unordered Accessors

            @objc.Accessor
            def addLanguagesObject_(self, value):
                pass

            @objc.Accessor
            def addLanguagues_(self, values):
                pass

            @objc.Accessor
            def intersectLanguagues_(self, values):
                pass

            self.assertIsInstance(addLanguagesObject_, objc.selector)
            self.assertIsInstance(addLanguagues_, objc.selector)
            self.assertIsInstance(intersectLanguagues_, objc.selector)

            self.assertEqual(addLanguagesObject_.signature, b"v@:@")
            self.assertEqual(addLanguagues_.signature, b"v@:@")
            self.assertEqual(intersectLanguagues_.signature, b"v@:@")

            # Validation
            @objc.Accessor
            def validateColor_error_(self, value, error):
                return (False, None)

            self.assertIsInstance(validateColor_error_, objc.selector)
            self.assertEqual(validateColor_error_.signature, objc._C_NSBOOL + b'@:N^@o^@')



            # Keyword arguments (**kwds) and varargs (*args) are
            # not supported:

            def attrib(self, *args):
                pass
            self.assertRaises(TypeError, objc.Accessor, attrib)

            def attrib(self, **kwds):
                pass
            self.assertRaises(TypeError, objc.Accessor, attrib)

            # Not really an accessor
            def attrib_error_(self, a, b):
                pass
            self.assertRaises(TypeError, objc.Accessor, attrib_error_)

            # Argument counts that don't match
            def validateObject_error_(self, a):
                pass
            self.assertRaises(TypeError, objc.Accessor, validateObject_error_)

            def validateObject_error_(self, a, b, c):
                pass
            self.assertRaises(TypeError, objc.Accessor, validateObject_error_)

            def validateObject_error_(self, a, b, c, d=1, e=2):
                pass
            self.assertRaises(TypeError, objc.Accessor, validateObject_error_)

            @objc.Accessor
            def validateObject_error_(self, a, b, c=1):
                pass

    def test_signature(self):

        @objc.signature(b"d@:ii")
        def myMethod_arg_(self, a, b):
            pass

        self.assertIsInstance(myMethod_arg_, objc.selector)
        self.assertEqual(myMethod_arg_.signature, b'd@:ii')
        self.assertEqual(myMethod_arg_.selector, b'myMethod:arg:')

        @objc.signature(b'q@:@q', selector=b'foo:bar:')
        def method(self, a, b):
            pass

        self.assertIsInstance(method, objc.selector)
        self.assertEqual(method.signature, b'q@:@q')
        self.assertEqual(method.selector, b'foo:bar:')







if __name__ == "__main__":
    main()
