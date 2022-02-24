from PyObjCTools.TestSupport import TestCase, min_os_level
import Contacts


class TestCNError(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Contacts.CNErrorCode)

    @min_os_level("10.11")
    def testConstants(self):
        self.assertIsInstance(Contacts.CNErrorDomain, str)

        self.assertEqual(Contacts.CNErrorCodeCommunicationError, 1)
        self.assertEqual(Contacts.CNErrorCodeDataAccessError, 2)
        self.assertEqual(Contacts.CNErrorCodeAuthorizationDenied, 100)
        self.assertEqual(Contacts.CNErrorCodeNoAccessableWritableContainers, 101)
        self.assertEqual(Contacts.CNErrorCodeUnauthorizedKeys, 102)
        self.assertEqual(Contacts.CNErrorCodeFeatureDisabledByUser, 103)
        self.assertEqual(Contacts.CNErrorCodeRecordDoesNotExist, 200)
        self.assertEqual(Contacts.CNErrorCodeInsertedRecordAlreadyExists, 201)
        self.assertEqual(Contacts.CNErrorCodeContainmentCycle, 202)
        self.assertEqual(Contacts.CNErrorCodeContainmentScope, 203)
        self.assertEqual(Contacts.CNErrorCodeParentRecordDoesNotExist, 204)
        self.assertEqual(Contacts.CNErrorCodeRecordIdentifierInvalid, 205)
        self.assertEqual(Contacts.CNErrorCodeRecordNotWritable, 206)
        self.assertEqual(Contacts.CNErrorCodeParentContainerNotWritable, 207)
        self.assertEqual(Contacts.CNErrorCodeValidationMultipleErrors, 300)
        self.assertEqual(Contacts.CNErrorCodeValidationTypeMismatch, 301)
        self.assertEqual(Contacts.CNErrorCodeValidationConfigurationError, 302)
        self.assertEqual(Contacts.CNErrorCodePredicateInvalid, 400)
        self.assertEqual(Contacts.CNErrorCodePolicyViolation, 500)
        self.assertEqual(Contacts.CNErrorCodeClientIdentifierInvalid, 600)
        self.assertEqual(Contacts.CNErrorCodeClientIdentifierDoesNotExist, 601)
        self.assertEqual(Contacts.CNErrorCodeClientIdentifierCollision, 602)
        self.assertEqual(Contacts.CNErrorCodeChangeHistoryExpired, 603)
        self.assertEqual(Contacts.CNErrorCodeChangeHistoryInvalidAnchor, 604)
        self.assertEqual(Contacts.CNErrorCodeChangeHistoryInvalidFetchRequest, 605)

        self.assertEqual(Contacts.CNErrorCodeVCardMalformed, 700)
        self.assertEqual(Contacts.CNErrorCodeVCardSummarizationError, 701)

        self.assertIsInstance(Contacts.CNErrorUserInfoAffectedRecordsKey, str)
        self.assertIsInstance(Contacts.CNErrorUserInfoAffectedRecordIdentifiersKey, str)
        self.assertIsInstance(Contacts.CNErrorUserInfoValidationErrorsKey, str)
        self.assertIsInstance(Contacts.CNErrorUserInfoKeyPathsKey, str)
