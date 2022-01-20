#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

@implementation OC_BuiltinPythonDate

+ (BOOL)supportsSecureCoding
{
    return YES;
}

+ (NSArray*)classFallbacksForKeyedArchiver
{
    return [NSArray arrayWithObjects:@"OC_PythonDate", @"NSDate", nil];
}

@end

NS_ASSUME_NONNULL_END
