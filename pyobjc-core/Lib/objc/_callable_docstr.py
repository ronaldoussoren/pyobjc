__all__ = ()
from objc._objc import _setCallableDoc
import objc

basic_types = {
        objc._C_VOID:     "void",
        objc._C_INT:      "int",
        objc._C_UINT:     "unsigned int",
        objc._C_LNG:      "long",
        objc._C_ULNG:     "unsigned long",
        objc._C_LNG_LNG:  "long long",
        objc._C_ULNG_LNG: "unsigned long long",
        objc._C_FLT:      "float",
        objc._C_DBL:      "double",
        objc._C_SHT:      "short",
        objc._C_USHT:     "unsigned short",
        objc._C_CHR:      "char",
        objc._C_UCHR:     "unsigned char",
        objc._C_CHAR_AS_INT:  "int8_t",
        objc._C_CHAR_AS_TEXT:  "char",
        objc._C_UNICHAR:  "UniChar",
        objc._C_BOOL:     "bool",
        objc._C_NSBOOL:   "BOOL",
        objc._C_ID:       "id",
        objc._C_CLASS:    "Class",
        objc._C_SEL:      "SEL",
        objc._C_CHARPTR:  "char*",
}

prefixes = {
    objc._C_IN:     "in ",
    objc._C_OUT:    "out ",
    objc._C_INOUT:  "inout ",
    objc._C_CONST:  "const ",
    objc._C_ONEWAY: "oneway ",
}

def describe_type(typestr):

    nm = basic_types.get(typestr)
    if nm is not None:
        return nm

    if typestr == b"^?":
        return "<FUNCTION>"
    elif typestr == b"@?":
        return "<BLOCK>"

    if typestr.startswith(objc._C_PTR):
        return describe_type(typestr[1:]) + '*'

    if typestr[0] in prefixes:
        return prefixes[typestr[0]] + describe_type(typestr[1:])

    # XXX: handle struct, union, array, bitfield
    return "<?>"
    


def describe_signature(callable):
    name     = callable.__name__
    metadata = callable.__metadata__()
    if isinstance(callable, objc.selector):
        class_name = callable.__objclass__

        name_parts = name.split(':')
        hdr_name = []
        for idx, (nm, info) in enumerate(zip(name_parts, metadata['arguments'][2:])):
            print(nm, info)
            hdr_name.append(nm)
            hdr_name.append(':(')
            hdr_name.append(describe_type(info['type']))
            hdr_name.append(')arg%d '%(idx,))
        if metadata['variadic']:
            hdr_name.append(", ...")

        header = "%s (%s)%s"%(
                "+" if callable.isClassMethod else "-",
                describe_type(metadata['retval']['type']),
                ''.join(hdr_name))
    else:
        class_name = None
        hdr_name = []
        for idx, info in enumerate(metadata['arguments']):
            if idx != 0:
                hdr_name.apend(', ')
            hdr_name.append(describe_type(info['type']))
            hdr_name.append(' arg%d'%(idx,))
        if metadata['variadic']:
            hdr_name.append(", ...")

        header = "%s %s(%s)"%(
                describe_type(metadata['retval']['type']),
                name,
                ''.join(hdr_name))

    # XXX: add more information about 'hard' arguments

    return header

_setCallableDoc(describe_signature)
