from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSCollectionView (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSCollectionViewItem.isSelected)
        self.failUnlessArgIsBOOL(NSCollectionViewItem.setSelected_, 0)

        self.failUnlessResultIsBOOL(NSCollectionView.isFirstResponder)

        self.failUnlessResultIsBOOL(NSCollectionView.isSelectable)
        self.failUnlessArgIsBOOL(NSCollectionView.setSelectable_, 0)
        self.failUnlessResultIsBOOL(NSCollectionView.allowsMultipleSelection)
        self.failUnlessArgIsBOOL(NSCollectionView.setAllowsMultipleSelection_, 0)

if __name__ == "__main__":
    main()
