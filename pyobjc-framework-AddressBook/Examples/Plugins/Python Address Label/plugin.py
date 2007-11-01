"""
This plugin adds an 'Python Address Label' action to "Adress" properties in
the AddressBook application.

To install this plugin you have to build it (using 'python setup.py py2app')
and then copy it to  '~/Library/Address\ Book\ Plug-Ins' (this folder may
not exist yet.
"""
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
