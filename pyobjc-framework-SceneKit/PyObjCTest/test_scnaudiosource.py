from PyObjCTools.TestSupport import TestCase, min_os_level

import SceneKit


class TestSCNAudioSource(TestCase):
    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBOOL(SceneKit.SCNAudioSource.isPositional)
        self.assertArgIsBOOL(SceneKit.SCNAudioSource.setPositional_, 0)

        self.assertResultIsBOOL(SceneKit.SCNAudioSource.loops)
        self.assertArgIsBOOL(SceneKit.SCNAudioSource.setLoops_, 0)

        self.assertResultIsBOOL(SceneKit.SCNAudioSource.shouldStream)
        self.assertArgIsBOOL(SceneKit.SCNAudioSource.setShouldStream_, 0)

        self.assertResultIsBlock(SceneKit.SCNAudioPlayer.willStartPlayback, b"v")
        self.assertArgIsBlock(SceneKit.SCNAudioPlayer.setWillStartPlayback_, 0, b"v")

        self.assertResultIsBlock(SceneKit.SCNAudioPlayer.didFinishPlayback, b"v")
        self.assertArgIsBlock(SceneKit.SCNAudioPlayer.setDidFinishPlayback_, 0, b"v")
