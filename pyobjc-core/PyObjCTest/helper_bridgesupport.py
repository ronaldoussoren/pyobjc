import sys

sys.path.insert(0, sys.argv[1])

import objc
if not objc.__file__.startswith(sys.argv[1]):
    print("Loaded objc from unexpected path")
    sys.exit(1)

try:
    unicode
except NameError:
    unicode = str

passed = True
g = {}
objc.initFrameworkWrapper("AddressBook",
        "/System/Library/Frameworks/AddressBook.framework",
        "com.apple.AddressBook.framework",
        g, scan_classes=False)

if 'ABAddPropertiesAndTypes' not in g:
    print("Cannot find 'ABAddPropertiesAndTypes'")
    passed = False

else:
    func = g['ABAddPropertiesAndTypes']
    if not isinstance(func, objc.function):
        print("'ABAddPropertiesAndTypes' not an objc.function")
        passed = False

    else:
        if func.__metadata__() != {
            'retval': {
                'already_retained': False,
                'already_cfretained': False,
                'type': 'q' if sys.maxint > 2**32 else 'l',
            },
            'arguments': (
                {
                    'null_accepted': True,
                    'already_retained': False,
                    'already_cfretained': False,
                    'type': '^{__ABAddressBookRef=}',
                },
                {
                    'null_accepted': True,
                    'already_retained': False,
                    'already_cfretained': False,
                    'type': '^{__CFString=}',
                }, {
                    'null_accepted': True,
                    'already_retained': False,
                    'already_cfretained': False,
                    'type': '^{__CFDictionary=}',
                }
            ),
            'variadic': False
            }:

            print("Unexpected metadata for 'ABAddPropertiesAndTypes'")
            passed = False

if 'ABAddressBookErrorDomain' not in g:
    print("'ABAddressBookErrorDomain' not found")
    passed = False

elif not isinstance(g['ABAddressBookErrorDomain'], unicode):
    print("'ABAddressBookErrorDomain' not a string")
    passed = False

if 'ABAddRecordsError' not in g:
    print("'ABAddRecordsError' not found")
    passed = False

elif g['ABAddRecordsError'] != 1001:
    print("'ABAddRecordsError' has wrong value")
    passed = False

if 'NSObject' in g:
    print("No scan_classes, but 'NSObject' found")
    passed = False

if 'ABAddressBook' in g:
    print("No scan_classes, but 'ABAddressBook' found")
    passed = False

g = {}
objc.initFrameworkWrapper("AddressBook",
        "/System/Library/Frameworks/AddressBook.framework",
        "com.apple.AddressBook.framework",
        g, scan_classes=True)

if 'ABAddressBook' not in g:
    print("'ABAddressBook' not found")
    passed = False

elif not isinstance(g['ABAddressBook'], objc.objc_class):
    print("'ABAddressBook' not a class")
    passed = False

else:
    m = g['ABAddressBook'].addRecord_.__metadata__()
    if m['retval']['type'] != objc._C_NSBOOL:
        print("'ABAddressBook' -addRecord: metadata not processed")
        passed = False

if passed:
    sys.exit(0)
else:
    sys.exit(1)
