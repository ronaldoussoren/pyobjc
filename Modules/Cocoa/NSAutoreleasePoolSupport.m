#import <Foundation/Foundation.h>

static NSString *_threadPoolIdentifier = @"PyObjC:  NSThread AutoreleasePool Identifier.";

@interface NSAutoreleasePool(PyObjCPushPopSupport)
@end
@implementation NSAutoreleasePool (PyObjCPushPopSupport)
+ (NSMutableArray *) pyobjcPoolStackForCurrentThread
{
  NSMutableDictionary *threadDictionary = [[NSThread currentThread] threadDictionary];
  NSMutableArray *poolStack;

  poolStack = [threadDictionary objectForKey: _threadPoolIdentifier];
  if (!poolStack) {
    poolStack = [NSMutableArray array];
    [threadDictionary setObject: poolStack forKey: _threadPoolIdentifier];
  }

  return poolStack;
}

+ (void) pyobjcPushPool
{
  NSAutoreleasePool *p = [[NSAutoreleasePool alloc] init];
  [[self pyobjcPoolStackForCurrentThread] addObject: [NSValue valueWithNonretainedObject: p]];
}

+ (void) pyobjcPopPool
{
  NSMutableArray *poolStack = [self pyobjcPoolStackForCurrentThread];
  NSAutoreleasePool *p = [poolStack lastObject];
  [p release];
  [poolStack removeLastObject];
}
@end
