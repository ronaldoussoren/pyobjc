"""
Some simple tests to check that the framework is properly wrapped.
"""
import objc
from PyObjCTools.TestSupport import *
import Collaboration


class TestCollaboration(TestCase):
    def testClasses(self):
        self.assertHasAttr(Collaboration, "CBIdentity")
        self.assertIsInstance(Collaboration.CBIdentity, objc.objc_class)
        self.assertHasAttr(Collaboration, "CBGroupIdentity")
        self.assertIsInstance(Collaboration.CBGroupIdentity, objc.objc_class)
        self.assertHasAttr(Collaboration, "CBIdentityPicker")
        self.assertIsInstance(Collaboration.CBIdentityPicker, objc.objc_class)


if __name__ == "__main__":
    main()
