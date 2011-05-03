from PyObjCTools.TestSupport import *
import socket, time, struct
from CoreFoundation import *
import CoreFoundation
import sys

def onTheNetwork():
    try:
        socket.gethostbyname('www.apple.com')

    except socket.gaierror:
        return False

    return True


class TestSocket (TestCase):
    def testTypes(self):
        self.assertIsCFType(CFSocketRef)

    def testTypeID(self):
        self.assertIsInstance(CFSocketGetTypeID(), (int, long))
    def testConstants(self):
        self.assertEqual(kCFSocketSuccess , 0)
        self.assertEqual(kCFSocketError , -1)
        self.assertEqual(kCFSocketTimeout , -2)
        self.assertEqual(kCFSocketNoCallBack , 0)
        self.assertEqual(kCFSocketReadCallBack , 1)
        self.assertEqual(kCFSocketAcceptCallBack , 2)
        self.assertEqual(kCFSocketDataCallBack , 3)
        self.assertEqual(kCFSocketConnectCallBack , 4)
        self.assertEqual(kCFSocketWriteCallBack , 8)
        self.assertEqual(kCFSocketAutomaticallyReenableReadCallBack , 1)
        self.assertEqual(kCFSocketAutomaticallyReenableAcceptCallBack , 2)
        self.assertEqual(kCFSocketAutomaticallyReenableDataCallBack , 3)
        self.assertEqual(kCFSocketAutomaticallyReenableWriteCallBack , 8)
        self.assertEqual(kCFSocketCloseOnInvalidate , 128)
        self.assertIsInstance(kCFSocketCommandKey, unicode)
        self.assertIsInstance(kCFSocketNameKey, unicode)
        self.assertIsInstance(kCFSocketValueKey, unicode)
        self.assertIsInstance(kCFSocketResultKey, unicode)
        self.assertIsInstance(kCFSocketErrorKey, unicode)
        self.assertIsInstance(kCFSocketRegisterCommand, unicode)
        self.assertIsInstance(kCFSocketRetrieveCommand, unicode)
        self.assertEqual(kCFSocketLeaveErrors, 64)


    def testStructs(self):
        o = CFSocketSignature()
        self.assertHasAttr(o, 'protocolFamily')
        self.assertHasAttr(o, 'socketType')
        self.assertHasAttr(o, 'protocol')
        self.assertHasAttr(o, 'address')
    def testNameRegistry(self):
        p1 = CFSocketGetDefaultNameRegistryPortNumber()
        self.assertIsInstance(p1, (int, long))
        CFSocketSetDefaultNameRegistryPortNumber(p1+1)
        p2 = CFSocketGetDefaultNameRegistryPortNumber()
        self.assertIsInstance(p2, (int, long))
        self.assertEqual(p2, p1+1)

        CFSocketSetDefaultNameRegistryPortNumber(p1)


    @onlyIf(onTheNetwork(), "cannot test without internet connection")
    def testSocketFunctions(self):
        data = {}
        state = []
        def callback(sock, kind, address, data, info):
            state.append((sock, kind, address, data, info))

        sock = CFSocketCreate(None, socket.AF_INET, socket.SOCK_STREAM, 0,
                kCFSocketReadCallBack|kCFSocketWriteCallBack,
                callback, data)
        self.assertIsInstance(sock, CFSocketRef)
        localaddr = struct.pack('>BBHBBBB', 16, socket.AF_INET, 9425, 127, 0, 0, 1)
        localaddr += b'\0' * 8
        if sys.version_info[0] == 2:
            localaddr = buffer(localaddr)
        err = CFSocketSetAddress(sock, localaddr)
        self.assertEqual(err, kCFSocketSuccess)


        sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        sock = CFSocketCreateWithNative(None, sd.fileno(),
                kCFSocketReadCallBack|kCFSocketWriteCallBack,
                callback, data)
        self.assertIsInstance(sock, CFSocketRef)
        n = CFSocketGetNative(sock)
        self.assertIsInstance(n, (int, long))
        self.assertEqual(n, sd.fileno())


    
        ctx = CFSocketGetContext(sock, None)
        self.assertIs(ctx, data)
        flags = CFSocketGetSocketFlags(sock)
        self.assertIsInstance(flags, (int, long))
        CFSocketSetSocketFlags(sock, kCFSocketAutomaticallyReenableReadCallBack|kCFSocketAutomaticallyReenableAcceptCallBack)
        flags2 = CFSocketGetSocketFlags(sock)
        self.assertIsInstance(flags2, (int, long))
        self.assertEqual(flags2, kCFSocketAutomaticallyReenableReadCallBack|kCFSocketAutomaticallyReenableAcceptCallBack)


        # Note: I don't expect anyone to actually use this api, building
        # struct sockaddr buffers by hand is madness in python.
        ip = socket.gethostbyname('www.apple.com')
        ip = map(int, ip.split('.'))

        sockaddr = struct.pack('>BBHBBBB', 16, socket.AF_INET, 80, *ip)
        sockaddr += b'\0' * 8
        if sys.version_info[0] == 2:
            sockaddr = buffer(sockaddr)

        e = CFSocketConnectToAddress(sock, sockaddr, 1.0)
        self.assertIsInstance(e, (int, long))
        self.assertEqual(e, kCFSocketSuccess)


        self.assertResultIsCFRetained(CFSocketCopyPeerAddress)
        addr = CFSocketCopyPeerAddress(sock)
        self.assertIsInstance(addr, CFDataRef)
        self.assertResultIsCFRetained(CFSocketCopyAddress)
        addr = CFSocketCopyAddress(sock)
        self.assertIsInstance(addr, CFDataRef)
        CFSocketDisableCallBacks(sock, kCFSocketReadCallBack|kCFSocketAcceptCallBack)
        CFSocketEnableCallBacks(sock, kCFSocketReadCallBack|kCFSocketAcceptCallBack)

        err = CFSocketSendData(sock, None, buffer("GET / HTTP/1.0"), 1.0)
        self.assertEqual(err, kCFSocketSuccess)



        ok = CFSocketIsValid(sock)
        self.assertIs(ok, True)
        CFSocketInvalidate(sock)
        self.assertResultIsBOOL(CFSocketIsValid)
        ok = CFSocketIsValid(sock)
        self.assertIs(ok, False)
        localaddr = struct.pack('>BBHBBBB', 16, socket.AF_INET, 9424, 127, 0, 0, 1)
        localaddr += '\0' * 8
        signature = CFSocketSignature(
                socket.AF_INET,
                socket.SOCK_STREAM,
                0,
                buffer(localaddr))

        sock = CFSocketCreateWithSocketSignature(None, signature,
                kCFSocketReadCallBack|kCFSocketWriteCallBack,
                callback, data)
        self.assertIsInstance(sock, CFSocketRef)
        signature = CFSocketSignature(
                socket.AF_INET,
                socket.SOCK_STREAM,
                0,
                buffer(sockaddr))
        sock = CFSocketCreateConnectedToSocketSignature(None, signature,
                kCFSocketReadCallBack|kCFSocketWriteCallBack,
                callback, data, 1.0)
        self.assertIsInstance(sock, CFSocketRef)
        self.assertResultIsCFRetained(CFSocketCreateRunLoopSource)
        src = CFSocketCreateRunLoopSource(None, sock, 0)
        self.assertIsInstance(src, CFRunLoopSourceRef)
    def testSocketNameServer(self):
        # The documentation says:
        #   Name server functionality is currently inoperable in Mac OS X.
        # 
        # Therefore these functions are not available from Python
        self.assertNotHasAttr(CoreFoundation, 'CFSocketCopyRegisteredSocketSignature')
        self.assertNotHasAttr(CoreFoundation, 'CFSocketCopyRegisteredValue')
        self.assertNotHasAttr(CoreFoundation, 'CFSocketRegisterSocketSignature')
        self.assertNotHasAttr(CoreFoundation, 'CFSocketRegisterValue')
        self.assertNotHasAttr(CoreFoundation, 'CFSocketUnregister')

if __name__ == "__main__":
    main()
