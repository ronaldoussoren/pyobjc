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
      </class>
    </signatures>
    ''', globals(), 'PyObjCTest')

# The blocks tests can only run when PyObjC was compiled with
# GCC 4.2 or later.
v = OCTestBlock.alloc().init()
if hasattr(v, 'getIntBlock'):
    blocksEnabled = True
else:
    blocksEnabled = False
del v

class TestBlocks (TestCase):
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
        return

        obj = OCTestBlock.alloc().init()

        lst = []
        def callback(a, b, c, d):
            return ((a, b), (c, d))

        v = obj.callStructBlock_withA_b_c_d_(callback, 1.5, 2.5, 3.5, 4.5)
        print(v)


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

        return

        block = obj.getStructBlock()
        value = block(1, 2, 3, 4)
        self.assertEqual(len(value), 4)
        self.assertEqual(list(value), ((1.0, 2.0), (3.0, 4.0)))


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



if __name__ == "__main__":
    main()
