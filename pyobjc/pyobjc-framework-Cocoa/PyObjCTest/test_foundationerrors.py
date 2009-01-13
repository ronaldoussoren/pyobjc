from Foundation import *
from PyObjCTools.TestSupport import *

class FoundationErrorsTest (TestCase):
    def testConstants(self):
        self.assertEquals(NSFileNoSuchFileError, 4)
        self.assertEquals(NSFileLockingError, 255)
        self.assertEquals(NSFileReadUnknownError, 256)
        self.assertEquals(NSFileReadNoPermissionError, 257)
        self.assertEquals(NSFileReadInvalidFileNameError, 258)
        self.assertEquals(NSFileReadCorruptFileError, 259)
        self.assertEquals(NSFileReadInapplicableStringEncodingError, 261)
        self.assertEquals(NSFileReadUnsupportedSchemeError, 262)
        self.assertEquals(NSFileReadTooLargeError, 263)
        self.assertEquals(NSFileReadUnknownStringEncodingError, 264)
        self.assertEquals(NSFileWriteUnknownError, 512)
        self.assertEquals(NSFileWriteNoPermissionError, 513)
        self.assertEquals(NSFileWriteInvalidFileNameError, 514)
        self.assertEquals(NSFileWriteInapplicableStringEncodingError, 517)
        self.assertEquals(NSFileWriteUnsupportedSchemeError, 518)
        self.assertEquals(NSKeyValueValidationError, 1024)
        self.assertEquals(NSUserCancelledError, 3072)
        self.assertEquals(NSExecutableNotLoadableError, 3584)
        self.assertEquals(NSExecutableArchitectureMismatchError, 3585)
        self.assertEquals(NSExecutableRuntimeMismatchError, 3586)
        self.assertEquals(NSExecutableLoadError, 3587)
        self.assertEquals(NSExecutableLinkError, 3588)
        self.assertEquals(NSFileErrorMinimum, 0)
        self.assertEquals(NSFileErrorMaximum, 1023)
        self.assertEquals(NSValidationErrorMinimum, 1024)
        self.assertEquals(NSValidationErrorMaximum, 2047)
        self.assertEquals(NSExecutableErrorMinimum, 3584)
        self.assertEquals(NSExecutableErrorMaximum, 3839)
        self.assertEquals(NSFormattingErrorMinimum, 2048)
        self.assertEquals(NSFormattingErrorMaximum, 2559)


if __name__ == "__main__":
    main()
