import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSURLHandle(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Foundation.NSURLHandleStatus)
        self.assertEqual(Foundation.NSURLHandleNotLoaded, 0)
        self.assertEqual(Foundation.NSURLHandleLoadSucceeded, 1)
        self.assertEqual(Foundation.NSURLHandleLoadInProgress, 2)
        self.assertEqual(Foundation.NSURLHandleLoadFailed, 3)

    def test_constants(self):
        self.assertIsInstance(Foundation.NSHTTPPropertyStatusCodeKey, str)
        self.assertIsInstance(Foundation.NSHTTPPropertyStatusReasonKey, str)
        self.assertIsInstance(Foundation.NSHTTPPropertyServerHTTPVersionKey, str)
        self.assertIsInstance(Foundation.NSHTTPPropertyRedirectionHeadersKey, str)
        self.assertIsInstance(Foundation.NSHTTPPropertyErrorPageDataKey, str)
        self.assertIsInstance(Foundation.NSHTTPPropertyHTTPProxy, str)
        self.assertIsInstance(Foundation.NSFTPPropertyUserLoginKey, str)
        self.assertIsInstance(Foundation.NSFTPPropertyUserPasswordKey, str)
        self.assertIsInstance(Foundation.NSFTPPropertyActiveTransferModeKey, str)
        self.assertIsInstance(Foundation.NSFTPPropertyFileOffsetKey, str)
        self.assertIsInstance(Foundation.NSFTPPropertyFTPProxy, str)

    def test_methods(self):
        self.assertArgIsBOOL(Foundation.NSURLHandle.didLoadBytes_loadComplete_, 1)
        self.assertResultIsBOOL(Foundation.NSURLHandle.canInitWithURL_)
        self.assertArgIsBOOL(Foundation.NSURLHandle.initWithURL_cached_, 1)
        self.assertResultIsBOOL(Foundation.NSURLHandle.writeProperty_forKey_)
        self.assertResultIsBOOL(Foundation.NSURLHandle.writeData_)

    def test_protocols(self):
        self.assertProtocolExists("NSURLHandleClient", Foundation)
