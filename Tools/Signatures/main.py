import os, sys

import objc
from PyObjCTools import AppHelper
from PyObjCTools import NibClassBuilder
import Foundation, AppKit
import tools, scanwrappers

objc.setVerbose(1)

NibClassBuilder.extractClasses('MainMenu')

def sortKey(item):
    return (not tools.signatureRequiresHelp(item['selector'], item['signature']), item.get('undocumented') or item.get('ignore'), item['clsName'], item['selector'])

def defaultXMLLocation():
    """
    Return the default location of the signatures file, two directories
    above our bundle (assuming we get run inside the 'dist' directory).
    """
    appbundle = Foundation.NSBundle.mainBundle()
    approot = appbundle.bundlePath()

    return os.path.join(
            os.path.dirname(os.path.dirname(approot)), 
            'signatures.xml')

def defaultSourceRoot():
    """
    Location of the sources, assuming we're run in the dist directory.
    """
    appbundle = Foundation.NSBundle.mainBundle()
    approot = appbundle.bundlePath()

    return os.path.dirname(
            os.path.dirname(
                os.path.dirname(
                    os.path.dirname(approot))))

def makeNSArray(values=None):
    if values is None:
        return Foundation.NSMutableArray.array()
    return Foundation.NSMutableArray.arrayWithArray_(values)

def makeNSDictionary(items):
    value = Foundation.NSMutableDictionary.dictionary()
    for k, v in items:
        value[k] = v
    return value

class SignatureValidTransformer (Foundation.NSValueTransformer):
    def transformedValue_(self, value):
        try:
            objc.splitSignature(value['signature'])
        except objc.error:
            return AppKit.NSColor.redColor()


        if value.get('manual'):
            return AppKit.NSColor.greenColor()

        elif value.get('ignore') or value.get('undocumented'):
            if tools.signatureRequiresHelp(value['selector'], value['signature']):
                return AppKit.NSColor.darkGrayColor()
            return AppKit.NSColor.grayColor()

        elif tools.signatureRequiresHelp(value['selector'], value['signature']):
            return AppKit.NSColor.orangeColor()

        else:
            return AppKit.NSColor.blackColor()

SignatureValidTransformer.setValueTransformer_forName_(
        SignatureValidTransformer.alloc().init(), "signatureValid")

class SignatureController (NibClassBuilder.AutoBaseClass):
    signaturemapping = None
    scanBusy = False

    filename = defaultXMLLocation()
    pydir = defaultSourceRoot()

    def awakeFromNib(self):
        self.scanBusy = False
        if os.path.exists(self.filename):
            fp = open(self.filename, 'r')
            new = tools.fromXML(file=fp,
                listFactory=list, dictFactory=makeNSDictionary)
            new.sort(key=sortKey)
            self.signaturemapping = Foundation.NSMutableArray.arrayWithArray_(new)
            fp.close()
        else:
            self.signaturemapping = Foundation.NSMutableArray.array()

    def save_(self, sender):
        if not self.signaturemapping:
            return

        tools.writeXML(self.filename, self.signaturemapping)

    def generatepy_(self, sender):
        if self.pydir is None:
            # TODO: use savepanel to ask for directory
            self.pydir = defaultSourceRoot()
    
        rootdir = os.path.join(self.pydir, 'Lib')
        for framework in os.listdir(rootdir):
            if not os.path.isdir(os.path.join(rootdir, framework)): continue
            if framework == '.svn': continue
            
            fn = os.path.join(rootdir, framework, '_signatures.py')
            tools.writeSignatures(fn, 
                tools.filterSignatures(framework, self.signaturemapping))

    def scan_(self, sender):
        self.scanBusy=True
        app = AppKit.NSApplication.sharedApplication()
        app.beginSheet_modalForWindow_modalDelegate_didEndSelector_contextInfo_(
                self.busyPanel, self.window, None, None, 0)
        self.performSelector_withObject_afterDelay_('doscan:', None, 0.1)


    def _scanAlert(self, message):
        app = AppKit.NSApplication.sharedApplication()
        app.endSheet_(self.busyPanel)
        self.busyPanel.orderOut_(self)

        AppKit.BeginAlertSheet("Scan failed", 
                "OK", None, None, self.window, None, None, 0,
                message)

    def doscan_(self, value):
        # Scan using a subprocess. Assume we're using a framework build in
        # /Library...
        # We're using a subprocess to avoid polluting this process.
        #
        # XXX: This function will block the entire GUI for quite some time.
        # 
        pyver = '.'.join(map(str, sys.version_info[:2]))
        pypath = '/Library/Frameworks/Python.framework/Versions/%s/bin/python'%(
            pyver)
        if not os.path.exists(pypath):
            pypath = '/System' + pypath
            if not os.path.exists(pypath):
                self._scanAlert("Cannot find Python executable")
                return
       
        script = Foundation.NSBundle.mainBundle().pathForResource_ofType_('tools', 'py')
        if script is None:
            self._scanAlert("Cannot find my tool script")
            return

        fmkdir = os.path.join(defaultSourceRoot(), 'Lib')
        frameworks = [dn for dn in os.listdir(fmkdir) 
                    if dn != '.svn' and os.path.isdir(os.path.join(fmkdir, dn))]

        # Use an elaborate way to start the script. This avoids pickling up
        # the site.py inside the application bundle as well as py2app specific
        # settings.
        fp = os.popen("unset PYTHONHOME; PYTHONPATH=; cd /; '%s' -c 'execfile(\"%s\")' %s"%(pypath, 
            script.replace("'", "'\"'\"'"), ' '.join(frameworks)), 'r')

        # Use NSMutable{Array,Dictionary} instead of python version because
        # we're using KVO.
        updated = tools.fromXML(file=fp,
            listFactory=makeNSArray, dictFactory=makeNSDictionary)
        fp.close()
        
        updated = tools.mergeSignatures(  
                updated, self.signaturemapping)
        updated.sort(key=sortKey)

        self.signaturemapping = updated

        wrappers = scanwrappers.scanModules(os.path.join(self.pydir, 'Modules'))
        for item in self.signaturemapping:
            k = item['clsName'], item['selector']
            if k in wrappers:
                item.update(wrappers[k])

        self.scanBusy=False
        app = AppKit.NSApplication.sharedApplication()
        app.endSheet_(self.busyPanel)
        self.busyPanel.orderOut_(self)

AppHelper.runEventLoop()
