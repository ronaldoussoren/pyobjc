#!/usr/bin/env python
# Using the AddressBook framework on MacOS X
#
# I didn't add a single line of C code for this!
import AddressBook

book = AddressBook.ABAddressBook.sharedAddressBook()
me = book.me()

if not me:
    import sys
    print """There doesn't appear to be an entry marked as 'your card'.

Mark a record in the address book as 'This is my card' under the Card
menu and run this script again.
"""
    sys.exit(1)

propNames = me.properties()
d = {}
for i in propNames:
    d[i] = me.valueForProperty_(i)

keys = d.keys()
keys.sort()
print "Information about me"
print "--------------------"
for k in keys:
    if d[k] == None: continue
    print '%s: %s'%(k, d[k])

