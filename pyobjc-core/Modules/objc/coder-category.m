/*
 * This defines a category that is used by the
 * NSCoding support code. All of these methods
 * are private, for PyObjC users the NSCoding
 * wrappers in pyobjc-framework-Cocoa work just
 * fine but we cannot use that in this package
 * to avoid creating circular dependencies.
 */
#import <Foundation/Foundation.h>

@implementation NSCoder (pyobjc)

-(void)__pyobjc__encodeInt:(int)value
{
	[self encodeValueOfObjCType:"i" at:&value];
}

-(void)__pyobjc__encodeInt32:(int)value
{
	[self encodeValueOfObjCType:"i" at:&value];
}

-(void)__pyobjc__encodeInt64:(long long)value
{
	[self encodeValueOfObjCType:"q" at:&value];
}

-(void)__pyobjc__encodeBool:(bool)value
{
	[self encodeValueOfObjCType:"b" at:&value];
}

-(int)__pyobjc__decodeInt
{
	int value;
	[self decodeValueOfObjCType:"i" at:&value];
	return value;
}

-(int)__pyobjc__decodeInt32
{
	int value;
	[self decodeValueOfObjCType:"i" at:&value];
	return value;
}

-(long long)__pyobjc__decodeInt64
{
	long long value;
	[self decodeValueOfObjCType:"q" at:&value];
	return value;
}

-(bool)__pyobjc__decodeBool
{
	bool value;
	[self decodeValueOfObjCType:"b" at:&value];
	return value;
}

@end
