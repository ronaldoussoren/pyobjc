from PyObjCTools.TestSupport import *
from CoreFoundation import *
import errno, time, os, socket, sys
import contextlib

from .test_cfsocket import onTheNetwork

try:
    long
except NameError:
    long = int

try:
    unicode
except NameError:
    unicode = str


class TestStream (TestCase):
    def testTypes(self):
        self.assertIsCFType(CFReadStreamRef)
        self.assertIsCFType(CFWriteStreamRef)

    def testConstants(self):
        self.assertEqual(kCFStreamStatusNotOpen , 0)
        self.assertEqual(kCFStreamStatusOpening , 1)
        self.assertEqual(kCFStreamStatusOpen , 2)
        self.assertEqual(kCFStreamStatusReading , 3)
        self.assertEqual(kCFStreamStatusWriting , 4)
        self.assertEqual(kCFStreamStatusAtEnd , 5)
        self.assertEqual(kCFStreamStatusClosed , 6)
        self.assertEqual(kCFStreamStatusError , 7)
        self.assertEqual(kCFStreamEventNone , 0)
        self.assertEqual(kCFStreamEventOpenCompleted , 1)
        self.assertEqual(kCFStreamEventHasBytesAvailable , 2)
        self.assertEqual(kCFStreamEventCanAcceptBytes , 4)
        self.assertEqual(kCFStreamEventErrorOccurred , 8)
        self.assertEqual(kCFStreamEventEndEncountered , 16)
        self.assertEqual(kCFStreamErrorDomainCustom , -1)
        self.assertEqual(kCFStreamErrorDomainPOSIX , 1)
        self.assertEqual(kCFStreamErrorDomainMacOSStatus , 2)
        self.assertIsInstance(kCFStreamPropertyDataWritten, unicode)
        self.assertIsInstance(kCFStreamPropertyAppendToFile, unicode)
        self.assertIsInstance(kCFStreamPropertyFileCurrentOffset, unicode)
        self.assertIsInstance(kCFStreamPropertySocketNativeHandle, unicode)
        self.assertIsInstance(kCFStreamPropertySocketRemoteHostName, unicode)
        self.assertIsInstance(kCFStreamPropertySocketRemotePortNumber, unicode)

    def testStructs(self):
        o = CFStreamError()
        self.assertHasAttr(o, 'domain')
        self.assertHasAttr(o, 'error')

    def testGetTypeID(self):
        v = CFReadStreamGetTypeID()
        self.assertIsInstance(v, (int, long))
        v = CFWriteStreamGetTypeID()
        self.assertIsInstance(v, (int, long))

    def testReadStream(self):
        strval = b"hello world"
        self.assertArgHasType(CFReadStreamCreateWithBytesNoCopy, 1, b'n^v')
        self.assertArgSizeInArg(CFReadStreamCreateWithBytesNoCopy, 1, 2)
        stream = CFReadStreamCreateWithBytesNoCopy(None,
                strval, len(strval), kCFAllocatorNull)
        self.assertIsInstance(stream, CFReadStreamRef)
        r, buf = CFReadStreamRead(stream, None, 10)
        self.assertEqual(r, -1)
        self.assertEqual(buf, b'')

        self.assertResultIsCFRetained(CFReadStreamCopyError)
        err  = CFReadStreamCopyError(stream)
        if err is not None:
            self.assertIsInstance(err, CFErrorRef)
        status = CFReadStreamGetStatus(stream)
        self.assertIsInstance(status, (int, long))
        self.assertEqual(status, kCFStreamStatusNotOpen)

        self.assertResultIsBOOL(CFReadStreamOpen)
        r = CFReadStreamOpen(stream)
        self.assertIs(r, True)
        status = CFReadStreamGetStatus(stream)
        self.assertIsInstance(status, (int, long))
        self.assertEqual(status, kCFStreamStatusOpen)

        self.assertResultIsBOOL(CFReadStreamHasBytesAvailable)
        r = CFReadStreamHasBytesAvailable(stream)
        self.assertIs(r, True)
        self.assertArgHasType(CFReadStreamRead, 1, b'o^v')
        self.assertArgSizeInArg(CFReadStreamRead, 1, 2)
        self.assertArgSizeInResult(CFReadStreamRead, 1)
        r, buf = CFReadStreamRead(stream, None, 5)
        self.assertEqual(r, 5)
        self.assertEqual(buf, b"hello")

        r, buf = CFReadStreamRead(stream, None, 10)
        self.assertEqual(r, 6)
        self.assertEqual(buf, b" world")

        r = CFReadStreamHasBytesAvailable(stream)
        self.assertIs(r, False)
        r = CFReadStreamClose(stream)
        self.assertIs(r, None)
        status = CFReadStreamGetStatus(stream)
        self.assertIsInstance(status, (int, long))
        self.assertEqual(status, kCFStreamStatusClosed)


        del stream

        self.assertResultIsCFRetained(CFReadStreamCreateWithFile)
        stream = CFReadStreamCreateWithFile(None,
                    CFURLCreateWithString(None, b"file:///etc/shells".decode('ascii'), None))
        self.assertIsInstance(stream, CFReadStreamRef)
        r = CFReadStreamOpen(stream)
        self.assertIs(r, True)
        status = CFReadStreamGetStatus(stream)
        self.assertIsInstance(status, (int, long))
        self.assertEqual(status, kCFStreamStatusOpen)

        r, buf = CFReadStreamRead(stream, None, 5)
        self.assertEqual(r, 5)
        self.assertIsInstance(buf, bytes)
        self.assertResultSizeInArg(CFReadStreamGetBuffer, 2)
        self.assertResultHasType(CFReadStreamGetBuffer, b'^v')
        self.assertArgIsOut(CFReadStreamGetBuffer, 2)
        buf, numBytes = CFReadStreamGetBuffer(stream, 20, None)
        if buf is objc.NULL:
            self.assertEqual(numBytes, 0)
        else:
            self.assertIsInstance(buf, str)
            self.assertEqual(numBytes, len(buf))

        val = CFReadStreamCopyProperty(stream, kCFStreamPropertyFileCurrentOffset)
        self.assertEqual(val, 5)

        r = CFReadStreamSetProperty(stream, kCFStreamPropertyFileCurrentOffset, 10)
        self.assertIs(r, True)
        val = CFReadStreamCopyProperty(stream, kCFStreamPropertyFileCurrentOffset)
        self.assertEqual(val, 10)

        err = CFReadStreamGetError(stream)
        self.assertIsInstance(err, CFStreamError)
        self.assertEqual(err.domain , 0)
        self.assertEqual(err.error , 0)

    def testWriteStream(self):
        import array
        a = array.array('b', b" "*20)

        # XXX: cannot express the actual type as metadata :-(
        self.assertArgHasType(CFWriteStreamCreateWithBuffer, 1, b'n^v')
        self.assertArgSizeInArg(CFWriteStreamCreateWithBuffer, 1, 2)
        stream = CFWriteStreamCreateWithBuffer(None, a, 20)
        self.assertIsInstance(stream, CFWriteStreamRef)
        self.assertResultIsBOOL(CFWriteStreamOpen)
        r = CFWriteStreamOpen(stream)
        self.assertIs(r, True)
        status = CFWriteStreamGetStatus(stream)
        self.assertIsInstance(status, (int, long))
        self.assertEqual(status, kCFStreamStatusOpen)

        self.assertResultIsBOOL(CFWriteStreamCanAcceptBytes)
        b = CFWriteStreamCanAcceptBytes(stream)
        self.assertIs(b, True)
        self.assertArgHasType(CFWriteStreamWrite, 1, b'n^v')
        self.assertArgSizeInArg(CFWriteStreamWrite, 1, 2)
        n = CFWriteStreamWrite(stream, b"0123456789ABCDE", 15)
        self.assertEqual(n, 15)

        if sys.version_info[0] == 3:
            self.assertEqual(bytes(a[0:1]), b'0')
            self.assertEqual(bytes(a[1:2]), b'1')
            self.assertEqual(bytes(a[9:10]), b'9')
        else:
            self.assertEqual((a[0]), ord('0'))
            self.assertEqual((a[1]), ord('1'))
            self.assertEqual((a[9]), ord('9'))

        n = CFWriteStreamWrite(stream, b"0123456789ABCDE", 15)
        self.assertEqual(n, -1)

        err = CFWriteStreamCopyError(stream)
        self.assertIsInstance(err, CFErrorRef)
        err = CFWriteStreamGetError(stream)
        self.assertIsInstance(err, CFStreamError)
        self.assertEqual(err.domain , kCFStreamErrorDomainPOSIX)
        self.assertEqual(err.error , errno.ENOMEM)
        status = CFWriteStreamGetStatus(stream)
        self.assertIsInstance(status, (int, long))
        self.assertEqual(status, kCFStreamStatusError)


        del stream


        self.assertResultIsCFRetained(CFWriteStreamCreateWithAllocatedBuffers)
        stream = CFWriteStreamCreateWithAllocatedBuffers(None, None)
        self.assertIsInstance(stream, CFWriteStreamRef)
        r = CFWriteStreamOpen(stream)
        self.assertIs(r, True)
        n = CFWriteStreamWrite(stream, b"0123456789ABCDE", 15)
        self.assertEqual(n, 15)

        self.assertResultIsCFRetained(CFWriteStreamCopyProperty)
        buf = CFWriteStreamCopyProperty(stream, kCFStreamPropertyDataWritten)
        self.assertIsInstance(buf, CFDataRef)
        buf = CFDataGetBytes(buf, (0, CFDataGetLength(buf)), None)
        self.assertIsInstance(buf, bytes)
        self.assertEqual(buf, b'0123456789ABCDE')

        CFWriteStreamClose(stream)
        status = CFWriteStreamGetStatus(stream)
        self.assertIsInstance(status, (int, long))
        self.assertEqual(status, kCFStreamStatusClosed)

        del stream


        stream = CFWriteStreamCreateWithFile(None,
                CFURLCreateWithString(None, b"file:///tmp/pyobjc.test.txt".decode('ascii'), None))
        self.assertIsInstance(stream, CFWriteStreamRef)
        r = CFWriteStreamOpen(stream)
        self.assertIs(r, True)
        n = CFWriteStreamWrite(stream, b"0123456789ABCDE", 15)
        self.assertEqual(n, 15)

        self.assertResultIsCFRetained(CFReadStreamCopyProperty)
        val = CFReadStreamCopyProperty(stream, kCFStreamPropertyFileCurrentOffset)
        self.assertEqual(val, 15)

        self.assertResultIsBOOL(CFReadStreamSetProperty)
        r = CFReadStreamSetProperty(stream, kCFStreamPropertyFileCurrentOffset, 10)
        self.assertIs(r, True)
        val = CFReadStreamCopyProperty(stream, kCFStreamPropertyFileCurrentOffset)
        self.assertEqual(val, 10)

        CFWriteStreamClose(stream)
        status = CFWriteStreamGetStatus(stream)
        self.assertIsInstance(status, (int, long))
        self.assertEqual(status, kCFStreamStatusClosed)

        self.assertResultIsBOOL(CFWriteStreamSetProperty)
        CFWriteStreamSetProperty(stream, kCFStreamPropertyFileCurrentOffset, 0)

        with open('/tmp/pyobjc.test.txt', 'rb') as fp:
            data = fp.read()
        self.assertEqual(data, b'0123456789ABCDE')
        os.unlink('/tmp/pyobjc.test.txt')

    def testStreamPair(self):

        self.assertArgIsOut(CFStreamCreateBoundPair, 1)
        self.assertArgIsOut(CFStreamCreateBoundPair, 2)
        readStream, writeStream = CFStreamCreateBoundPair(None, None, None, 1024*1024)
        self.assertIsInstance(readStream, CFReadStreamRef)
        self.assertIsInstance(writeStream, CFWriteStreamRef)
        # Make sure we actually have streams instead of random pointers.
        status = CFReadStreamGetStatus(readStream)
        self.assertIsInstance(status, (int, long))
        self.assertEqual(status, kCFStreamStatusNotOpen)

        status = CFWriteStreamGetStatus(writeStream)
        self.assertIsInstance(status, (int, long))
        self.assertEqual(status, kCFStreamStatusNotOpen)

        del readStream, writeStream

    @onlyIf(onTheNetwork)
    def testSockets(self):
        with contextlib.closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sd:
            sd.connect(('www.apple.com', 80))

            self.assertArgIsOut(CFStreamCreatePairWithSocket, 2)
            self.assertArgIsOut(CFStreamCreatePairWithSocket, 3)
            readStream, writeStream = CFStreamCreatePairWithSocket(None,
                    sd.fileno(), None, None)

            status = CFReadStreamGetStatus(readStream)
            self.assertIsInstance(status, (int, long))
            self.assertEqual(status, kCFStreamStatusNotOpen)

            status = CFWriteStreamGetStatus(writeStream)
            self.assertIsInstance(status, (int, long))
            self.assertEqual(status, kCFStreamStatusNotOpen)

            del readStream, writeStream, sd

        self.assertArgIsOut(CFStreamCreatePairWithSocketToHost, 3)
        self.assertArgIsOut(CFStreamCreatePairWithSocketToHost, 4)
        readStream, writeStream = CFStreamCreatePairWithSocketToHost(None,
                "www.apple.com", 80, None, None)

        status = CFReadStreamGetStatus(readStream)
        self.assertIsInstance(status, (int, long))
        self.assertEqual(status, kCFStreamStatusNotOpen)

        status = CFWriteStreamGetStatus(writeStream)
        self.assertIsInstance(status, (int, long))
        self.assertEqual(status, kCFStreamStatusNotOpen)

        del readStream, writeStream


        # Note: I don't expect anyone to actually use this api, building
        # struct sockaddr buffers by hand is madness in python.
        ip = socket.gethostbyname('www.apple.com')
        ip = map(int, ip.split('.'))

        import struct
        sockaddr = struct.pack('>BBHBBBB', 16, socket.AF_INET, 80, *ip)

        if sys.version_info[0] == 3:
            sockaddr_buffer = sockaddr
        else:
            sockaddr_buffer = buffer(sockaddr)

        signature = CFSocketSignature(
                protocolFamily=socket.AF_INET,
                socketType=socket.SOCK_STREAM,
                protocol=0,
                address=sockaddr_buffer)

        self.assertArgIsOut(CFStreamCreatePairWithPeerSocketSignature, 2)
        self.assertArgIsOut(CFStreamCreatePairWithPeerSocketSignature, 3)
        readStream, writeStream = CFStreamCreatePairWithPeerSocketSignature(
                None, signature, None, None)

        self.assertResultIsCFRetained(CFWriteStreamCopyError)
        status = CFReadStreamGetStatus(readStream)
        self.assertIsInstance(status, (int, long))
        self.assertEqual(status, kCFStreamStatusNotOpen)

        status = CFWriteStreamGetStatus(writeStream)
        self.assertIsInstance(status, (int, long))
        self.assertEqual(status, kCFStreamStatusNotOpen)

    def testReadSocketASync(self):
        rl = CFRunLoopGetCurrent()

        strval = b"hello world"
        readStream = CFReadStreamCreateWithBytesNoCopy(None,
                strval, len(strval), kCFAllocatorNull)
        self.assertIsInstance(readStream, CFReadStreamRef)
        data = {}

        state = []
        def callback(stream, kind, info):
            state.append((stream, kind, info))

        status = CFReadStreamGetStatus(readStream)
        self.assertIsInstance(status, (int, long))
        self.assertEqual(status, kCFStreamStatusNotOpen)

        CFReadStreamOpen(readStream)

        ok = CFReadStreamSetClient(readStream,
                kCFStreamEventHasBytesAvailable | kCFStreamEventErrorOccurred | kCFStreamEventEndEncountered,
                callback, data)
        self.assertTrue(ok)

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
            self.assertTrue(ok)

        self.assertEqual(len(state) , 1)
        self.assertIs(state[0][0], readStream)
        self.assertIs(state[0][2], data)
        self.assertEqual(state[0][1], kCFStreamEventHasBytesAvailable)


    def testWriteSocketAsync(self):
        rl = CFRunLoopGetCurrent()

        import array
        a = array.array('b', b" "*20)

        writeStream = CFWriteStreamCreateWithBuffer(None, a, 20)
        self.assertIsInstance(writeStream, CFWriteStreamRef)
        r = CFWriteStreamOpen(writeStream)
        self.assertIs(r, True)
        data = {}
        state = []
        def callback(stream, kind, info):
            state.append((stream, kind, info))

        ok = CFWriteStreamSetClient(writeStream,
                kCFStreamEventCanAcceptBytes | kCFStreamEventErrorOccurred | kCFStreamEventEndEncountered,
                callback, data)
        self.assertTrue(ok)

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
            self.assertTrue(ok)

        self.assertEqual(len(state) , 1)
        self.assertIs(state[0][0], writeStream)
        self.assertIs(state[0][2], data)
        self.assertEqual(state[0][1], kCFStreamEventCanAcceptBytes)

if __name__ == "__main__":
    main()
