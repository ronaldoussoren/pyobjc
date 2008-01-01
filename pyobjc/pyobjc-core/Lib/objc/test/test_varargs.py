import objc
import objc.test

NSObject = objc.lookUpClass("NSObject")

class VarargsMethod (objc.test.TestCase):
    def testVariableArgumentCount(self):
        class VarArgsClass1 (NSObject):
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
        l = []
        o.instanceMethod1_(l, 1, 2, 3)
        self.assertEquals(l, [(1,2,3)])

        l = []
        VarArgsClass1.classMethod1_(l, 3, 4, 5)
        self.assertEquals(l, [(3,4,5)])

        l = []
        o.instanceMethod2_(l, 1, 2, 3)
        self.assertEquals(l, [(1,2,3)])

        l = []
        VarArgsClass1.classMethod2_(l, 3, 4, 5)
        self.assertEquals(l, [(3,4,5)])

    def testKeywordArguments(self):
        class VarArgsClass2 (NSObject):
            def instanceMethod1_(self, arg1, **kwds):
                arg1.append(kwds)

            def classMethod1_(cls, arg1, **kwds):
                arg1.append(kwds)
            classMethod1_ = classmethod(classMethod1_)


        o = VarArgsClass2.alloc().init()
        l = []
        o.instanceMethod1_(l, a=1, c=2)
        self.assertEquals(l, [{'a':1 ,'c':2}])

        l = []
        VarArgsClass2.classMethod1_(l, foo='bar', baz='foo')
        self.assertEquals(l, [{'foo':'bar', 'baz':'foo'}])

if __name__ == "__main__":
    objc.test.main()
