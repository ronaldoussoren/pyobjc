import sys
from Cocoa import *
from Automator import *
from AddressBook import *
from InstantMessage import *

class GetBuddyInfo (AMBundleAction):
    def runWithInput_fromAction_error_(self, input, anAction, errorInfo):
        people = []
    
        # convert the input to a list of ABPerson objects
        if isinstance(input, NSAppleEventDescriptor):
            count = input.numberOfItems()

            for i in range(1, count+1):
                personDescriptor = input.desciptorAtIndex_(i)
                if personDescriptor is not None:
                    # get the uid of the person from this descriptor
                    if (personDescriptor.descriptorType() == typeObjectSpecifier):
                        container = personDescriptor.descriptorForKeyword_(keyAEContainer)
                        if container is not None:
                            uidDescriptor = container.descriptorAtIndex_(i).descriptorForKeyword_(keyAEKeyData)
                            if uidDescriptor is not None:
                                uid = uidDescriptor.stringValue()
                                if uid is not None:
                                    # get the person object from the uid
                                    person = ABAddressBook.sharedAddressBook().recordForUniqueId_(uid)
                                    if person is not None:
                                        people.append(person)

        info = []
        for person in people:
            for service in IMService.allServices():
                if isinstance(person, ABPerson):
                    screenNames = service.screenNamesForPerson_(person)
                    if screenNames is not None:
                        for screenName in screenNames:
                            dict = service.infoForScreenName_(screenName)
                            if dict is not None:
                                # build the description
                                description = "\rName: "

                                firstName = dict[IMPersonFirstNameKey]
                                if firstName is not None:
                                    description += firstName
                                    description += ' '
                            
                                lastName = dict[IMPersonLastNameKey]
                                if lastName is not None:
                                    description += lastName
                            
                                description += '\r'
                            
                                serviceName = dict[IMPersonServiceNameKey]
                                if serviceName is not None:
                                    description += "Service: "
                                    description += serviceName
                                    description += "\r"
                            
                                screenName = dict[IMPersonScreenNameKey]
                                if screenName is not None:
                                    description += "Screen Name: "
                                    description += screenName
                                    description += "\r"
                            
                                status = dict[IMPersonStatusKey]
                                if status is not None:
                                    description += "Status: "
                                
                                    if status == IMPersonStatusUnknown:
                                        description += "Unknown"
                                    elif status == IMPersonStatusOffline:
                                        description += "Offline"
                                    elif status == IMPersonStatusIdle:
                                        description += "Idle"
                                    elif status == IMPersonStatusAway:
                                        description += "Away"
                                    elif status == IMPersonStatusAvailable:
                                        description += "Available"
                                    
                                    description += "\r"
                            
                                message = dict[IMPersonStatusMessageKey]
                                if message is not None:
                                    description += "Message: "
                                    description += message
                                    description += "\r"
                            
                                info.append(description)
        return str(info)
