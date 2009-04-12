from CFNetwork import *
from PyObjCTools.TestSupport import *

class TestCFNetwork (TestCase):
    def testTypes(self):
        # Test fails because the type seems to be registered when the 
        # first instance is created ...
        self.failUnlessIsCFType(CFNetDiagnosticRef)

    def testConstants(self):
        self.failUnlessEqual(kCFNetDiagnosticNoErr, 0)
        self.failUnlessEqual(kCFNetDiagnosticErr, -66560)
        self.failUnlessEqual(kCFNetDiagnosticConnectionUp, -66559)
        self.failUnlessEqual(kCFNetDiagnosticConnectionIndeterminate, -66558)
        self.failUnlessEqual(kCFNetDiagnosticConnectionDown, -66557)


    def testFuncdtions(self):
        self.failUnlessResultIsCFRetained(CFNetDiagnosticCreateWithStreams)

        host = CFHostCreateWithName(None, u"www.apple.com")
        rd, wr = CFStreamCreatePairWithSocketToCFHost(None, host, 80, None, None)
        self.failUnlessIsInstance(rd, CFReadStreamRef)
        self.failUnlessIsInstance(wr, CFWriteStreamRef)

        ref = CFNetDiagnosticCreateWithStreams(None, rs, ws)
        self.failUnlessIsInstance(ref, CFNetDiagnosticRef)

        self.failUnlessResultIsCFRetained(CFNetDiagnosticCreateWithURL)
        ref = CFNetDiagnosticCreateWithURL(None, ref)
        self.failUnlessIsInstance(ref, CFNetDiagnosticRef)

        CFNetDiagnosticSetName(ref, u"hello world")

        sts = CFNetDiagnosticDiagnoseProblemInteractively(ref)
        self.failUnlesssIsInstance(sts, (int, long))

        self.failUnlessArgIsOut(CFNetDiagnosticCopyNetworkStatusPassively, 1)
        sts, descr = CFNetDiagnosticCopyNetworkStatusPassively(ref, None)
        self.failUnlesssIsInstance(sts, (int, long))
        self.failUnlessIsInstance(descr, unicode)

if __name__ == "__main__":
    main()
