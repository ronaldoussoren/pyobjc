#!/usr/bin/env python3
"""
Script for dumping contacts
"""
from __future__ import print_function
import Contacts

def print_info(contact, stop):
    if contact.isKeyAvailable_(Contacts.CNContactEmailAddressesKey):
        print(", ".join(val.value() for val in contact.emailAddresses()))
    else:
        print("Contact without e-mail")
    return False

def main():
    fetchRequest = Contacts.CNContactFetchRequest.alloc(
        ).initWithKeysToFetch_([Contacts.CNContactEmailAddressesKey])

    store = Contacts.CNContactStore.alloc().init()
    ok, error = store.enumerateContactsWithFetchRequest_error_usingBlock_(fetchRequest, None, print_info)
    if not ok:
        print("Fetching contacts failed", error)

if __name__ == "__main__":
    main()
