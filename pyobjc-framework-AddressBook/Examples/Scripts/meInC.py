#!/usr/bin/env python3
"""
This script prints some information on 'My Card'  record using
the AddressBook C API.
"""
from __future__ import print_function

from AddressBook import (
    ABGetMe,
    ABGetSharedAddressBook,
    ABMultiValueCopyValueAtIndex,
    ABMultiValueCount,
    ABRecordCopyValue,
    kABEmailProperty,
)


def main():
    book = ABGetSharedAddressBook()

    me = ABGetMe(book)
    emails = ABRecordCopyValue(me, kABEmailProperty)

    print("You have %d email adresses" % (ABMultiValueCount(emails),))

    for idx in range(ABMultiValueCount(emails)):
        value = ABMultiValueCopyValueAtIndex(emails, idx)
        print("Email %d: %s" % (idx + 1, value))


if __name__ == "__main__":
    main()
