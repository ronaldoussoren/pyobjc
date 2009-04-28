"""
Process the (optional) BrigeSupport.xml for a framework.

XXX: This file needs to be rewritten in C for optimal speed.
"""
__all__ = ('initFrameworkWrapper', )

import objc
import pkg_resources
import new, sys, os, struct
import textwrap

import objc._bindglobals

from objc import function, registerMetaDataForSelector


# Import ElementTree from one of the various locations where
# it might be found
try:
        # Python 2.5
        import xml.etree.cElementTree as ET
except ImportError:
        # And earlier (with separate install)
        try:
            import cElementTree as ET
        
        except ImportError:
            import elementtree.ElementTree as ET


# Are we in a 64-bit build:
is64Bit = (sys.maxint > 2147483647)
# Are we in a little-endian build:
isLittleEndian = (sys.byteorder == 'little')

# Cannot import Foundation, we're in the framework loading code.
NSAutoreleasePool = objc.lookUpClass('NSAutoreleasePool')
_gBridgeSupportDirectories = (
        '/System/Library/BridgeSupport',

# Don't use the rest of the default search path to avoid relying on data that
# might be on a single system. That would make it harder to create standalone
# apps in some cases.
#        '/Library/BridgeSupport',
#        os.path.expanduser('~/Library/BridgeSupport'),
    )

for method in ('alloc', 'copy', 'copyWithZone:', 'mutableCopy', 'mutableCopyWithZone:'):
    objc.registerMetaDataForSelector('NSObject', method,
            dict(
                retval=dict(already_retained=True),
            ))

def _parseBridgeSupport(data, globals, frameworkName, *args, **kwds):
    try:
        try:
            objc.parseBridgeSupport(data, globals, frameworkName, *args, **kwds)
        except objc.internal_error, e:
            import warnings
            warnings.warn("Error parsing BridgeSupport data for %s: %s" % (frameworkName, e), RuntimeWarning)
    finally:
        # Add formal protocols to the protocols submodule, for backward
        # compatibility with earlier versions of PyObjC
        if 'protocols' in globals:
            for p in objc.protocolsForProcess():
                setattr(globals['protocols'], p.__name__, p)

def initFrameworkWrapper(frameworkName,
        frameworkPath, frameworkIdentifier, globals, inlineTab=None, 
        scan_classes=None, frameworkResourceName=None):
    """
    Load the named framework, using the identifier if that has result otherwise
    using the path. Also loads the information in the bridgesupport file (
    either one embedded in the framework or one in a BrigeSupport library
    directory).
    """
    if frameworkResourceName is None:
        frameworkResourceName = frameworkName

    if frameworkIdentifier is None:
        if scan_classes is None:
            bundle = objc.loadBundle(
                frameworkName,
                globals,
                bundle_path=frameworkPath)
        else:
            bundle = objc.loadBundle(
                frameworkName,
                globals,
                bundle_path=frameworkPath,
                scan_classes=scan_classes)

    else:
        try:
            if scan_classes is None:
                bundle = objc.loadBundle(
                    frameworkName,
                    globals,
                    bundle_identifier=frameworkIdentifier)

            else:
                bundle = objc.loadBundle(
                    frameworkName,
                    globals,
                    bundle_identifier=frameworkIdentifier,
                    scan_classes=scan_classes)
        
        except ImportError:
            if scan_classes is None:
                bundle = objc.loadBundle(
                    frameworkName,
                    globals,
                    bundle_path=frameworkPath)
            else:
                bundle = objc.loadBundle(
                    frameworkName,
                    globals,
                    bundle_path=frameworkPath,
                    scan_classes=scan_classes)


    # Make the objc module available, because it contains a lot of useful
    # functionality.
    globals['objc'] = objc

    # Explicitly push objc.super into the globals dict, that way super
    # calls will behave as expected in all cases.
    globals['super'] = objc.super

    if 1:
        # Look for metadata in the Python wrapper and prefer that over the
        # data in the framework or in system locations. 
        # Needed because the system bridgesupport files are buggy.
        try:
            exists = pkg_resources.resource_exists(
                    frameworkResourceName, "PyObjC.bridgesupport")
        
        except ImportError:
            pass

        else:
            if exists:
                data = pkg_resources.resource_string(frameworkResourceName,
                    "PyObjC.bridgesupport")
                if data:
                    _parseBridgeSupport(data, globals, frameworkName, inlineTab=inlineTab)
                return bundle

    # Look for metadata in the framework bundle
    path = bundle.pathForResource_ofType_inDirectory_(frameworkName, 'bridgesupport', 'BridgeSupport')
    if path is not None:
        dylib_path = bundle.pathForResource_ofType_inDirectory_(frameworkName, 'dylib', 'BridgeSupport')
        data = open(path, 'rb').read()
        if dylib_path is not None:
            _parseBridgeSupport(data, globals, frameworkName, dylib_path)
        else:
            _parseBridgeSupport(data, globals, frameworkName)

        # Check if we have additional metadata bundled with PyObjC
        try:
            exists = pkg_resources.resource_exists(
                frameworkResourceName, "PyObjCOverrides.bridgesupport")
        
        except ImportError:
            pass

        else:
            if exists:
                data = pkg_resources.resource_string(frameworkResourceName,
                    "PyObjCOverrides.bridgesupport")
                if data:
                    _parseBridgeSupport(data, globals, frameworkName, inlineTab=inlineTab)

        return bundle
    
    # If there is no metadata there look for metadata in the standard Library
    # locations
    fn = frameworkName + '.bridgesupport'
    for dn in _gBridgeSupportDirectories:
        path = os.path.join(dn, fn)
        if os.path.exists(path):
            data = open(path, 'rb').read()
            doc = ET.fromstring(data)

            dylib_path = os.path.join(dn, frameworkName + '.dylib')
            if os.path.exists(dylib_path):
                _parseBridgeSupport(data, globals, frameworkName, dylib_path)
            else:
                _parseBridgeSupport(data, globals, frameworkName)
            
            # Check if we have additional metadata bundled with PyObjC
            try:
                exists = pkg_resources.resource_exists(
                    frameworkResourceName, "PyObjCOverrides.bridgesupport")

            except ImportError:
                pass

            else:
                if exists:
                    data = pkg_resources.resource_string(frameworkResourceName,
                        "PyObjCOverrides.bridgesupport")
                    if data:
                        _parseBridgeSupport(data, globals, frameworkName, inlineTab=inlineTab)
            return bundle
    
    # And if that fails look for the metadata in the framework wrapper
    if pkg_resources.resource_exists(
            frameworkName, "PyObjC.bridgesupport"):
        data = pkg_resources.resource_string(frameworkResourceName,
            "PyObjC.bridgesupport")
        if data:
            _parseBridgeSupport(data, globals, frameworkName, inlineTab=inlineTab)
        return bundle
    
    return bundle

def _setupCFClasses(globalDict, cftypes):
    """
    Foundation types have a fully procedural C-interface, but that can
    easily be transformed into an OO interface. This function performs that
    transformation.
    
    Function are transformed into methods by looking for functions whose name
    starts with the type and and whose first argument is of the type. As a
    special case 'Create' functions are transformed into class methods.
    
    Note that this function *adds* an OO-interface, the fully procedural API
    won't be removed.
    
    Example:
        
        url = CFURL.createWithFileSystemPath("/tmp")
        print url.copyHostName()
    
    In the procedural API:
        url = CFURLCreateWithFileSystemPath(None, "/tmp")
        print CFURLCopyHostName(url)
    
    XXX: need to add information about this feature to the documentation
    """
    for name, encoding in cftypes:
        if name.endswith('Ref'):
            name = name[:-3]
        tp = globalDict[name + 'Ref']

        for funcname in globalDict:
            if not funcname.startswith(name):
                continue
            f = globalDict[funcname]
            if not isinstance(f, function):
                continue
            metadata = f.__metadata__()

            rest = funcname[len(name):]
            if not rest[0].isupper():
                continue
            
            rest = rest[0].lower() + rest[1:]
            
            if rest.startswith('create') and metadata['retval']['type'] == encoding:
                if len(metadata['arguments']) >= 1 and metadata['arguments'][0]['type'] == '^{__CFAllocator=}':
                    argcount = len(metadata['arguments']) - 1
                    argPrefix= 'None, '
                    decorator = classmethod

                else:
                    argcount = len(metadata['arguments'])
                    argPrefix = ''
                    decorator = classmethod
           
            else:
                argcount = len(metadata['arguments']) - 1
                argPrefix= 'self, '
                decorator = lambda x: x

                if 'arguments' not in metadata or len(metadata['arguments']) == 0:
                    if metadata['retval']['type'] == encoding:
                        argPrefix = ''
                        decorator = classmethod
                        argcount = 0
                    
                    else:
                        continue
                
                elif metadata['arguments'][0]['type'] != encoding:
                    continue
            
            # We don't have argument names, therefore just count the
            # arguments...
            argList = ', '.join([ 'x%d'%(i) for i in range(argcount)])
            funcdef = textwrap.dedent('''\
                def %(rest)s(self, %(argList)s):
                    return %(funcname)s(%(argPrefix)s%(argList)s)
                ''')
            funcdef = funcdef % locals()
            g = {}
            g.update(globalDict)
            exec funcdef in g
            func = g[rest]
            
            setattr(tp, rest, decorator(func))
            
            # XXX: for compatibility with MacPython we migth want to add
            # `funcname` as a method as well (although preferably a version
            # that gives a DeprecationWarning)


_ivar_dict = objc._ivar_dict()
del objc._ivar_dict
def _structConvenience(structname, structencoding):
    def makevar(self, name=None):
        if name is None:
            return objc.ivar(type=structencoding)
        else:
            return objc.ivar(name=name, type=structencoding)
    _ivar_dict[structname] = classmethod(makevar)


# Fake it for basic C types
_structConvenience("bool", objc._C_BOOL)
_structConvenience("char", objc._C_CHR)
_structConvenience("int", objc._C_INT)
_structConvenience("short", objc._C_SHT)
_structConvenience("long", objc._C_LNG)
_structConvenience("long_long", objc._C_LNG_LNG)
_structConvenience("unsigned_char", objc._C_UCHR)
_structConvenience("unsigned_int", objc._C_UINT)
_structConvenience("unsigned_short", objc._C_USHT)
_structConvenience("unsigned_long", objc._C_ULNG)
_structConvenience("unsigned_long_long", objc._C_ULNG_LNG)
_structConvenience("float", objc._C_FLT)
_structConvenience("double", objc._C_DBL)
_structConvenience("BOOL", objc._C_NSBOOL)
_structConvenience("UniChar", objc._C_UNICHAR)
_structConvenience("char_text", objc._C_CHAR_AS_TEXT)
_structConvenience("char_int", objc._C_CHAR_AS_INT)

objc._setStructConvenience(_structConvenience)
del objc._setStructConvenience


# XXX: this is a nice-to-have, but adds a full second to the 
# load time of importing Quartz.
#objc._setSetupCFClasses(_setupCFClasses)
#del objc._setSetupCFClasses

# Optimize usage of global variables
objc._bindglobals.bind_all(sys.modules[__name__])
