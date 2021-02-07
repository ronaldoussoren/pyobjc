"""
Tests for dealing with 'FILE*' argument.
"""
import objc
from PyObjCTest.filepointer import OC_TestFilePointer
from PyObjCTools.TestSupport import TestCase

fp = objc.FILE("/etc/passwd", "r")
gFirstPasswdLine = fp.readline()
fp.close()


class TestFilePointer(TestCase):
    def testOpenInPython(self):
        fp = objc.FILE("/etc/passwd", "r")
        o = OC_TestFilePointer.new()
        line = o.readline_(fp)
        fp.close()

        self.assertEqual(line, gFirstPasswdLine.decode("utf-8"))

    def testOpenReadingInObjC(self):
        o = OC_TestFilePointer.new()
        fp = o.openFile_withMode_(b"/etc/passwd", b"r")
        self.assertIsInstance(fp, objc.FILE)

        line = fp.readline()
        fp.close()

        self.assertEqual(line, gFirstPasswdLine)

    def testOpenWritingInObjC(self):
        o = OC_TestFilePointer.new()
        fp = o.openFile_withMode_(b"/tmp/pyobjc.filepointer.txt", b"w")
        self.assertIsInstance(fp, objc.FILE)

        fp.write(b"foobar\n")
        fp.close()

        fp = open("/tmp/pyobjc.filepointer.txt")
        data = fp.read()
        self.assertEqual(data, "foobar\n")
        fp.close()

    def testOpenReadWriteInObjC(self):
        o = OC_TestFilePointer.new()
        fp = o.openFile_withMode_(b"/tmp/pyobjc.filepointer.txt", b"w+")
        self.assertIsInstance(fp, objc.FILE)
        fp.close()
