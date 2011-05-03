from Foundation import *
from PyObjCTools.TestSupport import *

class FoundationErrorsTest (TestCase):
    def testConstants(self):
        self.assertEqual(NSFileNoSuchFileError, 4)
        self.assertEqual(NSFileLockingError, 255)
        self.assertEqual(NSFileReadUnknownError, 256)
        self.assertEqual(NSFileReadNoPermissionError, 257)
        self.assertEqual(NSFileReadInvalidFileNameError, 258)
        self.assertEqual(NSFileReadCorruptFileError, 259)
        self.assertEqual(NSFileReadInapplicableStringEncodingError, 261)
        self.assertEqual(NSFileReadUnsupportedSchemeError, 262)
        self.assertEqual(NSFileReadTooLargeError, 263)
        self.assertEqual(NSFileReadUnknownStringEncodingError, 264)
        self.assertEqual(NSFileWriteUnknownError, 512)
        self.assertEqual(NSFileWriteNoPermissionError, 513)
        self.assertEqual(NSFileWriteInvalidFileNameError, 514)
        self.assertEqual(NSFileWriteInapplicableStringEncodingError, 517)
        self.assertEqual(NSFileWriteUnsupportedSchemeError, 518)
        self.assertEqual(NSKeyValueValidationError, 1024)
        self.assertEqual(NSUserCancelledError, 3072)
        self.assertEqual(NSExecutableNotLoadableError, 3584)
        self.assertEqual(NSExecutableArchitectureMismatchError, 3585)
        self.assertEqual(NSExecutableRuntimeMismatchError, 3586)
        self.assertEqual(NSExecutableLoadError, 3587)
        self.assertEqual(NSExecutableLinkError, 3588)
        self.assertEqual(NSFileErrorMinimum, 0)
        self.assertEqual(NSFileErrorMaximum, 1023)
        self.assertEqual(NSValidationErrorMinimum, 1024)
        self.assertEqual(NSValidationErrorMaximum, 2047)
        self.assertEqual(NSExecutableErrorMinimum, 3584)
        self.assertEqual(NSExecutableErrorMaximum, 3839)
        self.assertEqual(NSFormattingErrorMinimum, 2048)
        self.assertEqual(NSFormattingErrorMaximum, 2559)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(NSFileWriteVolumeReadOnlyError, 642)

        self.assertEqual(NSPropertyListReadCorruptError, 3840)
        self.assertEqual(NSPropertyListReadUnknownVersionError, 3841)
        self.assertEqual(NSPropertyListReadStreamError, 3842)
        self.assertEqual(NSPropertyListWriteStreamError, 3851)
        self.assertEqual(NSPropertyListErrorMinimum, 3840)
        self.assertEqual(NSPropertyListErrorMaximum, 4095)


if __name__ == "__main__":
    main()
