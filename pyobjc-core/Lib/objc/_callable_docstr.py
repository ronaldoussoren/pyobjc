__all__ = ()
from objc._objc import _setCallableDoc, _nameForSignature
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
        nm = _nameForSignature(typestr)
        if nm is not None:
            return nm
        return describe_type(typestr[1:]) + '*'

    if typestr[:1] in prefixes:
        return prefixes[typestr[:1]] + describe_type(typestr[1:])

    if typestr.startswith(objc._C_STRUCT_B):
        nm = _nameForSignature(typestr)
        if nm is not None:
            return nm

    # XXX: handle struct, union, array, bitfield
    return "<?>"

def describe_signature(callable):
    name     = callable.__name__
    metadata = callable.__metadata__()

    return describe_callable(name, metadata, ismethod=isinstance(callable, objc.selector))

def describe_callable(name, metadata, offset='', ismethod=False):
    arg_info = []
    if ismethod:
        arg_offset = 2

        name_parts = name.split(':')
        hdr_name = []
        if len(metadata['arguments']) > arg_offset:
            for idx, (nm, info) in enumerate(zip(name_parts, metadata['arguments'][arg_offset:])):
                hdr_name.append(nm)
                hdr_name.append(':(')
                hdr_name.append(describe_type(info['type']))
                hdr_name.append(')arg%d '%(idx,))

                if info['type'][:1] in prefixes and info['type'][:1] not in (objc._C_ONEWAY, objc._C_CONST):
                    arg_info.append((idx, info))
                if info.get('printf_format'):
                    arg_info.append((idx, info))
                if info.get('callable'):
                    arg_info.append((idx, info))


            if metadata['variadic']:
                hdr_name.append(", ...")
        else:
            hdr_name.append(name)


        header = "%s (%s)%s;"%(
                "+" if metadata['classmethod'] else "-",
                describe_type(metadata['retval']['type']),
                ''.join(hdr_name))
    else:
        hdr_name = []
        arg_offset = 0
        for idx, info in enumerate(metadata['arguments']):
            if idx != 0:
                hdr_name.append(', ')
            hdr_name.append(describe_type(info['type']))
            hdr_name.append(' arg%d'%(idx,))
            if info['type'][:1] in prefixes and info['type'][:1] not in (objc._C_ONEWAY, objc._C_CONST):
                arg_info.append((idx, info))
            if info.get('printf_format'):
                arg_info.append((idx, info))
            if info.get('callable'):
                arg_info.append((idx, info))
        if metadata['variadic']:
            hdr_name.append(", ...")

        header = "%s %s(%s);"%(
                describe_type(metadata['retval']['type']),
                name,
                ''.join(hdr_name))

    result = [header]
    if metadata.get('suggestion'):
        result.append('')
        result.append('WARNING: %s'%(metadata['suggestion'],))

    if arg_info:
        result.append('')
        for idx, info in arg_info:
            if info.get('printf_format'):
                result.append('arg%d: %%-style format'%(idx,))
                continue

            elif info.get('callable'):
                result.append('arg%d: %s'%(idx, describe_callable('callback', info['callable'], offset='    ' + offset)))
                continue

            else:
                arg = info.get('c_array_length_in_arg')
                if arg is not None:
                    if isinstance(arg, tuple):
                        result.append('arg%d: array with length on input in arg%d, and output in arg%d'%(idx, arg[0] - arg_offset, arg[1] - arg_offset))
                    else:
                        if info.get('c_array_length_in_result'):
                            result.append('arg%d: array with length on input in arg%d, and output in return value'%(idx, arg - arg_offset))
                        else:
                            result.append('arg%d: array with length in arg%d'%(idx, arg - arg_offset))
                    continue

                if info.get('c_array_length_in_result'):
                    result.append('arg%d: array with length in return value'%(idx,))
                    continue

                if info.get('c_array_of_fixed_length'):
                    result.append('arg%d: array with length %d'%(idx, info.get('c_array_of_fixed_length')))
                    continue

                if info.get('c_array_of_variable_length'):
                    result.append('arg%d: array with unknown length'%(idx,))
                    continue

                result.append('arg%d: pass-by-reference %sargument'%(idx, prefixes.get(info['type'][:1]),))

    return ('\n'+offset).join(result)

_setCallableDoc(describe_signature)
print(describe_signature(objc.runtime.NSObject.init))
