import AddressBook
import Cocoa
import objc


class ABPerson(objc.Category(AddressBook.ABPerson)):
    # Pull first and last name, organization, and record flags
    # If the entry is a company, display the organization name instead
    def displayName(self):
        firstName = self.valueForProperty_(AddressBook.kABFirstNameProperty)
        lastName = self.valueForProperty_(AddressBook.kABLastNameProperty)
        companyName = self.valueForProperty_(AddressBook.kABOrganizationProperty)
        flags = self.valueForProperty_(AddressBook.kABPersonFlags)
        if flags is None:
            flags = 0

        if (flags & AddressBook.kABShowAsMask) == AddressBook.kABShowAsCompany:
            if len(companyName):
                return companyName

        lastNameFirst = (
            flags & AddressBook.kABNameOrderingMask
        ) == AddressBook.kABLastNameFirst
        hasFirstName = firstName is not None
        hasLastName = lastName is not None

        if hasLastName and hasFirstName:
            if lastNameFirst:
                return Cocoa.NSString.stringWithString_("%s %s" % (lastName, firstName))
            else:
                return Cocoa.NSString.stringWithString_("%s %s" % (firstName, lastName))

        if hasLastName:
            return lastName

        return firstName

    def compareDisplayNames_(self, person):
        return self.displayName().localizedCaseInsensitiveCompare_(person.displayName())
