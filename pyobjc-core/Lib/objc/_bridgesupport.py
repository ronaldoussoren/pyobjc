"""
Backward compatibity with bridgesupport files
"""
__all__ = ('initFrameworkWrapper', 'parseBridgeSupport')

import sys
import xml.etree.ElementTree as ET
import ctypes
import objc
import re

from objc import registerMetaDataForSelector, error


for method in (b'alloc', b'copy', b'copyWithZone:', b'mutableCopy', b'mutableCopyWithZone:'):
    registerMetaDataForSelector(b'NSObject', method,
            dict(
                retval=dict(already_retained=True),
            ))


#
# The rest of this file contains support for bridgesupport
# XML files.
#
# TODO: parseBridgeSupport (and its support class) is a 
#       basic port from C, check if it can be simplified.

DEFAULT_SUGGESTION="don't use this method"
BOOLEAN_ATTRIBUTES=[
    "already_retained",
    "already_cfretained",
    "c_array_length_in_result",
    "c_array_delimited_by_null",
    "c_array_of_variable_length",
    "printf_format",
    "free_result",
]


if sys.version_info[0] == 2:
    def as_bytes(value):
        return value

    def as_string(value):
        return value

else:
    def as_bytes(value):
        return value.encode('ascii')

    def as_string(value):
        return value.decode('ascii')

class _BridgeSupportParser (object):
    TAG_MAP={}

    def __init__(self, xmldata, frameworkName):
        self.values = {}
        self.frameworkName = frameworkName
        self.func_aliases = []
        self.functions = []
        self.process_data(xmldata)

    def process_data(self, xmldata):
        root = ET.fromstring(xmldata.strip())

        if root.tag != 'signatures':
            raise error("invalid root node in bridgesupport file")

        for node in root:
            method = getattr(self, 'do_%s'%(node.tag,), None)
            if method is None:
                continue

            method(node)

    def typestr2typestr(self, typestr):
        result = []
        for item in objc.splitSignature(as_bytes(typestr)):
            if item == objc._C_BOOL:
                result.append(objc._C_NSBOOL)

            elif item == objc._C_NSBOOL:
                result.append(objc._C_BOOL)

            elif item.startswith(objc._C_STRUCT_B) or item.startswith(objc._C_UNION_B):
                m = re.match(r'.([^=]*=)?(.*).$', item)
                result.append(item[0])
                result.append(m.group(0) or '')
                fields = m.group(1)
                if fields.startswith('"'):
                    for idx, value in enumerate(re.split('("[^"]*")', fields))[1:]:
                        if idx % 2 == 0:
                            # name
                            result.append(value)
                        else:
                            result.append(self.typestr2typestr(value))
                else:
                    for value in objc.splitSignature(fields):
                        result.append(self.typestr2typestr(fields))

                result.append(item[-1])

            elif item.startswith(objc._C_ARY_B):
                m = re.match(r'^.(\d*)(.*).$', item)
                result.append(objc._C_ARY_B)
                item.append(m.group(1))
                item.append(self.typestr2typestr(m.group(2)))
                result.append(objc._C_ARY_E)

            else:
                result.append(item)

        result = b''.join(result)
        return as_string(result)


    if sys.maxsize > 2**32:
        def attribute_string(self, node, name, name64):
            if name64 is not None:
                value = node.get(name64)
                if value is not None:
                    return value

            return node.get(name)

    else:
        def attribute_string(self, node, name, name64):
            return node.get(name)

    def attribute_bool(self, node, name, name64, dflt):
        value = self.attribute_string(node, name, name64)
        if value is None:
            return dflt

        if value == "true":
            return True

        return False

    def import_name(self, name):
        module, field = name.rsplit('.', 1)
        m = __import__(module)
        try:
            for nm in module.split('.')[1:]:
                m = getattr(m, nm)

            return getattr(m, field)

        except AttributeError:
            raise ImportError(name)


    def xml_to_arg(self, node, is_method, is_arg):
        argIdx = None
        result = {}

        if is_arg:
            argIdx = int(self.attribute_string(node, "index", None))

        s = self.attribute_string(node, "type", "type64")
        if s:
            s = as_bytes(self.typestr2typestr(s))
            result["type"] = s

        s = self.attribute_string(node, "type_modifier", None)
        if s:
            result["type_modifier"] = as_bytes(s)

        s = self.attribute_string(node, "sel_of_type", "sel_of_type64")
        if s:
            s = as_bytes(self.typestr2typestr(s))
            result["sel_of_type"] = s

        s = self.attribute_string(node, "c_array_of_fixed_length", None)
        if s:
            result["c_array_of_fixed_length"] = int(s)

        for attr in BOOLEAN_ATTRIBUTES:
            s = self.attribute_bool(node, attr, None, False)
            if s:
                result[attr] = True

        s = self.attribute_bool(node, "null_accepted", None, True)
        if not s:
            result["null_accepted"] = False

        s = self.attribute_string(node, "c_array_length_in_arg", None)
        if s:
            if ',' in s:
                start, stop = map(int, s.split(','))
                if is_method:
                    start += 2
                    stop  += 2

                result["c_array_length_in_arg"] = (start, stop)

            else:
                s = int(s)
                if is_method:
                    s += 2

                result["c_array_length_in_arg"] = s

        if self.attribute_bool(node, "function_pointer", None, False) \
           or self.attribute_bool(node, "block", None, False):

            v = self.attribute_bool(node, "function_pointer_retained", None, True)
            result["callable_retained"] = v

            meta = result["callable"] = {}
            arguments = meta["arguments"] = {}
            idx = 0

            if self.attribute_bool(node, "block", None, False):
                # Blocks have an implicit first argument
                arguments[idx] = {
                    "type": b"^v",
                }
                idx += 1

            for al in node:
                if al.tag == "arg":
                    _, d = self.xml_to_arg(al, False, False)
                    arguments[idx] = d
                    idx += 1

                elif al.tag == "retval":
                    _, d = self.xml_to_arg(al, False, False)
                    meta["retval"] = d

        return argIdx, result

    def do_cftype(self, node):
        name    = self.attribute_string(node, "name", None)
        typestr = self.attribute_string(node, "type", "type64")
        funcname = self.attribute_string(node, "gettypeid_func", None)
        tollfree = self.attribute_string(node, "tollfree", None)

        if not name or not typestr:
            return

        typestr = as_bytes(self.typestr2typestr(typestr))

        if tollfree:
            objc.registerCFSignature(name, typestr, None, tollfree)
        else:
            try:
                dll = ctypes.cdll(None)
                gettypeid = getattr(dll, funcname)
                gettypeid.restype = ctypes.c_long
            except AttributeError:
                objc.registerCFSignature(name, typestr, None, "NSCFType")
                return

            objc.registerCFSignature(name, gettypeid(), typeId)


    def do_constant(self, node):
        name    = self.attribute_string(node, "name", None)
        typestr = self.attribute_string(node, "type", "type64")

        if name is None or not typestr:
            return

        typestr = as_bytes(self.typestr2typestr(typestr))

        if typestr.startswith(objc._C_STRUCT_B):
            # Look for structs with embbeded function pointers
            # and ignore those
            nm, fields = objc.splitStructSignature(as_bytes(typestr))
            for nm, tp in fields:
                if tp == b'?':
                    return

        magic = self.attribute_bool(node, "magic_cookie", None, False)
        try:
            value = objc._loadConstant(name, typestr, magic)
        except AttributeError:
            return

        self.values[name] = value


    def do_class(self, node):
        class_name = self.attribute_string(node, "name", None)
        if not class_name:
            return

        for method in node:
            if method.tag != "method":
                continue

            sel_name = as_bytes(self.attribute_string(method, "selector", None))
            variadic = self.attribute_bool(  method, "variadic", None, False)
            c_array  = self.attribute_bool(  method, "c_array_delimited_by_null", None, False)
            c_length = self.attribute_string(method, "c_array_length_in_arg", None)
            ignore   = self.attribute_bool(  method, "ignore", None, False)

            metadata = {}
            if ignore:
                suggestion = self.attribute_string(method, "suggestion", None)
                if not suggestion:
                    suggestion = DEFAULT_SUGGESTION

                metadata['suggestion'] = suggestion
            metadata['variadic'] = variadic
            if variadic:
                if c_array:
                    metadata['c_array_delimited_by_null'] = c_array

                if c_length:
                    metadata['c_array_length_in_arg'] = int(c_length);

            arguments = metadata['arguments'] = {}

            for al in method:
                if al.tag == "arg":
                    arg_idx, meta = self.xml_to_arg(al, True, True)
                    arguments[arg_idx+2] = meta

                elif al.tag == "retval":
                    _, meta = self.xml_to_arg(al, True, False)
                    metadata['retval'] = meta


            objc.registerMetaDataForSelector(as_bytes(class_name), bytes(sel_name), metadata)


    def do_enum(self, node):
        name  = self.attribute_string(node, "name", None)
        value = self.attribute_string(node, "value", "value64")

        if value is None:
            if sys.byteorder == 'little':
                value = self.attribute_string(node, "le_value", None)
            else:
                value = self.attribute_string(node, "be_value", None)

        if not name or not value:
            return

        if '.' in value:
            value = float(value)

        else:
            value = int(value, 10)

        self.values[name] = value


    def do_function(self, node):
        name = self.attribute_string(node, "name", None)
        if not name:
            return

        if self.attribute_bool(node, "ignore", None, False):
            return
        
        meta = {}
        siglist = [b"v"]
        arguments = meta["arguments"] = {}

        variadic = self.attribute_bool(node, "variadic", None, False)
        if variadic:
            meta["variadic"] = True
            v = self.attribute_bool(node, "c_array_delimited_by_null", None, False)
            if v:
                meta["c_array_delimited_by_null"] = True

            v = self.attribute_string(node, "c_array_length_in_arg", None)
            if v:
                meta["c_array_length_in_arg"] = int(v)

        for al in node:
            if al.tag == "arg":
                _, d = self.xml_to_arg(node, False, False)
                siglist.append(d["type"])

                arguments[len(siglist)-2] = d
            elif al.tag == "retval":
                _, d = self.xml_to_arg(node, False, False)
                siglist[0] = d["type"]
                meta["retval"] = d

        self.functions.append((name, b"".join(siglist), "", meta))



    def do_function_pointer(self, node):
        name = self.attribute_string(node, "name", None)
        original = self.attribute_string(node, "original", None)
        if not name or not original:
            return

        self.func_aliases.append((name, original))

    def do_informal_protocol(self, node):
        name = self.attribute_string(node, "name", None)
        if not name:
            return


        method_list = []
        for method in node:
            sel_name = attribute_string(method, "selector", None)
            typestr  = attribute_string(method, "type", "type64")
            is_class = attribute_bool(method, "classmethod", None, False)

            if not sel_name or not typestr:
                continue

            typestr = as_bytes(self.typestr2typestr(typestr))
            sel = objc.selector(None, selector=as_bytes(sel_name), 
                    signature=as_bytes(typestr), isClassMethod=is_class)
            method_list.append(sel)

        if method_list:
            proto = objc.informal_protocol(name, method_list)
            if "protocols" not in self.values:
                mod_name = "%s.protocols"%(self.frameworkName,)
                m = self.values["protocols"] = type(objc)(mod_name)
                sys.modules[mod_name] = m

            else:
                m = self.values["protocols"]

            setattr(m, name, proto)

    def do_null_const(self, node):
        name = self.attribute_string(node, "name", None)
        if not name:
            return

        self.values[name] = None

    def do_opaque(self, node):
        name    = self.attribute_string(node, "name", None)
        typestr = self.attribute_string(node, "type", "type64")

        if name is None or not typestr:
            return

        typestr = as_bytes(self.typestr2typestr(typestr))

        self.values[name] = objc.createOpaquePointerType(name, typestr)


    def do_struct(self, node):
        name    = self.attribute_string(node, "name", None)
        typestr = self.attribute_string(node, "type", "type64")
        alias   = self.attribute_string(node, "alias", None)

        if not name or not typestr:
            return

        typestr = as_bytes(self.typestr2typestr(typestr))

        if alias:
            try:
                value = self.import_name(alias)
            except ImportError:
                # Fall through to regular handling
                pass

            else:
                self.values[name] = value
                objc.registerStructAlias(typestr, value)
                _structConvenience(name, value)

        self.values[name] = value = objc.createStructType(name, typestr, None)
        _structConvenience(name, value)
        # XXX: new metadata should also use structConvenience!


    def do_string_constant(self, node):
        name  = self.attribute_string(node, "name", None)
        value = self.attribute_string(node, "value", "value64")
        nsstring = self.attribute_string(node, "nsstring", None, False)

        if not name or not value:
            return

        if sys.version_info[0] == 2:
            if nsstring:
                value = value.decode('utf-8')

        else:
            if not nsstring:
                value = value.encode('latin1')

        self.values[name] = value


_libraries = []

def parseBridgeSupport(xmldata, globals, frameworkName, dylib_path=None, inlineTab=None, bundle=None):

    if dylib_path:
        lib = ctypes.cdll.LoadLibrary(dylib_path)
        _libraries.append(lib)

    objc._updatingMetadata(True)
    try:
        prs = _BridgeSupportParser(xmldata, frameworkName)

        globals.update(prs.values)
        if prs.functions:
            if bundle is None and inlineTab is None:
                raise objc.error("Cannot load bundle functions without bundle argument")

            if bundle is not None:
                objc.loadBundleFunctions(bundle, globals, prs.functions)

            if inlineTab is not None:
                objc.loadFunctionList(inlineTab, globals, prs.functions)

        for name, orig in prs.func_aliases:
            try:
                globals[name] = globals[orig]
            except KeyError:
                pass

    finally:
        objc._updatingMetadata(False)





def _parseBridgeSupport(data, globals, frameworkName, *args, **kwds):
    try:
        try:
            objc.parseBridgeSupport(data, globals, frameworkName, *args, **kwds)
        except objc.internal_error as e:
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
                    _parseBridgeSupport(data, globals, frameworkName, inlineTab=inlineTab, bundle=bundle)
                return bundle

    # Look for metadata in the framework bundle
    path = bundle.pathForResource_ofType_inDirectory_(frameworkName, 'bridgesupport', 'BridgeSupport')
    if path is not None:
        dylib_path = bundle.pathForResource_ofType_inDirectory_(frameworkName, 'dylib', 'BridgeSupport')
        data = open(path, 'rb').read()
        if dylib_path is not None:
            _parseBridgeSupport(data, globals, frameworkName, dylib_path, bundle=bundle)
        else:
            _parseBridgeSupport(data, globals, frameworkName, bundle=bundle)

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
                    _parseBridgeSupport(data, globals, frameworkName, inlineTab=inlineTab, bundle=bundle)

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
                        _parseBridgeSupport(data, globals, frameworkName, inlineTab=inlineTab, bundle=bundle)
            return bundle
    
    # And if that fails look for the metadata in the framework wrapper
    if pkg_resources.resource_exists(
            frameworkName, "PyObjC.bridgesupport"):
        data = pkg_resources.resource_string(frameworkResourceName,
            "PyObjC.bridgesupport")
        if data:
            _parseBridgeSupport(data, globals, frameworkName, inlineTab=inlineTab, bundle=bundle)
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
