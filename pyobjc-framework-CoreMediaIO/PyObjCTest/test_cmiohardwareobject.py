import CoreMediaIO
from PyObjCTools.TestSupport import TestCase, fourcc

CMIOObjectPropertyListenerProc = b"iII^{CMIOObjectPropertyAddress=III}^v"
CMIOObjectPropertyListenerBlock = b"vIn^{CMIOObjectPropertyAddress=III}"


class TestCMIOHardwareObject(TestCase):
    def testStructs(self):
        v = CoreMediaIO.CMIOObjectPropertyAddress()
        self.assertEqual(v.mSelector, 0)
        self.assertEqual(v.mScope, 0)
        self.assertEqual(v.mElement, 0)
        self.assertPickleRoundTrips(v)

    def testConstants(self):
        self.assertEqual(
            CoreMediaIO.kCMIOObjectPropertySelectorWildcard, fourcc(b"****")
        )
        self.assertEqual(CoreMediaIO.kCMIOObjectPropertyScopeWildcard, fourcc(b"****"))
        self.assertEqual(CoreMediaIO.kCMIOObjectPropertyElementWildcard, 0xFFFFFFFF)

        self.assertEqual(CoreMediaIO.kCMIOObjectPropertyScopeGlobal, fourcc(b"glob"))
        self.assertEqual(CoreMediaIO.kCMIOObjectPropertyElementMaster, 0)
        self.assertEqual(CoreMediaIO.kCMIOObjectPropertyElementMain, 0)
        self.assertEqual(CoreMediaIO.kCMIOObjectClassID, fourcc(b"aobj"))
        self.assertEqual(CoreMediaIO.kCMIOObjectClassIDWildcard, fourcc(b"****"))
        self.assertEqual(CoreMediaIO.kCMIOObjectUnknown, 0)

        self.assertEqual(CoreMediaIO.kCMIOObjectPropertyClass, fourcc(b"clas"))
        self.assertEqual(CoreMediaIO.kCMIOObjectPropertyOwner, fourcc(b"stdv"))
        self.assertEqual(CoreMediaIO.kCMIOObjectPropertyCreator, fourcc(b"oplg"))
        self.assertEqual(CoreMediaIO.kCMIOObjectPropertyName, fourcc(b"lnam"))
        self.assertEqual(CoreMediaIO.kCMIOObjectPropertyManufacturer, fourcc(b"lmak"))
        self.assertEqual(CoreMediaIO.kCMIOObjectPropertyElementName, fourcc(b"lchn"))
        self.assertEqual(
            CoreMediaIO.kCMIOObjectPropertyElementCategoryName, fourcc(b"lccn")
        )
        self.assertEqual(
            CoreMediaIO.kCMIOObjectPropertyElementNumberName, fourcc(b"lcnn")
        )
        self.assertEqual(CoreMediaIO.kCMIOObjectPropertyOwnedObjects, fourcc(b"ownd"))
        self.assertEqual(CoreMediaIO.kCMIOObjectPropertyListenerAdded, fourcc(b"lisa"))
        self.assertEqual(
            CoreMediaIO.kCMIOObjectPropertyListenerRemoved, fourcc(b"lisr")
        )

    def testFunctions(self):
        CoreMediaIO.CMIOObjectShow
        self.assertArgIsIn(CoreMediaIO.CMIOObjectHasProperty, 1)

        self.assertArgIsIn(CoreMediaIO.CMIOObjectIsPropertySettable, 1)
        self.assertArgIsOut(CoreMediaIO.CMIOObjectIsPropertySettable, 2)

        self.assertArgIsIn(CoreMediaIO.CMIOObjectGetPropertyDataSize, 1)
        self.assertArgIsIn(CoreMediaIO.CMIOObjectGetPropertyDataSize, 3)
        self.assertArgSizeInArg(CoreMediaIO.CMIOObjectGetPropertyDataSize, 3, 2)
        self.assertArgIsOut(CoreMediaIO.CMIOObjectGetPropertyDataSize, 4)

        self.assertArgIsIn(CoreMediaIO.CMIOObjectGetPropertyData, 1)
        self.assertArgIsOut(CoreMediaIO.CMIOObjectGetPropertyData, 3)
        self.assertArgSizeInArg(CoreMediaIO.CMIOObjectGetPropertyData, 3, 2)
        self.assertArgIsOut(CoreMediaIO.CMIOObjectGetPropertyData, 5)
        self.assertArgIsOut(CoreMediaIO.CMIOObjectGetPropertyData, 6)
        self.assertArgSizeInArg(CoreMediaIO.CMIOObjectGetPropertyData, 6, (4, 5))

        self.assertArgIsIn(CoreMediaIO.CMIOObjectAddPropertyListener, 1)
        self.assertArgIsFunction(
            CoreMediaIO.CMIOObjectAddPropertyListener,
            2,
            CMIOObjectPropertyListenerProc,
            True,
        )

        self.assertArgIsIn(CoreMediaIO.CMIOObjectRemovePropertyListener, 1)
        self.assertArgIsFunction(
            CoreMediaIO.CMIOObjectRemovePropertyListener,
            2,
            CMIOObjectPropertyListenerProc,
            True,
        )

        self.assertArgIsIn(CoreMediaIO.CMIOObjectAddPropertyListenerBlock, 1)
        self.assertArgIsBlock(
            CoreMediaIO.CMIOObjectAddPropertyListenerBlock,
            3,
            CMIOObjectPropertyListenerBlock,
        )

        self.assertArgIsIn(CoreMediaIO.CMIOObjectRemovePropertyListenerBlock, 1)
        self.assertArgIsBlock(
            CoreMediaIO.CMIOObjectRemovePropertyListenerBlock,
            3,
            CMIOObjectPropertyListenerBlock,
        )

        self.assertArgIsIn(CoreMediaIO.CMIOObjectSetPropertyData, 1)
        self.assertArgIsIn(CoreMediaIO.CMIOObjectSetPropertyData, 3)
        self.assertArgSizeInArg(CoreMediaIO.CMIOObjectSetPropertyData, 3, 2)
        self.assertArgIsIn(CoreMediaIO.CMIOObjectSetPropertyData, 5)
        self.assertArgSizeInArg(CoreMediaIO.CMIOObjectSetPropertyData, 5, 4)
