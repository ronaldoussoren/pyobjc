from PyObjCTools.TestSupport import *
import objc
from PyObjCTest.fnd import *

objc.registerMetaDataForSelector(
        b"NSObject", b"validateValue:forKey:error:",
        dict(
            arguments={
                2: dict(type_modifier=objc._C_INOUT),
                4: dict(type_modifier=objc._C_OUT),
            },
        ))


class OCCopy (NSObject):
    def copy(self):
        return self.copyWithZone_(None)

    def copyWithZone_(self, zone):
        v = OCCopy.allocWithZone_(zone).init()
        return v

class OCObserve (NSObject):
    def init(self):
        self = super(OCObserve, self).init()
        self.values = []
        self.registrations = []
        return self

    def register(self, object, keypath):
        object.addObserver_forKeyPath_options_context_(
                self, keypath, 0x3, None)
        self.registrations.append((object, keypath))

    def unregister(self, object, keypath):
        object.removeObserver_forKeyPath_(self, keypath)

    def observeValueForKeyPath_ofObject_change_context_(
            self, keypath, object, change, context):
        self.values.append((object, keypath, change))

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        for o, k in self.registrations:
            self.unregister(o, k)
        self.registrations = []


class TestObjectProperty (TestCase):
    def testCreation(self):
        class OCTestObjectProperty1 (NSObject):
            p1 = objc.object_property()
            p2 = objc.object_property(copy=True)
            p3 = objc.object_property(read_only=True)
            p4 = objc.object_property(ivar='myp4')
            p5 = objc.object_property(typestr=objc._C_INT)
            p6 = objc.object_property(typestr=objc._C_DBL)


        o = OCTestObjectProperty1.alloc().init()

        self.assertTrue(o.respondsToSelector(b'p1'))
        self.assertTrue(o.respondsToSelector(b'setP1:'))

        v = OCCopy.alloc().init()
        o.p1 = v
        self.assertIs(o.p1, v)
        self.assertIs(o._p1, v)

        self.assertTrue(o.respondsToSelector(b'p2'))
        self.assertTrue(o.respondsToSelector(b'setP2:'))

        o.p2 = v
        self.assertIsInstance(o.p2, OCCopy)
        self.assertIsNot(o.p2, v)
        self.assertIsNot(o._p2, v)

        self.assertTrue(o.respondsToSelector(b'p3'))
        self.assertFalse(o.respondsToSelector(b'setP3:'))

        o._p3 = v
        self.assertIs(o.p3, v)


        self.assertTrue(o.respondsToSelector(b'p4'))
        self.assertTrue(o.respondsToSelector(b'setP4:'))

        o.p4 = v
        self.assertIs(o.p4, v)
        self.assertIs(o.myp4, v)

        self.assertTrue(o.respondsToSelector(b'p5'))
        self.assertTrue(o.respondsToSelector(b'setP5:'))
        self.assertTrue(o.respondsToSelector(b'p6'))
        self.assertTrue(o.respondsToSelector(b'setP6:'))
        s = o.methodSignatureForSelector_(b'p5')
        self.assertEquals(s.methodReturnType(), objc._C_INT)
        s = o.methodSignatureForSelector_(b'p6')
        self.assertEquals(s.methodReturnType(), objc._C_DBL)

    def testDepends(self):
        class OCTestObjectProperty2 (NSObject):
            p1 = objc.object_property()
            p2 = objc.object_property()
            p3 = objc.object_property(read_only=True, depends_on=['p1', 'p2'])

            @p3.getter
            def p3(self):
                return (self.p1, self.p2)

        observer = OCObserve.alloc().init()
        object = OCTestObjectProperty2.alloc().init()

        observer.register(object, 'p1')
        observer.register(object, 'p2')
        observer.register(object, 'p3')
        try:

            self.assertEquals(observer.values, [])

            object.p1 = "a"
            object.p2 = "b"
            self.assertEquals(object.p3, ("a", "b"))

            self.assertEquals(len(observer.values), 4)

            if observer.values[0][1] == 'p1':
                self.assertEquals(observer.values[1][1], 'p3')
            else:
                self.assertEquals(observer.values[0][1], 'p3')
                self.assertEquals(observer.values[1][1], 'p1')

            if observer.values[2][1] == 'p2':
                self.assertEquals(observer.values[3][1], 'p3')
            else:
                self.assertEquals(observer.values[2][1], 'p3')
                self.assertEquals(observer.values[3][1], 'p2')

        finally:
            observer.unregister(object, 'p1')
            observer.unregister(object, 'p2')
            observer.unregister(object, 'p3')

    def testMethods(self):
        l = []

        class OCTestObjectProperty4 (NSObject):

            p1 = objc.object_property()

            @p1.getter
            def p1(self):
                l.append(('get',))
                return self._p1 + '!'

            @p1.setter
            def p1(self, v):
                l.append(('set', v))
                self._p1 = v + '?'


            @p1.validate
            def p1(self, value, error):
                if value == 1:
                    return (True, value, None)
                else:
                    return (False, 2, u"snake")


        o = OCTestObjectProperty4.alloc().init()
        o.p1 = 'f'
        self.assertEquals(o.p1, 'f?!')
        self.assertEquals(o._p1, 'f?')
        self.assertEquals(l, [('set', 'f'), ('get',)])

        ok, value, error = o.validateValue_forKey_error_(
                1, 'p1', None)
        self.assertTrue(ok)
        self.assertEquals(value, 1)
        self.assertEquals(error, None)

        ok, value, error = o.validateValue_forKey_error_(
                9, 'p1', None)
        self.assertFalse(ok)
        self.assertEquals(value, 2)
        self.assertEquals(error, u"snake")

    def testNative(self):
        l = []
        class OCTestObjectProperty7 (NSObject):
            p1 = objc.object_property()

            @p1.getter
            def p1(self):
                l.append('get')
                return self._p1

            @p1.setter
            def p1(self, value):
                l.append('set')
                self._p1 = value


        o = OCTestObjectProperty7.alloc().init()
        o.setValue_forKey_(42, 'p1')
        self.assertEquals(o._p1, 42)

        o._p1 = u"monkey"
        v = o.valueForKey_('p1')
        self.assertEquals(v, u"monkey")

        self.assertEquals(l, ["set", "get"])


    def testDynamic(self):
        class OCTestObjectProperty8 (NSObject):
            p1 = objc.object_property(dynamic=True)

        self.assertFalse(OCTestObjectProperty8.instancesRespondToSelector_(b"p1"))
        self.assertFalse(OCTestObjectProperty8.instancesRespondToSelector_(b"setP1:"))

        v = [42]
        def getter(self):
            return v[0]
        def setter(self, value):
            v[0] = value

        OCTestObjectProperty8.p1 = getter
        OCTestObjectProperty8.setP1_ = setter

        self.assertTrue(OCTestObjectProperty8.instancesRespondToSelector_(b"p1"))
        self.assertTrue(OCTestObjectProperty8.instancesRespondToSelector_(b"setP1:"))

        o = OCTestObjectProperty8.alloc().init()
        self.assertIsInstance(OCTestObjectProperty8.p1, objc.object_property)


        self.assertEquals(o.p1, 42)
        o.p1 = 99
        self.assertEquals(o.p1, 99)
        self.assertEquals(v[0], 99)


    def testReadOnly(self):

        class OCTestObjectProperty3 (NSObject):
            p1 = objc.object_property(read_only=True)

        o = OCTestObjectProperty3.alloc().init()

        self.assertRaises(ValueError, setattr, o, 'p1', 42)
    
    def testSubclass(self):

        class OCTestObjectProperty5 (NSObject):
            p1 = objc.object_property(read_only=True)
            p2 = objc.object_property()

        class OCTestObjectProperty6 (OCTestObjectProperty5):
            @OCTestObjectProperty5.p1.setter
            def p1(self, value):
                self._p1 = value

        base = OCTestObjectProperty5.alloc().init()
        self.assertRaises(ValueError, setattr, base, 'p1', 1)
        base.p2 = 'b'
        self.assertEquals(base.p2, 'b')

        sub = OCTestObjectProperty6.alloc().init()
        sub.p1 = 1
        sub.p2 = 'a'
        self.assertEquals(sub.p1, 1)
        self.assertEquals(sub.p2, 'a')

if __name__ == "__main__":
    main()
