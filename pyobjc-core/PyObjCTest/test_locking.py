"""
Test locking objects and interaction with @synchronized() statements

These tests take an annoyingly long time to ensure that we'd hit a race condition when
locking doesn't actually lock. It should be possible to find a faster mechanism for this.
"""

import threading
import time

import objc
from PyObjCTest.locking import OC_LockTest
from PyObjCTools.TestSupport import TestCase

NSAutoreleasePool = objc.lookUpClass("NSAutoreleasePool")


class OtherThread(threading.Thread):
    def __init__(self, obj):
        self.obj = obj

        threading.Thread.__init__(self)

    def run(self):
        pool = NSAutoreleasePool.alloc().init()

        lck = objc.object_lock(self.obj)

        for i in range(6):
            time.sleep(0.05)
            lck.lock()
            if self.obj.isLocked():
                self.obj.appendToList_("LOCK FOUND")

            self.obj.setLocked_(True)
            self.obj.appendToList_("thread %d a" % (i,))
            time.sleep(0.5)
            self.obj.appendToList_("thread %d b" % (i,))
            self.obj.setLocked_(False)
            lck.unlock()

        del pool


class ObjCThread(threading.Thread):
    def __init__(self, obj):
        self.obj = obj

        threading.Thread.__init__(self)

    def run(self):
        pool = NSAutoreleasePool.alloc().init()

        native = OC_LockTest.alloc().init()
        native.threadFunc_(self.obj)

        del native
        del pool


class BaseClass(objc.lookUpClass("NSObject")):
    def initWithList_(self, aList):
        self = objc.super(BaseClass, self).init()
        if self is None:
            return None

        self.list = aList
        self._locked = False
        return self

    def isLocked(self):
        return self._locked

    def setLocked_(self, value):
        self._locked = value

    def appendToList_(self, value):
        self.list.append(value)


class TestLockingBasic(TestCase):
    def testBasicLocking(self):
        lst = []

        obj = BaseClass.alloc().initWithList_(lst)
        lck = objc.object_lock(obj)

        thr = OtherThread(obj)
        thr.start()
        for _ in range(5):
            time.sleep(0.1)
            lck.lock()
            self.assertFalse(obj.isLocked())
            obj.setLocked_(True)
            obj.appendToList_("mainthread")
            obj.setLocked_(False)
            lck.unlock()

        thr.join()

        self.assertNotIn("LOCK FOUND", lst)
        for idx in range(len(lst)):
            if lst[idx].endswith(" a"):
                self.assertTrue(lst[idx + 1].endswith(" b"))

    def testObjectiveCLocking(self):
        lst = []
        lst = []

        obj = BaseClass.alloc().initWithList_(lst)
        lck = objc.object_lock(obj)

        thr = ObjCThread(obj)
        thr.start()
        for _ in range(5):
            time.sleep(0.1)
            lck.lock()
            self.assertFalse(obj.isLocked())
            obj.setLocked_(True)
            obj.appendToList_("mainthread")
            time.sleep(0.5)
            obj.setLocked_(False)
            lck.unlock()

        thr.join()

        self.assertNotIn("LOCK FOUND", lst)
        for idx in range(len(lst)):
            if lst[idx].endswith(" a"):
                self.assertTrue(lst[idx + 1].endswith(" b"))


class TestLockingWithStatement(TestCase):
    def testBasicLocking(self):
        lst = []
        lst = []

        obj = BaseClass.alloc().initWithList_(lst)

        thr = OtherThread(obj)
        thr.start()
        for _ in range(5):
            time.sleep(0.1)
            with objc.object_lock(obj):
                self.assertFalse(obj.isLocked())
                obj.setLocked_(True)
                obj.appendToList_("mainthread")
                time.sleep(0.5)
                obj.setLocked_(False)

        thr.join()

        self.assertNotIn("LOCK FOUND", lst)
        for idx in range(len(lst)):
            if lst[idx].endswith(" a"):
                self.assertTrue(lst[idx + 1].endswith(" b"))
