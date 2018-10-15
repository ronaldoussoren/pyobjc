import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CoreML

    class TestMLModelConfiguration (TestCase):
        def test_constants(self):
            self.assertEqual(CoreML.MLComputeUnitsCPUOnly, 0)
            self.assertEqual(CoreML.MLComputeUnitsCPUAndGPU, 1)
            self.assertEqual(CoreML.MLComputeUnitsAll, 2)


if __name__ == "__main__":
    main()
