import Foundation
import objc
import CoreFoundation
from PyObjCTools.TestSupport import TestCase, NoObjCClass
import ctypes
from .runloophelper import check_cfrunloop_side_effects

MachPortClasses = tuple(
    cls for cls in objc.getClassList() if cls.__name__ == "NSMachPort"
)

# Very limited interface to mach/mach.h to enable testing of CFMachPortCreateWithPort
libc = ctypes.CDLL(None)

MACH_PORT_NULL = 0
MACH_SEND_MSG = 1
MACH_MSG_TYPE_MAKE_SEND = 20
MACH_PORT_RIGHT_SEND = 0
MACH_PORT_RIGHT_RECEIVE = 1


class MachMsgHeader(ctypes.Structure):
    _fields_ = [
        ("msgh_bits", ctypes.c_uint32),
        ("msgh_size", ctypes.c_uint32),
        ("msgh_remote_port", ctypes.c_uint32),
        ("msgh_local_port", ctypes.c_uint32),
        ("msgh_voucher_port", ctypes.c_uint32),
        ("msgh_id", ctypes.c_int32),
    ]


class SimpleMachMessage(ctypes.Structure):
    _fields_ = [("header", MachMsgHeader), ("payload", ctypes.c_uint32)]


libc.mach_port_allocate.restype = ctypes.c_int
libc.mach_port_allocate.argtypes = [
    ctypes.c_uint,
    ctypes.c_uint,
    ctypes.POINTER(ctypes.c_uint),
]
libc.mach_task_self.restype = ctypes.c_int
libc.mach_task_self.argtypes = []
libc.mach_port_deallocate.rtype = ctypes.c_int
libc.mach_port_deallocate.argtypes = [ctypes.c_uint, ctypes.c_uint]
libc.mach_msg.restype = ctypes.c_int32
libc.mach_msg.argtypes = [
    ctypes.POINTER(MachMsgHeader),
    ctypes.c_int32,
    ctypes.c_uint32,
    ctypes.c_uint32,
    ctypes.c_uint32,
    ctypes.c_uint32,
    ctypes.c_uint32,
]


def open_mach_port(rights):
    mach_port_loc = ctypes.c_uint()
    libc.mach_port_allocate(
        libc.mach_task_self(), MACH_PORT_RIGHT_RECEIVE, ctypes.byref(mach_port_loc)
    )

    return mach_port_loc.value


def send_mach_message(target_port_id, message_id, data_value):
    msg = SimpleMachMessage()

    msg.header.msgh_bits = MACH_MSG_TYPE_MAKE_SEND
    msg.header.msgh_size = ctypes.sizeof(SimpleMachMessage)
    msg.header.msgh_remote_port = target_port_id
    msg.header.msgh_local_port = MACH_PORT_NULL
    msg.header.msgh_voucher_port = MACH_PORT_NULL
    msg.header.msgh_id = message_id

    msg.payload = data_value

    result = libc.mach_msg(
        ctypes.byref(msg.header),  # Pointer to header
        MACH_SEND_MSG,  # Options flags
        msg.header.msgh_size,  # Send size
        0,  # Receive size (0 for send-only)
        MACH_PORT_NULL,  # Receive port name
        0,  # Timeout (0 for infinity/none)
        MACH_PORT_NULL,  # Notification port
    )

    if result != 0:
        raise RuntimeError(f"Sending failed: {result}")


class TestMachPort(TestCase):
    def test_types(self):
        try:
            if objc.lookUpClass("NSMachPort") is CoreFoundation.CFMachPortRef:
                return
        except objc.error:
            pass
        self.assertIsCFType(CoreFoundation.CFMachPortRef)

    def test_typeid(self):
        self.assertIsInstance(CoreFoundation.CFMachPortGetTypeID(), int)

    def test_create2(self):
        class Context:
            pass

        context = Context()

        def callout(port, msg, size, info):
            pass

        port, shouldFree = CoreFoundation.CFMachPortCreate(None, callout, context, None)

        self.assertIsInstance(port, MachPortClasses)

    @check_cfrunloop_side_effects
    def test_create_cfmachport(self):
        context = object()

        lst = []

        def callout(port, msg, size, info):
            lst.append((port, msg, size, info))

        with self.assertRaisesRegex(TypeError, "expected 4 arguments, got 0"):
            CoreFoundation.CFMachPortCreate()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            CoreFoundation.CFMachPortCreate(NoObjCClass(), callout, context, None)

        with self.assertRaisesRegex(ValueError, "'shouldFree' should be None or NULL"):
            CoreFoundation.CFMachPortCreate(None, callout, context, 42)

        port, shouldFree = CoreFoundation.CFMachPortCreate(None, callout, context, None)

        self.assertIsInstance(port, MachPortClasses)
        self.assertIsInstance(port, Foundation.NSPort)
        self.assertTrue(shouldFree is True or shouldFree is False)
        idx = CoreFoundation.CFMachPortGetPort(port)
        self.assertIsInstance(idx, int)

        with self.assertRaisesRegex(TypeError, "expected 2 arguments, got 0"):
            CoreFoundation.CFMachPortGetContext()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            CoreFoundation.CFMachPortGetContext(NoObjCClass(), None)

        with self.assertRaisesRegex(ValueError, "'context' must be None"):
            CoreFoundation.CFMachPortGetContext(port, 42)

        ctx = CoreFoundation.CFMachPortGetContext(port, None)
        self.assertIs(ctx, context)

        with self.assertRaisesRegex(TypeError, "expected 1 arguments, got 0"):
            CoreFoundation.CFMachPortGetInvalidationCallBack()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            CoreFoundation.CFMachPortGetInvalidationCallBack(NoObjCClass())

        cb = CoreFoundation.CFMachPortGetInvalidationCallBack(port)
        self.assertIs(cb, None)
        didInvalidate = False

        def invalidate(port, info):
            nonlocal didInvalidate
            didInvalidate = True

        with self.assertRaisesRegex(TypeError, "expected 2 arguments, got 0"):
            CoreFoundation.CFMachPortSetInvalidationCallBack()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            CoreFoundation.CFMachPortSetInvalidationCallBack(NoObjCClass(), invalidate)

        CoreFoundation.CFMachPortSetInvalidationCallBack(port, invalidate)
        cb = CoreFoundation.CFMachPortGetInvalidationCallBack(port)
        self.assertIs(invalidate, cb)
        rls = CoreFoundation.CFMachPortCreateRunLoopSource(None, port, 0)
        self.assertIsInstance(rls, CoreFoundation.CFRunLoopSourceRef)
        self.assertTrue(CoreFoundation.CFMachPortIsValid(port))
        CoreFoundation.CFMachPortInvalidate(port)
        self.assertFalse(CoreFoundation.CFMachPortIsValid(port))
        self.assertTrue(didInvalidate)

        port, shouldFree = CoreFoundation.CFMachPortCreate(
            None, callout, context, objc.NULL
        )
        self.assertIsInstance(port, MachPortClasses)
        self.assertIs(shouldFree, objc.NULL)

        runloop_mode = CoreFoundation.kCFRunLoopDefaultMode

        rls = CoreFoundation.CFMachPortCreateRunLoopSource(None, port, 0)
        rl = CoreFoundation.CFRunLoopGetCurrent()
        CoreFoundation.CFRunLoopAddSource(rl, rls, runloop_mode)

        mach_port = CoreFoundation.CFMachPortGetPort(port)

        send_mach_message(mach_port, 1, 42)

        print("Before")
        print(repr(rl))

        CoreFoundation.CFRunLoopRunInMode(runloop_mode, 0.5, False)

        CoreFoundation.CFRunLoopRemoveSource(rl, rls, runloop_mode)

        print("After")
        print(repr(rl))
        self.assertEqual(len(lst), 1)
        item = lst[0]
        self.assertIsInstance(item, tuple)
        self.assertIs(item[0], port)
        self.assertIsInstance(item[1], bytes)
        self.assertEqual(item[2], len(item[1]))
        self.assertIs(item[3], context)

        shouldRaise = False

        def invalidate2(port, info):
            if shouldRaise:
                raise RuntimeError("callback error")

        CoreFoundation.CFMachPortSetInvalidationCallBack(port, invalidate2)
        cb = CoreFoundation.CFMachPortGetInvalidationCallBack(port)
        self.assertIs(invalidate2, cb)

        shouldRaise = True
        with self.assertRaisesRegex(RuntimeError, "callback error"):
            CoreFoundation.CFMachPortInvalidate(port)
        shouldRaise = False
        CoreFoundation.CFMachPortInvalidate(port)

    @check_cfrunloop_side_effects
    def test_create_cfmachport_with_port(self):
        runloop_mode = CoreFoundation.kCFRunLoopDefaultMode

        context = object()

        def callout(port, msg, size, info):
            raise RuntimeError("callback error")

        with self.assertRaisesRegex(TypeError, "expected 5 arguments, got 0"):
            CoreFoundation.CFMachPortCreateWithPort()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            CoreFoundation.CFMachPortCreateWithPort(
                NoObjCClass(), 0, callout, context, None
            )

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned int', got 'str'"
        ):
            CoreFoundation.CFMachPortCreateWithPort(
                None, "port", callout, context, None
            )

        with self.assertRaisesRegex(ValueError, "'shouldFree' should be None or NULL"):
            CoreFoundation.CFMachPortCreateWithPort(None, 0, callout, context, 42)

        mach_port = open_mach_port(MACH_PORT_RIGHT_RECEIVE)
        try:
            port, shouldFree = CoreFoundation.CFMachPortCreateWithPort(
                None, mach_port, callout, context, None
            )
            self.assertIsInstance(port, MachPortClasses)
            self.assertIsInstance(shouldFree, bool)
            CoreFoundation.CFMachPortInvalidate(port)

            port, shouldFree = CoreFoundation.CFMachPortCreateWithPort(
                None, mach_port, callout, context, objc.NULL
            )
            self.assertIsInstance(port, MachPortClasses)
            self.assertIs(shouldFree, objc.NULL)

            rls = CoreFoundation.CFMachPortCreateRunLoopSource(None, port, 0)
            rl = CoreFoundation.CFRunLoopGetCurrent()
            CoreFoundation.CFRunLoopAddSource(rl, rls, runloop_mode)

            send_mach_message(mach_port, 2, 42)

            with self.assertRaisesRegex(RuntimeError, "callback error"):
                CoreFoundation.CFRunLoopRunInMode(runloop_mode, 0.5, False)

        finally:
            CoreFoundation.CFRunLoopRemoveSource(rl, rls, runloop_mode)
            libc.mach_port_deallocate(libc.mach_task_self(), mach_port)
