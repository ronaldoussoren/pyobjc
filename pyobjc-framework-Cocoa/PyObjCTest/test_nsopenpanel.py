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
        self.assertEqual(
            sig,
            'v@:@@@@@:i')

    def testMethods(self):
        self.assertResultIsBOOL(NSOpenPanel.resolvesAliases)
        self.assertArgIsBOOL(NSOpenPanel.setResolvesAliases_, 0)
        self.assertResultIsBOOL(NSOpenPanel.canChooseDirectories)
        self.assertArgIsBOOL(NSOpenPanel.setCanChooseDirectories_, 0)
        self.assertResultIsBOOL(NSOpenPanel.allowsMultipleSelection)
        self.assertArgIsBOOL(NSOpenPanel.setAllowsMultipleSelection_, 0)
        self.assertResultIsBOOL(NSOpenPanel.canChooseFiles)
        self.assertArgIsBOOL(NSOpenPanel.setCanChooseFiles_, 0)

        panel = NSOpenPanel.openPanel()
        self.assertArgIsSEL(panel.beginSheetForDirectory_file_types_modalForWindow_modalDelegate_didEndSelector_contextInfo_, 5, b'v@:@' + objc._C_NSInteger + b'^v')
        self.assertArgHasType(panel.beginSheetForDirectory_file_types_modalForWindow_modalDelegate_didEndSelector_contextInfo_, 6, b'^v')

        self.assertArgIsSEL(panel.beginForDirectory_file_types_modelessDelegate_didEndSelector_contextInfo_, 4, b'v@:@'+objc._C_NSInteger+b'^v')
        self.assertArgHasType(panel.beginForDirectory_file_types_modelessDelegate_didEndSelector_contextInfo_, 5, b'^v')



if __name__ == "__main__":
    main()
