from CFNetwork import *
from PyObjCTools.TestSupport import *

class TestCFNetwork (TestCase):
    def testTypes(self):
        # XXX: CFNetDiagnosticsRef is not actually a proper type
        # in Leopard, the result turns out to be a CFDictionaryRef...
        #self.assertIsCFType(CFNetDiagnosticRef)
        pass

    def testConstants(self):
        self.assertEqual(kCFNetDiagnosticNoErr, 0)
        self.assertEqual(kCFNetDiagnosticErr, -66560)
        self.assertEqual(kCFNetDiagnosticConnectionUp, -66559)
        self.assertEqual(kCFNetDiagnosticConnectionIndeterminate, -66558)
        self.assertEqual(kCFNetDiagnosticConnectionDown, -66557)


    def testFuncdtions(self):
        self.assertResultIsCFRetained(CFNetDiagnosticCreateWithStreams)

        host = CFHostCreateWithName(None, u"www.apple.com")
        rd, wr = CFStreamCreatePairWithSocketToCFHost(None, host, 80, None, None)
        self.assertIsInstance(rd, CFReadStreamRef)
        self.assertIsInstance(wr, CFWriteStreamRef)

        ref = CFNetDiagnosticCreateWithStreams(None, rd, wr)
        self.assertIsInstance(ref, objc.objc_object) #CFNetDiagnosticRef)

        self.assertResultIsCFRetained(CFNetDiagnosticCreateWithURL)
        ref = CFNetDiagnosticCreateWithURL(None, CFURLCreateWithString(None, u"http://www.apple.com/", None))
        self.assertIsInstance(ref, objc.objc_object) #CFNetDiagnosticRef)

        CFNetDiagnosticSetName(ref, u"hello world")

        sts = CFNetDiagnosticDiagnoseProblemInteractively(ref)
        self.assertIsInstance(sts, (int, long))

        self.assertArgIsOut(CFNetDiagnosticCopyNetworkStatusPassively, 1)
        sts, descr = CFNetDiagnosticCopyNetworkStatusPassively(ref, None)
        self.assertIsInstance(sts, (int, long))
        self.assertIsInstance(descr, unicode)

if __name__ == "__main__":
    main()
