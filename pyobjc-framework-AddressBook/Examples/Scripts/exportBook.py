#!/usr/bin/env python2.3
"""
This script gives a short example on how to use the addressbook framework,
it creates an CSV file containing information about all entries in the
addressbook.

Usage:
    python exportBook.py output.csv
"""
import csv
import sys

import AddressBook

# The names of fields in the export, and the corresponding property.
FIELD_NAMES=(
    ('Last Name',  AddressBook.kABLastNameProperty),
    ('First Name', AddressBook.kABFirstNameProperty),
    ('E-mail',     AddressBook.kABEmailProperty),
)

def encodeField(value):
    """
    Encode a value into an UTF-8 string
    """
    if value is None:
        return ''

    if isinstance(value, AddressBook.ABMultiValue):
        # A multi-valued property, merge them into a single string
        result = []
        for i in range(len(value)):
            result.append(value.valueAtIndex_(i).encode('utf-8'))
        return ', '.join(result)

    return value.encode('utf-8')

def personToFields(person, fieldnames):
    """ Extract the specified fields from a person object """
    return [ encodeField(person.valueForProperty_(nm)) for nm in fieldnames ]

def bookFields(book, fieldnames):
    """ Generate the records for all people in the book """
    for person in book.people():
        yield personToFields(person, fieldnames)

def main(argv = None):
    """ main entry point """

    if argv is None:
        argv = sys.argv[1:]

    if len(argv) != 1:
        print "Usage: python exportBook.py output.csv"
        sys.exit(1)

    book = AddressBook.ABAddressBook.sharedAddressBook()

    fp = open(argv[0], 'wb')
    csvStream = csv.writer(fp)
    csvStream.writerow([ f[0] for f in FIELD_NAMES])
    for row in bookFields(book, [ f[1] for f in FIELD_NAMES]):
        csvStream.writerow(row)
    fp.close()

if __name__ == "__main__":
    main()
