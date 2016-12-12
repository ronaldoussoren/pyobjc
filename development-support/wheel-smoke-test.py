"""
Helper script for performing smoke tests on an installed
copy of PyObjC

# NOTE: This file is not yet complete
"""

import platform
from distutils.version import LooseVersion

sys_version = LooseVersion(platform.mac_ver()[0])


import objc
from Cocoa import *
from Quartz import *
from AddressBook import *
from AppleScriptKit import *
from AppleScriptObjC import *
from ApplicationServices import *
from HIServices import *
from Automator import *
from CFNetwork import *
from CoreData import *
from DiskArbitration import *
from ExceptionHandling import *
from GameController import *

if sys_version >= LooseVersion('10.5'):
    from CalendarStore import *
    from Collaboration import *
    from CoreText import *
    from DictionaryServices import *
    from FSEvents import *

if sys_version >= LooseVersion('10.6'):
    from CoreLocation import *
    from CoreWLAN import *

if sys_version >= LooseVersion('10.7'):
    from AVFoundation import *

if sys_version >= LooseVersion('10.8'):
    from Accounts import *
    from EventKit import *
    from GameCenter import *

if sys_version >= LooseVersion('10.9'):
    from AVKit import *

if sys_version >= LooseVersion('10.10'):
    from CloudKit import *
    from CoreBluetooth import *
    from CryptoTokenKit import *
    from FinderSync import *

if sys_version >= LooseVersion('10.11'):
    from Contacts import *
    from ContactsUI import *
