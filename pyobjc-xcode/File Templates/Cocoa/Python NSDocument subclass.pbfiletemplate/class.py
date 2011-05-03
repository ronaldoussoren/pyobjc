#
#  «FILENAME»
#  «PROJECTNAME»
#
#  Created by «FULLUSERNAME» on «DATE».
#  Copyright (c) «YEAR» «ORGANIZATIONNAME». All rights reserved.
#

from objc import YES, NO, IBAction, IBOutlet
from Foundation import *
from AppKit import *

class «FILEBASENAMEASIDENTIFIER»(NSDocument):
    def windowNibName(self):
        # Implement this to return a nib to load OR 
        # implement -makeWindowControllers to manually create your controllers.
        return u"«FILEBASENAMEASIDENTIFIER»"

    def windowControllerDidLoadNib_(self, aController):
        super(«FILEBASENAMEASIDENTIFIER», self).windowControllerDidLoadNib_(aController)
        # Any UI customization that must be done after the NIB is loaded goes here.

    def dataOfType_error_(self, typeName, outError):
        # Insert code here to write your document to data of the specified type. If the given outError != NULL, 
        # ensure that you set *outError when returning nil.  You can also choose to override -fileWrapperOfType:error:, -writeToURL:ofType:error:,
        # or -writeToURL:ofType:forSaveOperation:originalContentsURL:error: instead.
        return None

    def readFromData_ofType_error_(self, data, typeName, outError):
        # Insert code here to read your document from the given data of the specified type.  If the given outError != NULL,
        # ensure that you set *outError when returning NO.  You can also choose to override -readFromFileWrapper:ofType:error:
        # or -readFromURL:ofType:error: instead. 
        return NO
