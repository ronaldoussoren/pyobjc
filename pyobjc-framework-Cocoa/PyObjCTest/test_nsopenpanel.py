from AppKit import *
from PyObjCTools.TestSupport import *

class TestOpenPanel (TestCase):
    def dont_testOpenPanelSignature(self):
        """
        This test failed sometime after the 1.0b1 release (on Panther).
        """

        o = NSOpenPanel.openPanel()
        sig = o.beginSheetForDirectory_file_types_modalForWindow_modalDelegate_didEndSelector_contextInfo_.signature
        dclass= o.beginSheetForDirectory_file_types_modalForWindow_modalDelegate_didEndSelector_contextInfo_.definingClass
        sig = ''.join(objc.splitSignature(sig))
        self.assertEquals(
            sig,
            'v@:@@@@@:i')

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSOpenPanel.resolvesAliases)
        self.failUnlessArgIsBOOL(NSOpenPanel.setResolvesAliases_, 0)
        self.failUnlessResultIsBOOL(NSOpenPanel.canChooseDirectories)
        self.failUnlessArgIsBOOL(NSOpenPanel.setCanChooseDirectories_, 0)
        self.failUnlessResultIsBOOL(NSOpenPanel.allowsMultipleSelection)
        self.failUnlessArgIsBOOL(NSOpenPanel.setAllowsMultipleSelection_, 0)
        self.failUnlessResultIsBOOL(NSOpenPanel.canChooseFiles)
        self.failUnlessArgIsBOOL(NSOpenPanel.setCanChooseFiles_, 0)

        panel = NSOpenPanel.openPanel()
        self.failUnlessArgIsSEL(panel.beginSheetForDirectory_file_types_modalForWindow_modalDelegate_didEndSelector_contextInfo_, 5, 'v@:@i^v')
        self.failUnlessArgHasType(panel.beginSheetForDirectory_file_types_modalForWindow_modalDelegate_didEndSelector_contextInfo_, 6, '^v')

        self.failUnlessArgIsSEL(panel.beginForDirectory_file_types_modelessDelegate_didEndSelector_contextInfo_, 4, 'v@:@i^v')
        self.failUnlessArgHasType(panel.beginForDirectory_file_types_modelessDelegate_didEndSelector_contextInfo_, 5, '^v')



if __name__ == "__main__":
    main()
