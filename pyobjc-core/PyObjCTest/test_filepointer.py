"""
Tests for dealing with 'FILE*' argument.
"""

import objc
import os
from PyObjCTest.filepointer import OC_TestFilePointer
from PyObjCTools.TestSupport import TestCase

fp = objc.FILE("/etc/passwd", "r")
gFirstPasswdLine = fp.readline()
fp.close()


class TestFilePointer(TestCase):
    def test_reading_from_null(self):
        o = OC_TestFilePointer.new()
        line = o.readline_(objc.NULL)
        self.assertIs(line, None)

    def testOpenInPython(self):
        with self.subTest("positional"):
            fp = objc.FILE("/etc/passwd", "r")
            o = OC_TestFilePointer.new()
            line = o.readline_(fp)
            fp.close()

            self.assertEqual(line, gFirstPasswdLine.decode("utf-8"))

        with self.subTest("keyword"):
            fp = objc.FILE(path="/etc/passwd", mode="r")
            o = OC_TestFilePointer.new()
            line = o.readline_(fp)
            fp.close()

            self.assertEqual(line, gFirstPasswdLine.decode("utf-8"))

        with self.subTest("no file"):
            with open("/etc/passwd") as fp:
                o = OC_TestFilePointer.new()
                with self.assertRaisesRegex(TypeError, "Expecting objc.FILE, got.*"):
                    o.readline_(fp)

    def testOpenReadingInObjC(self):
        with self.subTest("Valid file"):
            o = OC_TestFilePointer.new()
            fp = o.openFile_withMode_(b"/etc/passwd", b"r")
            self.assertIsInstance(fp, objc.FILE)

            line = fp.readline()
            fp.close()

            self.assertEqual(line, gFirstPasswdLine)

        with self.subTest("NULL file"):
            o = OC_TestFilePointer.new()
            fp = o.openNoFile()
            self.assertIs(fp, None)

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

    def test_invalid_new_args(self):
        with self.assertRaises(TypeError):
            objc.FILE("/etc/passwd", "r", "extra")

        with self.assertRaises(TypeError):
            objc.FILE("/etc/passwd", os.O_RDONLY)

    def test_open_nonexisting(self):
        with self.assertRaises(OSError):
            objc.FILE(f"/tmp/no-such-file.{os.getpid()}", "r")

    def test_open_invalid_mode(self):
        with self.assertRaises(OSError):
            objc.FILE("/etc/passwd", "MODE")

    def test_closing(self):
        with self.subTest("double close"):
            fp = objc.FILE("/etc/passwd", "r")
            fp.close()
            with self.assertRaisesRegex(ValueError, "Closing closed file"):
                fp.close()

        with self.subTest("fileno closed"):
            fp = objc.FILE("/etc/passwd", "r")
            os.close(fp.fileno())
            with self.assertRaisesRegex(OSError, ".*Bad file.*"):
                fp.close()

    def test_has_errors(self):
        fp = objc.FILE("/etc/passwd", "r")
        self.assertFalse(fp.has_errors())

        fp.write(b"hello")
        self.assertTrue(fp.has_errors())

        fp.close()
        with self.assertRaisesRegex(ValueError, "Using closed file"):
            fp.has_errors()

    def test_at_eof(self):
        fp = objc.FILE("/etc/passwd", "r")
        self.assertFalse(fp.at_eof())

        fp.read(1024 * 1024)
        self.assertTrue(fp.at_eof())

        fp.close()
        with self.assertRaisesRegex(ValueError, "Using closed file"):
            fp.at_eof()

    def test_seeking(self):
        fp = objc.FILE("/etc/passwd", "r")
        self.assertEqual(fp.tell(), 0)

        fp.read(100)
        self.assertEqual(fp.tell(), 100)

        fp.seek(10, 0)
        self.assertEqual(fp.tell(), 10)

        fp.seek(15, 1)
        self.assertEqual(fp.tell(), 25)

        fp.seek(whence=0, offset=5)
        self.assertEqual(fp.tell(), 5)

        with self.assertRaises(TypeError):
            fp.seek(offset=5, invalid=10)

        with self.assertRaises(TypeError):
            fp.seek("vier", 0)

        with self.assertRaises(TypeError):
            fp.seek(1, 2, 3)

        with self.assertRaises(TypeError):
            fp.seek(1)

        fp.close()

        with self.assertRaisesRegex(ValueError, "Using closed file"):
            fp.tell()

        with self.assertRaisesRegex(ValueError, "Using closed file"):
            fp.seek(0, 0)

        fp = objc.FILE("/etc/passwd", "r")
        os.close(fp.fileno())

        with self.assertRaisesRegex(OSError, ".*Bad file.*"):
            fp.tell()

        with self.assertRaisesRegex(OSError, ".*Bad file.*"):
            fp.seek(0, 0)

    def test_fileno(self):
        fp = objc.FILE("/etc/passwd", "r")
        self.assertIsInstance(fp.fileno(), int)

        fp.close()
        with self.assertRaisesRegex(ValueError, "Using closed file"):
            fp.fileno()

        fp = objc.FILE("/etc/passwd", "r")
        os.close(fp.fileno())
        self.assertIsInstance(fp.fileno(), int)

    def test_flush(self):
        try:
            fp = objc.FILE("/tmp/pyobjc.filepointer.txt", "w")
            fp.write(b"hello")
            self.assertIs(fp.flush(), None)

            fp.write(b"hello")
            os.close(fp.fileno())
            with self.assertRaisesRegex(OSError, ".*Bad file.*"):
                fp.flush()

            fp = objc.FILE("/etc/passwd", "r")
            fp.close()
            with self.assertRaisesRegex(ValueError, "Using closed file"):
                fp.flush()
        finally:
            if os.path.exists("/tmp/pyobjc.filepointer.txt"):
                os.unlink("/tmp/pyobjc.filepointer.txt")

    def test_write(self):
        try:
            fp = objc.FILE("/tmp/pyobjc.filepointer.txt", "w")

            with self.assertRaises(TypeError):
                fp.write("hello world\n")

            with self.assertRaises(TypeError):
                fp.write(b"hello world\n", 4)

            with self.assertRaises(TypeError):
                fp.write(data=b"hello world\n")

            fp.write(buffer=b"schrijf maar raak\n")
            fp.flush()

            with open("/tmp/pyobjc.filepointer.txt") as stream:
                self.assertEqual(stream.read(), "schrijf maar raak\n")

            fp.close()
            with self.assertRaisesRegex(ValueError, "Using closed file"):
                fp.write(b"meer!")

        finally:
            if os.path.exists("/tmp/pyobjc.filepointer.txt"):
                os.unlink("/tmp/pyobjc.filepointer.txt")

    def test_readline(self):
        fp = objc.FILE("/etc/passwd", "r")
        line = fp.readline()

        self.assertEqual(line, gFirstPasswdLine)

        fp.read(100000)
        self.assertTrue(fp.at_eof())

        self.assertEqual(fp.readline(), b"")

        fp.close()
        with self.assertRaisesRegex(ValueError, "Using closed file"):
            fp.readline()

    def test_read(self):
        with open("/etc/passwd") as fp:
            contents = fp.read().encode()

        fp = objc.FILE("/etc/passwd", "r")
        blob = fp.read(100)

        self.assertEqual(blob, contents[:100])

        fp.seek(len(contents) - 20, 0)
        blob = fp.read(size=100)
        self.assertEqual(blob, contents[-20:])

        blob = fp.read(100)
        self.assertEqual(blob, b"")

        with self.assertRaises(MemoryError):
            fp.read(2**50)

        with self.assertRaises(TypeError):
            fp.read(count=100)

        with self.assertRaises(TypeError):
            fp.read("42")

        with self.assertRaises(TypeError):
            fp.read()

        with self.assertRaises(TypeError):
            fp.read(1, 2)

        fp.close()

        with self.assertRaisesRegex(ValueError, "Using closed file"):
            fp.read(10)
