# These modules are otherwise completely standalone, they don't need any
# Mac- or PyObjC-specific stuff.
#
import os

from bundlebuilder import buildapp 
from plistlib import Plist 
    
images = [ os.path.join('Images', fn) for fn in os.listdir('Images') if fn.lower().endswith('.tiff') ]
icons = [ os.path.join('Icons', fn) for fn in os.listdir('Icons') if fn.lower().endswith('.icns') ]
src = [ fn for fn in os.listdir('.') if fn.endswith('.py') and fn not in ('main.py', 'setup-app.py') ]

buildapp(
    name = "ToDo", 
    mainprogram = "main.py",
    resources = ["English.lproj" ] + images + icons + src,
    nibname = "MainMenu",
    plist = Plist.fromFile('Info.plist'),
)   
