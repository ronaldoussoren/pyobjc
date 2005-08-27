from AddressBook import *
from AppKit import *

class PyAddressLabelDelegate (NSObject):
    def actionProperty(self):
        return kABAddressProperty

    def titleForPerson_identifier_(self, person, identifier):
        return u"Python Address Label"

    def shouldEnableActionForPerson_identifier_(self, person, identifier):
        return len(person.address()) > 0

    def performActionForPerson_identifier_(self, person, identifier):
        text = person.name()
        if person.department() is not NSNull.null():
            text += '\n' + person.department()

        if person.organization() is not NSNull.null():
            text += '\n' + person.organization()

        address = person.address()[0]
        text += '\n' + address.street()
        text += '\n' + address.zip() + ' ' + address.city()

        if address.country() is not NSNull.null():
            text += '\n' + address.country()

        pboard = NSPasteboard.generalPasteboard()
        pboard.declareTypes_owner_([NSStringPboardType], None)
        pboard.setString_forType_(text, NSStringPboardType)


# Debug
print "Loading plugin"
