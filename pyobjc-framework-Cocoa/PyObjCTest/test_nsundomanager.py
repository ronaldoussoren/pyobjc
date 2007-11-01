import unittest
import objc

from Foundation import *
import Foundation

class TestHelper (NSObject):
    def incFoo_(self, foo):
        foo[0] += 1

class TestNSUndoManager(unittest.TestCase):
    def testUndoManager(self):
        x = TestHelper.new()
        m = NSUndoManager.new()
        l = [ 0 ]

        m.prepareWithInvocationTarget_(x).incFoo_(l)
        m.undo()

        self.assertEquals(l[0], 1)

    def __del__(self, objc=objc):
        objc.recycleAutoreleasePool()

## Undo Integer test
## From David Eppstein
# test ability of int argument to pass through undo and then
# be used as parameter to another routine expecting an int
#
# the actual routine I want to use is
# NSTableView.editColumn_row_withEvent_select_
# but that involves setting up a UI; instead use NSIndexSpecifier

if hasattr(Foundation, 'NSIndexSpecifier'):
    class TestUndoInt(unittest.TestCase):
        class UndoInt(NSObject):
            undo = NSUndoManager.alloc().init()
            idx = NSIndexSpecifier.alloc().init()
            idx.setIndex_(0)

            def test_(self,i):
                self.undo.prepareWithInvocationTarget_(self).test_(self.idx.index())
                self.idx.setIndex_(i)

        def testUndoInt(self):
            # test that undo works
            x = TestUndoInt.UndoInt.alloc().init()
            x.test_(3)
            assert(x.idx.index() == 3)
            x.undo.undo()
            assert(x.idx.index() == 0)
## end Undo Integer test


class TestSubclassingUndo(unittest.TestCase):
    # Bugreport: 678759 Subclassing NSUndoManager fails

    pass

if 0:
    def testSubclass(self):
        class UndoSubclass (NSUndoManager):
            pass

        x = TestHelper.new()
        m = UndoSubclass.new()
        l = [ 0 ]

        m.prepareWithInvocationTarget_(x).incFoo_(l)
        m.undo()

        self.assertEquals(l[0], 1)

if __name__ == '__main__':
    unittest.main( )
