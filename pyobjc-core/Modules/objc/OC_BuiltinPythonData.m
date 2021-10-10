#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

@implementation OC_BuiltinPythonData

+ (BOOL)supportsSecureCoding
{
    return YES;
}

- (Class _Nullable)classForKeyedArchiver
{
    return [OC_BuiltinPythonData class];
}

+ (NSArray*)classFallbacksForKeyedArchiver
{
    return [NSArray arrayWithObjects:@"OC_PythonData", @"NSData", nil];
}

@end

NS_ASSUME_NONNULL_END
