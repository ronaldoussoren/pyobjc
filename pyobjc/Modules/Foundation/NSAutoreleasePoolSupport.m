/*
 * *** DEPRECATED ***
 * 
 * A category for working with NSAutoreleasePools. This was needed when 
 * PyObjC couldn't be used to create autoreleasepools in the regular way,
 * that is no longer a problem.
 */
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
	NSAutoreleasePool *p;
	PyGILState_STATE state;

	state = PyGILState_Ensure();
	PyErr_Warn(PyExc_DeprecationWarning, 
		"NSAutoreleasePool.pyobjcPushPool() is deprecated: Use NSAutoreleasePool.alloc().init() instead");
	if (PyErr_Occurred()) {
		PyObjCErr_ToObjCWithGILState(&state);
	}
	PyGILState_Release(state);

	p = [[NSAutoreleasePool alloc] init];

	[[self pyobjcPoolStackForCurrentThread] addObject: [NSValue valueWithNonretainedObject: p]];
}

+ (void) pyobjcPopPool
{
	NSMutableArray *poolStack = [self pyobjcPoolStackForCurrentThread];
	NSValue *pValue = [poolStack lastObject];
	[[pValue nonretainedObjectValue] release];
	[poolStack removeLastObject];
}
@end
