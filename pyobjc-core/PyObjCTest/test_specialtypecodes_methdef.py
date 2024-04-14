"""
Test handling of the private typecodes:
    _C_NSBOOL, _C_CHAR_AS_INT, _C_CHAR_AS_TEXT and _C_UNICHAR

These typecodes don't actually exists in the ObjC runtime but
are private to PyObjC. We use these to simplify the bridge code
while at the same time getting a higher fidelity bridge.

These tests ensure that private type codes don't leak into the Objective-C runtime.
"""

import objc

from PyObjCTest.fnd import NSObject
import PyObjCTest.specialtypecodes  # noqa: F401
from PyObjCTools.TestSupport import TestCase


class TestTypeCodeLeaks(TestCase):
    def testSimpleTypes(self):
        class OC_TestTypeCodeLeaks_Result(NSObject):
            def myBOOLResult(self):
                return True

            myBOOLResult = objc.selector(myBOOLResult, signature=objc._C_NSBOOL + b"@:")

            def myInt8Result(self):
                return True

            myInt8Result = objc.selector(
                myInt8Result, signature=objc._C_CHAR_AS_INT + b"@:"
            )

            def myByteResult(self):
                return True

            myByteResult = objc.selector(
                myByteResult, signature=objc._C_CHAR_AS_TEXT + b"@:"
            )

            def myUniCharResult(self):
                return True

            myUniCharResult = objc.selector(
                myUniCharResult, signature=objc._C_UNICHAR + b"@:"
            )

            def myUniStrResult(self):
                return True

            myUniStrResult = objc.selector(
                myUniStrResult, signature=objc._C_PTR + objc._C_UNICHAR + b"@:"
            )

        pysig = objc.splitSignature(OC_TestTypeCodeLeaks_Result.myBOOLResult.signature)
        csig = objc.splitSignature(
            OC_TestTypeCodeLeaks_Result.myBOOLResult.native_signature
        )
        self.assertEqual(pysig[0], objc._C_NSBOOL)
        if objc.arch == "arm64":
            self.assertEqual(csig[0], objc._C_BOOL)
        else:
            self.assertEqual(csig[0], objc._C_CHR)

        pysig = objc.splitSignature(OC_TestTypeCodeLeaks_Result.myInt8Result.signature)
        csig = objc.splitSignature(
            OC_TestTypeCodeLeaks_Result.myInt8Result.native_signature
        )
        self.assertEqual(pysig[0], objc._C_CHAR_AS_INT)
        self.assertEqual(csig[0], objc._C_CHR)

        pysig = objc.splitSignature(OC_TestTypeCodeLeaks_Result.myByteResult.signature)
        csig = objc.splitSignature(
            OC_TestTypeCodeLeaks_Result.myByteResult.native_signature
        )
        self.assertEqual(pysig[0], objc._C_CHAR_AS_TEXT)
        self.assertEqual(csig[0], objc._C_CHR)

        pysig = objc.splitSignature(
            OC_TestTypeCodeLeaks_Result.myUniCharResult.signature
        )
        csig = objc.splitSignature(
            OC_TestTypeCodeLeaks_Result.myUniCharResult.native_signature
        )
        self.assertEqual(pysig[0], objc._C_UNICHAR)
        self.assertEqual(csig[0], objc._C_SHT)

        pysig = objc.splitSignature(
            OC_TestTypeCodeLeaks_Result.myUniStrResult.signature
        )
        csig = objc.splitSignature(
            OC_TestTypeCodeLeaks_Result.myUniStrResult.native_signature
        )
        self.assertEqual(pysig[0], objc._C_PTR + objc._C_UNICHAR)
        self.assertEqual(csig[0], objc._C_PTR + objc._C_SHT)

    def testByRefIn(self):
        class OC_TestTypeCodeLeaks_RefIn(NSObject):
            def myBOOLArg_(self, arg):
                pass

            myBOOLArg_ = objc.selector(
                myBOOLArg_, signature=b"v@:" + objc._C_IN + objc._C_PTR + objc._C_NSBOOL
            )

            def myInt8Arg_(self, arg):
                pass

            myInt8Arg_ = objc.selector(
                myInt8Arg_,
                signature=b"v@:" + objc._C_IN + objc._C_PTR + objc._C_CHAR_AS_INT,
            )

            def myByteArg_(self, arg):
                pass

            myByteArg_ = objc.selector(
                myByteArg_,
                signature=b"v@:" + objc._C_IN + objc._C_PTR + objc._C_CHAR_AS_TEXT,
            )

            def myUniCharArg_(self, arg):
                pass

            myUniCharArg_ = objc.selector(
                myUniCharArg_,
                signature=b"v@:" + objc._C_IN + objc._C_PTR + objc._C_UNICHAR,
            )

        pysig = objc.splitSignature(OC_TestTypeCodeLeaks_RefIn.myBOOLArg_.signature)
        csig = objc.splitSignature(
            OC_TestTypeCodeLeaks_RefIn.myBOOLArg_.native_signature
        )
        self.assertEqual(pysig[3], objc._C_IN + objc._C_PTR + objc._C_NSBOOL)
        if objc.arch == "arm64":
            self.assertEqual(csig[3], objc._C_IN + objc._C_PTR + objc._C_BOOL)
        else:
            self.assertEqual(csig[3], objc._C_IN + objc._C_PTR + objc._C_CHR)

        pysig = objc.splitSignature(OC_TestTypeCodeLeaks_RefIn.myInt8Arg_.signature)
        csig = objc.splitSignature(
            OC_TestTypeCodeLeaks_RefIn.myInt8Arg_.native_signature
        )
        self.assertEqual(pysig[3], objc._C_IN + objc._C_PTR + objc._C_CHAR_AS_INT)
        self.assertEqual(csig[3], objc._C_IN + objc._C_PTR + objc._C_CHR)

        pysig = objc.splitSignature(OC_TestTypeCodeLeaks_RefIn.myByteArg_.signature)
        csig = objc.splitSignature(
            OC_TestTypeCodeLeaks_RefIn.myByteArg_.native_signature
        )
        self.assertEqual(pysig[3], objc._C_IN + objc._C_PTR + objc._C_CHAR_AS_TEXT)
        self.assertEqual(csig[3], objc._C_IN + objc._C_PTR + objc._C_CHR)

        pysig = objc.splitSignature(OC_TestTypeCodeLeaks_RefIn.myUniCharArg_.signature)
        csig = objc.splitSignature(
            OC_TestTypeCodeLeaks_RefIn.myUniCharArg_.native_signature
        )
        self.assertEqual(pysig[3], objc._C_IN + objc._C_PTR + objc._C_UNICHAR)
        self.assertEqual(csig[3], objc._C_IN + objc._C_PTR + objc._C_SHT)

    def testByRefInOut(self):
        class OC_TestTypeCodeLeaks_RefInOut(NSObject):
            def myBOOLArg_(self, arg):
                pass

            myBOOLArg_ = objc.selector(
                myBOOLArg_,
                signature=b"v@:" + objc._C_INOUT + objc._C_PTR + objc._C_NSBOOL,
            )

            def myInt8Arg_(self, arg):
                pass

            myInt8Arg_ = objc.selector(
                myInt8Arg_,
                signature=b"v@:" + objc._C_INOUT + objc._C_PTR + objc._C_CHAR_AS_INT,
            )

            def myByteArg_(self, arg):
                pass

            myByteArg_ = objc.selector(
                myByteArg_,
                signature=b"v@:" + objc._C_INOUT + objc._C_PTR + objc._C_CHAR_AS_TEXT,
            )

            def myUniCharArg_(self, arg):
                pass

            myUniCharArg_ = objc.selector(
                myUniCharArg_,
                signature=b"v@:" + objc._C_INOUT + objc._C_PTR + objc._C_UNICHAR,
            )

        pysig = objc.splitSignature(OC_TestTypeCodeLeaks_RefInOut.myBOOLArg_.signature)
        csig = objc.splitSignature(
            OC_TestTypeCodeLeaks_RefInOut.myBOOLArg_.native_signature
        )
        self.assertEqual(pysig[3], objc._C_INOUT + objc._C_PTR + objc._C_NSBOOL)
        if objc.arch == "arm64":
            self.assertEqual(csig[3], objc._C_INOUT + objc._C_PTR + objc._C_BOOL)
        else:
            self.assertEqual(csig[3], objc._C_INOUT + objc._C_PTR + objc._C_CHR)

        pysig = objc.splitSignature(OC_TestTypeCodeLeaks_RefInOut.myInt8Arg_.signature)
        csig = objc.splitSignature(
            OC_TestTypeCodeLeaks_RefInOut.myInt8Arg_.native_signature
        )
        self.assertEqual(pysig[3], objc._C_INOUT + objc._C_PTR + objc._C_CHAR_AS_INT)
        self.assertEqual(csig[3], objc._C_INOUT + objc._C_PTR + objc._C_CHR)

        pysig = objc.splitSignature(OC_TestTypeCodeLeaks_RefInOut.myByteArg_.signature)
        csig = objc.splitSignature(
            OC_TestTypeCodeLeaks_RefInOut.myByteArg_.native_signature
        )
        self.assertEqual(pysig[3], objc._C_INOUT + objc._C_PTR + objc._C_CHAR_AS_TEXT)
        self.assertEqual(csig[3], objc._C_INOUT + objc._C_PTR + objc._C_CHR)

        pysig = objc.splitSignature(
            OC_TestTypeCodeLeaks_RefInOut.myUniCharArg_.signature
        )
        csig = objc.splitSignature(
            OC_TestTypeCodeLeaks_RefInOut.myUniCharArg_.native_signature
        )
        self.assertEqual(pysig[3], objc._C_INOUT + objc._C_PTR + objc._C_UNICHAR)
        self.assertEqual(csig[3], objc._C_INOUT + objc._C_PTR + objc._C_SHT)

    def testByRefOut(self):
        class OC_TestTypeCodeLeaks_RefOut(NSObject):
            def myBOOLArg_(self, arg):
                pass

            myBOOLArg_ = objc.selector(
                myBOOLArg_,
                signature=b"v@:" + objc._C_OUT + objc._C_PTR + objc._C_NSBOOL,
            )

            def myInt8Arg_(self, arg):
                pass

            myInt8Arg_ = objc.selector(
                myInt8Arg_,
                signature=b"v@:" + objc._C_OUT + objc._C_PTR + objc._C_CHAR_AS_INT,
            )

            def myByteArg_(self, arg):
                pass

            myByteArg_ = objc.selector(
                myByteArg_,
                signature=b"v@:" + objc._C_OUT + objc._C_PTR + objc._C_CHAR_AS_TEXT,
            )

            def myUniCharArg_(self, arg):
                pass

            myUniCharArg_ = objc.selector(
                myUniCharArg_,
                signature=b"v@:" + objc._C_OUT + objc._C_PTR + objc._C_UNICHAR,
            )

        pysig = objc.splitSignature(OC_TestTypeCodeLeaks_RefOut.myBOOLArg_.signature)
        csig = objc.splitSignature(
            OC_TestTypeCodeLeaks_RefOut.myBOOLArg_.native_signature
        )
        self.assertEqual(pysig[3], objc._C_OUT + objc._C_PTR + objc._C_NSBOOL)
        if objc.arch == "arm64":
            self.assertEqual(csig[3], objc._C_OUT + objc._C_PTR + objc._C_BOOL)
        else:
            self.assertEqual(csig[3], objc._C_OUT + objc._C_PTR + objc._C_CHR)

        pysig = objc.splitSignature(OC_TestTypeCodeLeaks_RefOut.myInt8Arg_.signature)
        csig = objc.splitSignature(
            OC_TestTypeCodeLeaks_RefOut.myInt8Arg_.native_signature
        )
        self.assertEqual(pysig[3], objc._C_OUT + objc._C_PTR + objc._C_CHAR_AS_INT)
        self.assertEqual(csig[3], objc._C_OUT + objc._C_PTR + objc._C_CHR)

        pysig = objc.splitSignature(OC_TestTypeCodeLeaks_RefOut.myByteArg_.signature)
        csig = objc.splitSignature(
            OC_TestTypeCodeLeaks_RefOut.myByteArg_.native_signature
        )
        self.assertEqual(pysig[3], objc._C_OUT + objc._C_PTR + objc._C_CHAR_AS_TEXT)
        self.assertEqual(csig[3], objc._C_OUT + objc._C_PTR + objc._C_CHR)

        pysig = objc.splitSignature(OC_TestTypeCodeLeaks_RefOut.myUniCharArg_.signature)
        csig = objc.splitSignature(
            OC_TestTypeCodeLeaks_RefOut.myUniCharArg_.native_signature
        )
        self.assertEqual(pysig[3], objc._C_OUT + objc._C_PTR + objc._C_UNICHAR)
        self.assertEqual(csig[3], objc._C_OUT + objc._C_PTR + objc._C_SHT)

    def testByRefConst(self):
        class OC_TestTypeCodeLeaks_RefConst(NSObject):
            def myBOOLArg_(self, arg):
                pass

            myBOOLArg_ = objc.selector(
                myBOOLArg_,
                signature=b"v@:" + objc._C_CONST + objc._C_PTR + objc._C_NSBOOL,
            )

            def myInt8Arg_(self, arg):
                pass

            myInt8Arg_ = objc.selector(
                myInt8Arg_,
                signature=b"v@:" + objc._C_CONST + objc._C_PTR + objc._C_CHAR_AS_INT,
            )

            def myByteArg_(self, arg):
                pass

            myByteArg_ = objc.selector(
                myByteArg_,
                signature=b"v@:" + objc._C_CONST + objc._C_PTR + objc._C_CHAR_AS_TEXT,
            )

            def myUniCharArg_(self, arg):
                pass

            myUniCharArg_ = objc.selector(
                myUniCharArg_,
                signature=b"v@:" + objc._C_CONST + objc._C_PTR + objc._C_UNICHAR,
            )

        pysig = objc.splitSignature(OC_TestTypeCodeLeaks_RefConst.myBOOLArg_.signature)
        csig = objc.splitSignature(
            OC_TestTypeCodeLeaks_RefConst.myBOOLArg_.native_signature
        )
        self.assertEqual(pysig[3], objc._C_CONST + objc._C_PTR + objc._C_NSBOOL)
        if objc.arch == "arm64":
            self.assertEqual(csig[3], objc._C_CONST + objc._C_PTR + objc._C_BOOL)
        else:
            self.assertEqual(csig[3], objc._C_CONST + objc._C_PTR + objc._C_CHR)

        pysig = objc.splitSignature(OC_TestTypeCodeLeaks_RefConst.myInt8Arg_.signature)
        csig = objc.splitSignature(
            OC_TestTypeCodeLeaks_RefConst.myInt8Arg_.native_signature
        )
        self.assertEqual(pysig[3], objc._C_CONST + objc._C_PTR + objc._C_CHAR_AS_INT)
        self.assertEqual(csig[3], objc._C_CONST + objc._C_PTR + objc._C_CHR)

        pysig = objc.splitSignature(OC_TestTypeCodeLeaks_RefConst.myByteArg_.signature)
        csig = objc.splitSignature(
            OC_TestTypeCodeLeaks_RefConst.myByteArg_.native_signature
        )
        self.assertEqual(pysig[3], objc._C_CONST + objc._C_PTR + objc._C_CHAR_AS_TEXT)
        self.assertEqual(csig[3], objc._C_CONST + objc._C_PTR + objc._C_CHR)

        pysig = objc.splitSignature(
            OC_TestTypeCodeLeaks_RefConst.myUniCharArg_.signature
        )
        csig = objc.splitSignature(
            OC_TestTypeCodeLeaks_RefConst.myUniCharArg_.native_signature
        )
        self.assertEqual(pysig[3], objc._C_CONST + objc._C_PTR + objc._C_UNICHAR)
        self.assertEqual(csig[3], objc._C_CONST + objc._C_PTR + objc._C_SHT)

    def testInArrayDef(self):
        class OC_TestTypeCodeLeaks_ArrayDef(NSObject):
            def myBOOLArg_(self, arg):
                pass

            myBOOLArg_ = objc.selector(
                myBOOLArg_,
                signature=b"v@:"
                + objc._C_ARY_B
                + b"4"
                + objc._C_NSBOOL
                + objc._C_ARY_E,
            )

            def myInt8Arg_(self, arg):
                pass

            myInt8Arg_ = objc.selector(
                myInt8Arg_,
                signature=b"v@:"
                + objc._C_ARY_B
                + b"4"
                + objc._C_CHAR_AS_INT
                + objc._C_ARY_E,
            )

            def myByteArg_(self, arg):
                pass

            myByteArg_ = objc.selector(
                myByteArg_,
                signature=b"v@:"
                + objc._C_ARY_B
                + b"4"
                + objc._C_CHAR_AS_TEXT
                + objc._C_ARY_E,
            )

            def myUniCharArg_(self, arg):
                pass

            myUniCharArg_ = objc.selector(
                myUniCharArg_,
                signature=b"v@:"
                + objc._C_ARY_B
                + b"4"
                + objc._C_UNICHAR
                + objc._C_ARY_E,
            )

        pysig = objc.splitSignature(OC_TestTypeCodeLeaks_ArrayDef.myBOOLArg_.signature)
        csig = objc.splitSignature(
            OC_TestTypeCodeLeaks_ArrayDef.myBOOLArg_.native_signature
        )
        self.assertEqual(
            pysig[3], objc._C_ARY_B + b"4" + objc._C_NSBOOL + objc._C_ARY_E
        )
        if objc.arch == "arm64":
            self.assertEqual(
                csig[3], objc._C_ARY_B + b"4" + objc._C_BOOL + objc._C_ARY_E
            )
        else:
            self.assertEqual(
                csig[3], objc._C_ARY_B + b"4" + objc._C_CHR + objc._C_ARY_E
            )

        pysig = objc.splitSignature(OC_TestTypeCodeLeaks_ArrayDef.myInt8Arg_.signature)
        csig = objc.splitSignature(
            OC_TestTypeCodeLeaks_ArrayDef.myInt8Arg_.native_signature
        )
        self.assertEqual(
            pysig[3], objc._C_ARY_B + b"4" + objc._C_CHAR_AS_INT + objc._C_ARY_E
        )
        self.assertEqual(csig[3], objc._C_ARY_B + b"4" + objc._C_CHR + objc._C_ARY_E)

        pysig = objc.splitSignature(OC_TestTypeCodeLeaks_ArrayDef.myByteArg_.signature)
        csig = objc.splitSignature(
            OC_TestTypeCodeLeaks_ArrayDef.myByteArg_.native_signature
        )
        self.assertEqual(
            pysig[3], objc._C_ARY_B + b"4" + objc._C_CHAR_AS_TEXT + objc._C_ARY_E
        )
        self.assertEqual(csig[3], objc._C_ARY_B + b"4" + objc._C_CHR + objc._C_ARY_E)

        pysig = objc.splitSignature(
            OC_TestTypeCodeLeaks_ArrayDef.myUniCharArg_.signature
        )
        csig = objc.splitSignature(
            OC_TestTypeCodeLeaks_ArrayDef.myUniCharArg_.native_signature
        )
        self.assertEqual(
            pysig[3], objc._C_ARY_B + b"4" + objc._C_UNICHAR + objc._C_ARY_E
        )
        self.assertEqual(csig[3], objc._C_ARY_B + b"4" + objc._C_SHT + objc._C_ARY_E)

    def testInStructDef(self):
        class OC_TestTypeCodeLeaks_StructDef(NSObject):
            def myBOOLArg_(self, arg):
                pass

            myBOOLArg_ = objc.selector(
                myBOOLArg_,
                signature=b"v@:"
                + objc._C_STRUCT_B
                + b"test="
                + objc._C_NSBOOL
                + objc._C_STRUCT_E,
            )

            def myInt8Arg_(self, arg):
                pass

            myInt8Arg_ = objc.selector(
                myInt8Arg_,
                signature=b"v@:"
                + objc._C_STRUCT_B
                + b"test="
                + objc._C_CHAR_AS_INT
                + objc._C_STRUCT_E,
            )

            def myByteArg_(self, arg):
                pass

            myByteArg_ = objc.selector(
                myByteArg_,
                signature=b"v@:"
                + objc._C_STRUCT_B
                + b"test="
                + objc._C_CHAR_AS_TEXT
                + objc._C_STRUCT_E,
            )

            def myUniCharArg_(self, arg):
                pass

            myUniCharArg_ = objc.selector(
                myUniCharArg_,
                signature=b"v@:"
                + objc._C_STRUCT_B
                + b"test="
                + objc._C_UNICHAR
                + objc._C_STRUCT_E,
            )

        pysig = objc.splitSignature(OC_TestTypeCodeLeaks_StructDef.myBOOLArg_.signature)
        csig = objc.splitSignature(
            OC_TestTypeCodeLeaks_StructDef.myBOOLArg_.native_signature
        )
        self.assertEqual(
            pysig[3], objc._C_STRUCT_B + b"test=" + objc._C_NSBOOL + objc._C_STRUCT_E
        )
        if objc.arch == "arm64":
            self.assertEqual(
                csig[3], objc._C_STRUCT_B + b"test=" + objc._C_BOOL + objc._C_STRUCT_E
            )
        else:
            self.assertEqual(
                csig[3], objc._C_STRUCT_B + b"test=" + objc._C_CHR + objc._C_STRUCT_E
            )

        pysig = objc.splitSignature(OC_TestTypeCodeLeaks_StructDef.myInt8Arg_.signature)
        csig = objc.splitSignature(
            OC_TestTypeCodeLeaks_StructDef.myInt8Arg_.native_signature
        )
        self.assertEqual(
            pysig[3],
            objc._C_STRUCT_B + b"test=" + objc._C_CHAR_AS_INT + objc._C_STRUCT_E,
        )
        self.assertEqual(
            csig[3], objc._C_STRUCT_B + b"test=" + objc._C_CHR + objc._C_STRUCT_E
        )

        pysig = objc.splitSignature(OC_TestTypeCodeLeaks_StructDef.myByteArg_.signature)
        csig = objc.splitSignature(
            OC_TestTypeCodeLeaks_StructDef.myByteArg_.native_signature
        )
        self.assertEqual(
            pysig[3],
            objc._C_STRUCT_B + b"test=" + objc._C_CHAR_AS_TEXT + objc._C_STRUCT_E,
        )
        self.assertEqual(
            csig[3], objc._C_STRUCT_B + b"test=" + objc._C_CHR + objc._C_STRUCT_E
        )

        pysig = objc.splitSignature(
            OC_TestTypeCodeLeaks_StructDef.myUniCharArg_.signature
        )
        csig = objc.splitSignature(
            OC_TestTypeCodeLeaks_StructDef.myUniCharArg_.native_signature
        )
        self.assertEqual(
            pysig[3], objc._C_STRUCT_B + b"test=" + objc._C_UNICHAR + objc._C_STRUCT_E
        )
        self.assertEqual(
            csig[3], objc._C_STRUCT_B + b"test=" + objc._C_SHT + objc._C_STRUCT_E
        )
