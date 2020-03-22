import Cocoa
import CoreData
import objc


class DragAppAppDelegate(Cocoa.NSObject):
    clubWindow = objc.IBOutlet()
    peopleWindow = objc.IBOutlet()

    _managedObjectModel = objc.ivar()
    _managedObjectContext = objc.ivar()
    _things = objc.ivar()

    def managedObjectModel(self):
        if self._managedObjectModel is None:
            allBundles = Cocoa.NSMutableSet.alloc().init()
            allBundles.addObject_(Cocoa.NSBundle.mainBundle())
            allBundles.addObjectsFromArray_(Cocoa.NSBundle.allFrameworks())

            self._managedObjectModel = CoreData.NSManagedObjectModel.mergedModelFromBundles_(
                allBundles.allObjects()
            )

        return self._managedObjectModel

    # Change this path/code to point to your App's data store.
    def applicationSupportFolder(self):
        paths = Cocoa.NSSearchPathForDirectoriesInDomains(
            Cocoa.NSApplicationSupportDirectory, Cocoa.NSUserDomainMask, True
        )

        if len(paths) == 0:
            Cocoa.NSRunAlertPanel(
                "Alert", "Can't find application support folder", "Quit", None, None
            )
            Cocoa.NSApplication.sharedApplication().terminate_(self)
        else:
            applicationSupportFolder = paths[0].stringByAppendingPathComponent_(
                "DragApp"
            )

        return applicationSupportFolder

    def managedObjectContext(self):
        if self._managedObjectContext is None:
            fileManager = Cocoa.NSFileManager.defaultManager()
            applicationSupportFolder = self.applicationSupportFolder()

            if not fileManager.fileExistsAtPath_isDirectory_(
                applicationSupportFolder, None
            )[0]:
                fileManager.createDirectoryAtPath_attributes_(
                    applicationSupportFolder, None
                )

            url = Cocoa.NSURL.fileURLWithPath_(
                applicationSupportFolder.stringByAppendingPathComponent_("DragApp.xml")
            )

            coordinator = CoreData.NSPersistentStoreCoordinator.alloc().initWithManagedObjectModel_(  # noqa: B950
                self.managedObjectModel()
            )
            (
                result,
                error,
            ) = coordinator.addPersistentStoreWithType_configuration_URL_options_error_(
                CoreData.NSXMLStoreType, None, url, None, None
            )
            if result:
                self._managedObjectContext = (
                    CoreData.NSManagedObjectContext.alloc().init()
                )
                self._managedObjectContext.setPersistentStoreCoordinator_(coordinator)
            else:
                Cocoa.NSApplication.sharedApplication().presentError_(error)

        return self._managedObjectContext

    def windowWillReturnUndoManager_(self, window):
        return self.managedObjectContext().undoManager()

    @objc.IBAction
    def saveAction_(self, sender):
        res, error = self.managedObjectContext().save_(None)
        if not res:
            Cocoa.NSApplication.sharedApplication().presentError_(error)

    def applicationShouldTerminate_(self, sender):
        context = self.managedObjectContext()

        reply = Cocoa.NSTerminateNow

        if context is not None:
            if context.commitEditing():
                res, error = context.save_(None)
                if not res:
                    # This default error handling implementation should be
                    # changed to make sure the error presented includes
                    # application specific error recovery. For now, simply
                    # display 2 panels.
                    errorResult = Cocoa.NSApplication.sharedApplication().presentError_(
                        error
                    )

                    if errorResult:  # Then the error was handled
                        reply = Cocoa.NSTerminateCancel
                    else:
                        # Error handling wasn't implemented. Fall back to
                        # displaying a "quit anyway" panel.
                        alertReturn = Cocoa.NSRunAlertPanel(
                            None,
                            "Could not save changes while quitting. Quit anyway?",
                            "Quit anyway",
                            "Cancel",
                            None,
                        )
                        if alertReturn == Cocoa.NSAlertAlternateReturn:
                            reply = Cocoa.NSTerminateCancel

            else:
                reply = Cocoa.NSTerminateCancel

        return reply
