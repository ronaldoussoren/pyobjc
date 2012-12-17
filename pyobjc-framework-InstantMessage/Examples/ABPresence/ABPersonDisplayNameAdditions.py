from Cocoa import *
from AddressBook import *

class ABPerson (objc.Category(ABPerson)):
    # Pull first and last name, organization, and record flags
    # If the entry is a company, display the organization name instead
    def displayName(self):
        firstName = self.valueForProperty_(kABFirstNameProperty)
        lastName = self.valueForProperty_(kABLastNameProperty)
        companyName = self.valueForProperty_(kABOrganizationProperty)
        flags = self.valueForProperty_(kABPersonFlags)
        if flags is None:
            flags = 0

        if (flags & kABShowAsMask) == kABShowAsCompany:
            if len(companyName):
                return companyName;

        lastNameFirst = (flags & kABNameOrderingMask) == kABLastNameFirst
        hasFirstName = firstName is not None
        hasLastName = lastName is not None

        if hasLastName and hasFirstName:
            if lastNameFirst:
                return NSString.stringWithString_("%s %s"%(lastName, firstName))
            else:
                return NSString.stringWithString_("%s %s"%(firstName, lastName))

        if hasLastName:
            return lastName

        return firstName

    def compareDisplayNames_(self, person):
        return self.displayName().localizedCaseInsensitiveCompare_(
                person.displayName())
