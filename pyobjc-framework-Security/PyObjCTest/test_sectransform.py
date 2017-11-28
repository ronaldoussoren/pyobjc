from PyObjCTools.TestSupport import *

import Security

class TestSecTransform (TestCase):

    def test_constants(self):
        self.assertIsInstance(Security.kSecTransformErrorDomain, unicode)
        self.assertIsInstance(Security.kSecTransformPreviousErrorKey, unicode)
        self.assertIsInstance(Security.kSecTransformAbortOriginatorKey, unicode)

        self.assertEqual(Security.kSecTransformErrorAttributeNotFound, 1)
        self.assertEqual(Security.kSecTransformErrorInvalidOperation, 2)
        self.assertEqual(Security.kSecTransformErrorNotInitializedCorrectly, 3)
        self.assertEqual(Security.kSecTransformErrorMoreThanOneOutput, 4)
        self.assertEqual(Security.kSecTransformErrorInvalidInputDictionary, 5)
        self.assertEqual(Security.kSecTransformErrorInvalidAlgorithm, 6)
        self.assertEqual(Security.kSecTransformErrorInvalidLength, 7)
        self.assertEqual(Security.kSecTransformErrorInvalidType, 8)
        self.assertEqual(Security.kSecTransformErrorInvalidInput, 10)
        self.assertEqual(Security.kSecTransformErrorNameAlreadyRegistered, 11)
        self.assertEqual(Security.kSecTransformErrorUnsupportedAttribute, 12)
        self.assertEqual(Security.kSecTransformOperationNotSupportedOnGroup, 13)
        self.assertEqual(Security.kSecTransformErrorMissingParameter, 14)
        self.assertEqual(Security.kSecTransformErrorInvalidConnection, 15)
        self.assertEqual(Security.kSecTransformTransformIsExecuting, 16)
        self.assertEqual(Security.kSecTransformInvalidOverride, 17)
        self.assertEqual(Security.kSecTransformTransformIsNotRegistered, 18)
        self.assertEqual(Security.kSecTransformErrorAbortInProgress, 19)
        self.assertEqual(Security.kSecTransformErrorAborted, 20)
        self.assertEqual(Security.kSecTransformInvalidArgument, 21)

    @min_os_level('10.7')
    def test_constants10_7(self):
        self.assertIsInstance(Security.kSecTransformInputAttributeName, unicode)
        self.assertIsInstance(Security.kSecTransformOutputAttributeName, unicode)
        self.assertIsInstance(Security.kSecTransformDebugAttributeName, unicode)
        self.assertIsInstance(Security.kSecTransformTransformName, unicode)
        self.assertIsInstance(Security.kSecTransformAbortAttributeName, unicode)

    @min_os_level('10.7')
    def test_functions10_7(self):
        self.assertResultHasType(Security.SecTransformCreateFromExternalRepresentation, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecTransformCreateFromExternalRepresentation)
        self.assertArgHasType(Security.SecTransformCreateFromExternalRepresentation, 0, objc._C_ID)
        self.assertArgHasType(Security.SecTransformCreateFromExternalRepresentation, 1, objc._C_OUT + objc._C_PTR + objc._C_ID)

        self.assertResultHasType(Security.SecTransformCopyExternalRepresentation, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecTransformCopyExternalRepresentation)
        self.assertArgHasType(Security.SecTransformCopyExternalRepresentation, 0, objc._C_ID)

        self.assertResultHasType(Security.SecTransformCreateGroupTransform, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecTransformCreateGroupTransform)

        self.assertResultHasType(Security.SecTransformConnectTransforms, objc._C_ID)
        self.assertArgHasType(Security.SecTransformConnectTransforms, 0, objc._C_ID)
        self.assertArgHasType(Security.SecTransformConnectTransforms, 1, objc._C_ID)
        self.assertArgHasType(Security.SecTransformConnectTransforms, 2, objc._C_ID)
        self.assertArgHasType(Security.SecTransformConnectTransforms, 3, objc._C_ID)
        self.assertArgHasType(Security.SecTransformConnectTransforms, 4, objc._C_ID)
        self.assertArgHasType(Security.SecTransformConnectTransforms, 5, objc._C_OUT + objc._C_PTR + objc._C_ID)

        self.assertResultHasType(Security.SecTransformSetAttribute, objc._C_NSBOOL)
        self.assertArgHasType(Security.SecTransformSetAttribute, 0, objc._C_ID)
        self.assertArgHasType(Security.SecTransformSetAttribute, 1, objc._C_ID)
        self.assertArgHasType(Security.SecTransformSetAttribute, 2, objc._C_ID)
        self.assertArgHasType(Security.SecTransformSetAttribute, 3, objc._C_OUT + objc._C_PTR + objc._C_ID)

        self.assertResultHasType(Security.SecTransformGetAttribute, objc._C_ID)
        self.assertArgHasType(Security.SecTransformGetAttribute, 0, objc._C_ID)
        self.assertArgHasType(Security.SecTransformGetAttribute, 1, objc._C_ID)

        self.assertResultHasType(Security.SecTransformFindByName, objc._C_ID)
        self.assertArgHasType(Security.SecTransformFindByName, 0, objc._C_ID)
        self.assertArgHasType(Security.SecTransformFindByName, 1, objc._C_ID)

        self.assertResultHasType(Security.SecTransformExecute, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecTransformExecute)
        self.assertArgHasType(Security.SecTransformExecute, 0, objc._C_ID)
        self.assertArgHasType(Security.SecTransformExecute, 1, objc._C_OUT + objc._C_PTR + objc._C_ID)

        SecMessageBlock = b'v@@Z'
        self.assertResultHasType(Security.SecTransformExecuteAsync, objc._C_VOID)
        self.assertArgHasType(Security.SecTransformExecuteAsync, 0, objc._C_ID)
        self.assertArgHasType(Security.SecTransformExecuteAsync, 1, b'^{dispatch_queue_s=}')
        self.assertArgIsBlock(Security.SecTransformExecuteAsync, 2, SecMessageBlock)


if __name__ == "__main__":
    main()
