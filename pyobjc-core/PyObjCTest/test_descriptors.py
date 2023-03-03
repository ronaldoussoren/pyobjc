import warnings

import objc
from PyObjCTools.TestSupport import TestCase

_C_NSRange = b"{_NSRange=QQ}"


NSObject = objc.lookUpClass("NSObject")


class TestBasicDescriptors(TestCase):
    # IBOutlet is tested in test_ivar

    def test_IB_DESIGNABLE(self):
        @objc.IB_DESIGNABLE
        class Foo:
            pass

        self.assertIsInstance(Foo, type)

        v = 99999
        self.assertIs(objc.IB_DESIGNABLE(v), v)

    def test_IBInspectable(self):
        v = 99999
        self.assertIs(objc.IBInspectable(v), v)

    def test_ibaction(self):
        @objc.IBAction
        def myAction_(self, sender):
            return 1

        self.assertIsInstance(myAction_, objc.selector)
        self.assertEqual(myAction_.signature, b"v@:@")
        self.assertEqual(myAction_.selector, b"myAction:")
        self.assertFalse(myAction_.isClassMethod)

        # First is from 'IBAction', second is from 'selector'
        with self.assertRaisesRegex(TypeError, "IBAction argument must be a callable"):
            objc.IBAction(None)
        with self.assertRaisesRegex(TypeError, "argument 'method' must be callable"):
            objc.IBAction(42)

    def test_instancemethod(self):
        class TestDescriptorsClass1(NSObject):
            @objc.instancemethod
            def new(self):
                pass

        o = NSObject.alloc().init()
        self.assertFalse(hasattr(o, "new"))
        self.assertTrue(hasattr(NSObject, "new"))
        self.assertTrue(NSObject.new.isClassMethod)

        o = TestDescriptorsClass1.alloc().init()
        m = o.new
        self.assertIsInstance(m, objc.selector)
        self.assertFalse(m.isClassMethod)

        with self.assertRaisesRegex(
            TypeError, "instancemethod argument must be a callable"
        ):
            objc.instancemethod(None)
        with self.assertRaisesRegex(TypeError, "argument 'method' must be callable"):
            objc.instancemethod(42)

    def test_typedSelector(self):
        @objc.typedSelector(b"I@:qq")
        def mySelector_arg_(self, a, b):
            return 4

        @objc.typedSelector(b"q@:i")
        @classmethod
        def mySelector_(self, a):
            return 4

        self.assertIsInstance(mySelector_arg_, objc.selector)
        self.assertEqual(mySelector_arg_.signature, b"I@:qq")
        self.assertEqual(mySelector_arg_.selector, b"mySelector:arg:")
        self.assertFalse(mySelector_arg_.isClassMethod)

        self.assertIsInstance(mySelector_, objc.selector)
        self.assertEqual(mySelector_.signature, b"q@:i")
        self.assertEqual(mySelector_.selector, b"mySelector:")
        self.assertTrue(mySelector_.isClassMethod)

        with self.assertRaisesRegex(
            TypeError, r"typedSelector\(\) function argument must be a callable"
        ):
            objc.typedSelector(b"v@:i")(None)

        with self.assertRaisesRegex(TypeError, "argument 'method' must be callable"):
            objc.typedSelector(b"v@:i")(42)

        with self.assertRaisesRegex(ValueError, "invalid signature"):
            objc.typedSelector(b"v@:!")(lambda self, a: 42)

    def testNamedSelector(self):
        @objc.namedSelector(b"foo:bar:")
        def mymethod(self, a, b):
            pass

        @objc.namedSelector(b"foo:bar:")
        @classmethod
        def mymethod2(self, a, b):
            pass

        @objc.namedSelector(b"foo:bar:", signature=b"I@:qq")
        def mymethod3(self, a, b):
            pass

        @objc.namedSelector(b"foo:bar:", signature=b"I@:qq")
        @classmethod
        def mymethod4(self, a, b):
            pass

        self.assertIsInstance(mymethod, objc.selector)
        self.assertEqual(mymethod.signature, b"v@:@@")
        self.assertEqual(mymethod.selector, b"foo:bar:")
        self.assertFalse(mymethod.isClassMethod)

        self.assertIsInstance(mymethod2, objc.selector)
        self.assertEqual(mymethod2.signature, b"v@:@@")
        self.assertEqual(mymethod2.selector, b"foo:bar:")
        self.assertTrue(mymethod2.isClassMethod)

        self.assertIsInstance(mymethod3, objc.selector)
        self.assertEqual(mymethod3.signature, b"I@:qq")
        self.assertEqual(mymethod3.selector, b"foo:bar:")
        self.assertFalse(mymethod3.isClassMethod)

        self.assertIsInstance(mymethod4, objc.selector)
        self.assertEqual(mymethod4.signature, b"I@:qq")
        self.assertEqual(mymethod4.selector, b"foo:bar:")
        self.assertTrue(mymethod4.isClassMethod)

        with self.assertRaisesRegex(
            TypeError, "namedSelector argument must be a callable"
        ):
            objc.namedSelector(b"foo:bar:")(None)
        with self.assertRaisesRegex(TypeError, "argument 'method' must be callable"):
            objc.namedSelector(b"foo:bar:")(42)

        @objc.namedSelector(b"foo:bar:", signature=b"q@:qq")
        def mymethod(self, a, b):
            pass

        self.assertIsInstance(mymethod, objc.selector)
        self.assertEqual(mymethod.signature, b"q@:qq")
        self.assertEqual(mymethod.selector, b"foo:bar:")

        with self.assertRaisesRegex(
            TypeError, "namedSelector argument must be a callable"
        ):
            objc.namedSelector(b"foo:bar:", b"q@:qq")(None)
        with self.assertRaisesRegex(TypeError, "argument 'method' must be callable"):
            objc.namedSelector(b"foo:bar:", b"q@:qq")(42)

    def testNamedselector(self):
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)

            @objc.namedselector(b"foo:bar:")
            def mymethod(self, a, b):
                pass

            self.assertIsInstance(mymethod, objc.selector)
            self.assertEqual(mymethod.signature, b"v@:@@")
            self.assertEqual(mymethod.selector, b"foo:bar:")

            with self.assertRaisesRegex(
                TypeError, "namedSelector argument must be a callable"
            ):
                objc.namedselector(b"foo:bar:")(None)
            with self.assertRaisesRegex(
                TypeError, "argument 'method' must be callable"
            ):
                objc.namedselector(b"foo:bar:")(42)

            @objc.namedselector(b"foo:bar:", signature=b"q@:qq")
            def mymethod(self, a, b):
                pass

            self.assertIsInstance(mymethod, objc.selector)
            self.assertEqual(mymethod.signature, b"q@:qq")
            self.assertEqual(mymethod.selector, b"foo:bar:")

            with self.assertRaisesRegex(
                TypeError, "namedSelector argument must be a callable"
            ):
                objc.namedselector(b"foo:bar:", b"q@:qq")(None)
            with self.assertRaisesRegex(
                TypeError, "argument 'method' must be callable"
            ):
                objc.namedselector(b"foo:bar:", b"q@:qq")(42)

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
        def getFlavors_range_(self, bfr, rng):
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

        self.assertEqual(
            insertObject_inFlavorsAtIndex_.signature, b"v@:@" + objc._C_NSUInteger
        )
        self.assertEqual(insertFlavors_atIndexes_.signature, b"v@:@@")
        self.assertEqual(
            removeObjectFromFlavorsAtIndex_.signature, b"v@:" + objc._C_NSUInteger
        )
        self.assertEqual(removeFlavorsAtIndexes_.signature, b"v@:@")
        self.assertEqual(
            replaceObjectInFlavorsAtIndex_withObject_.signature,
            b"v@:" + objc._C_NSUInteger + b"@",
        )
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
        self.assertEqual(validateColor_error_.signature, objc._C_NSBOOL + b"@:N^@o^@")

        # Keyword arguments (**kwds) and varargs (*args) are
        # not supported:

        def attrib(self, *args):
            pass

        with self.assertRaisesRegex(
            TypeError,
            "attrib can not be an accessor because it accepts varargs, varkw or kwonly",
        ):
            objc.accessor(attrib)

        def attrib(self, **kwds):
            pass

        with self.assertRaisesRegex(
            TypeError,
            "attrib can not be an accessor because it accepts varargs, varkw or kwonly",
        ):
            objc.accessor(attrib)

        # Not really an accessor
        def attrib_error_(self, a, b):
            pass

        with self.assertRaisesRegex(
            TypeError, "attrib_error_ not recognized as an accessor"
        ):
            objc.accessor(attrib_error_)

        # Argument counts that don't match
        def validateObject_error_(self, a):
            pass

        with self.assertRaisesRegex(
            TypeError,
            r"validateObject_error_ expected to take 2 args, but must accept 3 "
            r"from Objective-C \(implicit self plus count of underscores\)",
        ):
            objc.accessor(validateObject_error_)

        def validateObject_error_(self, a, b, c):
            pass

        with self.assertRaisesRegex(
            TypeError,
            r"validateObject_error_ expected to take 4 args, but must accept "
            r"3 from Objective-C \(implicit self plus count of underscores\)",
        ):
            objc.accessor(validateObject_error_)

        def validateObject_error_(self, a, b, c, d=1, e=2):
            pass

        with self.assertRaisesRegex(
            TypeError,
            r"validateObject_error_ expected to take between 4 and 6 args, but "
            r"must accept 3 from Objective-C \(implicit self plus count of underscores\)",
        ):
            objc.accessor(validateObject_error_)

        @objc.accessor
        def validateObject_error_(self, a, b, c=1):
            pass

        def countOfFoo_withBar_withBaz_withNone_(self, foo, bar, baz, none):
            pass

        with self.assertRaisesRegex(
            TypeError,
            "countOfFoo_withBar_withBaz_withNone_ not recognized as an accessor",
        ):
            objc.accessor(countOfFoo_withBar_withBaz_withNone_)

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
        def getFlavors_range_(self, bfr, rng):
            return ["sour", "sweet"]

        self.assertIsInstance(countOfFlavors, objc.selector)
        self.assertIsInstance(objectInFlavorsAtIndex_, objc.selector)
        self.assertIsInstance(flavorsAtIndexes_, objc.selector)
        self.assertIsInstance(getFlavors_range_, objc.selector)

        self.assertEqual(countOfFlavors.signature, objc._C_NSUInteger + b"@:")
        self.assertEqual(
            objectInFlavorsAtIndex_.signature, mytype + b"@:" + objc._C_NSUInteger
        )
        self.assertEqual(flavorsAtIndexes_.signature, b"@@:@")  # XXX: is this correct?

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

        self.assertEqual(
            insertObject_inFlavorsAtIndex_.signature,
            b"v@:" + mytype + objc._C_NSUInteger,
        )
        self.assertEqual(
            insertFlavors_atIndexes_.signature, b"v@:@@"
        )  # XXX: is this correct?
        self.assertEqual(
            removeObjectFromFlavorsAtIndex_.signature, b"v@:" + objc._C_NSUInteger
        )
        self.assertEqual(removeFlavorsAtIndexes_.signature, b"v@:@")
        self.assertEqual(
            replaceObjectInFlavorsAtIndex_withObject_.signature,
            b"v@:" + objc._C_NSUInteger + mytype,
        )
        self.assertEqual(
            replaceFlavorsAtIndexes_withFlavors_.signature, b"v@:@@"
        )  # XXX: is this correct?

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
        self.assertEqual(addLanguagues_.signature, b"v@:@")  # XXX: is this correct?
        self.assertEqual(intersectLanguagues_.signature, b"v@:@")

        # Validation
        @objc.typedAccessor(mytype)
        def validateColor_error_(self, value, error):
            return (False, None)

        self.assertIsInstance(validateColor_error_, objc.selector)
        self.assertEqual(validateColor_error_.signature, objc._C_NSBOOL + b"@:N^@o^@")

    def test_Accessor(self):
        with warnings.catch_warnings():
            # NOTE: the optional type argument is tested through the typedAccessor function

            # Basic properties:
            warnings.filterwarnings("ignore", category=DeprecationWarning)

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
            def getFlavors_range_(self, buffer, rng):
                return ["sour", "sweet"]

            self.assertIsInstance(countOfFlavors, objc.selector)
            self.assertIsInstance(objectInFlavorsAtIndex_, objc.selector)
            self.assertIsInstance(flavorsAtIndexes_, objc.selector)
            self.assertIsInstance(getFlavors_range_, objc.selector)

            self.assertEqual(countOfFlavors.signature, objc._C_NSUInteger + b"@:")
            self.assertEqual(
                objectInFlavorsAtIndex_.signature, b"@@:" + objc._C_NSUInteger
            )
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
            self.assertIsInstance(
                replaceObjectInFlavorsAtIndex_withObject_, objc.selector
            )
            self.assertIsInstance(replaceFlavorsAtIndexes_withFlavors_, objc.selector)

            self.assertEqual(
                insertObject_inFlavorsAtIndex_.signature, b"v@:@" + objc._C_NSUInteger
            )
            self.assertEqual(insertFlavors_atIndexes_.signature, b"v@:@@")
            self.assertEqual(
                removeObjectFromFlavorsAtIndex_.signature, b"v@:" + objc._C_NSUInteger
            )
            self.assertEqual(removeFlavorsAtIndexes_.signature, b"v@:@")
            self.assertEqual(
                replaceObjectInFlavorsAtIndex_withObject_.signature,
                b"v@:" + objc._C_NSUInteger + b"@",
            )
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
            self.assertEqual(
                validateColor_error_.signature, objc._C_NSBOOL + b"@:N^@o^@"
            )

            # Keyword arguments (**kwds) and varargs (*args) are
            # not supported:

            def attrib(self, *args):
                pass

            with self.assertRaisesRegex(
                TypeError,
                "attrib can not be an accessor because it accepts varargs, varkw or kwonly",
            ):
                objc.Accessor(attrib)

            def attrib(self, **kwds):
                pass

            with self.assertRaisesRegex(
                TypeError,
                "attrib can not be an accessor because it accepts varargs, varkw or kwonly",
            ):
                objc.Accessor(attrib)

            # Not really an accessor
            def attrib_error_(self, a, b):
                pass

            with self.assertRaisesRegex(
                TypeError, "attrib_error_ not recognized as an accessor"
            ):
                objc.Accessor(attrib_error_)

            # Argument counts that don't match
            def validateObject_error_(self, a):
                pass

            with self.assertRaisesRegex(
                TypeError,
                r"validateObject_error_ expected to take 2 args, but must "
                r"accept 3 from Objective-C \(implicit self plus count of underscores\)",
            ):
                objc.Accessor(validateObject_error_)

            def validateObject_error_(self, a, b, c):
                pass

            with self.assertRaisesRegex(
                TypeError,
                r"validateObject_error_ expected to take 4 args, but must "
                r"accept 3 from Objective-C \(implicit self plus count of underscores\)",
            ):
                objc.Accessor(validateObject_error_)

            def validateObject_error_(self, a, b, c, d=1, e=2):
                pass

            with self.assertRaisesRegex(
                TypeError,
                r"validateObject_error_ expected to take between 4 and 6 args, "
                r"but must accept 3 from Objective-C \(implicit self plus count of underscores\)",
            ):
                objc.Accessor(validateObject_error_)

            @objc.Accessor
            def validateObject_error_(self, a, b, c=1):
                pass

            with self.assertRaisesRegex(
                TypeError,
                r"validateObject_error_ expected to take 2 args, but must "
                r"accept 3 from Objective-C \(implicit self plus count of underscores\)",
            ):
                objc.Accessor(validateObject_error_)

    def test_signature(self):
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)

            @objc.signature(b"d@:ii")
            def myMethod_arg_(self, a, b):
                pass

            self.assertIsInstance(myMethod_arg_, objc.selector)
            self.assertEqual(myMethod_arg_.signature, b"d@:ii")
            self.assertEqual(myMethod_arg_.selector, b"myMethod:arg:")

            @objc.signature(b"q@:@q", selector=b"foo:bar:")
            def method(self, a, b):
                pass

            self.assertIsInstance(method, objc.selector)
            self.assertEqual(method.signature, b"q@:@q")
            self.assertEqual(method.selector, b"foo:bar:")
