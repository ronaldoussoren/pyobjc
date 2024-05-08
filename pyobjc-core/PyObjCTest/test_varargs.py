import objc
from PyObjCTools.TestSupport import TestCase

NSObject = objc.lookUpClass("NSObject")


class VarargsMethod(TestCase):
    def testVariableArgumentCount(self):
        class VarArgsClass1(NSObject):
            def instanceMethod1_(self, arg1, *args):
                arg1.append(args)

            def classMethod1_(cls, arg1, *args):
                arg1.append(args)

            classMethod1_ = classmethod(classMethod1_)

            def instanceMethod2_(self, *args):
                args[0].append(args[1:])

            def classMethod2_(cls, *args):
                args[0].append(args[1:])

            classMethod2_ = classmethod(classMethod2_)

        o = VarArgsClass1.alloc().init()
        lst = []
        o.instanceMethod1_(lst, 1, 2, 3)
        self.assertEqual(lst, [(1, 2, 3)])

        lst = []
        VarArgsClass1.classMethod1_(lst, 3, 4, 5)
        self.assertEqual(lst, [(3, 4, 5)])

        lst = []
        o.instanceMethod2_(lst, 1, 2, 3)
        self.assertEqual(lst, [(1, 2, 3)])

        lst = []
        VarArgsClass1.classMethod2_(lst, 3, 4, 5)
        self.assertEqual(lst, [(3, 4, 5)])

    def testKeywordArguments(self):
        class VarArgsClass2(NSObject):
            def instanceMethod1_(self, arg1, **kwds):
                arg1.append(kwds)

            def classMethod1_(cls, arg1, **kwds):
                arg1.append(kwds)

            classMethod1_ = classmethod(classMethod1_)

        o = VarArgsClass2.alloc().init()
        lst = []
        o.instanceMethod1_(lst, a=1, c=2)
        self.assertEqual(lst, [{"a": 1, "c": 2}])

        lst = []
        VarArgsClass2.classMethod1_(lst, foo="bar", baz="foo")
        self.assertEqual(lst, [{"foo": "bar", "baz": "foo"}])
