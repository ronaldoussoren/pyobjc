from PyObjCTools.TestSupport import TestCase, min_os_level
import QTKit


class TestQTExportOptions(TestCase):
    @min_os_level("10.7")
    def testConstants(self):
        self.assertIsInstance(QTKit.QTExportOptionsAppleM4VCellular, str)
        self.assertIsInstance(QTKit.QTExportOptionsAppleM4V480pSD, str)
        self.assertIsInstance(QTKit.QTExportOptionsAppleM4ViPod, str)
        self.assertIsInstance(QTKit.QTExportOptionsAppleM4VAppleTV, str)
        self.assertIsInstance(QTKit.QTExportOptionsAppleM4VWiFi, str)
        self.assertIsInstance(QTKit.QTExportOptionsAppleM4V720pHD, str)
        self.assertIsInstance(QTKit.QTExportOptionsQuickTimeMovie480p, str)
        self.assertIsInstance(QTKit.QTExportOptionsQuickTimeMovie720p, str)
        self.assertIsInstance(QTKit.QTExportOptionsQuickTimeMovie1080p, str)
        self.assertIsInstance(QTKit.QTExportOptionsAppleM4A, str)
