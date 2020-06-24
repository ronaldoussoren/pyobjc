import DiscRecording
from PyObjCTools.TestSupport import TestCase
import objc


class TestDRFileHelper(DiscRecording.NSObject):
    def calculateSizeOfFile_fork_estimating_(self, a, b, c):
        return 1

    def prepareFileForBurn_(self, a):
        return 1

    def produceFile_fork_intoBuffer_length_atAddress_blockSize_(self, a, b, c, d, e, f):
        return 1

    def prepareFileForVerification_(self, a):
        return 1


class TestDRFile(TestCase):
    def testMethods(self):
        self.assertResultHasType(
            TestDRFileHelper.calculateSizeOfFile_fork_estimating_, objc._C_ULNG_LNG
        )
        self.assertArgHasType(
            TestDRFileHelper.calculateSizeOfFile_fork_estimating_, 1, objc._C_UINT
        )
        self.assertArgIsBOOL(TestDRFileHelper.calculateSizeOfFile_fork_estimating_, 2)

        self.assertResultIsBOOL(TestDRFileHelper.prepareFileForBurn_)

        self.assertResultHasType(
            TestDRFileHelper.produceFile_fork_intoBuffer_length_atAddress_blockSize_,
            objc._C_UINT,
        )
        self.assertArgHasType(
            TestDRFileHelper.produceFile_fork_intoBuffer_length_atAddress_blockSize_,
            1,
            objc._C_UINT,
        )
        self.assertArgHasType(
            TestDRFileHelper.produceFile_fork_intoBuffer_length_atAddress_blockSize_,
            2,
            b"o^v",
        )
        self.assertArgSizeInArg(
            TestDRFileHelper.produceFile_fork_intoBuffer_length_atAddress_blockSize_,
            2,
            3,
        )
        self.assertArgHasType(
            TestDRFileHelper.produceFile_fork_intoBuffer_length_atAddress_blockSize_,
            3,
            objc._C_UINT,
        )
        self.assertArgHasType(
            TestDRFileHelper.produceFile_fork_intoBuffer_length_atAddress_blockSize_,
            4,
            objc._C_ULNG_LNG,
        )
        self.assertArgHasType(
            TestDRFileHelper.produceFile_fork_intoBuffer_length_atAddress_blockSize_,
            5,
            objc._C_UINT,
        )

        self.assertResultIsBOOL(TestDRFileHelper.prepareFileForVerification_)

    def testProtocols(self):
        objc.protocolNamed("DRFileDataProduction")

    def testConstants(self):
        self.assertIsInstance(DiscRecording.DRLinkTypeHardLink, str)
        self.assertIsInstance(DiscRecording.DRLinkTypeSymbolicLink, str)
        self.assertIsInstance(DiscRecording.DRLinkTypeFinderAlias, str)

        self.assertEqual(DiscRecording.DRFileForkData, 0)
        self.assertEqual(DiscRecording.DRFileForkResource, 1)
