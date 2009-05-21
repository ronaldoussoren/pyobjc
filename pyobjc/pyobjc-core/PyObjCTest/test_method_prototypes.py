"""
These tests check if method prototypes match method signatures.

TODO: a separate test file that tests calls with optional arguments in 
method defintions:
        class MyClass (NSObject):
            def myMethod_(self, arg=1):
                pass
        o = MyClass.alloc().init()
        o.myMethod_(2)
        o.myMethod_() # should also work, arg == 1
"""

from PyObjCTools.TestSupport import *
from PyObjCTest.fnd import NSObject

class TestInheritedProtoype (TestCase):
    # 
    # These tests check for methods that are inherited from a superclass and
    # therefore have an explict method signature. The number of arguments in
    # the actual method implementation must match that signature.
    #
    def setUp(self):
        import warnings
        warnings.filterwarnings('error', category=DeprecationWarning)

    def tearDown(self):
        import warnings
        del warnings.filters[0]


    def testCorrectArgCount(self):
        # OK: same number of arguments

        class OC_InPro_CorrectArgCount1 (NSObject):
            def init(self):
                pass

        class OC_InPro_CorrectArgCount2 (NSObject):
            def replacementObjectForArchiver_(self, archiver):
                pass

        class OC_InPro_CorrectArgCount3 (NSObject):
            def replacementObjectForArchiver_(self, archiver=None):
                pass

    def testTooFewArguments(self):
        # BAD: too few arguments, should raise error

        try:
            class OC_InPro_TooFew1 (NSObject):
                def init():
                    pass
        
            self.fail()
        except objc.BadPrototypeError:
            pass

        try:
            class OC_InPro_TooFew2 (NSObject):
                def replacementObjectForArchiver_(self):
                    pass
        
            self.fail()
        except objc.BadPrototypeError:
            pass

        try:
            class OC_InPro_TooFew3 (NSObject):
                def replacementObjectForArchiver_():
                    pass
        
            self.fail()
        except objc.BadPrototypeError:
            pass

    def testTooManyArguments(self):
        # BAD: too many arguments, should raise error

        try:
            class OC_InPro_TooMany1 (NSObject):
                def init(self, arg):
                    pass
        
            self.fail()
        except objc.BadPrototypeError:
            pass

        try:
            class OC_InPro_TooMany2 (NSObject):
                def init(self, arg, arg2):
                    pass
        
            self.fail()
        except objc.BadPrototypeError:
            pass

        try:
            class OC_InPro_TooMany3 (NSObject):
                def replacementObjectForArchiver_(self, archiver, extra):
                    pass
        
            self.fail()
        except objc.BadPrototypeError:
            pass

        try:
            class OC_InPro_TooMany4 (NSObject):
                def replacementObjectForArchiver_(self, archiver, opt=3):
                    pass
        
            self.fail()
        except objc.BadPrototypeError:
            pass

    def testBadOverriddenSignature(self):
        # BAD: signature doesn't match super class signature
        try:
            class OC_InPro_BadSig1 (NSObject):
                def init(self):
                    pass
                init = objc.selector(init, signature='v@:')

            self.fail()

        except objc.BadPrototypeError:
            pass

        try:
            class OC_InPro_BadSig2 (NSObject):
                def init(self, arg1, arg2):
                    pass
                init = objc.selector(init, signature='v@:@@')

            self.fail()

        except objc.BadPrototypeError:
            pass


        # This one is fine, just to ensure PyObjC isn't too
        # strict.
        class OC_InPro_BadSig3 (NSObject):
            def init(self):
                pass
            init = objc.selector(init, signature='@@:')


    def testAllArgsOptional(self):
        # Dodgy, all arguments are optional using '*args, **kwds'
        # 
        # This should be accepted because simple decorators will use
        # a method signature like this and we don't want errors or warnings
        # for that.
        # 
        # NOTE: see also the 'decorator' library, that allows you to
        # use decorators without ending up with an ugly signature.
        class OC_InPro_AllOpt1 (NSObject):
            def init(*args, **kwds):
                pass

        class OC_InPro_AllOpt2 (NSObject):
            def replacementObjectForArchiver_(*args, **kwds):
                pass


        # Also allow versions with an explicit self argument, those
        # are commonly used as well.
        class OC_InPro_AllOpt3 (NSObject):
            def init(self, *args, **kwds):
                pass

        class OC_InPro_AllOpt4 (NSObject):
            def replacementObjectForArchiver_(self, *args, **kwds):
                pass

    def testOptionalArgs(self):
        # BAD: optional arguments, which don't exist in Objective-C
        try:
            class OC_InPro_OptArgs1 (NSObject):
                def replacementObjectForArchiver_(self, *args):
                    pass

            self.fail()
        except objc.BadPrototypeError:
            pass

        try:
            class OC_InPro_OptArgs2 (NSObject):
                def replacementObjectForArchiver_(self, **kwds):
                    pass

            self.fail()
        except objc.BadPrototypeError:
            pass

class TestExplicitPrototype (TestCase):
    # 
    # These tests check for methods with an explict method signature in the
    # python code (not inheritted). The python code should match the provided
    # signature.
    def setUp(self):
        import warnings
        warnings.filterwarnings('error', category=DeprecationWarning)

    def tearDown(self):
        import warnings
        del warnings.filters[0]

    def testCorrectArgCount(self):
        # OK: same number of arguments

        class OC_ExplProto_CorrectArgCount1 (NSObject):

            def noargsmethod(self):
                pass
            noargsmethod = objc.selector(noargsmethod, signature='v@:')

        class OC_ExplProto_CorrectArgCount2 (NSObject):
            def oneargmethod_(self, archiver):
                pass
            oneargmethod_ = objc.selector(oneargmethod_, signature='v@:i')

        class OC_ExplProto_CorrectArgCount3 (NSObject):
            def oneargmethod2_(self, archiver=None):
                pass
            oneargmethod2_ = objc.selector(oneargmethod2_, signature='v@:i')

    def testSignatureDoesNotMatchColons(self):
        # OK: the signature specifies more arguments than the implicit or
        # explicit selector seems to need.

        class OC_ExplProto_ColonVsCount1 (NSObject):
            def twoargmethod(self, arg1, arg2):
                pass
            twoargmethod = objc.selector(twoargmethod)

        class OC_ExplProto_ColonVsCount2 (NSObject):
            def twoargmethod(self, arg1, arg2):
                pass
            twoargmethod = objc.selector(twoargmethod, signature='v@:@@')

        class OC_ExplProto_ColonVsCount3 (NSObject):
            def twoargmethod(self, arg1, arg2):
                pass
            twoargmethod = objc.selector(twoargmethod, selector='twoargs')

        #class OC_ExplProto_ColonVsCount4 (NSObject):
        #    def noargmethod_(self):
        #        pass
        #    noargmethod_ = objc.selector(noargmethod_)

        #class OC_ExplProto_ColonVsCount5 (NSObject):
        #    def noargmethod_(self):
        #        pass
        #    noargmethod_ = objc.selector(noargmethod_, signature='v@:')

        #class OC_ExplProto_ColonVsCount6 (NSObject):
        #    def noargmethod_(self):
        #        pass
        #    noargmethod_ = objc.selector(noargmethod_, selector='doit:')


    def testTooFewArguments(self):
        # BAD: too few arguments, should raise error

        try:
            class OC_ExplProto_TooFew1 (NSObject):

                def oneargmethod3_(self):
                    pass
                oneargmethod3_ = objc.selector(oneargmethod3_, signature='i@:f')

            self.fail()
        except objc.BadPrototypeError:
            pass

    def testTooManyArguments(self):
        # BAD: too many arguments, should raise error

        try:
            class OC_ExplProto_TooMany1 (NSObject):
                def oneargmethod4_(self, a, b):
                    pass
                oneargmethod4_ = objc.selector(oneargmethod4_, signature='i@:f')
        
            self.fail()
        except objc.BadPrototypeError:
            pass

    def testAllArgsOptional(self):
        # Dodgy, all arguments are optional using '*args, **kwds'
        # 
        # This should be accepted because simple decorators will use
        # a method signature like this and we don't want errors or warnings
        # for that.
        # 
        # NOTE: see also the 'decorator' library, that allows you to
        # use decorators without ending up with an ugly signature.
        class OC_ExplProto_AllOpt1 (NSObject):
            def oneargmethod_(*args, **kwds):
                pass
            oneargmethod_ = objc.selector(oneargmethod_, signature='i@:i')

    def testOptionalArgs(self):
        # BAD: optional arguments, which don't exist in Objective-C
        try:
            class OC_ExplProto_OptArgs1 (NSObject):
                def oneargmethod_(self, *args):
                    pass
                oneargmethod_ = objc.selector(oneargmethod_, signature='i@:i')

            self.fail()
        except objc.BadPrototypeError:
            pass

        try:
            class OC_ExplProto_OptArgs2 (NSObject):
                def oneargmethod_(self, **kwds):
                    pass
                oneargmethod_ = objc.selector(oneargmethod_, signature='i@:i')

            self.fail()
        except objc.BadPrototypeError:
            pass

    def testOutputArgumentsPresent(self):
        # OK: Output arguments, all arguments are present
        class OC_ExplProto_OutputPresent1 (NSObject):

            def oneoutput_(self, output):
                pass
            oneoutput_ = objc.selector(oneoutput_, signature='i@:^@')

        class OC_ExplProto_OutputPresent2 (NSObject):

            def oneinput_output_(self, input, output):
                pass
            oneinput_output_ = objc.selector(oneinput_output_, 
                    signature='i@:f^@')

    def testOutputArgumentsAbsent(self):
        # BAD: Output arguments, output not in prototype
        # 
        # NOTE: this was a warning in PyObjC 2.0 and the only
        # valid way to work in PyObjC 1.x.
        try:
            class OC_ExplProto_OutputAbsent1 (NSObject):

                def oneoutput_(self):
                    pass
                oneoutput_ = objc.selector(oneoutput_, signature='i@:^@')

            self.fail()

        except objc.BadPrototypeError:
            pass

        try:
            class OC_ExplProto_OutputAbsent2 (NSObject):

                def oneinput_output_(self, input):
                    pass
                oneinput_output_ = objc.selector(oneinput_output_, 
                        signature='i@:i^@')

            self.fail()

        except objc.BadPrototypeError:
            pass

class TestImplicitSignature (TestCase):
    # 
    # These tests check for methods that aren't inheritted and don't have
    # an explicit prototype either
    #

    def setUp(self):
        import warnings
        warnings.filterwarnings('error', category=DeprecationWarning)

    def tearDown(self):
        import warnings
        del warnings.filters[0]

    def testColonMatch(self):
        # OK: the number of underscores matches the number of arguments
        class OC_ImplProto_ColonMatch1 (NSObject):
            def simplemethod(self):
                pass
        self.assertEquals(OC_ImplProto_ColonMatch1.simplemethod.selector, 'simplemethod')
        self.assertEquals(OC_ImplProto_ColonMatch1.simplemethod.signature, 'v@:')

        class OC_ImplProto_ColonMatch2 (NSObject):
            def simplemethod_arg2_(self, a, b):
                return 1
        self.assertEquals(OC_ImplProto_ColonMatch2.simplemethod_arg2_.selector, 'simplemethod:arg2:')
        self.assertEquals(OC_ImplProto_ColonMatch2.simplemethod_arg2_.signature, '@@:@@')

    def testTooFewColons(self):
        # OK: the number of implied colons is smaller than the actual number of
        # arguments.
        # 
        # This is fine because you want to use the regular python naming
        # conventions for methods that won't be called from Objective-C,
        # that keeps Python code as nice as possible.
        class OC_ImplProto_TooFew1 (NSObject):
            def myMethod(self, arg1, arg2=4):
                pass
        self.assertEquals(OC_ImplProto_TooFew1.myMethod.selector, 'myMethod')
        self.assertEquals(OC_ImplProto_TooFew1.myMethod.signature, 'v@:@@')

    def testTooManyColons(self):
        # OK: the number of implied colons is larger than the actual number
        # of arguments
        #
        # (see 'testTooFewColons', same argument but other coding style)
        class OC_ImplProto_TooMany2 (NSObject):
            def run_to_completion(self):
                pass
        self.assertEquals(OC_ImplProto_TooMany2.run_to_completion.selector, 'run_to_completion')
        self.assertEquals(OC_ImplProto_TooMany2.run_to_completion.signature, 'v@:')

    def testImpliedColonTooFew(self):
        # BAD: a method that is obviously intented to be an objective-C method, but
        # has too few arguments.
        try:
            class OC_ImplProto_TooFew2 (NSObject):
                def setFoo_(self):
                    pass
            self.fail()

        except objc.BadPrototypeError:
            pass

        # OK: leading underscore won't be converted to a colon
        class OC_ImplProto_TooFew3 (NSObject):
            def _setFoo_(self, value):
                pass

    def testImpliedColonTooMany(self):
        # BAD: a method that is obviously intended to be an objective-C method,
        # but has too many arguments.

        try:
            class OC_ImplProto_TooMany1 (NSObject):
                def setFoo_(self, value, other):
                    pass
            self.fail()
        except objc.BadPrototypeError:
            pass

        try:
            class OC_ImplProto_TooMany2 (NSObject):
                def setFoo_(self, value, other=3):
                    pass
            self.fail()
        except objc.BadPrototypeError:
            pass

        try:
            class OC_ImplProto_TooMany3 (NSObject):
                def setFoo_(self, value, *rest):
                    pass
            self.fail()
        except objc.BadPrototypeError:
            pass

        try:
            class OC_ImplProto_TooMany4 (NSObject):
                def setFoo_(self, value, **rest):
                    pass
            self.fail()
        except objc.BadPrototypeError:
            pass


    def testMethodVariations(self):
        # OK: all methods with an implied signature are fine
        # 
        # That is, as long as the implied selector doesn't contain
        # colons. If the implied selector does contain colons the
        # method must have the right number of parameters, that
        # should help us to avoid obvious errors.
        class OC_ImplProto_Variations (NSObject):
            def method1(self): pass
            def method2(self): return 1
            def method1_(self, arg): pass
            def methodWithX_andY_(self, x, y): pass
            def method_with_embedded_underscores(self, a): pass
            def __magic__(self): pass
            def _leadingColon(self): pass
            def _leadingColon_(self, arg): return 1
            def methodWithArg_(self, arg): pass

        # Check method signatures
        self.assertEquals(OC_ImplProto_Variations.method1.selector, "method1")
        self.assertEquals(OC_ImplProto_Variations.method2.selector, "method2")
        self.assertEquals(OC_ImplProto_Variations.method1_.selector, "method1:")
        self.assertEquals(OC_ImplProto_Variations.methodWithX_andY_.selector, "methodWithX:andY:")
        self.assertEquals(OC_ImplProto_Variations.method_with_embedded_underscores.selector, "method_with_embedded_underscores")
        #self.assertEquals(OC_ImplProto_Variations.__magic__.selector, "__magic__")
        self.assertEquals(OC_ImplProto_Variations._leadingColon.selector, "_leadingColon")
        self.assertEquals(OC_ImplProto_Variations._leadingColon_.selector, "_leadingColon:")
        self.assertEquals(OC_ImplProto_Variations.methodWithArg_.selector, "methodWithArg:")

        # And the implied type signature
        self.assertEquals(OC_ImplProto_Variations.method1.signature, "v@:")
        self.assertEquals(OC_ImplProto_Variations.method2.signature, "@@:")
        self.assertEquals(OC_ImplProto_Variations.method1_.signature, "v@:@")
        self.assertEquals(OC_ImplProto_Variations.methodWithX_andY_.signature, "v@:@@")
        self.assertEquals(OC_ImplProto_Variations.method_with_embedded_underscores.signature, "v@:@")
        #self.assertEquals(OC_ImplProto_Variations.__magic__.signature, "v@:")
        self.assertEquals(OC_ImplProto_Variations._leadingColon.signature, "v@:")
        self.assertEquals(OC_ImplProto_Variations._leadingColon_.signature, "@@:@")
        self.assertEquals(OC_ImplProto_Variations.methodWithArg_.signature, "v@:@")

if __name__ == "__main__":
    main()
