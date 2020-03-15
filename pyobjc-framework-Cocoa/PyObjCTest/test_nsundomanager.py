import Foundation
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestHelper(Foundation.NSObject):
    def incFoo_(self, foo):
        foo[0] += 1


class TestNSUndoManager(TestCase):
    def testUndoManager(self):
        x = TestHelper.new()
        m = Foundation.NSUndoManager.new()
        lst = [0]

        m.prepareWithInvocationTarget_(x).incFoo_(lst)
        m.undo()

        self.assertEqual(lst[0], 1)

    def __del__(self, objc=objc):
        objc.recycleAutoreleasePool()


# Undo Integer test
# From David Eppstein
#
# test ability of int argument to pass through undo and then
# be used as parameter to another routine expecting an int
#
# the actual routine I want to use is
# Foundation.NSTableView.editColumn_row_withEvent_select_
# but that involves setting up a UI; instead use Foundation.NSIndexSpecifier

if hasattr(Foundation, "NSIndexSpecifier"):

    class TestUndoInt(TestCase):
        class UndoInt(Foundation.NSObject):
            undo = Foundation.NSUndoManager.alloc().init()
            idx = Foundation.NSIndexSpecifier.alloc().init()
            idx.setIndex_(0)

            def test_(self, i):
                self.undo.prepareWithInvocationTarget_(self).test_(self.idx.index())
                self.idx.setIndex_(i)

        def testUndoInt(self):
            # test that undo works
            x = TestUndoInt.UndoInt.alloc().init()
            x.test_(3)
            assert x.idx.index() == 3
            x.undo.undo()
            assert x.idx.index() == 0


# end Undo Integer test


class TestSubclassingUndo(TestCase):
    # Bugreport: 678759 Subclassing Foundation.NSUndoManager fails

    def testSubclass(self):
        class UndoSubclass(Foundation.NSUndoManager):
            pass

        x = TestHelper.new()
        m = UndoSubclass.new()
        lst = [0]

        m.prepareWithInvocationTarget_(x).incFoo_(lst)
        m.undo()

        self.assertEqual(lst[0], 1)

    def testConstants(self):
        self.assertIsInstance(Foundation.NSUndoManagerCheckpointNotification, str)
        self.assertIsInstance(Foundation.NSUndoManagerWillUndoChangeNotification, str)
        self.assertIsInstance(Foundation.NSUndoManagerWillRedoChangeNotification, str)
        self.assertIsInstance(Foundation.NSUndoManagerDidUndoChangeNotification, str)
        self.assertIsInstance(Foundation.NSUndoManagerDidRedoChangeNotification, str)
        self.assertIsInstance(Foundation.NSUndoManagerDidOpenUndoGroupNotification, str)
        self.assertIsInstance(
            Foundation.NSUndoManagerWillCloseUndoGroupNotification, str
        )
        self.assertEqual(Foundation.NSUndoCloseGroupingRunLoopOrdering, 350_000)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(Foundation.NSUndoManagerGroupIsDiscardableKey, str)
        self.assertIsInstance(
            Foundation.NSUndoManagerDidCloseUndoGroupNotification, str
        )

    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSUndoManager.isUndoRegistrationEnabled)
        self.assertResultIsBOOL(Foundation.NSUndoManager.groupsByEvent)
        self.assertArgIsBOOL(Foundation.NSUndoManager.setGroupsByEvent_, 0)
        self.assertResultIsBOOL(Foundation.NSUndoManager.canUndo)
        self.assertResultIsBOOL(Foundation.NSUndoManager.canRedo)
        self.assertResultIsBOOL(Foundation.NSUndoManager.isUndoing)
        self.assertResultIsBOOL(Foundation.NSUndoManager.isRedoing)
        self.assertArgIsSEL(
            Foundation.NSUndoManager.registerUndoWithTarget_selector_object_, 1, b"v@:@"
        )

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertArgIsBOOL(Foundation.NSUndoManager.setActionIsDiscardable_, 0)
        self.assertResultIsBOOL(Foundation.NSUndoManager.undoActionIsDiscardable)
        self.assertResultIsBOOL(Foundation.NSUndoManager.redoActionIsDiscardable)

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertArgIsBlock(
            Foundation.NSUndoManager.registerUndoWithTarget_handler_, 1, b"v@"
        )
