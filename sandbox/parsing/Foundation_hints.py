#
# Scanframework hints for the framework 'Foundation'
#
# See scanframework.py for a description of the contents of this file.
#
ADDITIONAL_IMPORTS=(
    '_Foundation',
)

# Some headers that are not picked up by the default scanner
ADDITIONAL_HEADERS=(
    'NSDebug.h',
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

FOOTER="""\

def NSMakePoint(x, y):
    return NSPoint(x, y)

def NSMakeSize(w, h):
    return NSSize(w, h)

def NSMakeRect(x, y, w, h):
    return NSRect(NSPoint(x, y), NSSize(w, h))

def NSMakeRange(loc, len):
    return NSRange(loc, len)

# These function use indexes instead of attribute
# access because users might pass in tuples instead of
# NSRect instances. Both are supported.

def NSMaxX(aRect):
    '''float NSMaxX(NSRect aRect)'''
    return aRect[0][0] + aRect[1][0]

def NSMaxY(aRect):
    '''float NSMaxY(NSRect aRect)'''
    return aRect[0][1] + aRect[1][1]

def NSMidX(aRect):
    '''float NSMidX(NSRect aRect)'''
    return aRect[0][0] + aRect[1][0] / 2.0

def NSMidY(aRect):
    '''float NSMidY(NSRect aRect)'''
    return aRect[0][1] + aRect[1][1] / 2.0 

def NSMinX(aRect):
    '''float NSMinX(NSRect aRect)'''
    return aRect[0][0]

def NSMinY(aRect):
    '''float NSMinY(NSRect aRect)'''
    return aRect[0][1]

def NSWidth(aRect):
    '''float NSWidth(NSRect aRect);'''
    return aRect[1][0]

def NSHeight(aRect):
    '''float NSHeight(NSRect aRect); '''
    return aRect[0][1]

def NSMaxRange(range):
    '''unsigned int NSMaxRange(NSRange range);'''
    return range[0] + range[1]

def NSLocationInRange(loc, range):
    '''BOOL NSLocationInRange(unsigned int loc, NSRange range)'''
    return loc - range[0] < range[1]

def NSEqualRanges(range1, range2):
    '''BOOL NSEqualRanges(NSRange range1, NSRange range2)'''
    return range1[0] == range2[0] and range1[1] == range2[1]

# NSByteOrder.h
NSHostByteOrder = CFByteOrderGetCurrent
NSSwapShort = CFSwapInt16
NSSwapInt = CFSwapInt32
NSSwapLong = CFSwapInt32
NSSwapLongLong = CFSwapInt64
NSSwapBigShortToHost = CFSwapInt16BigToHost
NSSwapBigLongLongToHost = CFSwapInt64BigToHost
NSSwapHostShortToBig = CFSwapInt16HostToBig
NSSwapHostIntToBig = CFSwapInt32HostToBig
NSSwapHostLongToBig = CFSwapInt32HostToBig
NSSwapHostLongLongToBig = CFSwapInt64HostToBig
NSSwapLittleShortToHost = CFSwapInt16LittleToHost
NSSwapLittleIntToHost = CFSwapInt32LittleToHost
NSSwapLittleLongToHost = CFSwapInt32LittleToHost
NSSwapLittleLongLongToHost = CFSwapInt64LittleToHost
NSSwapHostShortToLittle = CFSwapInt16HostToLittle
NSSwapHostIntToLittle = CFSwapInt32HostToLittle
NSSwapHostLongToLittle = CFSwapInt32HostToLittle
NSSwapHostLongLongToLittle = CFSwapInt64HostToLittle

"""


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


    'NSMakePoint':      'static inine, wrapped by hand',
    'NSMakeSize':       'static inline, wrapped by hand',
    'NSMakeRect':       'static inline, wrapped by hand',
    'NSMakeRange':      'static inline, wrapped by hand',
    'NSMaxX':           'static inline, wrapped by hand',
    'NSMaxY':           'static inline, wrapped by hand',
    'NSMidX':           'static inline, wrapped by hand',
    'NSMidY':           'static inline, wrapped by hand',
    'NSMinX':           'static inline, wrapped by hand',
    'NSMinY':           'static inline, wrapped by hand',
    'NSWidth':          'static inline, wrapped by hand',
    'NSHeight':         'static inline, wrapped by hand',
    'NSMaxRange':       'static inline, wrapped by hand',
    'NSLocationInRange':'static inline, wrapped by hand',
    'NSEqualRanges':    'static inline, wrapped by hand',

    'NSHostByteOrder':              'static inline function alias',
    'NSSwapShort':                  'static inline function alias',
    'NSSwapInt':                    'static inline function alias',
    'NSSwapLong':                   'static inline function alias',
    'NSSwapLongLong':               'static inline function alias',
    'NSSwapBigShortToHost':         'static inline function alias',
    'NSSwapBigLongLongToHost':      'static inline function alias',
    'NSSwapHostShortToBig':         'static inline function alias',
    'NSSwapHostIntToBig':           'static inline function alias',
    'NSSwapHostLongToBig':          'static inline function alias',
    'NSSwapHostLongLongToBig':      'static inline function alias',
    'NSSwapLittleShortToHost':      'static inline function alias',
    'NSSwapLittleIntToHost':        'static inline function alias',
    'NSSwapLittleLongToHost':       'static inline function alias',
    'NSSwapLittleLongLongToHost':   'static inline function alias',
    'NSSwapHostShortToLittle':      'static inline function alias',
    'NSSwapHostIntToLittle':        'static inline function alias',
    'NSSwapHostLongToLittle':       'static inline function alias',
    'NSSwapHostLongLongToLittle':   'static inline function alias',
}
