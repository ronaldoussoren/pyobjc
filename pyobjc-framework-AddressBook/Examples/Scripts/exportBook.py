#!/usr/bin/env python3
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
FIELD_NAMES = (
    ("Last Name", AddressBook.kABLastNameProperty),
    ("First Name", AddressBook.kABFirstNameProperty),
    ("E-mail", AddressBook.kABEmailProperty),
)

if sys.version_info[0] == 2:

    def encodeField(value):
        """
        Encode a value into an UTF-8 string
        """
        if value is None:
            return ""

        if isinstance(value, AddressBook.ABMultiValue):
            # A multi-valued property, merge them into a single string
            result = []
            for i in range(value.count()):
                result.append(value.valueAtIndex_(i).encode("utf-8"))

            return "; ".join(result)

        return value.encode("utf-8")

else:

    def encodeField(value):
        """
        Encode a value into an UTF-8 string
        """
        if value is None:
            return ""

        if isinstance(value, AddressBook.ABMultiValue):
            # A multi-valued property, merge them into a single string
            result = []
            for i in range(value.count()):
                result.append(value.valueAtIndex_(i))

            return "; ".join(result)

        return value


def personToFields(person, fieldnames):
    """Extract the specified fields from a person object"""
    return [encodeField(person.valueForProperty_(nm)) for nm in fieldnames]


def bookFields(book, fieldnames):
    """Generate the records for all people in the book"""
    for person in book.people():
        yield personToFields(person, fieldnames)


def main(argv=None):
    """main entry point"""

    if argv is None:
        argv = sys.argv[1:]

    if len(argv) != 1:
        print("Usage: python exportBook.py output.csv", file=sys.stderr)
        sys.exit(1)

    book = AddressBook.ABAddressBook.sharedAddressBook()

    with open(argv[0], "w") as fp:
        csvStream = csv.writer(fp)
        csvStream.writerow([f[0] for f in FIELD_NAMES])
        for row in bookFields(book, [f[1] for f in FIELD_NAMES]):
            csvStream.writerow(row)


if __name__ == "__main__":
    main()
