#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

@implementation OC_BuiltinPythonArray

+ (BOOL)supportsSecureCoding
{
    return YES;
}

- (Class _Nullable)classForKeyedArchiver
{
    return [OC_BuiltinPythonArray class];
}

+ (NSArray*)classFallbacksForKeyedArchiver
{
    return [NSArray arrayWithObjects:@"OC_PythonArray", @"NSArray", nil];
}

@end

NS_ASSUME_NONNULL_END
