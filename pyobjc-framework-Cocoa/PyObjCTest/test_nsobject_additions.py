from PyObjCTools.TestSupport import *

import Foundation
import sys

if sys.version_info[0] == 2:
    from StringIO import StringIO
    def _str(v): return v
else:
    from io import StringIO
    def _str(v): 
        if isinstance(v, str):
            return v
        return v.decode('ascii')

class TheadingHelperTestHelper (Foundation.NSObject):
    def init(self):
        self = super(TheadingHelperTestHelper, self).init()
        if self is None:
            return None

        self.calls = []
        return self

    def performSelector_onThread_withObject_waitUntilDone_(self,
            selector, thread, object, wait):
        assert isinstance(selector, bytes)
        assert isinstance(thread, Foundation.NSThread)
        assert isinstance(wait, bool)

        self.calls.append((selector, thread, object, wait))
        getattr(self, _str(selector))(object)

    def performSelector_onThread_withObject_waitUntilDone_modes_(self,
            selector, thread, object, wait, modes):
        assert isinstance(selector, bytes)
        assert isinstance(thread, Foundation.NSThread)
        assert isinstance(wait, bool)

        self.calls.append((selector, thread, object, wait, modes))
        getattr(self, _str(selector))(object)

    def performSelector_withObject_afterDelay_(self,
            selector, object, delay):
        assert isinstance(selector, bytes)

        self.calls.append((selector, object, delay))
        getattr(self, _str(selector))(object)

    def performSelector_withObject_afterDelay_inModes_(self,
            selector, object, delay, modes):
        assert isinstance(selector, bytes)

        self.calls.append((selector, object, delay, modes))
        getattr(self, _str(selector))(object)

    def performSelectorInBackground_withObject_(self,
            selector, object):
        self.calls.append((selector, object))
        getattr(self, _str(selector))(object)

    def performSelectorOnMainThread_withObject_waitUntilDone_(self,
            selector, object, wait):
        self.calls.append((selector, object, wait))
        getattr(self, _str(selector))(object)

    def performSelectorOnMainThread_withObject_waitUntilDone_modes_(self,
            selector, object, wait, modes):
        self.calls.append((selector, object, wait, modes))
        getattr(self, _str(selector))(object)

    def sel1_(self, arg):
        pass

    def sel2_(self, arg):
        return arg * 2

    def sel3_(self, arg):
        return 1/arg

class TestThreadingHelpers (TestCase):
    def testAsyncOnThreadNoResult(self):
        # pyobjc_performSelector_onThread_withObject_waitUntilDone_
        obj = TheadingHelperTestHelper.alloc().init()
        thr = Foundation.NSThread.mainThread()

        obj.pyobjc_performSelector_onThread_withObject_waitUntilDone_(
                b'sel1:', thr, 1, False),
        obj.pyobjc_performSelector_onThread_withObject_waitUntilDone_(
                b'sel2:', thr, 2, True)
        obj.pyobjc_performSelector_onThread_withObject_waitUntilDone_(
                b'isEqual:', thr, obj, True)

        self.assertEqual(obj.calls, [
            (b'_pyobjc_performOnThread:', thr, (b'sel1:', 1), False),
            (b'_pyobjc_performOnThread:', thr, (b'sel2:', 2), True),
            (b'_pyobjc_performOnThread:', thr, (b'isEqual:', obj), True),
        ])

        # Raise an exception
        orig_stderr = sys.stderr
        sys.stderr = StringIO()
        try:
            obj.calls[:] = []
            obj.pyobjc_performSelector_onThread_withObject_waitUntilDone_(
                    b'sel3:', thr, 0, False)
            self.assertEqual(obj.calls, [
                (b'_pyobjc_performOnThread:', thr, (b'sel3:', 0), False),
            ])
            self.assertIn('Traceback', sys.stderr.getvalue())
        finally:
            sys.stderr = orig_stderr

    def testAsyncOnThreadNoResultModes(self):
        # pyobjc_performSelector_onThread_withObject_waitUntilDone_modes_
        obj = TheadingHelperTestHelper.alloc().init()
        thr = Foundation.NSThread.mainThread()

        obj.pyobjc_performSelector_onThread_withObject_waitUntilDone_modes_(
                b'sel1:', thr, 1, False, 0),
        obj.pyobjc_performSelector_onThread_withObject_waitUntilDone_modes_(
                b'sel2:', thr, 2, True, 1)
        obj.pyobjc_performSelector_onThread_withObject_waitUntilDone_modes_(
                b'isEqual:', thr, obj, True, 2)

        self.assertEqual(obj.calls, [
            (b'_pyobjc_performOnThread:', thr, (b'sel1:', 1), False, 0),
            (b'_pyobjc_performOnThread:', thr, (b'sel2:', 2), True, 1),
            (b'_pyobjc_performOnThread:', thr, (b'isEqual:', obj), True, 2),
        ])

        # Raise an exception
        orig_stderr = sys.stderr
        sys.stderr = StringIO()
        try:
            obj.calls[:] = []
            obj.pyobjc_performSelector_onThread_withObject_waitUntilDone_modes_(
                    b'sel3:', thr, 0, False, 4)
            self.assertEqual(obj.calls, [
                (b'_pyobjc_performOnThread:', thr, (b'sel3:', 0), False, 4),
            ])
            self.assertIn('Traceback', sys.stderr.getvalue())
        finally:
            sys.stderr = orig_stderr

    def testAsyncWithDelayNoResult(self):
        # pyobjc_performSelector_withObject_afterDelay_
        obj = TheadingHelperTestHelper.alloc().init()

        obj.pyobjc_performSelector_withObject_afterDelay_(b'sel1:', 1, 1.0)
        obj.pyobjc_performSelector_withObject_afterDelay_(b'sel2:', 2, 4.5)
        obj.pyobjc_performSelector_withObject_afterDelay_(b'isEqual:', obj, 8.5)

        self.assertEqual(obj.calls, [
            (b'_pyobjc_performOnThread:', (b'sel1:', 1), 1.0),
            (b'_pyobjc_performOnThread:', (b'sel2:', 2), 4.5),
            (b'_pyobjc_performOnThread:', (b'isEqual:', obj), 8.5),
        ])

        # Raise an exception
        orig_stderr = sys.stderr
        sys.stderr = StringIO()
        try:
            obj.calls[:] = []
            obj.pyobjc_performSelector_withObject_afterDelay_(
                    b'sel3:', 0, 0.5)
            self.assertEqual(obj.calls, [
                (b'_pyobjc_performOnThread:', (b'sel3:', 0), 0.5),
            ])
            self.assertIn('Traceback', sys.stderr.getvalue())
        finally:
            sys.stderr = orig_stderr

    def testAsyncWithDelayNoResultModes(self):
        # pyobjc_performSelector_withObject_afterDelay_inModes_
        obj = TheadingHelperTestHelper.alloc().init()

        obj.pyobjc_performSelector_withObject_afterDelay_inModes_(b'sel1:', 1, 1.0, 0)
        obj.pyobjc_performSelector_withObject_afterDelay_inModes_(b'sel2:', 2, 4.5, 1)
        obj.pyobjc_performSelector_withObject_afterDelay_inModes_(b'isEqual:', obj, 8.5, 2)

        self.assertEqual(obj.calls, [
            (b'_pyobjc_performOnThread:', (b'sel1:', 1), 1.0, 0),
            (b'_pyobjc_performOnThread:', (b'sel2:', 2), 4.5, 1),
            (b'_pyobjc_performOnThread:', (b'isEqual:', obj), 8.5, 2),
        ])

        # Raise an exception
        orig_stderr = sys.stderr
        sys.stderr = StringIO()
        try:
            obj.calls[:] = []
            obj.pyobjc_performSelector_withObject_afterDelay_inModes_(
                    b'sel3:', 0, 0.5, 3)
            self.assertEqual(obj.calls, [
                (b'_pyobjc_performOnThread:', (b'sel3:', 0), 0.5, 3),
            ])
            self.assertIn('Traceback', sys.stderr.getvalue())
        finally:
            sys.stderr = orig_stderr

    def testInBGNoResult(self):
        # pyobjc_performSelectorInBackground_withObject_

        obj = TheadingHelperTestHelper.alloc().init()

        obj.pyobjc_performSelectorInBackground_withObject_(b'sel1:', 1)
        obj.pyobjc_performSelectorInBackground_withObject_(b'sel2:', 2)
        obj.pyobjc_performSelectorInBackground_withObject_(b'isEqual:', obj)

        self.assertEqual(obj.calls, [
            (b'_pyobjc_performOnThread:', (b'sel1:', 1)),
            (b'_pyobjc_performOnThread:', (b'sel2:', 2)),
            (b'_pyobjc_performOnThread:', (b'isEqual:', obj)),
        ])

        # Raise an exception
        orig_stderr = sys.stderr
        sys.stderr = StringIO()
        try:
            obj.calls[:] = []
            obj.pyobjc_performSelectorInBackground_withObject_(
                    b'sel3:', 0)
            self.assertEqual(obj.calls, [
                (b'_pyobjc_performOnThread:', (b'sel3:', 0)),
            ])
            self.assertIn('Traceback', sys.stderr.getvalue())
        finally:
            sys.stderr = orig_stderr

    def testOnMtNoResultWait(self):
        # pyobjc_performSelectorInBackground_withObject_waitUntilDone_

        obj = TheadingHelperTestHelper.alloc().init()

        obj.pyobjc_performSelectorOnMainThread_withObject_waitUntilDone_(b'sel1:', 1, True)
        obj.pyobjc_performSelectorOnMainThread_withObject_waitUntilDone_(b'sel2:', 2, False)
        obj.pyobjc_performSelectorOnMainThread_withObject_waitUntilDone_(b'isEqual:', obj, True)

        self.assertEqual(obj.calls, [
            (b'_pyobjc_performOnThread:', (b'sel1:', 1), True),
            (b'_pyobjc_performOnThread:', (b'sel2:', 2), False),
            (b'_pyobjc_performOnThread:', (b'isEqual:', obj), True),
        ])

        # Raise an exception
        orig_stderr = sys.stderr
        sys.stderr = StringIO()
        try:
            obj.calls[:] = []
            obj.pyobjc_performSelectorOnMainThread_withObject_waitUntilDone_(
                    b'sel3:', 0, False)
            self.assertEqual(obj.calls, [
                (b'_pyobjc_performOnThread:', (b'sel3:', 0), False),
            ])
            self.assertIn('Traceback', sys.stderr.getvalue())
        finally:
            sys.stderr = orig_stderr

    def testOnMtNoResultWaitModes(self):
        # pyobjc_performSelectorInBackground_withObject_waitUntilDone_modes_

        obj = TheadingHelperTestHelper.alloc().init()

        obj.pyobjc_performSelectorOnMainThread_withObject_waitUntilDone_modes_(b'sel1:', 1, True, 4)
        obj.pyobjc_performSelectorOnMainThread_withObject_waitUntilDone_modes_(b'sel2:', 2, False, 5)
        obj.pyobjc_performSelectorOnMainThread_withObject_waitUntilDone_modes_(b'isEqual:', obj, True, 6)

        self.assertEqual(obj.calls, [
            (b'_pyobjc_performOnThread:', (b'sel1:', 1), True, 4),
            (b'_pyobjc_performOnThread:', (b'sel2:', 2), False, 5),
            (b'_pyobjc_performOnThread:', (b'isEqual:', obj), True, 6),
        ])

        # Raise an exception
        orig_stderr = sys.stderr
        sys.stderr = StringIO()
        try:
            obj.calls[:] = []
            obj.pyobjc_performSelectorOnMainThread_withObject_waitUntilDone_modes_(
                    b'sel3:', 0, False, 7)
            self.assertEqual(obj.calls, [
                (b'_pyobjc_performOnThread:', (b'sel3:', 0), False, 7),
            ])
            self.assertIn('Traceback', sys.stderr.getvalue())
        finally:
            sys.stderr = orig_stderr

    def testOnMtWithResult(self):
        # pyobjc_performSelectorOnMainThread_withObject_
        obj = TheadingHelperTestHelper.alloc().init()

        r = obj.pyobjc_performSelectorOnMainThread_withObject_('sel2:', 3)
        self.assertEqual(r, 6)
        r = obj.pyobjc_performSelectorOnMainThread_withObject_('sel3:', 2.0)
        self.assertEqual(r, 0.5)

        self.assertEqual(obj.calls, [
            (b'_pyobjc_performOnThreadWithResult:', ('sel2:', 3, [(True, 6)]), True),
            (b'_pyobjc_performOnThreadWithResult:', ('sel3:', 2.0, [(True, 0.5)]), True),
        ])

        # Raise an exception
        orig_stderr = sys.stderr
        sys.stderr = StringIO()
        try:
            obj.calls[:] = []

            self.assertRaises(ZeroDivisionError, obj.pyobjc_performSelectorOnMainThread_withObject_,
                    b'sel3:', 0)

            self.assertEqual(len(obj.calls), 1)
            self.assertEqual(obj.calls[0][0], b'_pyobjc_performOnThreadWithResult:')
            self.assertEqual(obj.calls[0][1][-1][0][0],  False)
            self.assertNotIn('Traceback', sys.stderr.getvalue())
        finally:
            sys.stderr = orig_stderr

    def testOnMtWithResultModes(self):
        obj = TheadingHelperTestHelper.alloc().init()

        r = obj.pyobjc_performSelectorOnMainThread_withObject_modes_('sel2:', 3, 1)
        self.assertEqual(r, 6)
        r = obj.pyobjc_performSelectorOnMainThread_withObject_modes_('sel3:', 2.0, 2)
        self.assertEqual(r, 0.5)

        self.assertEqual(obj.calls, [
            (b'_pyobjc_performOnThreadWithResult:', ('sel2:', 3, [(True, 6)]), True, 1),
            (b'_pyobjc_performOnThreadWithResult:', ('sel3:', 2.0, [(True, 0.5)]), True, 2),
        ])

        # Raise an exception
        orig_stderr = sys.stderr
        sys.stderr = StringIO()
        try:
            obj.calls[:] = []

            self.assertRaises(ZeroDivisionError, obj.pyobjc_performSelectorOnMainThread_withObject_modes_,
                    b'sel3:', 0, 3)

            self.assertEqual(len(obj.calls), 1)
            self.assertEqual(obj.calls[0][0], b'_pyobjc_performOnThreadWithResult:')
            self.assertEqual(obj.calls[0][1][-1][0][0],  False)
            self.assertNotIn('Traceback', sys.stderr.getvalue())
        finally:
            sys.stderr = orig_stderr

    def testOnThreadWithResult(self):
        obj = TheadingHelperTestHelper.alloc().init()
        thr = Foundation.NSThread.mainThread()

        r = obj.pyobjc_performSelector_onThread_withObject_('sel2:', thr, 3)
        self.assertEqual(r, 6)
        r = obj.pyobjc_performSelector_onThread_withObject_('sel3:', thr, 2.0)
        self.assertEqual(r, 0.5)

        self.assertEqual(obj.calls, [
            (b'_pyobjc_performOnThreadWithResult:', thr, ('sel2:', 3, [(True, 6)]), True),
            (b'_pyobjc_performOnThreadWithResult:', thr, ('sel3:', 2.0, [(True, 0.5)]), True),
        ])

        # Raise an exception
        orig_stderr = sys.stderr
        sys.stderr = StringIO()
        try:
            obj.calls[:] = []

            self.assertRaises(ZeroDivisionError, obj.pyobjc_performSelector_onThread_withObject_,
                    b'sel3:', thr, 0)

            self.assertEqual(len(obj.calls), 1)
            self.assertEqual(obj.calls[0][0], b'_pyobjc_performOnThreadWithResult:')
            self.assertEqual(obj.calls[0][2][-1][0][0],  False)
            self.assertNotIn('Traceback', sys.stderr.getvalue())
        finally:
            sys.stderr = orig_stderr

    def testOnThreadWithResultModes(self):
        obj = TheadingHelperTestHelper.alloc().init()
        thr = Foundation.NSThread.mainThread()

        r = obj.pyobjc_performSelector_onThread_withObject_modes_('sel2:', thr, 3, 1)
        self.assertEqual(r, 6)
        r = obj.pyobjc_performSelector_onThread_withObject_modes_('sel3:', thr, 2.0, 2)
        self.assertEqual(r, 0.5)

        self.assertEqual(obj.calls, [
            (b'_pyobjc_performOnThreadWithResult:', thr, ('sel2:', 3, [(True, 6)]), True, 1),
            (b'_pyobjc_performOnThreadWithResult:', thr, ('sel3:', 2.0, [(True, 0.5)]), True, 2),
        ])

        # Raise an exception
        orig_stderr = sys.stderr
        sys.stderr = StringIO()
        try:
            obj.calls[:] = []

            self.assertRaises(ZeroDivisionError, obj.pyobjc_performSelector_onThread_withObject_modes_,
                    b'sel3:', thr, 0, 3)

            self.assertEqual(len(obj.calls), 1)
            self.assertEqual(obj.calls[0][0], b'_pyobjc_performOnThreadWithResult:')
            self.assertEqual(obj.calls[0][2][-1][0][0],  False)
            self.assertNotIn('Traceback', sys.stderr.getvalue())
        finally:
            sys.stderr = orig_stderr

if __name__ == "__main__":
    main()
