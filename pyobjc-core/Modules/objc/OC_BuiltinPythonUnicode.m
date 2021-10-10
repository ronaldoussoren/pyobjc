#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

@implementation OC_BuiltinPythonUnicode

+ (BOOL)supportsSecureCoding
{
    return YES;
}

- (Class _Nullable)classForKeyedArchiver
{
    return [OC_BuiltinPythonUnicode class];
}

+ (NSArray*)classFallbacksForKeyedArchiver
{
    return [NSArray arrayWithObjects:@"OC_PythonString", @"NSString", nil];
}

@end

NS_ASSUME_NONNULL_END
