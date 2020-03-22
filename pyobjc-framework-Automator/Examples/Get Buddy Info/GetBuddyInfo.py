import struct
from AddressBook import ABAddressBook, ABPerson
from Automator import AMBundleAction
from Cocoa import NSAppleEventDescriptor
from InstantMessage import (
    IMPersonFirstNameKey,
    IMPersonLastNameKey,
    IMPersonScreenNameKey,
    IMPersonServiceNameKey,
    IMPersonStatusAvailable,
    IMPersonStatusAway,
    IMPersonStatusIdle,
    IMPersonStatusKey,
    IMPersonStatusMessageKey,
    IMPersonStatusOffline,
    IMPersonStatusUnknown,
    IMService,
)

typeObjectSpecifier = struct.unpack(">i", b"obj ")[0]
keyAEContainer = struct.unpack(">i", b"from")[0]
keyAEKeyData = struct.unpack(">i", b"seld")[0]


class GetBuddyInfo(AMBundleAction):
    def runWithInput_fromAction_error_(self, value, anAction, errorInfo):
        people = []

        # convert the input to a list of ABPerson objects
        if isinstance(value, NSAppleEventDescriptor):
            count = value.numberOfItems()

            for i in range(1, count + 1):
                personDescriptor = value.descriptorAtIndex_(i)
                if personDescriptor is not None:
                    # get the uid of the person from this descriptor
                    if personDescriptor.descriptorType() == typeObjectSpecifier:
                        container = personDescriptor.descriptorForKeyword_(
                            keyAEContainer
                        )
                        if container is not None:
                            uidDescriptor = container.descriptorAtIndex_(
                                i
                            ).descriptorForKeyword_(keyAEKeyData)
                            if uidDescriptor is not None:
                                uid = uidDescriptor.stringValue()
                                if uid is not None:
                                    # get the person object from the uid
                                    person = ABAddressBook.sharedAddressBook().recordForUniqueId_(  # noqa: B950
                                        uid
                                    )
                                    if person is not None:
                                        people.append(person)

        info = []
        for person in people:
            for service in IMService.allServices():
                if isinstance(person, ABPerson):
                    screenNames = service.screenNamesForPerson_(person)
                    if screenNames is not None:
                        for screenName in screenNames:
                            info_dict = service.infoForScreenName_(screenName)
                            if info_dict is not None:
                                # build the description
                                description = "\rName: "

                                firstName = info_dict[IMPersonFirstNameKey]
                                if firstName is not None:
                                    description += firstName
                                    description += " "

                                lastName = info_dict[IMPersonLastNameKey]
                                if lastName is not None:
                                    description += lastName

                                description += "\r"

                                serviceName = info_dict[IMPersonServiceNameKey]
                                if serviceName is not None:
                                    description += "Service: "
                                    description += serviceName
                                    description += "\r"

                                screenName = info_dict[IMPersonScreenNameKey]
                                if screenName is not None:
                                    description += "Screen Name: "
                                    description += screenName
                                    description += "\r"

                                status = info_dict[IMPersonStatusKey]
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

                                message = info_dict[IMPersonStatusMessageKey]
                                if message is not None:
                                    description += "Message: "
                                    description += message
                                    description += "\r"

                                info.append(description)
        return str(info)
