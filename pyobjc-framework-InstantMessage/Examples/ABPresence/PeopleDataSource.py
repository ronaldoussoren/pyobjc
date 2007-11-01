from Cocoa import *
from AddressBook import *
from InstantMessage import *

from ServiceWatcher import *

class PeopleDataSource (NSObject):
    _abPeople = objc.ivar()
    _imPersonStatus = objc.ivar() # Parallel array to abPeople
    _table = objc.IBOutlet()

    def awakeFromNib(self):
	self._imPersonStatus = NSMutableArray.alloc().init()

	# We don't need to query the staus of everyone, we will wait for 
        # notifications of their status to arrive, so we just set them all up 
        # as offline.
	self.setupABPeople()

	NSNotificationCenter.defaultCenter().addObserver_selector_name_object_(
                self, 'abDatabaseChangedExternallyNotification:',
                kABDatabaseChangedExternallyNotification, None)

	NSNotificationCenter.defaultCenter().addObserver_selector_name_object_(
                self, 'addressBookPersonStatusChanged:',
                kAddressBookPersonStatusChanged, None)

	NSNotificationCenter.defaultCenter().addObserver_selector_name_object_(
                self, 'statusImagesChanged:', 
                kStatusImagesChanged, None)

    # This dumps all the status information and rebuilds the array against 
    # the current _abPeople
    # Fairly expensive, so this is only done when necessary
    def rebuildStatusInformation(self):
	# Now scan through all the people, adding their status to the status 
        # cache array
        for i, person in enumerate(self._abPeople):
                # Let's assume they're offline to start
		bestStatus = IMPersonStatusOffline 

                for service in IMService.allServices():
			screenNames = service.screenNamesForPerson_(person)
			
                        for screenName in screenNames:
				dictionary = service.infoForScreenName_(
                                        screenName)
				status = dictionary.get(IMPersonStatusKey)
                                if status is not None:
					thisStatus = status
                                        if IMComparePersonStatus(bestStatus, thisStatus) != NSOrderedAscending:
						bestStatus = thisStatus;
		
		self._imPersonStatus[i] = bestStatus

	self._table.reloadData()

    # Rebuild status information for a given person, much faster than a full 
    # rebuild
    def rebuildStatusInformationForPerson_(self, forPerson):
        for i, person in enumerate(self._abPeople):
            if person is forPerson:
                bestStatus = IMPersonStatusOffline
			
                # Scan through all the services, taking the 'best' status we 
                # can find
                for service in IMService.allServices():
                    screenNames = service.screenNamesForPerson_(person)

                    # Ask for the status on each of their screen names
                    for screenName in screenNames:
                        dictionary = service.infoForScreenName_(screenName)
                        status = dictionary.get(IMPersonStatusKey)
                        if status is not None:
                            thisStatus = status
                            if IMComparePersonStatus(bestStatus, thisStatus) != NSOrderedAscending:
                                bestStatus = thisStatus
			
                self._imPersonStatus[i] = bestStatus
                self._table.reloadData()
                break

    # Sets up all our internal data
    def setupABPeople(self):
	# Keep around a copy of all the people in the AB now
	self._abPeople = ABAddressBook.sharedAddressBook().people().mutableCopy()
	
	# Sort them by display name
        self._abPeople.sortUsingSelector_('compareDisplayNames:')

	# Assume everyone is offline.
	self._imPersonStatus.removeAllObjects()
	offlineNumber =  IMPersonStatusOffline
        for i in range(len(self._abPeople)):
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
        if identifier == u"image":
            status = self._imPersonStatus[row]
            return NSImage.imageNamed_(IMService.imageNameForStatus_(status))
		
        elif identifier == u"name":
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
