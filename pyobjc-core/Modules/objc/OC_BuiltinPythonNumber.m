#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

@implementation OC_BuiltinPythonNumber

+ (BOOL)supportsSecureCoding
{
    return YES;
}

+ (NSArray*)classFallbacksForKeyedArchiver
{
    return [NSArray arrayWithObjects:@"OC_PythonNumber", @"NSNumber", nil];
}

@end

NS_ASSUME_NONNULL_END
