#import <Foundation/Foundation.h>

static NSMutableArray *_poolStack;

@interface NSAutoreleasePool(PyObjCPushPopSupport)
@end
@implementation NSAutoreleasePool (PyObjCPushPopSupport)
+ (void) load
{
  _poolStack = [[NSMutableArray alloc] init];
}

+ (void) pyobjcPushPool
{
  NSAutoreleasePool *p = [[NSAutoreleasePool alloc] init];
  [_poolStack addObject: [NSValue valueWithNonretainedObject: p]];
}

+ (void) pyobjcPopPool
{
  NSAutoreleasePool *p = [_poolStack lastObject];
  [p release];
  [_poolStack removeLastObject];
}
@end
