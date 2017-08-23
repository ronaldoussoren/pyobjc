# Tests for interaction with ObjC "blocks".
#
# These tests are fairly minimal at the moment.
from PyObjCTools.TestSupport import *
from PyObjCTest.block import OCTestBlock
import objc
import sys

if sys.maxsize > 2 ** 32:
    NSRect_tp = b'{CGRect={CGPoint=dd}{CGSize=dd}}'
else:
    NSRect_tp = b'{_NSRect={_NSPoint=ff}{_NSSize=ff}}'

objc.parseBridgeSupport('''\
    <?xml version='1.0'?>
    <!DOCTYPE signatures SYSTEM "file://localhost/System/Library/DTDs/BridgeSupport.dtd">
    <signatures version='1.0'>
      <class name='OCTestBlock'>
        <method selector='getStructBlock'>
          <retval block='true' >
              <retval type='%(NSRect_tp)s' />
              <arg type='d' />
              <arg type='d' />
              <arg type='d' />
              <arg type='d' />
          </retval>
        </method>
        <method selector='getIntBlock'>
          <retval block='true' >
              <retval type='i' />
          </retval>
        </method>
        <method selector='getFloatBlock'>
          <retval block='true' >
              <retval type='d' />
              <arg type='d' />
              <arg type='d' />
          </retval>
        </method>
        <method selector='callOptionalBlock:withValue:'>
          <arg index='0' block='true'>
            <retval type='@'/>
            <arg type='@' />
          </arg>
        </method>
        <method selector='callIntBlock:withValue:'>
          <arg index='0' block='true' >
              <retval type='v' />
              <arg type='i' />
          </arg>
        </method>
        <method selector='callDoubleBlock:withValue:andValue:'>
          <arg index='0' block='true' >
              <retval type='d' />
              <arg type='d' />
              <arg type='d' />
          </arg>
        </method>
        <method selector='callStructBlock:withA:b:c:d:'>
          <arg index='0' block='true' >
              <retval type='%(NSRect_tp)s' />
              <arg type='d' />
              <arg type='d' />
              <arg type='d' />
              <arg type='d' />
          </arg>
        </method>
        <method selector='signatureForBlock1:'>
          <arg index='0' block='true'>
           <retval type='d' />
           <arg type='d' />
           <arg type='d' />
          </arg>
        </method>
        <method selector='signatureForBlock2:'>
          <arg index='0' block='true'>
           <retval type='@' />
           <arg type='@' />
          </arg>
        </method>
        <method selector='signatureForBlock3:'>
          <arg index='0' block='true'>
           <retval type='@' />
           <arg type='s' />
          </arg>
        </method>
        <method selector='signatureForBlock4:'>
          <arg index='0' block='true'>
           <retval type='c' />
           <arg type='i' />
           <arg type='i' />
           <arg type='f' />
          </arg>
        </method>
      </class>
      <class name='NSObject'>
        <method selector='processBlock:'>
          <retval type='d' />
          <arg index='0' block='true' type='@?'>
            <retval type='d'/>
            <arg type='d' />
            <arg type='d' />
          </arg>
        </method>
        <method selector='callWithCompletion:'>
          <arg index='0' block='true' type='@?'>
            <retval type='v'/>
            <arg type='@' />
          </arg>
        </method>
        <method selector='optionalBlock:'>
          <retval type='@' />
          <arg index='0' block='true' type='@?'>
            <retval type='@'/>
            <arg type='@' />
          </arg>
        </method>
      </class>
    </signatures>
    ''' % dict(NSRect_tp=NSRect_tp if sys.version_info[0] == 2 else NSRect_tp.decode('ascii')),
    globals(), 'PyObjCTest')

# The blocks tests can only run when PyObjC was compiled with
# GCC 4.2 or later.
v = OCTestBlock.alloc().init()
if hasattr(v, 'getIntBlock'):
    blocksEnabled = True
else:
    blocksEnabled = False
del v

class BlocksHelper (objc.lookUpClass('NSObject')):
    def processBlock_(self, block):
        return -block(2.5, 4.0)

    def optionalBlock_(self, block):
        if block is None:
            return "no block"

        else:
            return block("x")


class BlocksCompletion (objc.lookUpClass('NSObject')):
    def callWithCompletion_(self, completion):
        completion('hello')
        completion('world')

class BlockWithStoredCompletion (objc.lookUpClass('NSObject')):
    def callWithCompletion_(self, completion):
        self.completion = completion

    def performCompletions(self):
        self.completion('hello')
        self.completion('world')

class TestBlocks (TestCase):
    @min_os_level('10.6')
    @onlyIf(blocksEnabled, "no blocks")
    def testOptionalBlock(self):
        obj = OCTestBlock.alloc().init()

        self.assertEqual(obj.callOptionalBlock_withValue_(None, "hello"), "NOBLOCK")
        self.assertEqual(obj.callOptionalBlock_withValue_(lambda x: x+x, "hello"), "hellohello")

    @min_os_level('10.6')
    @onlyIf(blocksEnabled, "no blocks")
    def testBlockToObjC(self):
        obj = OCTestBlock.alloc().init()

        lst = []
        def callback(v):
            lst.append(v)

        obj.callIntBlock_withValue_(callback, 42)
        self.assertEqual(len(lst), 1)
        obj.callIntBlock_withValue_(callback, 43)
        self.assertEqual(len(lst), 2)

        self.assertEqual(lst, [42, 43])

        class Helper (object):
            def __init__(self):
                self.values = []

            def callback(self, v):
                self.values.append(v)

        helper = Helper()
        obj.callIntBlock_withValue_(helper.callback, 42)
        self.assertEqual(len(helper.values), 1)
        obj.callIntBlock_withValue_(helper.callback, 43)
        self.assertEqual(len(helper.values), 2)
        self.assertEqual(helper.values, [42, 43])

        class Helper2 (objc.lookUpClass('NSObject')):
            def init(self):
                self = objc.super(Helper2, self).init()
                if self is None:
                    return None
                self.values = []
                return self

            def callback_(self, v):
                self.values.append(v)

        helper = Helper2.alloc().init()
        self.assertIsNot(helper, None)
        self.assertEqual(len(helper.values), 0)
        obj.callIntBlock_withValue_(helper.callback_, 42)
        self.assertEqual(len(helper.values), 1)
        obj.callIntBlock_withValue_(helper.callback_, 43)
        self.assertEqual(len(helper.values), 2)
        self.assertEqual(helper.values, [42, 43])

    @min_os_level('10.6')
    @onlyIf(blocksEnabled, "no blocks")
    def testStackBlocksWithDirectUse(self):
        obj = OCTestBlock.alloc().init()
        tester = BlocksCompletion.alloc().init()
        a = []

        obj.callCompletionOn_andArray_(tester, a)
        self.assertEqual(a, ['hello', 'world'])

    @min_os_level('10.6')
    @onlyIf(blocksEnabled, "no blocks")
    def testStackBlocksWithIndirectUse(self):
        obj = OCTestBlock.alloc().init()
        tester = BlockWithStoredCompletion.alloc().init()
        a = []

        obj.callCompletionOn_andArray_(tester, a)
        self.assertEqual(a, [])

        tester.performCompletions()

        self.assertEqual(a, ['hello', 'world'])

    @min_os_level('10.6')
    @onlyIf(blocksEnabled, "no blocks")
    def testBlockToObjC2(self):
        obj = OCTestBlock.alloc().init()

        lst = []
        def callback(a, b):
            return a * b

        self.assertEqual(obj.callDoubleBlock_withValue_andValue_(callback, 2.0, 3.5), 7.0)
        self.assertEqual(obj.callDoubleBlock_withValue_andValue_(callback, 2.5, 10), 25.0)

    @min_os_level('10.6')
    @onlyIf(blocksEnabled, "no blocks")
    def testBlockToObjC3(self):
        obj = OCTestBlock.alloc().init()

        lst = []
        def callback(a, b, c, d):
            return ((a, b), (c, d))

        v = obj.callStructBlock_withA_b_c_d_(callback, 1.5, 2.5, 3.5, 4.5)
        self.assertEqual(v, ((1.5, 2.5), (3.5, 4.5)))


    @min_os_level('10.6')
    @onlyIf(blocksEnabled, "no blocks")
    def testBlockFromObjC(self):
        obj = OCTestBlock.alloc().init()

        block = obj.getIntBlock()
        value = block()
        self.assertEqual(value, 42)

        value = block()
        self.assertEqual(value, 42)

    @min_os_level('10.6')
    @onlyIf(blocksEnabled, "no blocks")
    def testBlockFromObjC2(self):
        obj = OCTestBlock.alloc().init()

        block = obj.getFloatBlock()
        value = block(1, 2)
        self.assertEqual(value, 3.0)

        value = block(2.5, 7.0)
        self.assertEqual(value, 9.5)

    @min_os_level('10.6')
    @onlyIf(blocksEnabled, "no blocks")
    def testBlockFromObjC3(self):
        obj = OCTestBlock.alloc().init()

        block = obj.getStructBlock()
        v = block(1.5, 2.5, 3.5, 4.5)
        self.assertEqual(v, ((1.5, 2.5), (3.5, 4.5)))


    @min_os_level('10.6')
    @onlyIf(blocksEnabled, "no blocks")
    def testBlockSignatures(self):
        obj = OCTestBlock.alloc().init()

        block = obj.getFloatBlock()
        sig = objc.splitSignature(objc._block_signature(block))
        self.assertEqual(sig,  (objc._C_DBL, objc._C_ID + b'?', objc._C_DBL, objc._C_DBL))

        block = obj.getStructBlock()
        sig = objc.splitSignature(objc._block_signature(block))
        self.assertEqual(sig,  (NSRect_tp, objc._C_ID + b'?', objc._C_DBL, objc._C_DBL, objc._C_DBL, objc._C_DBL))

    @min_os_level('10.6')
    @onlyIf(blocksEnabled, "no blocks")
    def testBlockArgumentToPython(self):
        obj = OCTestBlock.alloc().init()
        helper = BlocksHelper.alloc().init()
        value = obj.callProcessBlockOn_(helper)
        self.assertEqual(value, -(2.5 * 4.0))

        value = obj.callOptionalBlockOn_(helper)
        self.assertEqual(value, "no block")

    @min_os_level('10.6')
    @onlyIf(blocksEnabled, "no blocks")
    def testBlocksWithoutMetadata(self):
        obj = OCTestBlock.alloc().init()

        block = obj.getIntBlock2()
        value = block(4)
        self.assertEqual(value, 8)

        block = obj.getIntBlock3()
        value = block(4, 8)
        self.assertEqual(value, 12)

        block = obj.getObjectBlock()
        value = block("hello")
        self.assertEqual(value, 5)

        block = obj.getObjectBlock2()
        value = block("hello", "world");
        self.assertEqual(value, 10)

BLOCK_SELF_TYPE=objc._C_PTR + objc._C_VOID
class TestBlockRuntimeSignature (TestCase):
    @onlyIf(blocksEnabled, "no blocks")
    def testBlock1(self):
        obj = OCTestBlock.alloc().init()
        signature = obj.signatureForBlock1_(lambda a, b: a*b)
        self.assertEqual(signature, (objc._C_DBL + BLOCK_SELF_TYPE + objc._C_DBL + objc._C_DBL).decode('utf-8'))

    @onlyIf(blocksEnabled, "no blocks")
    def testBlock2(self):
        obj = OCTestBlock.alloc().init()
        signature = obj.signatureForBlock2_(lambda a: a)
        self.assertEqual(signature, (objc._C_ID + BLOCK_SELF_TYPE + objc._C_ID).decode('utf-8'))

    @onlyIf(blocksEnabled, "no blocks")
    def testBlock3(self):
        obj = OCTestBlock.alloc().init()
        signature = obj.signatureForBlock3_(lambda a: a)
        self.assertEqual(signature, (objc._C_ID + BLOCK_SELF_TYPE + objc._C_SHT).decode('utf-8'))

    @onlyIf(blocksEnabled, "no blocks")
    def testBlock4(self):
        obj = OCTestBlock.alloc().init()
        signature = obj.signatureForBlock4_(lambda a, b, c: a)
        self.assertEqual(signature, (objc._C_CHR + BLOCK_SELF_TYPE + objc._C_INT + objc._C_INT + objc._C_FLT).decode('utf-8'))



if __name__ == "__main__":
    main()
