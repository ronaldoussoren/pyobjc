'''
Wrappers for the "CalendarStore" on macOS 10.5 and later. The CalendarStore
frameworks provides access to the iCal data. It's possible to fetch iCal
records, such as calendars and tasks, as well as modify them and get
notifications when records change in iCal.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup

VERSION="5.1"

setup(
    name='pyobjc-framework-CalendarStore',
    description = "Wrappers for the framework CalendarStore on macOS",
    min_os_level='10.5',
    packages = [ "CalendarStore" ],
    version=VERSION,
    install_requires = [
        'pyobjc-core>='+VERSION,
        'pyobjc-framework-Cocoa>='+VERSION,
    ],
    long_description=__doc__,
)
