from PyObjCTools.TestSupport import *
import socket, time, struct
from CoreFoundation import *
import CoreFoundation


class TestSocket (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CFSocketRef)

    def testTypeID(self):
        self.failUnless(isinstance(CFSocketGetTypeID(), (int, long)))

    def testConstants(self):
        self.failUnless(kCFSocketSuccess == 0)
        self.failUnless(kCFSocketError == -1)
        self.failUnless(kCFSocketTimeout == -2)

        self.failUnless(kCFSocketNoCallBack == 0)
        self.failUnless(kCFSocketReadCallBack == 1)
        self.failUnless(kCFSocketAcceptCallBack == 2)
        self.failUnless(kCFSocketDataCallBack == 3)
        self.failUnless(kCFSocketConnectCallBack == 4)
        self.failUnless(kCFSocketWriteCallBack == 8)

        self.failUnless(kCFSocketAutomaticallyReenableReadCallBack == 1)
        self.failUnless(kCFSocketAutomaticallyReenableAcceptCallBack == 2)
        self.failUnless(kCFSocketAutomaticallyReenableDataCallBack == 3)
        self.failUnless(kCFSocketAutomaticallyReenableWriteCallBack == 8)
        self.failUnless(kCFSocketCloseOnInvalidate == 128)

        self.failUnless(isinstance(kCFSocketCommandKey, unicode))
        self.failUnless(isinstance(kCFSocketNameKey, unicode))
        self.failUnless(isinstance(kCFSocketValueKey, unicode))
        self.failUnless(isinstance(kCFSocketResultKey, unicode))
        self.failUnless(isinstance(kCFSocketErrorKey, unicode))
        self.failUnless(isinstance(kCFSocketRegisterCommand, unicode))
        self.failUnless(isinstance(kCFSocketRetrieveCommand, unicode))


    def testStructs(self):
        o = CFSocketSignature()
        self.failUnless(hasattr(o, 'protocolFamily'))
        self.failUnless(hasattr(o, 'socketType'))
        self.failUnless(hasattr(o, 'protocol'))
        self.failUnless(hasattr(o, 'address'))

    def testNameRegistry(self):
        p1 = CFSocketGetDefaultNameRegistryPortNumber()
        self.failUnless(isinstance(p1, (int, long)))

        CFSocketSetDefaultNameRegistryPortNumber(p1+1)
        p2 = CFSocketGetDefaultNameRegistryPortNumber()
        self.failUnless(isinstance(p2, (int, long)))
        self.assertEquals(p2, p1+1)

        CFSocketSetDefaultNameRegistryPortNumber(p1)


    def testSocketFunctions(self):
        data = {}
        state = []
        def callback(sock, kind, address, data, info):
            state.append((sock, kind, address, data, info))

        sock = CFSocketCreate(None, socket.AF_INET, socket.SOCK_STREAM, 0,
                kCFSocketReadCallBack|kCFSocketWriteCallBack,
                callback, data)
        self.failUnless(isinstance(sock, CFSocketRef))

        localaddr = struct.pack('>BBHBBBB', 16, socket.AF_INET, 9425, 127, 0, 0, 1)
        localaddr += '\0' * 8
        err = CFSocketSetAddress(sock, buffer(localaddr))
        self.assertEquals(err, kCFSocketSuccess)


        sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        sock = CFSocketCreateWithNative(None, sd.fileno(),
                kCFSocketReadCallBack|kCFSocketWriteCallBack,
                callback, data)
        self.failUnless(isinstance(sock, CFSocketRef))

        n = CFSocketGetNative(sock)
        self.failUnless(isinstance(n, (int, long)))
        self.assertEquals(n, sd.fileno())


    
        ctx = CFSocketGetContext(sock, None)
        self.failUnless(ctx is data)

        flags = CFSocketGetSocketFlags(sock)
        self.failUnless(isinstance(flags, (int, long)))

        CFSocketSetSocketFlags(sock, kCFSocketAutomaticallyReenableReadCallBack|kCFSocketAutomaticallyReenableAcceptCallBack)
        flags2 = CFSocketGetSocketFlags(sock)
        self.failUnless(isinstance(flags2, (int, long)))
        self.assertEquals(flags2, kCFSocketAutomaticallyReenableReadCallBack|kCFSocketAutomaticallyReenableAcceptCallBack)


        # Note: I don't expect anyone to actually use this api, building
        # struct sockaddr buffers by hand is madness in python.
        ip = socket.gethostbyname('www.apple.com')
        ip = map(int, ip.split('.'))

        sockaddr = struct.pack('>BBHBBBB', 16, socket.AF_INET, 80, *ip)
        sockaddr += '\0' * 8

        e = CFSocketConnectToAddress(sock, buffer(sockaddr), 1.0)
        self.failUnless(isinstance(e, (int, long)))
        self.assertEquals(e, kCFSocketSuccess)


        self.failUnlessResultIsCFRetained(CFSocketCopyPeerAddress)
        addr = CFSocketCopyPeerAddress(sock)
        self.failUnless( isinstance(addr, CFDataRef))

        self.failUnlessResultIsCFRetained(CFSocketCopyAddress)
        addr = CFSocketCopyAddress(sock)
        self.failUnless( isinstance(addr, CFDataRef))


        CFSocketDisableCallBacks(sock, kCFSocketReadCallBack|kCFSocketAcceptCallBack)
        CFSocketEnableCallBacks(sock, kCFSocketReadCallBack|kCFSocketAcceptCallBack)

        err = CFSocketSendData(sock, None, buffer("GET / HTTP/1.0"), 1.0)
        self.assertEquals(err, kCFSocketSuccess)



        ok = CFSocketIsValid(sock)
        self.failUnless(ok is True)

        CFSocketInvalidate(sock)
        self.failUnlessResultIsBOOL(CFSocketIsValid)
        ok = CFSocketIsValid(sock)
        self.failUnless(ok is False)

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
        self.failUnless(isinstance(sock, CFSocketRef))
        
        signature = CFSocketSignature(
                socket.AF_INET,
                socket.SOCK_STREAM,
                0,
                buffer(sockaddr))
        sock = CFSocketCreateConnectedToSocketSignature(None, signature,
                kCFSocketReadCallBack|kCFSocketWriteCallBack,
                callback, data, 1.0)
        self.failUnless(isinstance(sock, CFSocketRef))

        self.failUnlessResultIsCFRetained(CFSocketCreateRunLoopSource)
        src = CFSocketCreateRunLoopSource(None, sock, 0)
        self.failUnless(isinstance(src, CFRunLoopSourceRef))


    def testSocketNameServer(self):
        # The documentation says:
        #   Name server functionality is currently inoperable in Mac OS X.
        # 
        # Therefore these functions are not available from Python
        self.failIf( hasattr(CoreFoundation, 'CFSocketCopyRegisteredSocketSignature') )
        self.failIf( hasattr(CoreFoundation, 'CFSocketCopyRegisteredValue') )
        self.failIf( hasattr(CoreFoundation, 'CFSocketRegisterSocketSignature') )
        self.failIf( hasattr(CoreFoundation, 'CFSocketRegisterValue') )
        self.failIf( hasattr(CoreFoundation, 'CFSocketUnregister') )


if __name__ == "__main__":
    main()
