from PyObjCTools.TestSupport import *
from CoreFoundation import *
import errno, time, os, socket


class TestStream (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CFReadStreamRef)
        self.failUnlessIsCFType(CFWriteStreamRef)

    def testConstants(self):
        self.failUnless(kCFStreamStatusNotOpen == 0)
        self.failUnless(kCFStreamStatusOpening == 1)
        self.failUnless(kCFStreamStatusOpen == 2)
        self.failUnless(kCFStreamStatusReading == 3) 
        self.failUnless(kCFStreamStatusWriting == 4)
        self.failUnless(kCFStreamStatusAtEnd == 5)
        self.failUnless(kCFStreamStatusClosed == 6)
        self.failUnless(kCFStreamStatusError == 7)

        self.failUnless(kCFStreamEventNone == 0)
        self.failUnless(kCFStreamEventOpenCompleted == 1)
        self.failUnless(kCFStreamEventHasBytesAvailable == 2)
        self.failUnless(kCFStreamEventCanAcceptBytes == 4)
        self.failUnless(kCFStreamEventErrorOccurred == 8)
        self.failUnless(kCFStreamEventEndEncountered == 16)

        self.failUnless(kCFStreamErrorDomainCustom == -1)
        self.failUnless(kCFStreamErrorDomainPOSIX == 1)
        self.failUnless(kCFStreamErrorDomainMacOSStatus == 2)

        self.failUnless(isinstance(kCFStreamPropertyDataWritten, unicode))
        self.failUnless(isinstance(kCFStreamPropertyAppendToFile, unicode))
        self.failUnless(isinstance(kCFStreamPropertyFileCurrentOffset, unicode))
        self.failUnless(isinstance(kCFStreamPropertySocketNativeHandle, unicode))
        self.failUnless(isinstance(kCFStreamPropertySocketRemoteHostName, unicode))
        self.failUnless(isinstance(kCFStreamPropertySocketRemotePortNumber, unicode))

    def testStructs(self):
        o = CFStreamError()
        self.failUnless(hasattr(o, 'domain'))
        self.failUnless(hasattr(o, 'error'))


    def testGetTypeID(self):
        v = CFReadStreamGetTypeID()
        self.failUnless(isinstance(v, (int, long)))
        
        v = CFWriteStreamGetTypeID()
        self.failUnless(isinstance(v, (int, long)))

    def testReadStream(self):
        strval = "hello world"
        self.failUnlessArgHasType(CFReadStreamCreateWithBytesNoCopy, 1, 'n^v')
        self.failUnlessArgSizeInArg(CFReadStreamCreateWithBytesNoCopy, 1, 2)
        stream = CFReadStreamCreateWithBytesNoCopy(None,
                strval, len(strval), kCFAllocatorNull)
        self.failUnless(isinstance(stream, CFReadStreamRef))

        r, buf = CFReadStreamRead(stream, None, 10)
        self.assertEquals(r, -1)
        self.assertEquals(buf, '')

        self.failUnlessResultIsCFRetained(CFReadStreamCopyError)
        err  = CFReadStreamCopyError(stream)
        self.failUnless(err is None or isinstance(err, CFErrorRef))

        status = CFReadStreamGetStatus(stream)
        self.failUnless(isinstance(status, (int, long)))
        self.assertEquals(status, kCFStreamStatusNotOpen)

        self.failUnlessResultIsBOOL(CFReadStreamOpen)
        r = CFReadStreamOpen(stream)
        self.failUnless(r is True)

        status = CFReadStreamGetStatus(stream)
        self.failUnless(isinstance(status, (int, long)))
        self.assertEquals(status, kCFStreamStatusOpen)

        self.failUnlessResultIsBOOL(CFReadStreamHasBytesAvailable)
        r = CFReadStreamHasBytesAvailable(stream)
        self.failUnless(r is True)

        self.failUnlessArgHasType(CFReadStreamRead, 1, 'o^v')
        self.failUnlessArgSizeInArg(CFReadStreamRead, 1, 2)
        self.failUnlessArgSizeInResult(CFReadStreamRead, 1)
        r, buf = CFReadStreamRead(stream, None, 5)
        self.assertEquals(r, 5)
        self.assertEquals(buf, "hello")

        r, buf = CFReadStreamRead(stream, None, 10)
        self.assertEquals(r, 6)
        self.assertEquals(buf, " world")

        r = CFReadStreamHasBytesAvailable(stream)
        self.failUnless(r is False)

        r = CFReadStreamClose(stream)
        self.failUnless(r is None)
        status = CFReadStreamGetStatus(stream)
        self.failUnless(isinstance(status, (int, long)))
        self.assertEquals(status, kCFStreamStatusClosed)


        del stream

        self.failUnlessResultIsCFRetained(CFReadStreamCreateWithFile)
        stream = CFReadStreamCreateWithFile(None, 
                    CFURLCreateWithString(None, u"file:///etc/shells", None))
        self.failUnless(isinstance(stream, CFReadStreamRef))
        r = CFReadStreamOpen(stream)
        self.failUnless(r is True)

        status = CFReadStreamGetStatus(stream)
        self.failUnless(isinstance(status, (int, long)))
        self.assertEquals(status, kCFStreamStatusOpen)

        r, buf = CFReadStreamRead(stream, None, 5)
        self.assertEquals(r, 5)
        self.failUnless(isinstance(buf, str))

        self.failUnlessResultSizeInArg(CFReadStreamGetBuffer, 2)
        self.failUnlessResultHasType(CFReadStreamGetBuffer, '^v')
        self.failUnlessArgIsOut(CFReadStreamGetBuffer, 2)
        buf, numBytes = CFReadStreamGetBuffer(stream, 20, None)
        if buf is objc.NULL:
            self.assertEquals(numBytes, 0)
        else:
            self.failUnless(isinstance(buf, str))
            self.assertEquals(numBytes, len(buf))

        val = CFReadStreamCopyProperty(stream, kCFStreamPropertyFileCurrentOffset)
        self.assertEquals(val, 5)

        r = CFReadStreamSetProperty(stream, kCFStreamPropertyFileCurrentOffset, 10)
        self.failUnless(r is True)
        val = CFReadStreamCopyProperty(stream, kCFStreamPropertyFileCurrentOffset)
        self.assertEquals(val, 10)

        err = CFReadStreamGetError(stream)
        self.failUnless(isinstance(err, CFStreamError))
        self.failUnless(err.domain == 0)
        self.failUnless(err.error == 0)
        

    def testWriteStream(self):
        import array
        a = array.array('c', " "*20)

        # XXX: cannot express the actual type as metadata :-(
        self.failUnlessArgHasType(CFWriteStreamCreateWithBuffer, 1, 'n^v')
        self.failUnlessArgSizeInArg(CFWriteStreamCreateWithBuffer, 1, 2)
        stream = CFWriteStreamCreateWithBuffer(None, a, 20)
        self.failUnless(isinstance(stream, CFWriteStreamRef))

        self.failUnlessResultIsBOOL(CFWriteStreamOpen)
        r = CFWriteStreamOpen(stream)
        self.failUnless(r is True)

        status = CFWriteStreamGetStatus(stream)
        self.failUnless(isinstance(status, (int, long)))
        self.assertEquals(status, kCFStreamStatusOpen)

        self.failUnlessResultIsBOOL(CFWriteStreamCanAcceptBytes)
        b = CFWriteStreamCanAcceptBytes(stream)
        self.failUnless(b is True)

        self.failUnlessArgHasType(CFWriteStreamWrite, 1, 'n^v')
        self.failUnlessArgSizeInArg(CFWriteStreamWrite, 1, 2)
        n = CFWriteStreamWrite(stream, "0123456789ABCDE", 15)
        self.assertEquals(n, 15)

        self.assertEquals(a[0], '0')
        self.assertEquals(a[1], '1')
        self.assertEquals(a[9], '9')

        n = CFWriteStreamWrite(stream, "0123456789ABCDE", 15)
        self.assertEquals(n, -1)

        err = CFWriteStreamCopyError(stream)
        self.failUnless(isinstance(err, CFErrorRef))

        err = CFWriteStreamGetError(stream)
        self.failUnless(isinstance(err, CFStreamError))
        self.failUnless(err.domain == kCFStreamErrorDomainPOSIX)
        self.failUnless(err.error == errno.ENOMEM)


        status = CFWriteStreamGetStatus(stream)
        self.failUnless(isinstance(status, (int, long)))
        self.assertEquals(status, kCFStreamStatusError)


        del stream


        self.failUnlessResultIsCFRetained(CFWriteStreamCreateWithAllocatedBuffers)
        stream = CFWriteStreamCreateWithAllocatedBuffers(None, None)
        self.failUnless(isinstance(stream, CFWriteStreamRef))

        r = CFWriteStreamOpen(stream)
        self.failUnless(r is True)

        n = CFWriteStreamWrite(stream, "0123456789ABCDE", 15)
        self.assertEquals(n, 15)

        self.failUnlessResultIsCFRetained(CFWriteStreamCopyProperty)
        buf = CFWriteStreamCopyProperty(stream, kCFStreamPropertyDataWritten)
        self.failUnless(isinstance(buf, CFDataRef))
        buf = CFDataGetBytes(buf, (0, CFDataGetLength(buf)), None)
        self.failUnless(isinstance(buf, str))
        self.assertEquals(buf, '0123456789ABCDE')

        CFWriteStreamClose(stream)
        status = CFWriteStreamGetStatus(stream)
        self.failUnless(isinstance(status, (int, long)))
        self.assertEquals(status, kCFStreamStatusClosed)

        del stream


        stream = CFWriteStreamCreateWithFile(None, 
                CFURLCreateWithString(None, u"file:///tmp/pyobjc.test.txt", None))
        self.failUnless(isinstance(stream, CFWriteStreamRef))

        r = CFWriteStreamOpen(stream)
        self.failUnless(r is True)

        n = CFWriteStreamWrite(stream, "0123456789ABCDE", 15)
        self.assertEquals(n, 15)

        self.failUnlessResultIsCFRetained(CFReadStreamCopyProperty)
        val = CFReadStreamCopyProperty(stream, kCFStreamPropertyFileCurrentOffset)
        self.assertEquals(val, 15)

        self.failUnlessResultIsBOOL(CFReadStreamSetProperty)
        r = CFReadStreamSetProperty(stream, kCFStreamPropertyFileCurrentOffset, 10)
        self.failUnless(r is True)
        val = CFReadStreamCopyProperty(stream, kCFStreamPropertyFileCurrentOffset)
        self.assertEquals(val, 10)

        CFWriteStreamClose(stream)
        status = CFWriteStreamGetStatus(stream)
        self.failUnless(isinstance(status, (int, long)))
        self.assertEquals(status, kCFStreamStatusClosed)

        self.failUnlessResultIsBOOL(CFWriteStreamSetProperty)
        CFWriteStreamSetProperty(stream, kCFStreamPropertyFileCurrentOffset, 0)

        data = open('/tmp/pyobjc.test.txt', 'rb').read()
        self.assertEquals(data, '0123456789ABCDE')
        os.unlink('/tmp/pyobjc.test.txt')

    def testStreamPair(self):

        self.failUnlessArgIsOut(CFStreamCreateBoundPair, 1)
        self.failUnlessArgIsOut(CFStreamCreateBoundPair, 2)
        readStream, writeStream = CFStreamCreateBoundPair(None, None, None, 1024*1024)
        self.failUnless(isinstance(readStream, CFReadStreamRef))
        self.failUnless(isinstance(writeStream, CFWriteStreamRef))

        # Make sure we actually have streams instead of random pointers.
        status = CFReadStreamGetStatus(readStream)
        self.failUnless(isinstance(status, (int, long)))
        self.assertEquals(status, kCFStreamStatusNotOpen)

        status = CFWriteStreamGetStatus(writeStream)
        self.failUnless(isinstance(status, (int, long)))
        self.assertEquals(status, kCFStreamStatusNotOpen)

        del readStream, writeStream

    def testSockets(self):
        sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        sd.connect(('www.apple.com', 80))

        self.failUnlessArgIsOut(CFStreamCreatePairWithSocket, 2)
        self.failUnlessArgIsOut(CFStreamCreatePairWithSocket, 3)
        readStream, writeStream = CFStreamCreatePairWithSocket(None,
                sd.fileno(), None, None)

        status = CFReadStreamGetStatus(readStream)
        self.failUnless(isinstance(status, (int, long)))
        self.assertEquals(status, kCFStreamStatusNotOpen)

        status = CFWriteStreamGetStatus(writeStream)
        self.failUnless(isinstance(status, (int, long)))
        self.assertEquals(status, kCFStreamStatusNotOpen)

        del readStream, writeStream, sd

        self.failUnlessArgIsOut(CFStreamCreatePairWithSocketToHost, 3)
        self.failUnlessArgIsOut(CFStreamCreatePairWithSocketToHost, 4)
        readStream, writeStream = CFStreamCreatePairWithSocketToHost(None,
                "www.apple.com", 80, None, None)

        status = CFReadStreamGetStatus(readStream)
        self.failUnless(isinstance(status, (int, long)))
        self.assertEquals(status, kCFStreamStatusNotOpen)

        status = CFWriteStreamGetStatus(writeStream)
        self.failUnless(isinstance(status, (int, long)))
        self.assertEquals(status, kCFStreamStatusNotOpen)

        del readStream, writeStream


        # Note: I don't expect anyone to actually use this api, building
        # struct sockaddr buffers by hand is madness in python.
        ip = socket.gethostbyname('www.apple.com')
        ip = map(int, ip.split('.'))

        import struct
        sockaddr = struct.pack('>BBHBBBB', 16, socket.AF_INET, 80, *ip)

        signature = CFSocketSignature(
                protocolFamily=socket.AF_INET,
                socketType=socket.SOCK_STREAM,
                protocol=0,
                address=buffer(sockaddr))

        self.failUnlessArgIsOut(CFStreamCreatePairWithPeerSocketSignature, 2)
        self.failUnlessArgIsOut(CFStreamCreatePairWithPeerSocketSignature, 3)
        readStream, writeStream = CFStreamCreatePairWithPeerSocketSignature(
                None, signature, None, None)

        self.failUnlessResultIsCFRetained(CFWriteStreamCopyError)
        status = CFReadStreamGetStatus(readStream)
        self.failUnless(isinstance(status, (int, long)))
        self.assertEquals(status, kCFStreamStatusNotOpen)

        status = CFWriteStreamGetStatus(writeStream)
        self.failUnless(isinstance(status, (int, long)))
        self.assertEquals(status, kCFStreamStatusNotOpen)

    def testReadSocketASync(self):
        rl = CFRunLoopGetCurrent()

        strval = "hello world"
        readStream = CFReadStreamCreateWithBytesNoCopy(None,
                strval, len(strval), kCFAllocatorNull)
        self.failUnless(isinstance(readStream, CFReadStreamRef))

        data = {}

        state = []
        def callback(stream, kind, info):
            state.append((stream, kind, info))

        status = CFReadStreamGetStatus(readStream)
        self.failUnless(isinstance(status, (int, long)))
        self.assertEquals(status, kCFStreamStatusNotOpen)

        CFReadStreamOpen(readStream)
         
        ok = CFReadStreamSetClient(readStream,
                kCFStreamEventHasBytesAvailable | kCFStreamEventErrorOccurred | kCFStreamEventEndEncountered,
                callback, data)
        self.failUnless(ok)

        CFReadStreamScheduleWithRunLoop(readStream, rl, kCFRunLoopDefaultMode)
        try:
            CFRunLoopRunInMode(kCFRunLoopDefaultMode, 1.0, True)
            CFRunLoopWakeUp(rl)
        finally:
            CFReadStreamClose(readStream)
            CFReadStreamUnscheduleFromRunLoop(readStream, rl, kCFRunLoopDefaultMode)
            ok = CFReadStreamSetClient(readStream,
                kCFStreamEventHasBytesAvailable | kCFStreamEventErrorOccurred | kCFStreamEventEndEncountered,
                callback, objc.NULL)
            self.failUnless(ok)

        self.failUnless(len(state) == 1)
        self.failUnless(state[0][0] is readStream)
        self.failUnless(state[0][2] is data)
        self.assertEquals(state[0][1], kCFStreamEventHasBytesAvailable)


    def testWriteSocketAsync(self):
        rl = CFRunLoopGetCurrent()

        import array
        a = array.array('c', " "*20)

        writeStream = CFWriteStreamCreateWithBuffer(None, a, 20)
        self.failUnless(isinstance(writeStream, CFWriteStreamRef))

        r = CFWriteStreamOpen(writeStream)
        self.failUnless(r is True)

        data = {}
        state = []
        def callback(stream, kind, info):
            state.append((stream, kind, info))

        ok = CFWriteStreamSetClient(writeStream,
                kCFStreamEventCanAcceptBytes | kCFStreamEventErrorOccurred | kCFStreamEventEndEncountered,
                callback, data)
        self.failUnless(ok)

        CFWriteStreamScheduleWithRunLoop(writeStream, rl, kCFRunLoopDefaultMode)
        try:
            CFRunLoopRunInMode(kCFRunLoopDefaultMode, 1.0, True)
            CFRunLoopWakeUp(rl)
        finally:
            CFWriteStreamClose(writeStream)
            CFWriteStreamUnscheduleFromRunLoop(writeStream, rl, kCFRunLoopDefaultMode)
            ok = CFWriteStreamSetClient(writeStream,
                kCFStreamEventCanAcceptBytes | kCFStreamEventErrorOccurred | kCFStreamEventEndEncountered,
                callback, objc.NULL)
            self.failUnless(ok)

        self.failUnless(len(state) == 1)
        self.failUnless(state[0][0] is writeStream)
        self.failUnless(state[0][2] is data)
        self.assertEquals(state[0][1], kCFStreamEventCanAcceptBytes)

if __name__ == "__main__":
    main()
