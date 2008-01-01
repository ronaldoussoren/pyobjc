'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
import unittest
import LatentSemanticMapping

class TestLatentSemanticMapping (unittest.TestCase):
    def testClasses(self):
        self.assert_( hasattr(LatentSemanticMapping, 'LSMMapRef') )
        self.assert_( issubclass(LatentSemanticMapping.LSMMapRef, objc.lookUpClass('NSCFType')) )
        self.assert_( LatentSemanticMapping.LSMMapRef is not objc.lookUpClass('NSCFType') )

        self.assert_( hasattr(LatentSemanticMapping, 'LSMTextRef') )
        self.assert_( issubclass(LatentSemanticMapping.LSMTextRef, objc.lookUpClass('NSCFType')) )
        self.assert_( LatentSemanticMapping.LSMTextRef is not objc.lookUpClass('NSCFType') )

        self.assert_( hasattr(LatentSemanticMapping, 'LSMResultRef') )
        self.assert_( issubclass(LatentSemanticMapping.LSMResultRef, objc.lookUpClass('NSCFType')) )
        self.assert_( LatentSemanticMapping.LSMResultRef is not objc.lookUpClass('NSCFType') )

    def testValues(self):
         self.assert_( hasattr(LatentSemanticMapping, 'kLSMMapNoSuchCategory') )
         self.assert_( isinstance(LatentSemanticMapping.kLSMMapNoSuchCategory, (int, long)) )
         self.assertEquals(LatentSemanticMapping.kLSMMapNoSuchCategory, -6641)


         self.assert_( hasattr(LatentSemanticMapping, 'kLSMAlgorithmDense') )
         self.assert_( isinstance(LatentSemanticMapping.kLSMAlgorithmDense, (str, unicode)) )
         self.assertEquals(LatentSemanticMapping.kLSMAlgorithmDense, 'LSMAlgorithmDense')


    def testFunctions(self):
        self.assert_( hasattr(LatentSemanticMapping, 'LSMMapCreate') )
        self.assert_( hasattr(LatentSemanticMapping, 'LSMMapSetStopWords') )



if __name__ == "__main__":
    unittest.main()

