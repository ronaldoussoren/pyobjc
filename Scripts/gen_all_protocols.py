#!/usr/bin/env python

"""Use this script to generate protocol definitions for the frameworks as
shipped by PyObjC.
"""

import sys
import os
from gen_protocols import genProtocols

script = os.path.abspath(sys.argv[0])
libdir = os.path.join(os.path.dirname(os.path.dirname(script)), "Lib")

SPECIALS={}
SPECIALS['AppKit'] = {
    'control:textView:completions:forPartialWordRange:indexOfSelectedItem:':
        '@@:@@@{_NSRange=II}N^i',
    'textView:completions:forPartialWordRange:indexOfSelectedItem:':
        '@@:@@{_NSRange=II}N^i',

}

for framework in [
        "AppKit", 
        "Foundation", 
        "AddressBook", 
        "InterfaceBuilder", 
      ]:
    path = "/System/Library/Frameworks/%s.framework" % framework
    protfile = file(os.path.join(libdir, framework, "protocols.py"), "w")
    print "generating protocols for", framework
    genProtocols(path, protfile, SPECIALS.get(framework, {}))

# Optional frameworks
for framework in ["WebKit", ]:
    path = "/System/Library/Frameworks/%s.framework" % framework
    protfile = file(os.path.join(libdir, framework, "protocols.py"), "w")

    if not os.path.exists(path): continue

    print "generating protocols for", framework
    genProtocols(path, protfile)

if os.path.isdir('/System/Library/Frameworks/SecurityInterface.framework'):
    framework = 'SecurityInterface'
    path = "/System/Library/Frameworks/%s.framework" % framework
    protfile = file(os.path.join(libdir, framework, "protocols.py"), "w")
    print "generating protocols for", framework
    genProtocols(path, protfile, SPECIALS.get(framework, {}), 'SFAuthorizationView')
