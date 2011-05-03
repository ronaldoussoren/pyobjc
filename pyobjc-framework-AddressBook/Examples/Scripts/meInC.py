#!/usr/bin/env python
"""
This script prints some information on 'My Card'  record using
the AddressBook C API.
"""
from AddressBook import *

def main():
    book = ABGetSharedAddressBook()

    me = ABGetMe(book)
    emails = ABRecordCopyValue(me, kABEmailProperty)

    print "You have %d email adresses"%(ABMultiValueCount(emails),)

    for idx in range(ABMultiValueCount(emails)):
        value = ABMultiValueCopyValueAtIndex(emails, idx)
        print "Email %d: %s"%(idx+1,  value)

if __name__ == "__main__":
    main()
