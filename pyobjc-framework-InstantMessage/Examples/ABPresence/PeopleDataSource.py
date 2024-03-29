import AddressBook
import Cocoa
import InstantMessage
import objc
from ServiceWatcher import kAddressBookPersonStatusChanged, kStatusImagesChanged


class PeopleDataSource(Cocoa.NSObject):
    _abPeople = objc.ivar()
    _imPersonStatus = objc.ivar()  # Parallel array to abPeople
    _table = objc.IBOutlet()

    def awakeFromNib(self):
        self._imPersonStatus = Cocoa.NSMutableArray.alloc().init()

        # We don't need to query the status of everyone, we will wait for
        # notifications of their status to arrive, so we just set them all up
        # as offline.
        self.setupABPeople()

        Cocoa.NSNotificationCenter.defaultCenter().addObserver_selector_name_object_(
            self,
            b"abDatabaseChangedExternallyNotification:",
            AddressBook.kABDatabaseChangedExternallyNotification,
            None,
        )

        Cocoa.NSNotificationCenter.defaultCenter().addObserver_selector_name_object_(
            self,
            b"addressBookPersonStatusChanged:",
            kAddressBookPersonStatusChanged,
            None,
        )

        Cocoa.NSNotificationCenter.defaultCenter().addObserver_selector_name_object_(
            self, b"statusImagesChanged:", kStatusImagesChanged, None
        )

    # This dumps all the status information and rebuilds the array against
    # the current _abPeople
    # Fairly expensive, so this is only done when necessary
    def rebuildStatusInformation(self):
        # Now scan through all the people, adding their status to the status
        # cache array
        for i, person in enumerate(self._abPeople):
            # Let's assume they're offline to start
            bestStatus = InstantMessage.IMPersonStatusOffline

            for service in InstantMessage.IMService.allServices():
                screenNames = service.screenNamesForPerson_(person)

                for screenName in screenNames:
                    dictionary = service.infoForScreenName_(screenName)
                    status = dictionary.get(InstantMessage.IMPersonStatusKey)
                    if status is not None:
                        thisStatus = status
                        if (
                            InstantMessage.IMComparePersonStatus(bestStatus, thisStatus)
                            != Cocoa.NSOrderedAscending
                        ):
                            bestStatus = thisStatus

            self._imPersonStatus[i] = bestStatus

        self._table.reloadData()

    # Rebuild status information for a given person, much faster than a full
    # rebuild
    def rebuildStatusInformationForPerson_(self, forPerson):
        for i, person in enumerate(self._abPeople):
            if person is forPerson:
                bestStatus = InstantMessage.IMPersonStatusOffline

                # Scan through all the services, taking the 'best' status we
                # can find
                for service in InstantMessage.IMService.allServices():
                    screenNames = service.screenNamesForPerson_(person)

                    # Ask for the status on each of their screen names
                    for screenName in screenNames:
                        dictionary = service.infoForScreenName_(screenName)
                        status = dictionary.get(InstantMessage.IMPersonStatusKey)
                        if status is not None:
                            thisStatus = status
                            if (
                                InstantMessage.IMComparePersonStatus(
                                    bestStatus, thisStatus
                                )
                                != Cocoa.NSOrderedAscending
                            ):
                                bestStatus = thisStatus

                self._imPersonStatus[i] = bestStatus
                self._table.reloadData()
                break

    # Sets up all our internal data
    def setupABPeople(self):
        # Keep around a copy of all the people in the AB now
        self._abPeople = (
            AddressBook.ABAddressBook.sharedAddressBook().people().mutableCopy()
        )

        # Sort them by display name
        self._abPeople.sortUsingSelector_("compareDisplayNames:")

        # Assume everyone is offline.
        self._imPersonStatus.removeAllObjects()
        offlineNumber = InstantMessage.IMPersonStatusOffline
        for _ in range(len(self._abPeople)):
            self._imPersonStatus.append(offlineNumber)

    # This will do a full flush of people in our AB Cache, along with
    # rebuilding their status */
    def reloadABPeople(self):
        self.setupABPeople()

        # Now recache all the status info, this will spawn a reload of the table
        self.rebuildStatusInformation()

    def numberOfRowsInTableView_(self, tableView):
        if self._abPeople is None:
            return 0
        return len(self._abPeople)

    def tableView_objectValueForTableColumn_row_(self, tableView, tableColumn, row):
        identifier = tableColumn.identifier()
        if identifier == "image":
            status = self._imPersonStatus[row]
            return Cocoa.NSImage.imageNamed_(
                InstantMessage.IMService.imageNameForStatus_(status)
            )

        elif identifier == "name":
            return self._abPeople[row].displayName()

        return None

    # Posted from ServiceWatcher
    # The object of this notification is an ABPerson who's status has
    # Changed
    def addressBookPersonStatusChanged_(self, notification):
        self.rebuildStatusInformationForPerson_(notification.object())

    # Posted from ServiceWatcher
    # We should reload the tableview, because the user has changed the
    # status images that iChat is using.
    def statusImagesChanged_(self, notification):
        self._table.reloadData()

    # If the AB database changes, force a reload of everyone
    # We could look in the notification to catch differential updates, but
    # for now this is fine.
    def abDatabaseChangedExternallyNotification_(self, notification):
        self.reloadABPeople()
