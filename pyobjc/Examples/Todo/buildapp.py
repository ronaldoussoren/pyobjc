# These modules are otherwise completely standalone, they don't need any
# Mac- or PyObjC-specific stuff.
#
import os

from bundlebuilder import buildapp
from plistlib import Plist, Dict
    
images = [ os.path.join('Images', fn) for fn in os.listdir('Images') if fn.lower().endswith('.tiff') ]
icons = [ os.path.join('Icons', fn) for fn in os.listdir('Icons') if fn.lower().endswith('.icns') ]
src = [ fn for fn in os.listdir('.') if fn.endswith('.py') and fn not in ('main.py', 'buildapp.py') ]

infoPlist = Plist(
    NSHelpFile='',
    CFBundleShortVersionString='To Do v1',
    CFBundleSignature='????',
    CFBundleInfoDictionaryVersion='6.0',
    CFBundleIconFile='ToDoApp.icns',
    NSMainNibFile='MainMenu',
    CFBundleGetInfoString='To Do v1',
    CFBundleIdentifier='com.apple.ToDo',
    CFBundleDocumentTypes=[
        Dict(
            CFBundleTypeName='To Do list',
            CFBundleTypeRole='Editor',
            NSDocumentClass='ToDoDocument',
            CFBundleTypeIconFile='ToDoDoc.icns',
            CFBundleTypeExtensions=['ToDo'],
            CFBundleTypeOSTypes=['ToDo'],
        ),
    ],
    CFBundleDevelopmentRegion='English',
    CFBundleExecutable='python',
    CFBundleName='To Do',
    CFBundlePackageType='APPL',
    NSPrincipalClass='NSApplication',
    CFBundleVersion='0.1')

buildapp(
    name = "ToDo",
    mainprogram = "main.py",
    resources = ["English.lproj" ] + images + icons + src,
    nibname = "MainMenu",
    #plist = Plist.fromFile('Info.plist'),
    plist = infoPlist
)
