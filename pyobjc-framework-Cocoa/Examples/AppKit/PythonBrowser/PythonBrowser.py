"""PythonBrowser.py -- a module and/or demo program implementing a Python
object browser.

It can be used in two ways:
1) as a standalone demo app that shows how to use the NSOutlineView class
2) as a module to add an object browser to your app.

For the latter usage, include PythonBrowser.nib in your app bundle,
make sure that PythonBrowser.py and PythonBrowserModel.py can be found
on sys.path, and call

    PythonBrowser.PythonBrowserWindowController(aBrowsableObject)

from your app. The object to be browsed can't be a number, a string or
None, any other kind of object is fine.

To build the demo program, run this line in Terminal.app:

    $ python setup.py py2app -A

This creates a directory "dist" containing PythonBrowser.app. (The
-A option causes the files to be symlinked to the .app bundle instead
of copied. This means you don't have to rebuild the app if you edit the
sources or nibs.)
"""

from Cocoa import *
import sys


# class defined in PythonBrowser.nib
class PythonBrowserWindowController(NSWindowController):
    outlineView = objc.IBOutlet()

    def __new__(cls, obj):
        # "Pythonic" constructor
        return cls.alloc().initWithObject_(obj)

    def initWithObject_(self, obj):
        from PythonBrowserModel import PythonBrowserModel
        self = self.initWithWindowNibName_("PythonBrowser")
        self.setWindowTitleForObject_(obj)
        self.model = PythonBrowserModel.alloc().initWithObject_(obj)
        self.outlineView.setDataSource_(self.model)
        self.outlineView.setDelegate_(self.model)
        self.outlineView.setTarget_(self)
        self.outlineView.setDoubleAction_("doubleClick:")
        self.window().makeFirstResponder_(self.outlineView)
        self.showWindow_(self)
        # The window controller doesn't need to be retained (referenced)
        # anywhere, so we pretend to have a reference to ourselves to avoid
        # being garbage collected before the window is closed. The extra
        # reference will be released in self.windowWillClose_()
        self.retain()
        return self

    def windowWillClose_(self, notification):
        # see comment in self.initWithObject_()
        self.autorelease()

    def setWindowTitleForObject_(self, obj):
        if hasattr(obj, "__name__"):
            title = "PythonBrowser -- %s: %s" % (type(obj).__name__, obj.__name__)
        else:
            title = "PythonBrowser -- %s" % (type(obj).__name__,)
        self.window().setTitle_(title)

    def setObject_(self, obj):
        self.setWindowTitleForObject_(obj)
        self.model.setObject_(obj)
        self.outlineView.reloadData()

    @objc.IBAction
    def doubleClick_(self, sender):
        # Open a new browser window for each selected expandable item
        for row in self.outlineView.selectedRowEnumerator():
            item = self.outlineView.itemAtRow_(row)
            if item.isExpandable():
                PythonBrowserWindowController(item.object)

    @objc.IBAction
    def pickRandomModule_(self, sender):
        """Test method, hooked up from the "Pick Random Module" menu in
        MainMenu.nib, to test changing the browsed object after the window
        has been created."""
        from random import choice
        mod = None
        while mod is None:
            mod = sys.modules[choice(sys.modules.keys())]
        self.setObject_(mod)


class PythonBrowserAppDelegate(NSObject):

    def applicationDidFinishLaunching_(self, notification):
        self.newBrowser_(self)

    @objc.IBAction
    def newBrowser_(self, sender):
        # The PythonBrowserWindowController instance will retain itself,
        # so we don't (have to) keep track of all instances here.
        PythonBrowserWindowController(sys)


if __name__ == "__main__":
    from PyObjCTools import AppHelper
    AppHelper.runEventLoop()
