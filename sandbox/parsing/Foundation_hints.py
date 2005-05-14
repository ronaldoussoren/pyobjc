#
# Scanframework hints for the framework 'Foundation'
#
# See scanframework.py for a description of the contents of this file.
#
ADDITIONAL_IMPORTS=(
    '_Foundation',
)

_ARGUMENT_KINDS={
    ('NSGetSizeAndAlignment', 1):   'objc._C_OUT',
    ('NSGetSizeAndAlignment', 2):   'objc._C_OUT',
    ('NSDivideRect', 1):            'objc._C_OUT',
    ('NSDivideRect', 2):            'objc._C_OUT',
    ('NSJavaClassesFromPath', 3):   'objc._C_OUT',
    ('NSJavaClassesForBundle', 2):  'objc._C_OUT',
}

def argument_kind(name, idx, nm, tp):
    try:
        return _ARGUMENT_KINDS[(name, idx)]
    except KeyError:
        if name.startswith('NSDecimal'):
            return 'objc._C_OUT'
        return None

def should_create_struct_wrapper(name, fieldnames, fieldtypes):
    if name == 'NSDecimal':
        # NSDecimal is wrapped using a custom wrapper, to give
        # it a full set of numeric methods.
        return False

    return True


# Items that should not be wrapped. The key is the C object that shouldn't
# be wrapped, the value should describe why it isn't wrapped.
IGNORES={
    'NSLogv': 'Varargs function, manually wrapped',
    'NSLog':  'Varargs function, manually wrapped',

    # If these turn out to be useful after all we should write a custom
    # buffer-like type to represent memory.
    'NSZoneFromPointer': 'Memory management, not useful in Python',
    'NSZoneCalloc':      'Memory management, not useful in Python',
    'NSZoneMalloc':      'Memory management, not useful in Python',
    'NSZoneRealloc':     'Memory management, not useful in Python',
    'NSZoneFree':        'Memory management, not useful in Python',
    'NSAllocateMemoryPages':   'More memory management',
    'NSDeallocateMemoryPages': 'More memory management',
    'NSCopyMemoryPages':       'More memory management',
    'NSAllocateCollectable':    'Yet more memory management',
    'NSReallocateCollectable':  'Yet more memory management',

    # Low-level exception handing, these are not useful in python
    'NSGetUncaughtExceptionHandler': 'Low-level exception handling',
    'NSSetUncaughtExceptionHandler': 'Low-level exception handling',

    # Hashtables use callback functions and are not used in the highlevel
    # API's. 
    'NSCreateHashTableWithZone':            'NSHashtable are like dicts',
    'NSCreateHashTable':                    'NSHashtable are like dicts',
    'NSHashGet':                            'NSHashtable are like dicts',
    'NSHashInsert':                         'NSHashtable are like dicts',
    'NSHashInsertKnownAbsent':              'NSHashtable are like dicts',
    'NSHashInsertIfAbsent':                 'NSHashtable are like dicts',
    'NSHashRemove':                         'NSHashtable are like dicts',
    'NSEnumerateHashTable':                 'NSHashtable are like dicts',
    'NSNextHashEnumeratorItem':             'NSHashtable are like dicts',
    'NSEndHashTableEnumeration':            'NSHashtable are like dicts',
    'NSIntHashCallBacks':                   'NSHashtable are like dicts',
    'NSNonOwnedPointerHashCallBacks':       'NSHashtable are like dicts',
    'NSNonRetainedObjectHashCallBacks':     'NSHashtable are like dicts',
    'NSObjectHashCallBacks':                'NSHashtable are like dicts',
    'NSOwnedObjectIdentityHashCallBacks':   'NSHashtable are like dicts',
    'NSOwnedPointerHashCallBacks':          'NSHashtable are like dicts',
    'NSPointerToStructHashCallBacks':       'NSHashtable are like dicts',

    # Maptables use callback functions and are not used in the highlevel
    # API's.
    'NSCreateMapTableWithZone':             'NSMaptables are like dicts',
    'NSCreateMapTable':                     'NSMaptables are like dicts',
    'NSMapMember':                          'NSMaptables are like dicts',
    'NSMapGet':                             'NSMaptables are like dicts',
    'NSMapInsert':                          'NSMaptables are like dicts',
    'NSMapInsertKnownAbsent':               'NSMaptables are like dicts',
    'NSMapInsertIfAbsent':                  'NSMaptables are like dicts',
    'NSMapRemove':                          'NSMaptables are like dicts',
    'NSEnumerateMapTable':                  'NSMaptables are like dicts',
    'NSNextMapEnumeratorPair':              'NSMaptables are like dicts',
    'NSEndMapTableEnumeration':             'NSMaptables are like dicts',
    'NSIntMapKeyCallBacks':                 'NSMaptables are like dicts',
    'NSNonOwnedPointerMapKeyCallBacks':     'NSMaptables are like dicts',
    'NSNonOwnedPointerOrNullMapKeyCallBacks': 'NSMaptables are like dicts',
    'NSNonRetainedObjectMapKeyCallBacks':   'NSMaptables are like dicts',
    'NSObjectMapKeyCallBacks':              'NSMaptables are like dicts',
    'NSOwnedPointerMapKeyCallBacks':        'NSMaptables are like dicts',
    'NSIntMapValueCallBacks':               'NSMaptables are like dicts',
    'NSNonOwnedPointerMapValueCallBacks':   'NSMaptables are like dicts',
    'NSNonRetainedObjectMapValueCallBacks': 'NSMaptables are like dicts',
    'NSOwnedPointerMapValueCallBacks':      'NSMaptables are like dicts',
}
