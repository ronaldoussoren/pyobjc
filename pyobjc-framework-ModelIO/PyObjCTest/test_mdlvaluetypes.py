from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2**32:
    import ModelIO

    class TestMDLValueTypes (TestCase):
        @min_os_level('10.13')
        @expectedFailure
        def testMethodsSIMD(self):
            # SIMD types
            self.assertArgSizeInArg(MDLMatrix4x4Array.setFloat4x4Array_count_, 0, 1)
            self.assertArgIsIn(MDLMatrix4x4Array.setFloat4x4Array_count_, 0)

            self.assertArgSizeInArg(MDLMatrix4x4Array.setDouble4x4Array_count_, 0, 1)
            self.assertArgIsIn(MDLMatrix4x4Array.setDouble4x4Array_count_, 0)

            self.assertArgSizeInArg(MDLMatrix4x4Array.getFloat4x4Array_maxCount_, 0, 1)
            self.assertArgSizeInResult(MDLMatrix4x4Array.getFloat4x4Array_maxCount_, 0)
            self.assertArgIsOut(MDLMatrix4x4Array.getFloat4x4Array_maxCount_, 0)

            self.assertArgSizeInArg(MDLMatrix4x4Array.getDouble4x4Array_maxCount_, 0, 1)
            self.assertArgSizeInResult(MDLMatrix4x4Array.getDouble4x4Array_maxCount_, 0)
            self.assertArgIsOut(MDLMatrix4x4Array.getDouble4x4Array_maxCount_, 0)


if __name__ == "__main__":
    main()
