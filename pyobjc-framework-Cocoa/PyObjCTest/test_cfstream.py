import contextlib
import errno
import os
import socket
import sys

import CoreFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level, skipUnless
import objc

from .test_cfsocket import onTheNetwork


class TestStream(TestCase):
    def testTypes(self):
        try:
            if (
                objc.lookUpClass("__NSCFInputStream")
                is not CoreFoundation.CFReadStreamRef
            ):
                self.assertIsCFType(CoreFoundation.CFReadStreamRef)
        except objc.error:
            try:
                if (
                    objc.lookUpClass("NSCFInputStream")
                    is not CoreFoundation.CFReadStreamRef
                ):
                    self.assertIsCFType(CoreFoundation.CFReadStreamRef)
            except objc.error:
                self.assertIsCFType(CoreFoundation.CFReadStreamRef)

        try:
            if (
                objc.lookUpClass("__NSCFOutputStream")
                is not CoreFoundation.CFWriteStreamRef
            ):
                self.assertIsCFType(CoreFoundation.CFWriteStreamRef)
        except objc.error:
            try:
                if (
                    objc.lookUpClass("NSCFOutputStream")
                    is not CoreFoundation.CFWriteStreamRef
                ):
                    self.assertIsCFType(CoreFoundation.CFWriteStreamRef)
            except objc.error:
                self.assertIsCFType(CoreFoundation.CFWriteStreamRef)

    def testConstants(self):
        self.assertEqual(CoreFoundation.kCFStreamStatusNotOpen, 0)
        self.assertEqual(CoreFoundation.kCFStreamStatusOpening, 1)
        self.assertEqual(CoreFoundation.kCFStreamStatusOpen, 2)
        self.assertEqual(CoreFoundation.kCFStreamStatusReading, 3)
        self.assertEqual(CoreFoundation.kCFStreamStatusWriting, 4)
        self.assertEqual(CoreFoundation.kCFStreamStatusAtEnd, 5)
        self.assertEqual(CoreFoundation.kCFStreamStatusClosed, 6)
        self.assertEqual(CoreFoundation.kCFStreamStatusError, 7)
        self.assertEqual(CoreFoundation.kCFStreamEventNone, 0)
        self.assertEqual(CoreFoundation.kCFStreamEventOpenCompleted, 1)
        self.assertEqual(CoreFoundation.kCFStreamEventHasBytesAvailable, 2)
        self.assertEqual(CoreFoundation.kCFStreamEventCanAcceptBytes, 4)
        self.assertEqual(CoreFoundation.kCFStreamEventErrorOccurred, 8)
        self.assertEqual(CoreFoundation.kCFStreamEventEndEncountered, 16)
        self.assertEqual(CoreFoundation.kCFStreamErrorDomainCustom, -1)
        self.assertEqual(CoreFoundation.kCFStreamErrorDomainPOSIX, 1)
        self.assertEqual(CoreFoundation.kCFStreamErrorDomainMacOSStatus, 2)
        self.assertIsInstance(CoreFoundation.kCFStreamPropertyDataWritten, str)
        self.assertIsInstance(CoreFoundation.kCFStreamPropertyAppendToFile, str)
        self.assertIsInstance(CoreFoundation.kCFStreamPropertyFileCurrentOffset, str)
        self.assertIsInstance(CoreFoundation.kCFStreamPropertySocketNativeHandle, str)
        self.assertIsInstance(CoreFoundation.kCFStreamPropertySocketRemoteHostName, str)
        self.assertIsInstance(
            CoreFoundation.kCFStreamPropertySocketRemotePortNumber, str
        )

        self.assertIsInstance(CoreFoundation.kCFStreamErrorDomainSOCKS, int)
        self.assertIsInstance(CoreFoundation.kCFStreamPropertySOCKSProxy, str)
        self.assertIsInstance(CoreFoundation.kCFStreamPropertySOCKSProxyHost, str)
        self.assertIsInstance(CoreFoundation.kCFStreamPropertySOCKSProxyPort, str)
        self.assertIsInstance(CoreFoundation.kCFStreamPropertySOCKSVersion, str)
        self.assertIsInstance(CoreFoundation.kCFStreamSocketSOCKSVersion4, str)
        self.assertIsInstance(CoreFoundation.kCFStreamSocketSOCKSVersion5, str)
        self.assertIsInstance(CoreFoundation.kCFStreamPropertySOCKSUser, str)
        self.assertIsInstance(CoreFoundation.kCFStreamPropertySOCKSPassword, str)
        self.assertIsInstance(CoreFoundation.kCFStreamErrorDomainSSL, int)
        self.assertIsInstance(CoreFoundation.kCFStreamPropertySocketSecurityLevel, str)
        self.assertIsInstance(CoreFoundation.kCFStreamSocketSecurityLevelNone, str)
        self.assertIsInstance(CoreFoundation.kCFStreamSocketSecurityLevelSSLv2, str)
        self.assertIsInstance(CoreFoundation.kCFStreamSocketSecurityLevelSSLv3, str)
        self.assertIsInstance(CoreFoundation.kCFStreamSocketSecurityLevelTLSv1, str)
        self.assertIsInstance(
            CoreFoundation.kCFStreamSocketSecurityLevelNegotiatedSSL, str
        )
        self.assertIsInstance(
            CoreFoundation.kCFStreamPropertyShouldCloseNativeSocket, str
        )

    def testStructs(self):
        o = CoreFoundation.CFStreamError()
        self.assertHasAttr(o, "domain")
        self.assertHasAttr(o, "error")

        self.assertPickleRoundTrips(o)

    def testGetTypeID(self):
        v = CoreFoundation.CFReadStreamGetTypeID()
        self.assertIsInstance(v, int)
        v = CoreFoundation.CFWriteStreamGetTypeID()
        self.assertIsInstance(v, int)

    def testReadStream(self):
        strval = b"hello world"
        self.assertArgHasType(
            CoreFoundation.CFReadStreamCreateWithBytesNoCopy, 1, b"n^v"
        )
        self.assertArgSizeInArg(CoreFoundation.CFReadStreamCreateWithBytesNoCopy, 1, 2)
        stream = CoreFoundation.CFReadStreamCreateWithBytesNoCopy(
            None, strval, len(strval), CoreFoundation.kCFAllocatorNull
        )
        self.assertIsInstance(stream, CoreFoundation.CFReadStreamRef)
        r, buf = CoreFoundation.CFReadStreamRead(stream, None, 10)
        self.assertEqual(r, -1)
        self.assertEqual(buf, b"")

        self.assertResultIsCFRetained(CoreFoundation.CFReadStreamCopyError)
        err = CoreFoundation.CFReadStreamCopyError(stream)
        if err is not None:
            self.assertIsInstance(err, CoreFoundation.CFErrorRef)
        status = CoreFoundation.CFReadStreamGetStatus(stream)
        self.assertIsInstance(status, int)
        self.assertEqual(status, CoreFoundation.kCFStreamStatusNotOpen)

        self.assertResultIsBOOL(CoreFoundation.CFReadStreamOpen)
        r = CoreFoundation.CFReadStreamOpen(stream)
        self.assertIs(r, True)
        status = CoreFoundation.CFReadStreamGetStatus(stream)
        self.assertIsInstance(status, int)
        self.assertEqual(status, CoreFoundation.kCFStreamStatusOpen)

        self.assertResultIsBOOL(CoreFoundation.CFReadStreamHasBytesAvailable)
        r = CoreFoundation.CFReadStreamHasBytesAvailable(stream)
        self.assertIs(r, True)
        self.assertArgHasType(CoreFoundation.CFReadStreamRead, 1, b"o^v")
        self.assertArgSizeInArg(CoreFoundation.CFReadStreamRead, 1, 2)
        self.assertArgSizeInResult(CoreFoundation.CFReadStreamRead, 1)
        r, buf = CoreFoundation.CFReadStreamRead(stream, None, 5)
        self.assertEqual(r, 5)
        self.assertEqual(buf, b"hello")

        r, buf = CoreFoundation.CFReadStreamRead(stream, None, 10)
        self.assertEqual(r, 6)
        self.assertEqual(buf, b" world")

        r = CoreFoundation.CFReadStreamHasBytesAvailable(stream)
        self.assertIs(r, False)
        r = CoreFoundation.CFReadStreamClose(stream)
        self.assertIs(r, None)
        status = CoreFoundation.CFReadStreamGetStatus(stream)
        self.assertIsInstance(status, int)
        self.assertEqual(status, CoreFoundation.kCFStreamStatusClosed)

        del stream

        self.assertResultIsCFRetained(CoreFoundation.CFReadStreamCreateWithFile)
        stream = CoreFoundation.CFReadStreamCreateWithFile(
            None, CoreFoundation.CFURLCreateWithString(None, "file:///etc/shells", None)
        )
        self.assertIsInstance(stream, CoreFoundation.CFReadStreamRef)
        r = CoreFoundation.CFReadStreamOpen(stream)
        self.assertIs(r, True)
        status = CoreFoundation.CFReadStreamGetStatus(stream)
        self.assertIsInstance(status, int)
        self.assertEqual(status, CoreFoundation.kCFStreamStatusOpen)

        r, buf = CoreFoundation.CFReadStreamRead(stream, None, 5)
        self.assertEqual(r, 5)
        self.assertIsInstance(buf, bytes)
        self.assertResultSizeInArg(CoreFoundation.CFReadStreamGetBuffer, 2)
        self.assertResultHasType(CoreFoundation.CFReadStreamGetBuffer, b"^v")
        self.assertArgIsOut(CoreFoundation.CFReadStreamGetBuffer, 2)
        buf, numBytes = CoreFoundation.CFReadStreamGetBuffer(stream, 20, None)
        if buf is objc.NULL:
            self.assertEqual(numBytes, 0)
        else:
            self.assertIsInstance(buf, str)
            self.assertEqual(numBytes, len(buf))

        val = CoreFoundation.CFReadStreamCopyProperty(
            stream, CoreFoundation.kCFStreamPropertyFileCurrentOffset
        )
        self.assertEqual(val, 5)

        r = CoreFoundation.CFReadStreamSetProperty(
            stream, CoreFoundation.kCFStreamPropertyFileCurrentOffset, 10
        )
        self.assertIs(r, True)
        val = CoreFoundation.CFReadStreamCopyProperty(
            stream, CoreFoundation.kCFStreamPropertyFileCurrentOffset
        )
        self.assertEqual(val, 10)

        err = CoreFoundation.CFReadStreamGetError(stream)
        self.assertIsInstance(err, CoreFoundation.CFStreamError)
        self.assertEqual(err.domain, 0)
        self.assertEqual(err.error, 0)

    def testWriteStream(self):
        import array

        a = array.array("b", b" " * 20)

        # XXX: cannot express the actual type as metadata :-(
        self.assertArgHasType(CoreFoundation.CFWriteStreamCreateWithBuffer, 1, b"n^v")
        self.assertArgSizeInArg(CoreFoundation.CFWriteStreamCreateWithBuffer, 1, 2)
        stream = CoreFoundation.CFWriteStreamCreateWithBuffer(None, a, 20)
        self.assertIsInstance(stream, CoreFoundation.CFWriteStreamRef)
        self.assertResultIsBOOL(CoreFoundation.CFWriteStreamOpen)
        r = CoreFoundation.CFWriteStreamOpen(stream)
        self.assertIs(r, True)
        status = CoreFoundation.CFWriteStreamGetStatus(stream)
        self.assertIsInstance(status, int)
        self.assertEqual(status, CoreFoundation.kCFStreamStatusOpen)

        self.assertResultIsBOOL(CoreFoundation.CFWriteStreamCanAcceptBytes)
        b = CoreFoundation.CFWriteStreamCanAcceptBytes(stream)
        self.assertIs(b, True)
        self.assertArgHasType(CoreFoundation.CFWriteStreamWrite, 1, b"n^v")
        self.assertArgSizeInArg(CoreFoundation.CFWriteStreamWrite, 1, 2)
        n = CoreFoundation.CFWriteStreamWrite(stream, b"0123456789ABCDE", 15)
        self.assertEqual(n, 15)

        if sys.version_info[0] == 3:
            self.assertEqual(bytes(a[0:1]), b"0")
            self.assertEqual(bytes(a[1:2]), b"1")
            self.assertEqual(bytes(a[9:10]), b"9")
        else:
            self.assertEqual((a[0]), ord("0"))
            self.assertEqual((a[1]), ord("1"))
            self.assertEqual((a[9]), ord("9"))

        n = CoreFoundation.CFWriteStreamWrite(stream, b"0123456789ABCDE", 15)
        self.assertEqual(n, -1)

        err = CoreFoundation.CFWriteStreamCopyError(stream)
        self.assertIsInstance(err, CoreFoundation.CFErrorRef)
        err = CoreFoundation.CFWriteStreamGetError(stream)
        self.assertIsInstance(err, CoreFoundation.CFStreamError)
        self.assertEqual(err.domain, CoreFoundation.kCFStreamErrorDomainPOSIX)
        self.assertEqual(err.error, errno.ENOMEM)
        status = CoreFoundation.CFWriteStreamGetStatus(stream)
        self.assertIsInstance(status, int)
        self.assertEqual(status, CoreFoundation.kCFStreamStatusError)

        del stream

        self.assertResultIsCFRetained(
            CoreFoundation.CFWriteStreamCreateWithAllocatedBuffers
        )
        stream = CoreFoundation.CFWriteStreamCreateWithAllocatedBuffers(None, None)
        self.assertIsInstance(stream, CoreFoundation.CFWriteStreamRef)
        r = CoreFoundation.CFWriteStreamOpen(stream)
        self.assertIs(r, True)
        n = CoreFoundation.CFWriteStreamWrite(stream, b"0123456789ABCDE", 15)
        self.assertEqual(n, 15)

        self.assertResultIsCFRetained(CoreFoundation.CFWriteStreamCopyProperty)
        buf = CoreFoundation.CFWriteStreamCopyProperty(
            stream, CoreFoundation.kCFStreamPropertyDataWritten
        )
        self.assertIsInstance(buf, CoreFoundation.CFDataRef)
        buf = CoreFoundation.CFDataGetBytes(
            buf, (0, CoreFoundation.CFDataGetLength(buf)), None
        )
        self.assertIsInstance(buf, bytes)
        self.assertEqual(buf, b"0123456789ABCDE")

        CoreFoundation.CFWriteStreamClose(stream)
        status = CoreFoundation.CFWriteStreamGetStatus(stream)
        self.assertIsInstance(status, int)
        self.assertEqual(status, CoreFoundation.kCFStreamStatusClosed)

        del stream

        stream = CoreFoundation.CFWriteStreamCreateWithFile(
            None,
            CoreFoundation.CFURLCreateWithString(
                None, "file:///tmp/pyobjc.test.txt", None
            ),
        )
        self.assertIsInstance(stream, CoreFoundation.CFWriteStreamRef)
        r = CoreFoundation.CFWriteStreamOpen(stream)
        self.assertIs(r, True)
        n = CoreFoundation.CFWriteStreamWrite(stream, b"0123456789ABCDE", 15)
        self.assertEqual(n, 15)

        self.assertResultIsCFRetained(CoreFoundation.CFReadStreamCopyProperty)
        val = CoreFoundation.CFReadStreamCopyProperty(
            stream, CoreFoundation.kCFStreamPropertyFileCurrentOffset
        )
        self.assertEqual(val, 15)

        self.assertResultIsBOOL(CoreFoundation.CFReadStreamSetProperty)
        r = CoreFoundation.CFReadStreamSetProperty(
            stream, CoreFoundation.kCFStreamPropertyFileCurrentOffset, 10
        )
        self.assertIs(r, True)
        val = CoreFoundation.CFReadStreamCopyProperty(
            stream, CoreFoundation.kCFStreamPropertyFileCurrentOffset
        )
        self.assertEqual(val, 10)

        CoreFoundation.CFWriteStreamClose(stream)
        status = CoreFoundation.CFWriteStreamGetStatus(stream)
        self.assertIsInstance(status, int)
        self.assertEqual(status, CoreFoundation.kCFStreamStatusClosed)

        self.assertResultIsBOOL(CoreFoundation.CFWriteStreamSetProperty)
        CoreFoundation.CFWriteStreamSetProperty(
            stream, CoreFoundation.kCFStreamPropertyFileCurrentOffset, 0
        )

        with open("/tmp/pyobjc.test.txt", "rb") as fp:
            data = fp.read()
        self.assertEqual(data, b"0123456789ABCDE")
        os.unlink("/tmp/pyobjc.test.txt")

    def testStreamPair(self):

        self.assertArgIsOut(CoreFoundation.CFStreamCreateBoundPair, 1)
        self.assertArgIsOut(CoreFoundation.CFStreamCreateBoundPair, 2)
        readStream, writeStream = CoreFoundation.CFStreamCreateBoundPair(
            None, None, None, 1024 * 1024
        )
        self.assertIsInstance(readStream, CoreFoundation.CFReadStreamRef)
        self.assertIsInstance(writeStream, CoreFoundation.CFWriteStreamRef)
        # Make sure we actually have streams instead of random pointers.
        status = CoreFoundation.CFReadStreamGetStatus(readStream)
        self.assertIsInstance(status, int)
        self.assertEqual(status, CoreFoundation.kCFStreamStatusNotOpen)

        status = CoreFoundation.CFWriteStreamGetStatus(writeStream)
        self.assertIsInstance(status, int)
        self.assertEqual(status, CoreFoundation.kCFStreamStatusNotOpen)

        del readStream, writeStream

    @skipUnless(onTheNetwork(), "Test requires a working Internet connection")
    def testSockets(self):
        with contextlib.closing(
            socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ) as sd:
            sd.connect(("www.apple.com", 80))

            self.assertArgIsOut(CoreFoundation.CFStreamCreatePairWithSocket, 2)
            self.assertArgIsOut(CoreFoundation.CFStreamCreatePairWithSocket, 3)
            readStream, writeStream = CoreFoundation.CFStreamCreatePairWithSocket(
                None, sd.fileno(), None, None
            )

            status = CoreFoundation.CFReadStreamGetStatus(readStream)
            self.assertIsInstance(status, int)
            self.assertEqual(status, CoreFoundation.kCFStreamStatusNotOpen)

            status = CoreFoundation.CFWriteStreamGetStatus(writeStream)
            self.assertIsInstance(status, int)
            self.assertEqual(status, CoreFoundation.kCFStreamStatusNotOpen)

            del readStream, writeStream, sd

        self.assertArgIsOut(CoreFoundation.CFStreamCreatePairWithSocketToHost, 3)
        self.assertArgIsOut(CoreFoundation.CFStreamCreatePairWithSocketToHost, 4)
        readStream, writeStream = CoreFoundation.CFStreamCreatePairWithSocketToHost(
            None, "www.apple.com", 80, None, None
        )

        status = CoreFoundation.CFReadStreamGetStatus(readStream)
        self.assertIsInstance(status, int)
        self.assertEqual(status, CoreFoundation.kCFStreamStatusNotOpen)

        status = CoreFoundation.CFWriteStreamGetStatus(writeStream)
        self.assertIsInstance(status, int)
        self.assertEqual(status, CoreFoundation.kCFStreamStatusNotOpen)

        del readStream, writeStream

        # Note: I don't expect anyone to actually use this api, building
        # struct sockaddr buffers by hand is madness in python.
        ip = socket.gethostbyname("www.apple.com")
        ip = map(int, ip.split("."))

        import struct

        sockaddr = struct.pack(">BBHBBBB", 16, socket.AF_INET, 80, *ip)

        signature = CoreFoundation.CFSocketSignature(
            protocolFamily=socket.AF_INET,
            socketType=socket.SOCK_STREAM,
            protocol=0,
            address=sockaddr,
        )

        self.assertArgIsOut(CoreFoundation.CFStreamCreatePairWithPeerSocketSignature, 2)
        self.assertArgIsOut(CoreFoundation.CFStreamCreatePairWithPeerSocketSignature, 3)
        (
            readStream,
            writeStream,
        ) = CoreFoundation.CFStreamCreatePairWithPeerSocketSignature(
            None, signature, None, None
        )

        self.assertResultIsCFRetained(CoreFoundation.CFWriteStreamCopyError)
        status = CoreFoundation.CFReadStreamGetStatus(readStream)
        self.assertIsInstance(status, int)
        self.assertEqual(status, CoreFoundation.kCFStreamStatusNotOpen)

        status = CoreFoundation.CFWriteStreamGetStatus(writeStream)
        self.assertIsInstance(status, int)
        self.assertEqual(status, CoreFoundation.kCFStreamStatusNotOpen)

    def testReadSocketASync(self):
        rl = CoreFoundation.CFRunLoopGetCurrent()

        strval = b"hello world"
        readStream = CoreFoundation.CFReadStreamCreateWithBytesNoCopy(
            None, strval, len(strval), CoreFoundation.kCFAllocatorNull
        )
        self.assertIsInstance(readStream, CoreFoundation.CFReadStreamRef)
        data = {}

        state = []

        def callback(stream, kind, info):
            state.append((stream, kind, info))

        status = CoreFoundation.CFReadStreamGetStatus(readStream)
        self.assertIsInstance(status, int)
        self.assertEqual(status, CoreFoundation.kCFStreamStatusNotOpen)

        CoreFoundation.CFReadStreamOpen(readStream)

        ok = CoreFoundation.CFReadStreamSetClient(
            readStream,
            CoreFoundation.kCFStreamEventHasBytesAvailable
            | CoreFoundation.kCFStreamEventErrorOccurred
            | CoreFoundation.kCFStreamEventEndEncountered,
            callback,
            data,
        )
        self.assertTrue(ok)

        CoreFoundation.CFReadStreamScheduleWithRunLoop(
            readStream, rl, CoreFoundation.kCFRunLoopDefaultMode
        )
        try:
            CoreFoundation.CFRunLoopRunInMode(
                CoreFoundation.kCFRunLoopDefaultMode, 1.0, True
            )
            CoreFoundation.CFRunLoopWakeUp(rl)
        finally:
            CoreFoundation.CFReadStreamClose(readStream)
            CoreFoundation.CFReadStreamUnscheduleFromRunLoop(
                readStream, rl, CoreFoundation.kCFRunLoopDefaultMode
            )
            ok = CoreFoundation.CFReadStreamSetClient(
                readStream,
                CoreFoundation.kCFStreamEventHasBytesAvailable
                | CoreFoundation.kCFStreamEventErrorOccurred
                | CoreFoundation.kCFStreamEventEndEncountered,
                callback,
                objc.NULL,
            )
            self.assertTrue(ok)

        self.assertEqual(len(state), 1)
        self.assertIs(state[0][0], readStream)
        self.assertIs(state[0][2], data)
        self.assertEqual(state[0][1], CoreFoundation.kCFStreamEventHasBytesAvailable)

    def testWriteSocketAsync(self):
        rl = CoreFoundation.CFRunLoopGetCurrent()

        import array

        a = array.array("b", b" " * 20)

        writeStream = CoreFoundation.CFWriteStreamCreateWithBuffer(None, a, 20)
        self.assertIsInstance(writeStream, CoreFoundation.CFWriteStreamRef)
        r = CoreFoundation.CFWriteStreamOpen(writeStream)
        self.assertIs(r, True)
        data = {}
        state = []

        def callback(stream, kind, info):
            state.append((stream, kind, info))

        ok = CoreFoundation.CFWriteStreamSetClient(
            writeStream,
            CoreFoundation.kCFStreamEventCanAcceptBytes
            | CoreFoundation.kCFStreamEventErrorOccurred
            | CoreFoundation.kCFStreamEventEndEncountered,
            callback,
            data,
        )
        self.assertTrue(ok)

        CoreFoundation.CFWriteStreamScheduleWithRunLoop(
            writeStream, rl, CoreFoundation.kCFRunLoopDefaultMode
        )
        try:
            CoreFoundation.CFRunLoopRunInMode(
                CoreFoundation.kCFRunLoopDefaultMode, 1.0, True
            )
            CoreFoundation.CFRunLoopWakeUp(rl)
        finally:
            CoreFoundation.CFWriteStreamClose(writeStream)
            CoreFoundation.CFWriteStreamUnscheduleFromRunLoop(
                writeStream, rl, CoreFoundation.kCFRunLoopDefaultMode
            )
            ok = CoreFoundation.CFWriteStreamSetClient(
                writeStream,
                CoreFoundation.kCFStreamEventCanAcceptBytes
                | CoreFoundation.kCFStreamEventErrorOccurred
                | CoreFoundation.kCFStreamEventEndEncountered,
                callback,
                objc.NULL,
            )
            self.assertTrue(ok)

        self.assertEqual(len(state), 1)
        self.assertIs(state[0][0], writeStream)
        self.assertIs(state[0][2], data)
        self.assertEqual(state[0][1], CoreFoundation.kCFStreamEventCanAcceptBytes)

    @min_os_level("10.9")
    def testFunctions10_9(self):
        CoreFoundation.CFReadStreamSetDispatchQueue  # Nothing to test
        CoreFoundation.CFWriteStreamSetDispatchQueue  # Nothing to test
        CoreFoundation.CFReadStreamCopyDispatchQueue  # Nothing to test
        CoreFoundation.CFWriteStreamCopyDispatchQueue  # Nothing to test
