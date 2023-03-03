import objc
from PyObjCTools.TestSupport import TestCase

NSObject = objc.lookUpClass("NSObject")
NSSortDescriptor = objc.lookUpClass("NSSortDescriptor")

objc.registerMetaDataForSelector(
    b"NSObject", b"selector", {"retval": {"type": objc._C_VOID}}
)


class MetadataInheritanceHelper(NSObject):
    def selector(self):
        return 1


class TestMetadataInheritance(TestCase):
    # These tests that PyObjC's signatures overrides don't
    # kick in when the new signature is incompatible with
    # the native signature.
    def testPythonMeta(self):
        o = MetadataInheritanceHelper.alloc().init()
        self.assertResultHasType(o.selector, objc._C_VOID)

    def testObjCMeta(self):
        o = NSSortDescriptor.alloc().init()
        self.assertResultHasType(o.selector, objc._C_SEL)
