import objc
import Cocoa
import AppDrawing

def getURLToExport(suffix):
    savePanel = Cocoa.NSSavePanel.savePanel()

    initialFileName = u"Quartz2DBasics.%s"%(suffix,)

    if savePanel.runModalForDirectory_file_(None, initialFileName) == Cocoa.NSFileHandlingPanelOKButton:
        return savePanel.URL()

    return None

class MyAppController (Cocoa.NSObject):
    theView = objc.IBOutlet()

    @objc.IBAction
    def print_(self, sender):
        self.theView.print_(sender)

    @objc.IBAction
    def exportAsPNG_(self, sender):
        url = getURLToExport("png")
        if url:
            AppDrawing.myExportCGDrawingAsPNG(url, self.theView.currentPrintableCommand())

    @objc.IBAction
    def exportAsPDF_(self, sender):
        url = getURLToExport("pdf")
        if url:
            AppDrawing.myCreatePDFDocument(url, self.theView.currentPrintableCommand())
