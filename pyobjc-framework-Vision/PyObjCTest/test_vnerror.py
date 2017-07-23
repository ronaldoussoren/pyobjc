from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2**32:
    import Vision

    class TestVNError (TestCase):
        def testConstants(self):
            self.asertEqual(Vision.VNErrorOK, 0)
            self.asertEqual(Vision.VNErrorRequestCancelled, 1)
            self.asertEqual(Vision.VNErrorInvalidFormat, 2)
            self.asertEqual(Vision.VNErrorOperationFailed, 3)
            self.asertEqual(Vision.VNErrorOutOfBoundsError, 4)
            self.asertEqual(Vision.VNErrorInvalidOption, 5)
            self.asertEqual(Vision.VNErrorIOError, 6)
            self.asertEqual(Vision.VNErrorMissingOption, 7)
            self.asertEqual(Vision.VNErrorNotImplemented, 8)
            self.asertEqual(Vision.VNErrorInternalError, 9)
            self.asertEqual(Vision.VNErrorOutOfMemory, 10)
            self.asertEqual(Vision.VNErrorUnknownError, 11)
            self.asertEqual(Vision.VNErrorInvalidOperation, 12)
            self.asertEqual(Vision.VNErrorInvalidImage, 13)
            self.asertEqual(Vision.VNErrorInvalidArgument, 14)
            self.asertEqual(Vision.VNErrorInvalidModel, 15)


if __name__ == "__main__":
    main()
