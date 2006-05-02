#!/usr/bin/env python2.4
"""
Tools for finding odd selectors...

Odd selectors are those:
- With a pointer as return value (ignoring void*)
- Pointer arguments that are not of the in/out/inout variety (ignoring void*)

TODO:
- Any multi-level indirection unless it is an in/out/inout argument pointing
  to a wrapped pointer
"""
import sys, os
import objc
from Foundation import NSBundle
from elementtree import ElementTree as ET
import platform
from objc._convenience import defaultSignatureUpdates

_gVoidPtr = objc._C_PTR + objc._C_VOID
_gWrappedPointers = set((
        '^{_NSZone=}',
        '^{_NSModalSession=}',
        '^{_NSModalSession=@@^{_NSModalSession}iciI^vi@@:^vi@}',

        # FILE*
        '^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}',
        '^{__sFILE=}',
    ))

_gModifiers = (
    objc._C_IN,
    objc._C_OUT,
    objc._C_INOUT,
    objc._C_ONEWAY,
)

def registerWrappedPointerType(typestr):
    _gWrappedPointers.add(typestr)


def signatureRequiresHelp(selector, signature):
    """
    Return True iff PyObjC won't be able to handle methods with this 
    signature without further instructions.
    """
    signature = defaultSignatureUpdates(selector, signature)
    args = objc.splitSignature(signature)
    retval = args[0]
    args = args[1:]

    # Strip modifiers from the return type, those will be ignored by the core.
    while retval and retval[0] in _gModifiers:
        retval = retval[1:]

    if retval != _gVoidPtr  and retval.startswith(objc._C_PTR) \
            and retval not in _gWrappedPointers:
        # A pointer as a return value.
        return True

    for arg in args:

        # Ignore the oneway modifier
        while arg and args[0] in objc._C_ONEWAY:
            arg = arg[1:]

        if arg.startswith(objc._C_PTR) and arg != _gVoidPtr \
                and arg not in _gWrappedPointers:
            return True

    return False

def frameworkForClass(cls):
    return os.path.splitext(
            os.path.basename(NSBundle.bundleForClass_(cls).bundlePath()))[0]

def findSignatures():
    result = []

    for cls in objc.getClassList():
        clsName = cls.__name__

        if clsName.startswith('_'): 
            # Private class of some sort
            continue

        elif clsName.startswith('%'): 
            # Posing...
            continue

        elif clsName == 'Object':
            continue

        elif clsName.startswith('OC_'):
            continue

        for nm in dir(cls):
            try:
                method = cls.__dict__[nm]
            except KeyError:
                continue

            if not isinstance(method, objc.selector):
                continue

            if cls.__bases__[0] != 'Object' and hasattr(cls.__bases__[0], nm):
                # Inherited from a superclass
                continue
            
            if method.selector.startswith('_'): 
                # Private method 
                continue

            if method.native_signature is None:
                # Implemented in python
                continue

            if signatureRequiresHelp(method.selector, method.native_signature):
                result.append(dict(
                        clsName=clsName, 
                        selector=method.selector, 
                        origSignature=simplifySignature(method.native_signature), 
                        signature=simplifySignature(method.signature),
                        framework=frameworkForClass(cls),
                    ))

    return result


def fromXML(file, listFactory=list, dictFactory=dict):
    """
    Unflatten the XML-ified list and return it.
    """
    result = listFactory()
    tree=ET.ElementTree(file=file)
    for elem in tree.getroot().getchildren():
        new = dictFactory(elem.items())
        if 'ignore' in new:
            if new['ignore'] == 'True':
                new['ignore'] = True
            elif new['ignore'] == 'False':
                new['ignore'] = False
            else:
                new['ignore'] = int(new['ignore'])
        if 'manual' in new:
            if new['manual'] == 'True':
                new['manual'] = True
            elif new['manual'] == 'False':
                new['manual'] = False
            else:
                new['manual'] = int(new['manual'])
        if 'undocumented' in new:
            if new['undocumented'] == 'True':
                new['undocumented'] = True
            elif new['undocumented'] == 'False':
                new['undocumented'] = False
            else:
                new['undocumented'] = int(new['undocumented'])
        result.append(new)
    return result

def writeSignatures(filename, signatures):
    # This isn't quite right, need to replicate the default algoritm here
    # to avoid writing unnecessary updates.

    # Don't write the signatures file if we don't have signatures
    signatures = iter(signatures)
    try:
        item = signatures.next()
    except StopIteration:
        if os.path.exists(filename):
            os.unlink(filename)
        return

    def _s(sel, signature):
        return defaultSignatureUpdates(sel, simplifySignature(signature))

    fp = open(filename, 'w')
    fp.write("# This file is generated using the Signatures tool, don't edit\n")
    fp.write("from objc import setSignatureForSelector\n")
    if _s(item['selector'], item['signature']) != _s(item['selector'], item['origSignature']): 
        fp.write('setSignatureForSelector("%(clsName)s", "%(selector)s", "%(signature)s")\n'%(item))

    for item in signatures:
        if _s(item['selector'], item['signature']) == _s(item['selector'], item['origSignature']): continue

        fp.write("setSignatureForSelector(%(clsName)r, %(selector)r, %(signature)r)\n"%(item))

    fp.write("# end of file\n")
    fp.close()

def filterSignatures(framework, signatures):
    for item in signatures:
        if item['framework'] == framework:
            yield item

def simplifySignature(signature):
    return ''.join(objc.splitSignature(signature))

def main():

    for framework in sys.argv[1:]:
        try:
            __import__(framework)
        except ImportError:
            print >>sys.stderr, "WARN: ImportError for %s"%(framework,)

    root = ET.Element('signaturelist')
    root.tail = '\n'

    signatures = findSignatures()
    for item in signatures:
        e = ET.SubElement(root, 'signature', item)
        e.tail='\n'

    tree = ET.ElementTree(root)
    tree.write(sys.stdout, encoding='utf-8')

def writeXML(filename, signatures):
    """
    Use XML as too pickle the signature list to avoid being locked into
    this tool.
    """
    root = ET.Element('signaturelist')
    root.tail = '\n'

    for item in signatures:
        e = ET.SubElement(root, 'signature', 
                dict([(k, str(v)) for k,v in item.iteritems()]))
        e.tail='\n'

    tree = ET.ElementTree(root)
    tree.write(open(filename, 'wb'), encoding='utf-8')

def mergeSignatures(scanData, fileData):
    if not fileData:
        return scanData
    result = {}
    for item in fileData:
        result[(item['clsName'], item['selector'])] = item

    for item in scanData:
        k = item['clsName'], item['selector']

        if not k in result:
            result[k] = item

        else:
            curItem = result[k]
            curItem['signature'] = item['signature']

            if curItem['origSignature'] != item['origSignature']:
                print "WARN: signature changed" # XXXFIXME
                curItem['origSignature'] = item['origSignature']

            if item['oslevel'] < curItem['oslevel']:
                curItem['oslevel'] = item['oslevel']

    return result

if __name__ == "__main__":
    main()
