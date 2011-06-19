"""
Process the (optional) BrigeSupport.xml for a framework.

XXX: This file needs to be rewritten in C for optimal speed.
"""
#__all__ = ('initFrameworkWrapper', )
__all__ = ()

import objc
import pkg_resources
import sys, os, struct
import textwrap
import warnings

from objc import function, registerMetaDataForSelector


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

for method in (b'alloc', b'copy', b'copyWithZone:', b'mutableCopy', b'mutableCopyWithZone:'):
    objc.registerMetaDataForSelector(b'NSObject', method,
            dict(
                retval=dict(already_retained=True),
            ))

if 0:
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
        warnings.warn("objc.initFrameworkWrapper is deprecated", DeprecationWaring)

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
