#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

@implementation OC_BuiltinPythonSet

+ (BOOL)supportsSecureCoding
{
    return YES;
}

- (Class _Nullable)classForKeyedArchiver
{
    return [OC_BuiltinPythonSet class];
}

+ (NSArray*)classFallbacksForKeyedArchiver
{
    return [NSArray arrayWithObjects:@"OC_PythonSet", @"NSSet", nil];
}

@end

NS_ASSUME_NONNULL_END
