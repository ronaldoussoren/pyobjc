#include "pyobjc.h"

#if PY_MAJOR_VERSION == 2

@implementation OC_BuiltinPythonString

+ (BOOL)supportsSecureCoding {
    return YES;
}

-(Class)classForKeyedArchiver
{
    return [OC_BuiltinPythonString class];
}

+(NSArray*)classFallbacksForKeyedArchiver
{
    return [NSArray arrayWithObjects:@"OC_PythonString", @"NSString", nil];
}

@end

#endif /* !Py3k */
