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

POINTER_INFO={}
POINTER_INFO['AppKit'] = {
    ('control:textView:completions:forPartialWordRange:indexOfSelectedItem:', 5): 'o',
    ('datePickerCell:validateProposedDateValue:timeInterval:', 2): 'N',
    ('datePickerCell:validateProposedDateValue:timeInterval:', 3): 'N',
    ('commitEditingWithDelegate:didCommitSelector:contextInfo:', 3): 'i',
    ('menuHasKeyEquivalent:forEvent:target:action:', 3): 'o',
    ('menuHasKeyEquivalent:forEvent:target:action:', 4): 'o',
    ('outlineView:toolTipForCell:rect:tableColumn:item:mouseLocation:', 3): 'N',
    ('tableView:toolTipForCell:rect:tableColumn:row:mouseLocation:', 3): 'N',
    ('textView:completions:forPartialWordRange:indexOfSelectedItem:', 4): 'o',
    ('tokenFieldCell:completionsForSubstring:indexOfToken:indexOfSelectedItem:', 4): 'o',
    ('tokenField:completionsForSubstring:indexOfToken:indexOfSelectedItem:', 4): 'o',
    ('view:stringForToolTip:point:userData:', 4): 'i',
}
POINTER_INFO['Foundation'] = {
    ('zone', 0): None,
    ('copyWithZone:', 1): None,
    ('mutableCopyWithZone:', 1): None,
    ('attemptRecoveryFromError:optionIndex:delegate:didRecoverSelector:contextInfo:', 5): 'i',
    ('validateValue:forKey:error:', 1): 'N',
    ('validateValue:forKey:error:', 3): 'o',
    ('validateValue:forKeyPath:error:', 1): 'N',
    ('validateValue:forKeyPath:error:', 3): 'o',
    ('addObserver:forKeyPath:options:context:', 4): 'i',
    ('observeValueForKeyPath:ofObject:change:context:', 4): 'i',
    ('observationInfo', 0): 'i',
    ('setObservationInfo:', 1): 'i',
    ('handleMachMessage:', 1): None, # FIXME
    ('deserializeObjectAt:ofObjCType:fromData:atCursor:', 1): None, # Deprecated
    ('deserializeObjectAt:ofObjCType:fromData:atCursor:', 4): None, # Deprecated
    ('serializeObjectAt:ofObjCType:intoData:', 1): None, # Deprecated
    ('spellServer:findMisspelledWordInString:language:wordCount:countOnly:', 4): 'o',
}
POINTER_INFO['WebKit'] = {
    ('webPlugInCallJava:isStatic:returnType:method:arguments:callingURL:exceptionDescription:', 1): None,
    ('webPlugInCallJava:isStatic:returnType:method:arguments:callingURL:exceptionDescription:', 4): None,
    ('webPlugInCallJava:isStatic:returnType:method:arguments:callingURL:exceptionDescription:', 5): None,
    ('webPlugInCallJava:isStatic:returnType:method:arguments:callingURL:exceptionDescription:', 7): None,
    ('webPlugInGetApplet', 0): None,
}
POINTER_INFO['DiscRecordingUI'] = {
    ('setupPanel:deviceContainsSuitableMedia:promptString:', 3): 'o',
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
    genProtocols(path, protfile, SPECIALS.get(framework, {}), ALTMAIN.get(framework, None), EXTRASTUFF.get(framework, ""), pointerInfo=POINTER_INFO.get(framework, {}))

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
    genProtocols(path, protfile, SPECIALS.get(framework, {}), ALTMAIN.get(framework, None), EXTRASTUFF.get(framework, ""), pointerInfo=POINTER_INFO.get(framework, {}))
