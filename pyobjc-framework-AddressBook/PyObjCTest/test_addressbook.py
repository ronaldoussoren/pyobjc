import AddressBook
from PyObjCTools.TestSupport import TestCase


class TestAddressBook(TestCase):
    def testNoTypedefs(self):
        # Just in case: the following is a typedef not a function definition
        self.assertFalse(hasattr(AddressBook, "ABActionGetPropertyCallback"))

    def testOpaque(self):
        self.assertTrue(hasattr(AddressBook, "ABPickerRef"))

        # Supporting this would require C code, but that won't happen as
        # this type basically just C-glue around an Objective-C class which is
        # available:
        self.assertFalse(hasattr(AddressBook, "ABActionCallbacks"))

    def testProtocols(self):
        self.assertFalse(hasattr(AddressBook, "protocols"))


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(
            AddressBook,
            exclude_attrs={
                # All of these are private APIs, test cannot see if APIs are public or not.
                (
                    "ABAddressBookRef",
                    "nts_managedObjectContextWithStoreDescription_databasePath_loadFailure_",
                ),
                ("ABAddressBookRef", "abGlobalAPIUnlockInFile_line_"),
                (
                    "ABAddressBookRef",
                    "abGlobalAPIUnlockInFile_line_togglingSuddenTermination_",
                ),
                (
                    "ABAddressBookRef",
                    "abGlobalAPITryLockInFile_line_togglingSuddenTermination_",
                ),
                (
                    "ABAddressBookRef",
                    "abGlobalAPILockInFile_line_contextBlock_togglingSuddenTermination_",
                ),
                ("ABAddressBookRef", "abRunWithGlobalAPILockInFile_line_block_"),
                ("ABAddressBookRef", "abGlobalAPILockInFile_line_"),
                (
                    "ABAddressBookRef",
                    "abGlobalAPILockInFile_line_togglingSuddenTermination_",
                ),
                ("ABAddressBookRef", "abGlobalAPITryLockInFile_line_"),
                ("ABAddressBookRef", "globalAPIUnlockForAddressBook_inFile_line_"),
                ("ABAddressBookRef", "abGlobalAPILockInFile_line_contextBlock_"),
                (
                    "ABAddressBookRef",
                    "abGlobalAPIUnlockInFile_line_contextBlock_togglingSuddenTermination_",
                ),
                ("ABAddressBookRef", "abGlobalAPIUnlockInFile_line_contextBlock_"),
                ("ABAddressBookRef", "abResultWithGlobalAPILockInFile_line_block_"),
                ("ABPersonRef", "abGlobalAPILockInFile_line_"),
                (
                    "ABPersonRef",
                    "abGlobalAPILockInFile_line_togglingSuddenTermination_",
                ),
                ("ABPersonRef", "abGlobalAPITryLockInFile_line_"),
                ("ABPersonRef", "globalAPIUnlockForAddressBook_inFile_line_"),
                ("ABPersonRef", "abGlobalAPILockInFile_line_contextBlock_"),
                ("ABPersonRef", "globalAPILockForAddressBook_inFile_line_"),
                ("ABGroupRef", "abGlobalAPILockInFile_line_"),
                ("ABGroupRef", "abGlobalAPILockInFile_line_togglingSuddenTermination_"),
                ("ABGroupRef", "abGlobalAPITryLockInFile_line_"),
                ("ABGroupRef", "globalAPIUnlockForAddressBook_inFile_line_"),
                ("ABGroupRef", "abGlobalAPILockInFile_line_contextBlock_"),
                ("ABGroupRef", "globalAPILockForAddressBook_inFile_line_"),
                ("ABAddressBookRef", "abGlobalMailRecentAPILockInFile_line_"),
                ("ABAddressBookRef", "abGlobalMailRecentAPIUnlockInFile_line_"),
                ("ABAddressBookRef", "abGlobalMailRecentAPILockInFile_line_"),
                ("ABAddressBookRef", "abGlobalMailRecentAPIUnlockInFile_line_"),
            },
        )
