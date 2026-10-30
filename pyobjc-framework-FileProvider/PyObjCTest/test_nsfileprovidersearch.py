from PyObjCTools.TestSupport import TestCase, min_sdk_level

import FileProvider  # noqa: F401


class TestNSFileProviderSearch(TestCase):
    @min_sdk_level("26.0")
    def test_protocols(self):
        self.assertProtocolExists("NSFileProviderSearchResult", FileProvider)
        self.assertProtocolExists(
            "NSFileProviderSearchEnumerationObserver", FileProvider
        )
        self.assertProtocolExists("NSFileProviderSearchEnumerator", FileProvider)
        self.assertProtocolExists("NSFileProviderSearching", FileProvider)
