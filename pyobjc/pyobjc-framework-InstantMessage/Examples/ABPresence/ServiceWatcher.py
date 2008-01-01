from Cocoa import *
from InstantMessage import *
from AddressBook import *

kAddressBookPersonStatusChanged = u"AddressBookPersonStatusChanged"
kStatusImagesChanged = u"StatusImagesChanged"

class ServiceWatcher (NSObject):
    def startMonitoring(self):
	nCenter = IMService.notificationCenter()

	nCenter.addObserver_selector_name_object_(
                self, 'imPersonStatusChangedNotification:',
                IMPersonStatusChangedNotification, None)
	
	nCenter.addObserver_selector_name_object_(
                self, 'imStatusImagesChangedAppearanceNotification:',
                IMStatusImagesChangedAppearanceNotification, None)

    def stopMonitoring(self):
	nCenter = IMService.notificationCenter()
	nCenter.removeObserver_(self)

    def awakeFromNib(self):
        self.startMonitoring()

    # Received from IMService's custom notification center. Posted when a 
    # different user (screenName) logs in, logs off, goes away, 
    # and so on. This notification is for the IMService object. The user 
    # information dictionary will always contain an 
    # IMPersonScreenNameKey and an IMPersonStatusKey, and no others.
    def imPersonStatusChangedNotification_(self, notification):
	service = notification.object()
	userInfo = notification.userInfo()
	screenName = userInfo[IMPersonScreenNameKey]
	abPersons = service.peopleWithScreenName_(screenName)

        center = NSNotificationCenter.defaultCenter()
        for person in abPersons:
            center.postNotificationName_object_(
                    kAddressBookPersonStatusChanged, person)

    # Received from IMService's custom notification center. Posted when the 
    # user changes their preferred images for displaying status. 
    # This notification is relevant to no particular object. The user 
    # information dictionary will not contain keys. Clients that display 
    # status information graphically (using the green/yellow/red dots) should 
    # call <tt>imageURLForStatus:</tt> to get the new image. 
    # See "Class Methods" for IMService in this document.
    def imStatusImagesChangedAppearanceNotification_(self, notification):
        NSNotificationCenter.defaultCenter().postNotificationName_object_(
                kStatusImagesChanged, self)
