from PyObjCTools.TestSupport import *

import DiscRecording

DRFileProc = b'i^v^{__DRFile=}I^v'

class TestDRContentFile (TestCase):
    def testFunctions(self):
        self.assertIsInstance(DiscRecording.DRFileGetTypeID(), (int, long))

        self.assertResultIsCFRetained(DiscRecording.DRFileCreateReal)
        self.assertArgIsIn(DiscRecording.DRFileCreateReal, 0)

        self.assertResultIsCFRetained(DiscRecording.DRFileCreateRealWithURL)

        self.assertResultIsCFRetained(DiscRecording.DRFileCreateVirtualWithData)
        self.assertArgIsIn(DiscRecording.DRFileCreateVirtualWithData, 1)
        self.assertArgSizeInArg(DiscRecording.DRFileCreateVirtualWithData, 1, 2)

        self.assertResultIsCFRetained(DiscRecording.DRFileCreateVirtualWithCallback)
        self.assertArgIsFunction(DiscRecording.DRFileCreateVirtualWithCallback, 1, DRFileProc, True)

        DiscRecording.DRFileCreateVirtualLink

    def testConstants(self):
        self.assertEqual(DiscRecording.kDRLinkTypeHardLink, 1)
        self.assertEqual(DiscRecording.kDRLinkTypeSymbolicLink, 2)
        self.assertEqual(DiscRecording.kDRLinkTypeFinderAlias, 3)

        self.assertEqual(DiscRecording.kDRFileMessageForkSize, fourcc(b'fsiz'))
        self.assertEqual(DiscRecording.kDRFileMessagePreBurn, fourcc(b'pre '))
        self.assertEqual(DiscRecording.kDRFileMessageProduceData, fourcc(b'prod'))
        self.assertEqual(DiscRecording.kDRFileMessageVerificationStarting, fourcc(b'vrfy'))
        self.assertEqual(DiscRecording.kDRFileMessagePostBurn, fourcc(b'post'))
        self.assertEqual(DiscRecording.kDRFileMessageRelease, fourcc(b'bye '))

        self.assertEqual(DiscRecording.kDRFileForkData, 0)
        self.assertEqual(DiscRecording.kDRFileForkResource, 1)

        self.assertEqual(DiscRecording.kDRFileForkSizeActual, 0)
        self.assertEqual(DiscRecording.kDRFileForkSizeEstimate, 1)

    def testStructs(self):
        v = DiscRecording.DRFileForkSizeInfo()
        self.assertEqual(v.fork, 0)
        self.assertEqual(v.query, 0)
        self.assertEqual(v.size, 0)

        # XXX: Requires manual work
        v = DiscRecording.DRFileProductionInfo()
        self.assertEqual(v.requestedAddress, 0)
        self.assertEqual(v.buffer, None)
        self.assertEqual(v.reqCount, 0)
        self.assertEqual(v.actCount, 0)
        self.assertEqual(v.blockSize, 0)
        self.assertEqual(v.fork, 0)


if __name__ == "__main__":
    main()
