from Cocoa import *
from Quartz import *
from LaunchServices import *

import os

#	openFiles
#
#	A simple C function that opens NSOpenPanel and returns an array of file paths.
#	It uses uniform type identifiers (UTIs) for proper filtering of image files.
# -------------------------------------------------------------------------
def openFiles():
    # Get a list of extensions to filter in our NSOpenPanel.
    panel = NSOpenPanel.openPanel()

    # The user can choose a folder; images in the folder are added recursively.
    panel.setCanChooseDirectories_(True)
    panel.setCanChooseFiles_(True)
    panel.setAllowsMultipleSelection_(True)
	
    if panel.runModalForTypes_(NSImage.imageUnfilteredTypes()) == NSOKButton:
        return panel.filenames()
    
    return []

#==============================================================================
# This is the data source object.
class myImageObject (NSObject):
    _path = objc.ivar()

    # -------------------------------------------------------------------------
    #	setPath:path
    #
    #	The data source object is just a file path representation
    # -------------------------------------------------------------------------
    def setPath_(self, inPath):
        self._path = inPath

    # The required methods of the IKImageBrowserItem protocol.

    # -------------------------------------------------------------------------
    #	imageRepresentationType:
    #
    #	Set up the image browser to use a path representation.
    # -------------------------------------------------------------------------
    def imageRepresentationType(self):
        return IKImageBrowserPathRepresentationType

    # -------------------------------------------------------------------------
    #	imageRepresentation:
    #
    #	Give the path representation to the image browser.
    # -------------------------------------------------------------------------
    def imageRepresentation(self):
        return self._path

    # -------------------------------------------------------------------------
    #	imageUID:
    #
    #	Use the absolute file path as the identifier.
    # -------------------------------------------------------------------------
    def imageUID(self):
        return self._path

class ImageBrowserController (NSWindowController):
    imageBrowser = objc.IBOutlet()

    images = objc.ivar()
    importedImages = objc.ivar()


    # -------------------------------------------------------------------------
    #	awakeFromNib:
    # -------------------------------------------------------------------------
    def awakeFromNib(self):
        # Create two arrays : The first is for the data source representation.
        # The second one contains temporary imported images  for thread safeness.
        self.images = NSMutableArray.alloc().init()
        self.importedImages = NSMutableArray.alloc().init()
        
        # Allow reordering, animations and set the dragging destination 
        # delegate.
        self.imageBrowser.setAllowsReordering_(True)
        self.imageBrowser.setAnimates_(True)
        self.imageBrowser.setDraggingDestinationDelegate_(self)

    # -------------------------------------------------------------------------
    #	updateDatasource:
    #
    #	This is the entry point for reloading image browser data and 
    #   triggering setNeedsDisplay.
    # -------------------------------------------------------------------------
    def updateDatasource(self):
        # Update the datasource, add recently imported items.
        self.images.extend(self.importedImages)
            
        # Empty the temporary array.
        del self.importedImages[:]
        
        # Reload the image browser, which triggers setNeedsDisplay.
        self.imageBrowser.reloadData()


    # -------------------------------------------------------------------------
    #	isImageFile:filePath
    #
    #	This utility method indicates if the file located at 'filePath' is
    #	an image file based on the UTI. It relies on the ImageIO framework for 
    #   the supported type identifiers.
    #
    # -------------------------------------------------------------------------
    def isImageFile_(self, filePath):
        isImageFile = False
        uti = None
        
        url = CFURLCreateWithFileSystemPath(None, filePath, kCFURLPOSIXPathStyle, False)
        
        res, info =  LSCopyItemInfoForURL(url, kLSRequestExtension | kLSRequestTypeCreator, None)
        if res == 0:
            # Obtain the UTI using the file information.
            
            # If there is a file extension, get the UTI.
            if info[3] != None:
                    uti = UTTypeCreatePreferredIdentifierForTag(kUTTagClassFilenameExtension, info[3], kUTTypeData)

            # No UTI yet
            if uti is None:
                # If there is an OSType, get the UTI.
                typeString = UTCreateStringForOSType(info.filetype)
                if typeString != None:
                    uti = UTTypeCreatePreferredIdentifierForTag(kUTTagClassOSType, typeString, kUTTypeData)
                
            # Verify that this is a file that the ImageIO framework supports.
            if uti is not None:
                supportedTypes = CGImageSourceCopyTypeIdentifiers()

                for item in supportedTypes:
                    if UTTypeConformsTo(uti, item):
                        isImageFile = True
                        break

        return isImageFile

    # -------------------------------------------------------------------------
    #	addAnImageWithPath:path
    # -------------------------------------------------------------------------
    def addAnImageWithPath_(self, path):
        addObject = False
            
        fileAttribs = NSFileManager.defaultManager().fileAttributesAtPath_traverseLink_(path, True)
        if fileAttribs is not None:
            # Check for packages.
            if NSFileTypeDirectory == fileAttribs[NSFileType]:
                if not NSWorkspace.sharedWorkspace().isFilePackageAtPath_(path):
                    addObject = True	# If it is a file, it's OK to add.

            else:
                    addObject = True	# It is a file, so it's OK to add.
        
        if addObject and self.isImageFile_(path):
            # Add a path to the temporary images array.
            p = myImageObject.alloc().init()
            p.setPath_(path)
            self.importedImages.append(p)

    # -------------------------------------------------------------------------
    #	addImagesWithPath:path:recursive
    # -------------------------------------------------------------------------
    def addImagesWithPath_recursive_(self, path, recursive):
        dir = os.path.isdir(path)
        if dir:
            content = os.listdir(path)
            # Parse the directory content.
            for fn in content:
                if recursive:
                    self.addImagesWithPath_recursive_(
                            os.path.join(path, fn), True)
                else:
                    self.addAnImageWithPath_(os.path.join(path, fn))

        else:
            self.addAnImageWithPath_(path)

    # -------------------------------------------------------------------------
    #	addImagesWithPaths:paths
    #
    #	Performed in an independent thread, parse all paths in "paths" and
    #	add these paths in the temporary images array.
    # -------------------------------------------------------------------------
    def addImagesWithPaths_(self, paths):
        pool = NSAutoreleasePool.alloc().init()

        for path in paths:
            isdir = os.path.isdir(path)
            self.addImagesWithPath_recursive_(path, isdir)

        # Update the data source in the main thread.
        self.performSelectorOnMainThread_withObject_waitUntilDone_(
                'updateDatasource', None, True)

        del pool


    #pragma mark -
    #pragma mark actions

    # -------------------------------------------------------------------------
    #	addImageButtonClicked:sender
    #
    #	The user clicked the Add button.d
    # -------------------------------------------------------------------------
    @objc.IBAction
    def addImageButtonClicked_(self, sender):
        path = openFiles()
        if path:
            # launch import in an independent thread
            NSThread.detachNewThreadSelector_toTarget_withObject_(
                    'addImagesWithPaths:', self, path)

    # -------------------------------------------------------------------------
    #	addImageButtonClicked:sender
    #
    #	Action called when the zoom slider changes.
    # ------------------------------------------------------------------------- 
    @objc.IBAction
    def zoomSliderDidChange_(self, sender):
        # update the zoom value to scale images
        self.imageBrowser.setZoomValue_(sender.floatValue())
            
        # redisplay
        self.imageBrowser.setNeedsDisplay_(True)

    # Implement the image browser  data source protocol .
    # The data source representation is a simple mutable array.

    # -------------------------------------------------------------------------
    #	numberOfItemsInImageBrowser:view
    # ------------------------------------------------------------------------- 
    def numberOfItemsInImageBrowser_(self, view):
        # The item count to display is the datadsource item count.
        return len(self.images)

    # -------------------------------------------------------------------------
    #	imageBrowser:view:index:
    # ------------------------------------------------------------------------- 
    def imageBrowser_itemAtIndex_(self, view, index):
        return self.images[index]


    # Implement some optional methods of the image browser  datasource protocol to allow for removing and reodering items.

    # -------------------------------------------------------------------------
    #	removeItemsAtIndexes:
    #
    #	The user wants to delete images, so remove these entries from the data source.	
    # ------------------------------------------------------------------------- 
    def imageBrowser_removeItemsAtIndexes_(self, view, indexes):
        self.images.removeObjectsAtIndexes_(indexes)

    # -------------------------------------------------------------------------
    #	moveItemsAtIndexes:
    #
    #	The user wants to reorder images, update the datadsource and the browser
    #	will reflect our changes.
    # ------------------------------------------------------------------------- 
    def imageBrowser_moveItemsAtIndexes_toIndex_(self, browser, indexes, destinationIndex):
        temporaryArray = []

        # First remove items from the data source and keep them in a 
        # temporary array.
        for index in reversed(sorted(list(indexes))):
            if index < destinationIndex:
                destinationIndex -= 1

            obj = self.images[index]
            temporaryArray.append(obj)
            del images[index]

        # Then insert the removed items at the appropriate location.
        for item in temporaryArray:
            self.images.insertObject_atIndex_(item, destinationIndex)

        return True


    # -------------------------------------------------------------------------
    #	draggingEntered:sender
    # ------------------------------------------------------------------------- 
    def draggingEntered_(self, sender):
        return NSDragOperationCopy

    # -------------------------------------------------------------------------
    #	draggingUpdated:sender
    # ------------------------------------------------------------------------- 
    def draggingUpdated_(self, sender): 
        return NSDragOperationCopy

    # -------------------------------------------------------------------------
    #	performDragOperation:sender
    # ------------------------------------------------------------------------- 
    def performDragOperation_(self, sender):
        pasteboard = sender.draggingPasteboard()

        # Look for paths on the pasteboard.
        data = None
        if NSFilenamesPboardType in pasteboard.types():
            data = pasteboard.dataForType_(NSFilenamesPboardType)

        if data is not None:
            # Retrieve  paths.
            filenames, format, errorDescription = NSPropertyListSerialization.propertyListFromData_mutabilityOption_format_errorDescription_(
                    data , kCFPropertyListImmutable, None, None)

            # Add paths to the data source.
            for fn in filenames:
                self.addAnImageWithPath_(fn)

            # Make the image browser reload the data source.
            self.updateDatasource()

        # Accept the drag operation.
        return True
