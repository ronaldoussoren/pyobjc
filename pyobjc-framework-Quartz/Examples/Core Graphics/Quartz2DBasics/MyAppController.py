from Cocoa import *
from CoreFoundation import *
import AppDrawing

from PyObjCTools import NibClassBuilder

def getURLToExport(suffix):
    savePanel = NSSavePanel.savePanel()

    initialFileName = u"Quartz2DBasics.%s"%(suffix,)

    if savePanel.runModalForDirectory_file_(None, initialFileName) == NSFileHandlingPanelOKButton:
        return savePanel.URL()

    return None

class MyAppController (NibClassBuilder.AutoBaseClass):
    def print_(self, sender):
        self.theView.print_(sender)

    def exportAsPNG_(self, sender):
        url = getURLToExport("png")
        if url:
            AppDrawing.myExportCGDrawingAsPNG(url, self.theView.currentPrintableCommand())

    def exportAsPDF_(self, sender):
        url = getURLToExport("pdf")
        if url:
            AppDrawing.myCreatePDFDocument(url, self.theView.currentPrintableCommand())
