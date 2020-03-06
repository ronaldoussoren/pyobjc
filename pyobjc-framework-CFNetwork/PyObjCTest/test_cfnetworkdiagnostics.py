import CFNetwork
import objc
from PyObjCTools.TestSupport import TestCase, expectedFailure


class TestCFNetwork(TestCase):
    @expectedFailure
    def testTypes(self):
        self.assertIsCFType(CFNetwork.CFNetDiagnosticRef)

    def testConstants(self):
        self.assertEqual(CFNetwork.kCFNetDiagnosticNoErr, 0)
        self.assertEqual(CFNetwork.kCFNetDiagnosticErr, -66560)
        self.assertEqual(CFNetwork.kCFNetDiagnosticConnectionUp, -66559)
        self.assertEqual(CFNetwork.kCFNetDiagnosticConnectionIndeterminate, -66558)
        self.assertEqual(CFNetwork.kCFNetDiagnosticConnectionDown, -66557)

    def testFuncdtions(self):
        self.assertResultIsCFRetained(CFNetwork.CFNetDiagnosticCreateWithStreams)

        host = CFNetwork.CFHostCreateWithName(None, "www.apple.com")
        rd, wr = CFNetwork.CFStreamCreatePairWithSocketToCFHost(
            None, host, 80, None, None
        )
        self.assertIsInstance(rd, CFNetwork.CFReadStreamRef)
        self.assertIsInstance(wr, CFNetwork.CFWriteStreamRef)

        ref = CFNetwork.CFNetDiagnosticCreateWithStreams(None, rd, wr)
        self.assertIsInstance(ref, objc.objc_object)  # CFNetDiagnosticRef)

        self.assertResultIsCFRetained(CFNetwork.CFNetDiagnosticCreateWithURL)
        ref = CFNetwork.CFNetDiagnosticCreateWithURL(
            None, CFNetwork.CFURLCreateWithString(None, "http://www.apple.com/", None)
        )
        self.assertIsInstance(ref, objc.objc_object)  # CFNetDiagnosticRef)

        CFNetwork.CFNetDiagnosticSetName(ref, "hello world")

        sts = CFNetwork.CFNetDiagnosticDiagnoseProblemInteractively(ref)
        self.assertIsInstance(sts, int)

        self.assertArgIsOut(CFNetwork.CFNetDiagnosticCopyNetworkStatusPassively, 1)
        sts, descr = CFNetwork.CFNetDiagnosticCopyNetworkStatusPassively(ref, None)
        self.assertIsInstance(sts, int)
        self.assertIsInstance(descr, str)
