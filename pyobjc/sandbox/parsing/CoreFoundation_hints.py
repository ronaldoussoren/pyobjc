#
# Scanframework hints for the framework 'Foundation'
#
# See scanframework.py for a description of the contents of this file.
#
ADDITIONAL_IMPORTS=(
    '_CoreFoundation',
)

_ARGUMENT_KINDS={
    #('NSGetSizeAndAlignment', 1):   'objc._C_OUT',
    #('NSGetSizeAndAlignment', 2):   'objc._C_OUT',
    #('NSDivideRect', 1):            'objc._C_OUT',
    #('NSDivideRect', 2):            'objc._C_OUT',
    #('NSJavaClassesFromPath', 3):   'objc._C_OUT',
    #('NSJavaClassesForBundle', 2):  'objc._C_OUT',
}

def argument_kind(name, idx, nm, tp):
    try:
        return _ARGUMENT_KINDS[(name, idx)]
    except KeyError:
        #if name.startswith('NSDecimal'):
        #    return 'objc._C_OUT'
        return None

def should_create_struct_wrapper(name, fieldnames, fieldtypes):
    #if name == 'NSDecimal':
    #    # NSDecimal is wrapped using a custom wrapper, to give
    #    # it a full set of numeric methods.
    #    return False

    return True


# Items that should not be wrapped. The key is the C object that shouldn't
# be wrapped, the value should describe why it isn't wrapped.
IGNORES={
    u'kCFAllocatorUseContext': "Not valid for CFTypeID() for some reason",
}
