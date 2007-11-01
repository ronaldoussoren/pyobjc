from Cocoa import *
import objc

import PDFHandling
import BitmapContext
import Utilities

# Initial defaults
_dpi = 144
_useQT = False

def getURLToExport(suffix):
    savePanel = NSSavePanel.savePanel()
    
    initialFileName = "BasicDrawing.%s"%(suffix,)

    if savePanel.runModalForDirectory_file_(None, initialFileName) == NSFileHandlingPanelOKButton:
        return savePanel.URL()

    return None


class MyAppController (NSObject):
    theView = objc.IBOutlet()
    currentDPIMenuItem  = objc.IBOutlet()
    currentExportStyleMenuItem  = objc.IBOutlet()

    @objc.IBAction
    def print_(self, sender):
        self.theView.print_(sender)

    def updateDPIMenu_(self, sender):
        if self.currentDPIMenuItem is not sender:
            # Uncheck the previous item.
            if self.currentDPIMenuItem is not None:
                self.currentDPIMenuItem.setState_(NSOffState)
            # Update to the current item.
            self.currentDPIMenuItem = sender
            # Check new menu item.
            self.currentDPIMenuItem.setState_(NSOnState)

    def updateExportStyleMenu_(self, sender):
        if self.currentExportStyleMenuItem is not sender:
            # Uncheck the previous item.
            if self.currentExportStyleMenuItem is not None:
                self.currentExportStyleMenuItem.setState_(NSOffState)
            # Update to the current item.
            self.currentExportStyleMenuItem = sender
            # Check new menu item.
            self.currentExportStyleMenuItem.setState_(NSOnState)

    @objc.IBAction
    def setExportResolution_(self, sender):
        global _dpi
        _dpi = sender.tag()
        self.updateDPIMenu_(sender)

    @objc.IBAction
    def setUseQT_(self, sender):
        global _useQT
        _useQT = True
        self.updateExportStyleMenu_(sender)

    @objc.IBAction
    def setUseCGImageSource_(self, sender):
        global _useQT
        _useQT = False
        self.updateExportStyleMenu_(sender)

    def setupExportInfo_(self, exportInfoP):
        # Use the printable version of the current command. This produces
        # the best results for exporting.
        exportInfoP.command = self.theView.currentPrintableCommand()
        exportInfoP.fileType = '    '	# unused
        exportInfoP.useQTForExport = _useQT
        exportInfoP.dpi = _dpi

    @objc.IBAction
    def exportAsPDF_(self, sender):
        url = getURLToExport("pdf")
        if url is not None:
		exportInfo = Utilities.ExportInfo()
		self.setupExportInfo_(exportInfo)
		PDFHandling.MakePDFDocument(url, exportInfo)

    @objc.IBAction
    def exportAsPNG_(self, sender):
        url = getURLToExport("png")
        if url is not None:
		exportInfo = Utilities.ExportInfo()
		self.setupExportInfo_(exportInfo)
		BitmapContext.MakePNGDocument(url, exportInfo)

    @objc.IBAction
    def exportAsTIFF_(self, sender):
        url = getURLToExport("tif")
        if url is not None:
		exportInfo = Utilities.ExportInfo()
		self.setupExportInfo_(exportInfo)
		BitmapContext.MakeTIFFDocument(url, exportInfo)


    @objc.IBAction
    def exportAsJPEG_(self, sender):
        url = getURLToExport("jpg")
        if url is not None:
		exportInfo = Utilities.ExportInfo()
		self.setupExportInfo_(exportInfo)
		BitmapContext.MakeJPEGDocument(url, exportInfo)

    def validateMenuItem_(self, menuItem):
        if menuItem.tag == _dpi:
            currentDPIMenuItem = menuItem
            menuItem.setState_(True)
        elif menuItem.action() == 'setUseQT:':
            if _useQT:
                self.currentDPIMenuItem = menuItem
                menuItem.setState_(True)
            else:
                menuItem.setState_(False)
        
        elif menuItem.action() == 'setUseCGImageSource:':
            if _useQT:
                currentDPIMenuItem = menuItem
                menuItem.setState_(True)
            else:
                menuItem.setState_(False)
        
	return True
