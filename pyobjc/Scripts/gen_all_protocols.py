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

ALTMAIN={
    'SecurityInterface':'SFAuthorizationView',
    'ExceptionHandling':'NSExceptionHandler',
    'AppleScriptKit':'ASKPluginObject',
}

EXTRASTUFF={
    "WebKit":"#import <WebKit/WebKit.h>\n#import <WebKit/WebJavaPlugIn.h>",
    "Automator":"#import <Cocoa/Cocoa.h>",
    "SecurityInterface":"\n".join(
        ["#import <SecurityInterface/%s>" % (s,) for s in 
            """
            SFAuthorizationView.h
            SFCertificatePanel.h
            SFCertificateTrustPanel.h
            SFCertificateView.h
            SFChooseIdentityPanel.h
            SFKeychainSavePanel.h
            SFKeychainSettingsPanel.h
            """.split()
        ]),
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
for framework in [
        "WebKit", "ExceptionHandling", "SecurityInterface", "AppleScriptKit",
        "Automator", "CoreData", "XgridFoundation",
        "SyncServices", "DiscRecording", "DiscRecordingUI", 'QTKit', "OSAKit",
        "SenTestingKit",
        ]:
    path = "/System/Library/Frameworks/%s.framework" % framework
    protfile = file(os.path.join(libdir, framework, "protocols.py"), "w")

    if not os.path.exists(path): continue

    print "generating protocols for", framework
    genProtocols(path, protfile, SPECIALS.get(framework, {}), ALTMAIN.get(framework, None), EXTRASTUFF.get(framework, ""))
