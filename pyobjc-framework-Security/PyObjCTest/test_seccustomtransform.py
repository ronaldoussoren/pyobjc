import Security
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

SecTransformActionBlock = b"@"
SecTransformAttributeActionBlock = b"@@@"
SecTransformDataBlock = b"@@"
SecTransformInstanceBlock = b"@"
SecTransformCreateFP = b"@?^{__CFString=}@^{OpaqueSecTransformImplementation=}"


class TestSecCustomTransform(TestCase):
    def test_types(self):
        self.assertIsOpaquePointer(Security.SecTransformImplementationRef)

    def test_constants(self):
        self.assertEqual(Security.kSecTransformMetaAttributeValue, 0)
        self.assertEqual(Security.kSecTransformMetaAttributeName, 1)
        self.assertEqual(Security.kSecTransformMetaAttributeRef, 2)
        self.assertEqual(Security.kSecTransformMetaAttributeRequired, 3)
        self.assertEqual(
            Security.kSecTransformMetaAttributeRequiresOutboundConnection, 4
        )
        self.assertEqual(Security.kSecTransformMetaAttributeDeferred, 5)
        self.assertEqual(Security.kSecTransformMetaAttributeStream, 6)
        self.assertEqual(Security.kSecTransformMetaAttributeCanCycle, 7)
        self.assertEqual(Security.kSecTransformMetaAttributeExternalize, 8)
        self.assertEqual(Security.kSecTransformMetaAttributeHasOutboundConnections, 9)
        self.assertEqual(Security.kSecTransformMetaAttributeHasInboundConnection, 10)

        self.assertIsInstance(Security.kSecTransformActionCanExecute, str)
        self.assertIsInstance(Security.kSecTransformActionStartingExecution, str)
        self.assertIsInstance(Security.kSecTransformActionFinalize, str)
        self.assertIsInstance(Security.kSecTransformActionExternalizeExtraData, str)
        self.assertIsInstance(Security.kSecTransformActionProcessData, str)
        self.assertIsInstance(Security.kSecTransformActionInternalizeExtraData, str)
        self.assertIsInstance(Security.kSecTransformActionAttributeNotification, str)
        self.assertIsInstance(Security.kSecTransformActionAttributeValidation, str)

    def test_functions(self):
        self.assertResultHasType(Security.SecTransformSetAttributeAction, objc._C_ID)
        self.assertArgHasType(
            Security.SecTransformSetAttributeAction,
            0,
            Security.SecTransformImplementationRef.__typestr__,
        )
        self.assertArgHasType(Security.SecTransformSetAttributeAction, 1, objc._C_ID)
        self.assertArgHasType(Security.SecTransformSetAttributeAction, 2, objc._C_ID)
        self.assertArgIsBlock(
            Security.SecTransformSetAttributeAction, 3, SecTransformAttributeActionBlock
        )

        self.assertResultHasType(Security.SecTransformSetDataAction, objc._C_ID)
        self.assertArgHasType(
            Security.SecTransformSetDataAction,
            0,
            Security.SecTransformImplementationRef.__typestr__,
        )
        self.assertArgHasType(Security.SecTransformSetDataAction, 1, objc._C_ID)
        self.assertArgIsBlock(
            Security.SecTransformSetDataAction, 2, SecTransformDataBlock
        )

        self.assertResultHasType(Security.SecTransformSetTransformAction, objc._C_ID)
        self.assertArgHasType(
            Security.SecTransformSetTransformAction,
            0,
            Security.SecTransformImplementationRef.__typestr__,
        )
        self.assertArgHasType(Security.SecTransformSetTransformAction, 1, objc._C_ID)
        self.assertArgIsBlock(
            Security.SecTransformSetTransformAction, 2, SecTransformActionBlock
        )

        self.assertResultHasType(Security.SecTranformCustomGetAttribute, objc._C_ID)
        self.assertArgHasType(
            Security.SecTranformCustomGetAttribute,
            0,
            Security.SecTransformImplementationRef.__typestr__,
        )
        self.assertArgHasType(Security.SecTranformCustomGetAttribute, 1, objc._C_ID)
        self.assertArgHasType(
            Security.SecTranformCustomGetAttribute, 2, objc._C_NSInteger
        )

        self.assertResultHasType(Security.SecTransformCustomGetAttribute, objc._C_ID)
        self.assertArgHasType(
            Security.SecTransformCustomGetAttribute,
            0,
            Security.SecTransformImplementationRef.__typestr__,
        )
        self.assertArgHasType(Security.SecTransformCustomGetAttribute, 1, objc._C_ID)
        self.assertArgHasType(
            Security.SecTransformCustomGetAttribute, 2, objc._C_NSInteger
        )

        self.assertResultHasType(Security.SecTransformCustomSetAttribute, objc._C_ID)
        self.assertArgHasType(
            Security.SecTransformCustomSetAttribute,
            0,
            Security.SecTransformImplementationRef.__typestr__,
        )
        self.assertArgHasType(Security.SecTransformCustomSetAttribute, 1, objc._C_ID)
        self.assertArgHasType(
            Security.SecTransformCustomSetAttribute, 2, objc._C_NSInteger
        )
        self.assertArgHasType(Security.SecTransformCustomSetAttribute, 3, objc._C_ID)

        self.assertResultHasType(Security.SecTransformPushbackAttribute, objc._C_ID)
        self.assertArgHasType(
            Security.SecTransformPushbackAttribute,
            0,
            Security.SecTransformImplementationRef.__typestr__,
        )
        self.assertArgHasType(Security.SecTransformPushbackAttribute, 1, objc._C_ID)
        self.assertArgHasType(Security.SecTransformPushbackAttribute, 2, objc._C_ID)

    @min_os_level("10.7")
    def test_functions_10_7(self):
        self.assertResultHasType(Security.SecTransformRegister, objc._C_NSBOOL)
        self.assertArgHasType(Security.SecTransformRegister, 0, b"^{__CFString=}")
        self.assertArgIsFunction(
            Security.SecTransformRegister, 1, SecTransformCreateFP, 1
        )
        self.assertArgHasType(Security.SecTransformRegister, 2, b"o^^{__CFError=}")

        self.assertResultHasType(Security.SecTransformCreate, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecTransformCreate)
        self.assertArgHasType(Security.SecTransformCreate, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SecTransformCreate, 1, objc._C_OUT + objc._C_PTR + objc._C_ID
        )

        self.assertResultHasType(Security.SecTransformNoData, objc._C_ID)
