from PyObjCTools import MachSignals
from PyObjCTools.TestSupport import TestCase
import signal
import os
import objc


class TestMachSignals(TestCase):
    # Note that the MachSignals module only
    # proceses signals when a run loop is
    # active, that makes testing slightly more
    # complicated...
    #
    # The tests cannot mock the system,
    # the C code needs to be tested as well.
    #
    # Another complication for testing is
    # that MachSignals (a) overwrites the
    # process signal state and (b) has no way
    # to reset the signal handler.
    #
    # Therefore testing uses the SIGUSR2 signal
    # that isn't normally used.
    #
    # Because of all this there's one test that
    # does all the work, with
    def test_basic_test(self):
        # Check that SIGUSR2 isn't used
        self.assertEqual(signal.getsignal(signal.SIGUSR2), signal.SIG_DFL)

        # getsignal returns None when no signal is registered
        # through MachSignals
        self.assertIs(MachSignals.getsignal(signal.SIGUSR2), None)

        signal.signal(signal.SIGUSR2, lambda x, y: None)
        self.assertIs(MachSignals.getsignal(signal.SIGUSR2), None)
        signal.signal(signal.SIGUSR2, signal.SIG_DFL)

        seen = []

        def handler(signum):
            seen.append(signum)

        # Install a signal handler
        MachSignals.signal(signal.SIGUSR2, handler)

        # Raise a signal
        os.kill(os.getpid(), signal.SIGUSR2)

        # The signal is only processed when the
        # default runloop is running
        self.assertEqual(seen, [])

        # Run the default runloop for a while
        NSRunLoop = objc.lookUpClass("NSRunLoop")
        NSDate = objc.lookUpClass("NSDate")
        loop = NSRunLoop.currentRunLoop()
        loop.runUntilDate_(NSDate.dateWithTimeIntervalSinceNow_(0.5))

        # And check that the signal is actually processed
        self.assertEqual(seen, [signal.SIGUSR2])
        del seen[:]

        # Clear the signal handler
        del MachSignals._machsignals._signalmapping[signal.SIGUSR2]

        # Check that handling the signal won't cause
        # problems due to a missing handler.
        os.kill(os.getpid(), signal.SIGUSR2)
        loop.runUntilDate_(NSDate.dateWithTimeIntervalSinceNow_(0.5))

        # The handler wasn't in the mapping, hence not called.
        self.assertEqual(seen, [])

        # "install" a new handler that raises and exception
        def new_handler(signum):
            raise RuntimeError("foo the bar")

        MachSignals._machsignals._signalmapping[signal.SIGUSR2] = new_handler

        os.kill(os.getpid(), signal.SIGUSR2)

        # Check that the exception is forwarded through the
        # runloop
        with self.assertRaisesRegex(RuntimeError, "foo the bar"):
            loop.runUntilDate_(NSDate.dateWithTimeIntervalSinceNow_(0.5))

        # "install" a new handler with an invalid signature
        def new_handler():
            pass

        MachSignals._machsignals._signalmapping[signal.SIGUSR2] = new_handler

        os.kill(os.getpid(), signal.SIGUSR2)

        # Check that the resulting exception is forwarded through
        # the runloop
        with self.assertRaises(TypeError):
            loop.runUntilDate_(NSDate.dateWithTimeIntervalSinceNow_(0.5))

        # Reset the C signal handler through the signal module
        signal.signal(signal.SIGUSR2, lambda x, y: None)

        os.kill(os.getpid(), signal.SIGUSR2)
        signal.signal(signal.SIGUSR2, signal.SIG_DFL)

        # Check that resetting the signal through the
        # signal module undoes the work of MachSignals
        self.assertEqual(seen, [])

    def test_api_misuse(self):
        with self.assertRaises(TypeError):
            MachSignals._machsignals.handle_signal("a")

        with self.assertRaises(TypeError):
            MachSignals._machsignals.handle_signal(signal.SIGUSR2, lambda x: None)

    def test_handler_raises(self):
        MachSignals.signal(signal.SIGUSR2, lambda x: x / 0)
        os.kill(os.getpid(), signal.SIGUSR2)

        NSRunLoop = objc.lookUpClass("NSRunLoop")
        NSDate = objc.lookUpClass("NSDate")
        loop = NSRunLoop.currentRunLoop()

        with self.assertRaises(ZeroDivisionError):
            loop.runUntilDate_(NSDate.dateWithTimeIntervalSinceNow_(0.5))
