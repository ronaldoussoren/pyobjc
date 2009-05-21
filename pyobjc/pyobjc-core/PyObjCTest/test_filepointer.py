from PyObjCTest.filepointer import OC_TestFilePointer
from PyObjCTools.TestSupport import *

fp = open('/etc/passwd', 'r')
gFirstPasswdLine = fp.readline()
fp.close()

class TestFilePointer (TestCase):
    def testOpenInPython(self):
        fp = open('/etc/passwd', 'r')
        o = OC_TestFilePointer.new()
        line = o.readline_(fp)
        fp.close()

        self.assertEquals(line, gFirstPasswdLine)

    def testOpenReadingInObjC(self):
        o = OC_TestFilePointer.new()
        fp = o.openFile_withMode_('/etc/passwd', 'r')
        self.assert_(isinstance(fp, file))
        self.assertEquals(fp.mode, 'r')

        line = fp.readline()
        fp.close()

        self.assertEquals(line, gFirstPasswdLine)

    def testOpenWritingInObjC(self):
        o = OC_TestFilePointer.new()
        fp = o.openFile_withMode_('/tmp/pyobjc.filepointer.txt', 'w')
        self.assert_(isinstance(fp, file))
        self.assertEquals(fp.mode, 'w')

        fp.write('foobar\n')
        fp.flush() # XXX: this isn't quite correct?
        fp.close()

        fp = open('/tmp/pyobjc.filepointer.txt')
        data = fp.read()
        self.assertEquals(data, 'foobar\n')
        fp.close()

    def testOpenReadWriteInObjC(self):
        o = OC_TestFilePointer.new()
        fp = o.openFile_withMode_('/tmp/pyobjc.filepointer.txt', 'w+')
        self.assert_(isinstance(fp, file))
        self.assertEquals(fp.mode, 'w+')

    def dont_testOpenAppendInObjC(self):
        # We can't reliably detect append mode, don't bother testing for it.
        o = OC_TestFilePointer.new()
        fp = o.openFile_withMode_('/tmp/pyobjc.filepointer.txt', 'a')
        self.assert_(isinstance(fp, file))
        self.assertEquals(fp.mode, 'a')

        o = OC_TestFilePointer.new()
        fp = o.openFile_withMode_('/tmp/pyobjc.filepointer.txt', 'a+')
        self.assert_(isinstance(fp, file))
        self.assertEquals(fp.mode, 'a+')

if __name__ == "__main__":
    main()
