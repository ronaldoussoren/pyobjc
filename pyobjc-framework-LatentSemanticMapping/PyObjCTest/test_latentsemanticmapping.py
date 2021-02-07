import LatentSemanticMapping
from PyObjCTools.TestSupport import TestCase
import objc


class TestLatentSemanticMapping(TestCase):
    def testConstants(self):
        self.assertEqual(LatentSemanticMapping.kLSMMapOutOfState, -6640)
        self.assertEqual(LatentSemanticMapping.kLSMMapNoSuchCategory, -6641)
        self.assertEqual(LatentSemanticMapping.kLSMMapWriteError, -6642)
        self.assertEqual(LatentSemanticMapping.kLSMMapBadPath, -6643)
        self.assertEqual(LatentSemanticMapping.kLSMMapBadCluster, -6644)
        self.assertEqual(LatentSemanticMapping.kLSMMapOverflow, -6645)

        self.assertEqual(LatentSemanticMapping.kLSMMapPairs, 1)
        self.assertEqual(LatentSemanticMapping.kLSMMapTriplets, 2)
        self.assertEqual(LatentSemanticMapping.kLSMMapHashText, 256)

        self.assertEqual(LatentSemanticMapping.kLSMAlgorithmKey, "LSMAlgorithm")
        self.assertEqual(LatentSemanticMapping.kLSMAlgorithmDense, "LSMAlgorithmDense")
        self.assertEqual(
            LatentSemanticMapping.kLSMAlgorithmSparse, "LSMAlgorithmSparse"
        )
        self.assertEqual(LatentSemanticMapping.kLSMPrecisionKey, "LSMPrecision")
        self.assertEqual(LatentSemanticMapping.kLSMPrecisionFloat, "LSMPrecisionFloat")
        self.assertEqual(
            LatentSemanticMapping.kLSMPrecisionDouble, "LSMPrecisionDouble"
        )
        self.assertEqual(LatentSemanticMapping.kLSMDimensionKey, "LSMDimension")
        self.assertEqual(LatentSemanticMapping.kLSMIterationsKey, "LSMIterations")
        self.assertEqual(LatentSemanticMapping.kLSMSweepAgeKey, "LSMSweepAge")
        self.assertEqual(LatentSemanticMapping.kLSMSweepCutoffKey, "LSMSweepCutoff")

        self.assertEqual(LatentSemanticMapping.kLSMClusterCategories, 0)
        self.assertEqual(LatentSemanticMapping.kLSMClusterWords, 1)
        self.assertEqual(LatentSemanticMapping.kLSMClusterTokens, 2)
        self.assertEqual(LatentSemanticMapping.kLSMClusterKMeans, 0)
        self.assertEqual(LatentSemanticMapping.kLSMClusterAgglomerative, 4)

        self.assertEqual(LatentSemanticMapping.kLSMResultBestWords, 1)

        self.assertEqual(LatentSemanticMapping.kLSMMapDiscardCounts, 1)
        self.assertEqual(LatentSemanticMapping.kLSMMapLoadMutable, 2)

        self.assertEqual(LatentSemanticMapping.kLSMTextPreserveCase, 1)
        self.assertEqual(LatentSemanticMapping.kLSMTextPreserveAcronyms, 2)
        self.assertEqual(LatentSemanticMapping.kLSMTextApplySpamHeuristics, 4)

    def testTypes(self):
        self.assertIsInstance(LatentSemanticMapping.LSMMapRef, objc.objc_class)
        self.assertIsInstance(LatentSemanticMapping.LSMTextRef, objc.objc_class)
        self.assertIsInstance(LatentSemanticMapping.LSMResultRef, objc.objc_class)

    def testFunctions(self):
        self.assertIsInstance(LatentSemanticMapping.LSMMapGetTypeID(), int)
        self.assertIsInstance(LatentSemanticMapping.LSMTextGetTypeID(), int)
        self.assertIsInstance(LatentSemanticMapping.LSMResultGetTypeID(), int)

        self.assertResultIsCFRetained(LatentSemanticMapping.LSMMapCreate)
        map1 = LatentSemanticMapping.LSMMapCreate(
            None, LatentSemanticMapping.kLSMMapPairs
        )
        self.assertIsInstance(map1, LatentSemanticMapping.LSMMapRef)

        v = LatentSemanticMapping.LSMMapGetProperties(map1)
        self.assertIsInstance(v, LatentSemanticMapping.CFDictionaryRef)

        LatentSemanticMapping.LSMMapSetProperties(map1, {"key": "value"})
        v = LatentSemanticMapping.LSMMapGetProperties(map1)
        self.assertIsInstance(v, (LatentSemanticMapping.CFDictionaryRef, dict))

        v = LatentSemanticMapping.LSMMapStartTraining(map1)
        self.assertIsInstance(v, int)

        cat = LatentSemanticMapping.LSMMapAddCategory(map1)
        self.assertIsInstance(cat, int)

        cat2 = LatentSemanticMapping.LSMMapAddCategory(map1)
        self.assertIsInstance(cat2, int)

        v = LatentSemanticMapping.LSMMapGetCategoryCount(map1)
        self.assertIsInstance(v, int)

        self.assertResultIsCFRetained(LatentSemanticMapping.LSMTextCreate)
        text = LatentSemanticMapping.LSMTextCreate(None, map1)
        self.assertIsInstance(text, LatentSemanticMapping.LSMTextRef)
        text2 = LatentSemanticMapping.LSMTextCreate(None, map1)
        self.assertIsInstance(text2, LatentSemanticMapping.LSMTextRef)
        words = LatentSemanticMapping.LSMTextCreate(None, map1)
        self.assertIsInstance(words, LatentSemanticMapping.LSMTextRef)

        v = LatentSemanticMapping.LSMTextAddWord(words, "the")
        self.assertIsInstance(v, int)
        v = LatentSemanticMapping.LSMTextAddWord(words, "and")
        self.assertIsInstance(v, int)

        v = LatentSemanticMapping.LSMTextAddWords(
            text,
            "the world goes on and on",
            LatentSemanticMapping.CFLocaleCopyCurrent(),
            0,
        )
        self.assertIsInstance(v, int)
        v = LatentSemanticMapping.LSMTextAddWords(
            text2,
            "on a bright and sunny morning",
            LatentSemanticMapping.CFLocaleCopyCurrent(),
            0,
        )
        self.assertIsInstance(v, int)

        v = LatentSemanticMapping.LSMMapSetStopWords(map1, words)
        self.assertIsInstance(v, int)

        v = LatentSemanticMapping.LSMMapAddText(map1, text, cat)
        self.assertIsInstance(v, int)

        # fn = __file__
        # fn = os.path.splitext(fn)[0] + ".py"
        fn = "/usr/share/dict/README"
        with open(fn, "r") as fp:
            for line in fp:
                t = LatentSemanticMapping.LSMTextCreate(None, map1)
                LatentSemanticMapping.LSMTextAddWords(
                    t, line, LatentSemanticMapping.CFLocaleCopyCurrent(), 0
                )
                LatentSemanticMapping.LSMMapAddText(map1, t, cat)

        v = LatentSemanticMapping.LSMMapAddTextWithWeight(map1, text2, cat2, 2.0)
        self.assertIsInstance(v, int)

        v = LatentSemanticMapping.LSMMapCompile(map1)
        self.assertIsInstance(v, int)

        text3 = LatentSemanticMapping.LSMTextCreate(None, map1)
        self.assertIsInstance(text2, LatentSemanticMapping.LSMTextRef)
        v = LatentSemanticMapping.LSMTextAddWords(
            text3,
            "foo the bar and worlds away",
            LatentSemanticMapping.CFLocaleCopyCurrent(),
            0,
        )

        if 1:
            self.assertResultIsCFRetained(LatentSemanticMapping.LSMMapCreateClusters)
            clusters = LatentSemanticMapping.LSMMapCreateClusters(
                None, map1, None, 2, 0
            )
            self.assertIsInstance(
                clusters, (LatentSemanticMapping.CFArrayRef, type(None))
            )

            v = LatentSemanticMapping.LSMMapApplyClusters(map1, clusters)
            self.assertIsInstance(v, int)

        v = LatentSemanticMapping.LSMMapStartTraining(map1)

        mytext = LatentSemanticMapping.LSMTextCreate(None, map1)
        v = LatentSemanticMapping.LSMTextAddWords(
            mytext,
            "the world goes on and on",
            LatentSemanticMapping.CFLocaleCopyCurrent(),
            0,
        )
        self.assertIsInstance(v, int)

        v = LatentSemanticMapping.LSMMapCompile(map1)

        # FIXME: Tests crash, probably due to misuse of the
        # APIs. I haven't found usable API docs for this
        # framework :-(
        # return

        self.assertResultIsCFRetained(LatentSemanticMapping.LSMResultCreate)
        # res = LatentSemanticMapping.LSMResultCreate(None, map1, mytext, 2, 0)
        # self.assertIsInstance(res, LatentSemanticMapping.LSMResultRef)

        LatentSemanticMapping.LSMResultGetCount
        # v = LatentSemanticMapping.LSMResultGetCount(res);
        # self.assertIsInstance(v, int)
        # self.assertTrue(v)

        LatentSemanticMapping.LSMResultGetCategory
        # v = LatentSemanticMapping.LSMResultGetCategory(res, 0)
        # self.assertIsInstance(v, int)

        LatentSemanticMapping.LSMResultGetScore
        # v = LatentSemanticMapping.LSMResultGetScore(res, 0)
        # self.assertIsInstance(v, float)

        self.assertResultIsCFRetained(LatentSemanticMapping.LSMResultCopyWord)
        # v = LatentSemanticMapping.LSMResultCopyWord(res, 0)
        # self.assertIsInstance(v, str)

        self.assertResultIsCFRetained(LatentSemanticMapping.LSMResultCopyToken)
        # v = LatentSemanticMapping.LSMResultCopyToken(res, 0)
        # self.assertIsInstance(v, CFDataRef)

        v = LatentSemanticMapping.LSMMapStartTraining(map1)
        mytext = LatentSemanticMapping.LSMTextCreate(None, map1)

        v = LatentSemanticMapping.LSMTextAddToken(
            mytext, LatentSemanticMapping.NSData.data()
        )
        self.assertIsInstance(v, int)

        self.assertResultIsCFRetained(LatentSemanticMapping.LSMResultCopyWordCluster)
        # v = LatentSemanticMapping.LSMResultCopyWordCluster(res, 0)
        # self.assertIsInstance(v, CFArrayRef)

        self.assertResultIsCFRetained(LatentSemanticMapping.LSMResultCopyTokenCluster)
        # v = LatentSemanticMapping.LSMResultCopyTokenCluster(res, 0)
        # self.assertIsInstance(v, CFArrayRef)

        LatentSemanticMapping.LSMMapWriteToURL
        # fn = '/tmp/pyobjc.test'
        # url = CFURLCreateWithFileSystemPath(None, fn, kCFURLPOSIXPathStyle, False)
        # self.assertIsInstance(url, CFURLRef)
        # v = LatentSemanticMapping.LSMMapWriteToURL(map1, url, 0)
        # self.assertIsInstance(v, int)

        self.assertResultIsCFRetained(LatentSemanticMapping.LSMMapCreateFromURL)
        # map2 = LatentSemanticMapping.LSMMapCreateFromURL(None, url, 0)
        # self.assertIsInstance(map2, LatentSemanticMapping.LSMMapRef)

        # if os.path.exists(fn):
        #    os.unlink(fn)

        # fp = CFWriteStreamCreateWithAllocatedBuffers(None, None)
        # self.assertIsInstance(fp, CFWriteStreamRef)
        # CFWriteStreamOpen(fp)

        LatentSemanticMapping.LSMMapWriteToStream
        # v = LatentSemanticMapping.LSMMapWriteToStream(map1, text, fp, 0)
        # sel.assertIsInstance(v, int)
