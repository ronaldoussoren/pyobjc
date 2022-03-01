import warnings
import sys
import io
import os
from unittest import mock

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from PyObjCTools import Signals
from PyObjCTools.TestSupport import TestCase
import signal


class TestSignals(TestCase):
    # XXX: As the docstring for the module
    #      notes the PyObjCTools.Signals module
    #      is not very robust, and will be removed
    #      in the next major release.
    def setUp(self):
        self._orig_handlers = {}
        self._signal_called = {}
        for sig in signal.Signals:
            try:
                self._orig_handlers[sig] = signal.signal(sig, self._handle_signal)
            except OSError:
                # We try to install a handler for all signals,
                # not all of them can have a handler.
                pass

    def tearDown(self):
        for sig, handler in self._orig_handlers.items():
            if handler is None:
                # Can be caused by faulthandler
                continue
            signal.signal(sig, handler)

    def _handle_signal(self, signum, frame):
        self._signal_called[signum] = frame

    def test_installing(self):
        orig = Signals.originalHandlers
        Signals.originalHandlers = {}
        orig_stderr = sys.stderr
        sys.stderr = io.StringIO()
        try:
            Signals.installHandler(signal.SIGUSR1)
            self.assertIn(signal.SIGUSR1, Signals.originalHandlers)
            self.assertIs(signal.getsignal(signal.SIGUSR1), Signals.dumpHandler)

            os.kill(os.getpid(), signal.SIGUSR1)
            self.assertIn(signal.SIGUSR1, self._signal_called)

            stderr = sys.stderr.getvalue()
            self.assertIn("*** Handling fatal signal '", stderr)
            self.assertIn("*** Restored handlers and resignaling.", stderr)
            self.assertIn(f'File "{__file__}", ', stderr)

            # Signal handler resets the orignals
            self.assertIs(Signals.originalHandlers, None)

            self.assertEqual(signal.getsignal(signal.SIGUSR1), self._handle_signal)

        finally:
            sys.stderr = orig_stderr
            Signals.originalHandlers = orig

    @mock.patch("PyObjCTools.Signals.installHandler")
    def test_setup(self, installHandler):
        Signals.dumpStackOnFatalSignal()

        installHandler.assert_any_call(signal.SIGQUIT)
        installHandler.assert_any_call(signal.SIGILL)
        installHandler.assert_any_call(signal.SIGTRAP)
        installHandler.assert_any_call(signal.SIGABRT)
        installHandler.assert_any_call(signal.SIGEMT)
        installHandler.assert_any_call(signal.SIGFPE)
        installHandler.assert_any_call(signal.SIGBUS)
        installHandler.assert_any_call(signal.SIGSEGV)
        installHandler.assert_any_call(signal.SIGSYS)
        self.assertEqual(installHandler.call_count, 9)

        # Calling the function twice shouldn't matter
        # First add something to the ``orignalHandlers`` dict,
        # that's normally done by ``installHandler`` but
        # that was mocked for this test.
        Signals.originalHandlers[signal.SIGUSR1] = 1
        Signals.dumpStackOnFatalSignal()
        self.assertEqual(installHandler.call_count, 9)

    def test_cleanup_with_nothing(self):
        Signals.resetFatalSignals()
