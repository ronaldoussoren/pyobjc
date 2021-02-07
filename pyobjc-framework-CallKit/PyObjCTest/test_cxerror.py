from PyObjCTools.TestSupport import TestCase
import CallKit


class TestCXError(TestCase):
    def test_constants(self):
        self.assertIsInstance(CallKit.CXErrorDomain, str)
        self.assertIsInstance(CallKit.CXErrorDomainIncomingCall, str)
        self.assertIsInstance(CallKit.CXErrorDomainRequestTransaction, str)
        self.assertIsInstance(CallKit.CXErrorDomainCallDirectoryManager, str)

        self.assertEqual(CallKit.CXErrorCodeUnknownError, 0)
        self.assertEqual(CallKit.CXErrorCodeUnentitled, 1)
        self.assertEqual(CallKit.CXErrorCodeInvalidArgument, 2)

        self.assertEqual(CallKit.CXErrorCodeIncomingCallErrorUnknown, 0)
        self.assertEqual(CallKit.CXErrorCodeIncomingCallErrorUnentitled, 1)
        self.assertEqual(CallKit.CXErrorCodeIncomingCallErrorCallUUIDAlreadyExists, 2)
        self.assertEqual(CallKit.CXErrorCodeIncomingCallErrorFilteredByDoNotDisturb, 3)
        self.assertEqual(CallKit.CXErrorCodeIncomingCallErrorFilteredByBlockList, 4)

        self.assertEqual(CallKit.CXErrorCodeRequestTransactionErrorUnknown, 0)
        self.assertEqual(CallKit.CXErrorCodeRequestTransactionErrorUnentitled, 1)
        self.assertEqual(
            CallKit.CXErrorCodeRequestTransactionErrorUnknownCallProvider, 2
        )
        self.assertEqual(CallKit.CXErrorCodeRequestTransactionErrorEmptyTransaction, 3)
        self.assertEqual(CallKit.CXErrorCodeRequestTransactionErrorUnknownCallUUID, 4)
        self.assertEqual(
            CallKit.CXErrorCodeRequestTransactionErrorCallUUIDAlreadyExists, 5
        )
        self.assertEqual(CallKit.CXErrorCodeRequestTransactionErrorInvalidAction, 6)
        self.assertEqual(
            CallKit.CXErrorCodeRequestTransactionErrorMaximumCallGroupsReached, 7
        )

        self.assertEqual(CallKit.CXErrorCodeCallDirectoryManagerErrorUnknown, 0)
        self.assertEqual(
            CallKit.CXErrorCodeCallDirectoryManagerErrorNoExtensionFound, 1
        )
        self.assertEqual(
            CallKit.CXErrorCodeCallDirectoryManagerErrorLoadingInterrupted, 2
        )
        self.assertEqual(
            CallKit.CXErrorCodeCallDirectoryManagerErrorEntriesOutOfOrder, 3
        )
        self.assertEqual(
            CallKit.CXErrorCodeCallDirectoryManagerErrorDuplicateEntries, 4
        )
        self.assertEqual(
            CallKit.CXErrorCodeCallDirectoryManagerErrorMaximumEntriesExceeded, 5
        )
        self.assertEqual(
            CallKit.CXErrorCodeCallDirectoryManagerErrorExtensionDisabled, 6
        )
        self.assertEqual(
            CallKit.CXErrorCodeCallDirectoryManagerErrorCurrentlyLoading, 7
        )
        self.assertEqual(
            CallKit.CXErrorCodeCallDirectoryManagerErrorUnexpectedIncrementalRemoval, 8
        )
