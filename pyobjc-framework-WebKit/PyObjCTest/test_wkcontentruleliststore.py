from PyObjCTools.TestSupport import *
from WebKit import *


class TestWKContentRuleListStore (TestCase):
    @onlyOn64Bit
    @min_os_level('10.13')
    def testMethods(self):
        self.assertArgIsBlock(WKContentRuleListStore.compileContentRuleListForIdentifier_encodedContentRuleList_completionHandler_, 2, b'v@@')
        self.assertArgIsBlock(WKContentRuleListStore.lookUpContentRuleListForIdentifier_completionHandler_, 1, b'v@@')
        self.assertArgIsBlock(WKContentRuleListStore.removeContentRuleListForIdentifier_completionHandler_, 1, b'v@')
        self.assertArgIsBlock(WKContentRuleListStore.getAvailableContentRuleListIdentifiers_, 0, b'v@')


if __name__ == "__main__":
    main()
