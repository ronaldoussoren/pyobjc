import Security
from PyObjCTools.TestSupport import TestCase


class TestSecTransform(TestCase):
    def test_enums(self):
        # Unnamed enum:
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

    def test_constants(self):
        self.assertIsInstance(Security.kSecTransformErrorDomain, str)
        self.assertIsInstance(Security.kSecTransformPreviousErrorKey, str)
        self.assertIsInstance(Security.kSecTransformAbortOriginatorKey, str)

        self.assertIsInstance(Security.kSecTransformInputAttributeName, str)
        self.assertIsInstance(Security.kSecTransformOutputAttributeName, str)
        self.assertIsInstance(Security.kSecTransformDebugAttributeName, str)
        self.assertIsInstance(Security.kSecTransformTransformName, str)
        self.assertIsInstance(Security.kSecTransformAbortAttributeName, str)

    def test_functions(self):
        self.assertResultIsCFRetained(
            Security.SecTransformCreateFromExternalRepresentation
        )
        self.assertArgIsOut(
            Security.SecTransformCreateFromExternalRepresentation,
            1,
        )

        self.assertResultIsCFRetained(Security.SecTransformCopyExternalRepresentation)

        self.assertResultIsCFRetained(Security.SecTransformCreateGroupTransform)

        self.assertArgIsOut(
            Security.SecTransformConnectTransforms,
            5,
        )
        self.assertArgIsCFRetained(
            Security.SecTransformConnectTransforms,
            5,
        )

        self.assertResultIsBOOL(Security.SecTransformSetAttribute)
        self.assertArgIsOut(Security.SecTransformSetAttribute, 3)
        self.assertArgIsCFRetained(Security.SecTransformSetAttribute, 3)

        Security.SecTransformGetAttribute

        Security.SecTransformFindByName

        self.assertResultIsCFRetained(Security.SecTransformExecute)
        self.assertArgIsOut(Security.SecTransformExecute, 1)

        SecMessageBlock = b"v@@Z"
        self.assertArgIsBlock(Security.SecTransformExecuteAsync, 2, SecMessageBlock)
