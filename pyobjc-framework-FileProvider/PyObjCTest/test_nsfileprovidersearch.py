from PyObjCTools.TestSupport import TestCase, min_sdk_level

import FileProvider  # noqa: F401


class TestNSFileProviderSearch(TestCase):
    @min_sdk_level("26.0")
    def test_protocols(self):
        self.assertProtocolExists("NSFileProviderSearchResult")
        self.assertProtocolExists("NSFileProviderSearchEnumerationObserver")
        self.assertProtocolExists("NSFileProviderSearchEnumerator")
        self.assertProtocolExists("NSFileProviderSearching")
