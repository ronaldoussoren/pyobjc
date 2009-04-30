from CFNetwork import *
from PyObjCTools.TestSupport import *

class TestCFNetwork (TestCase):
    def testTypes(self):
        # XXX: CFNetDiagnosticsRef is not actually a proper type
        # in Leopard, the result turns out to be a CFDictionaryRef...
        #self.failUnlessIsCFType(CFNetDiagnosticRef)
        pass

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

        ref = CFNetDiagnosticCreateWithStreams(None, rd, wr)
        self.failUnlessIsInstance(ref, objc.objc_object) #CFNetDiagnosticRef)

        self.failUnlessResultIsCFRetained(CFNetDiagnosticCreateWithURL)
        ref = CFNetDiagnosticCreateWithURL(None, CFURLCreateWithString(None, u"http://www.apple.com/", None))
        self.failUnlessIsInstance(ref, objc.objc_object) #CFNetDiagnosticRef)

        CFNetDiagnosticSetName(ref, u"hello world")

        sts = CFNetDiagnosticDiagnoseProblemInteractively(ref)
        self.failUnlessIsInstance(sts, (int, long))

        self.failUnlessArgIsOut(CFNetDiagnosticCopyNetworkStatusPassively, 1)
        sts, descr = CFNetDiagnosticCopyNetworkStatusPassively(ref, None)
        self.failUnlessIsInstance(sts, (int, long))
        self.failUnlessIsInstance(descr, unicode)

if __name__ == "__main__":
    main()
