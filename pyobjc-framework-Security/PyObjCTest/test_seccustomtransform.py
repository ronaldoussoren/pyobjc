import Security
from PyObjCTools.TestSupport import TestCase
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
        self.assertArgHasType(
            Security.SecTransformSetAttributeAction,
            0,
            Security.SecTransformImplementationRef.__typestr__,
        )
        self.assertArgIsBlock(
            Security.SecTransformSetAttributeAction, 3, SecTransformAttributeActionBlock
        )

        self.assertArgHasType(
            Security.SecTransformSetDataAction,
            0,
            Security.SecTransformImplementationRef.__typestr__,
        )
        self.assertArgIsBlock(
            Security.SecTransformSetDataAction, 2, SecTransformDataBlock
        )

        self.assertArgHasType(
            Security.SecTransformSetTransformAction,
            0,
            Security.SecTransformImplementationRef.__typestr__,
        )
        self.assertArgIsBlock(
            Security.SecTransformSetTransformAction, 2, SecTransformActionBlock
        )

        self.assertArgHasType(
            Security.SecTranformCustomGetAttribute,
            0,
            Security.SecTransformImplementationRef.__typestr__,
        )
        self.assertArgHasType(
            Security.SecTranformCustomGetAttribute, 2, objc._C_NSInteger
        )

        self.assertArgHasType(
            Security.SecTransformCustomGetAttribute,
            0,
            Security.SecTransformImplementationRef.__typestr__,
        )
        self.assertArgHasType(
            Security.SecTransformCustomGetAttribute, 2, objc._C_NSInteger
        )

        self.assertArgHasType(
            Security.SecTransformCustomSetAttribute,
            0,
            Security.SecTransformImplementationRef.__typestr__,
        )
        self.assertArgHasType(
            Security.SecTransformCustomSetAttribute, 2, objc._C_NSInteger
        )

        self.assertArgHasType(
            Security.SecTransformPushbackAttribute,
            0,
            Security.SecTransformImplementationRef.__typestr__,
        )

        self.assertResultIsBOOL(Security.SecTransformRegister)
        self.assertArgIsFunction(
            Security.SecTransformRegister, 1, SecTransformCreateFP, 1
        )
        self.assertArgIsOut(Security.SecTransformRegister, 2)
        self.assertArgIsCFRetained(Security.SecTransformRegister, 2)

        self.assertResultIsCFRetained(Security.SecTransformCreate)
        self.assertArgIsOut(Security.SecTransformCreate, 1)
        self.assertArgIsCFRetained(Security.SecTransformCreate, 1)

        Security.SecTransformNoData
