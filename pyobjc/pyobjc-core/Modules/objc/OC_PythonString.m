#include "pyobjc.h"

#if PY_MAJOR_VERSION == 2
#import "OC_PythonString.h"

@implementation OC_PythonString 

+ stringWithPythonObject:(PyObject*)v;
{
	OC_PythonString* res;

	res = [[OC_PythonString alloc] initWithPythonObject:v];
	[res autorelease];
	return res;
}

- initWithPythonObject:(PyObject*)v;
{
	Py_INCREF(v);
	Py_XDECREF(value);
	value = v;
	return self;
}

-(PyObject*)__pyobjc_PythonObject__
{
	Py_INCREF(value);
	return value;
}

-(PyObject*)__pyobjc_PythonTransient__:(int*)cookie
{
	*cookie = 0;
	Py_INCREF(value);
	return value;
}


-(void)release
{
	/* See comment in OC_PythonUnicode */
	PyObjC_BEGIN_WITH_GIL
		[super release];
	PyObjC_END_WITH_GIL
}
        


-(void)dealloc
{
	PyObjC_BEGIN_WITH_GIL
		PyObjC_UnregisterObjCProxy(value, self);
		[realObject release];
		Py_XDECREF(value);
	PyObjC_END_WITH_GIL

	[super dealloc];
}

-(id)__realObject__
{
	static int supportsNoCopy = -1;
	if (supportsNoCopy == -1) {
		supportsNoCopy = (int)[NSString instancesRespondToSelector:@selector(initWithBytesNoCopy:length:encoding:freeWhenDone:)];
	}
	if (!realObject) {
#if defined(__LP64__) || MAC_OS_X_VERSION_MIN_REQUIRED >= MAC_OS_X_VERSION_10_3
		/* This sucks big-time: +defaultCStringEncoding is not necessarily 
		 * related to the system encoding. The code below tries to
		 * compensate...
		 */
		NSStringEncoding encoding = [NSString defaultCStringEncoding];
		const char* pycoding = PyUnicode_GetDefaultEncoding();
		if (strcmp(pycoding, "ascii") == 0) {
			encoding = NSASCIIStringEncoding;
		} else if (strcmp(pycoding, "utf-8") == 0) {
			encoding = NSUTF8StringEncoding;
		} else if (strcmp(pycoding, "latin1") == 0) {
			encoding = NSISOLatin1StringEncoding;
		} else if (strcmp(pycoding, "macroman") == 0) {
			encoding = NSMacOSRomanStringEncoding;
		} else {
			/* A very non-standard system encoding, use
			 * whatever Cocoa believes to be the encoding.
			 */
		}


		realObject = [[NSString alloc]
			initWithBytesNoCopy:PyString_AS_STRING(value)
			length:(NSUInteger)PyString_GET_SIZE(value)
			encoding:encoding
			freeWhenDone:NO];

#else
		if (supportsNoCopy) {
			// Mac OS X 10.3+
			realObject = [[NSString alloc]
				initWithBytesNoCopy:PyString_AS_STRING(value)
				length:(NSUInteger)PyString_GET_SIZE(value)
				encoding:[NSString defaultCStringEncoding]
				freeWhenDone:NO];
		} else {
			// Mac OS X 10.2
			realObject = [[NSString alloc]
				initWithBytes:PyString_AS_STRING(value)
				length:(NSUInteger)PyString_GET_SIZE(value)
				encoding:[NSString defaultCStringEncoding]];
		}
#endif
	}
	return realObject;
}

-(NSUInteger)length
{
	return [((NSString *)[self __realObject__]) length];
}

-(unichar)characterAtIndex:(NSUInteger)anIndex
{
	return [((NSString *)[self __realObject__]) characterAtIndex:anIndex];
}

-(void)getCharacters:(unichar *)buffer range:(NSRange)aRange
{
	[((NSString *)[self __realObject__]) getCharacters:buffer range:aRange];
}


- (id)initWithCharactersNoCopy:(unichar *)characters 
			length:(NSUInteger)length 
		  freeWhenDone:(BOOL)flag
{
#ifndef PyObjC_UNICODE_FAST_PATH
# error "Wide UNICODE builds are not supported at the moment"
#endif
	PyObjC_BEGIN_WITH_GIL
		PyObject* v;
		v = PyUnicode_FromUnicode((Py_UNICODE*)characters, length);
		if (v == NULL) {
			PyObjC_GIL_FORWARD_EXC();
		}

		value = PyUnicode_AsEncodedString(v, NULL, NULL);
		Py_DECREF(v);
		if (value == NULL) {
			PyObjC_GIL_FORWARD_EXC();
		}

		PyString_InternInPlace(&value);

	PyObjC_END_WITH_GIL;
	if (flag) {
		free(characters);
	}
	return self;
}

-initWithBytes:(void*)bytes length:(NSUInteger)length encoding:(NSStringEncoding)encoding
{
	NSString* tmpval = [[NSString alloc] initWithBytes:bytes length:length encoding:encoding];

	PyObjC_BEGIN_WITH_GIL
		value = PyString_FromString([tmpval UTF8String]);
		if (value == NULL) {
			PyObjC_GIL_FORWARD_EXC();
		}
		PyString_InternInPlace(&value);

	PyObjC_END_WITH_GIL

	[tmpval release];
	return self;
}




/* 
 * Helper method for initWithCoder, needed to deal with
 * recursive objects (e.g. o.value = o)
 */
-(void)pyobjcSetValue:(NSObject*)other
{
	PyObject* v = PyObjC_IdToPython(other);
	Py_XDECREF(value);
	value = v;
}

- initWithCoder:(NSCoder*)coder
{
	int v;
	
	if ([coder allowsKeyedCoding]) {
		v = [coder decodeInt32ForKey:@"pytype"];
	} else {
		[coder decodeValueOfObjCType:@encode(int) at:&v];
	}
	if (v == 1) {
		[super initWithCoder:coder];
	} else if (v == 2) {

		if (PyObjC_Decoder != NULL) {
			PyObjC_BEGIN_WITH_GIL
				PyObject* cdr = PyObjC_IdToPython(coder);
				if (cdr == NULL) {
					PyObjC_GIL_FORWARD_EXC();
				}

				PyObject* setValue;
				PyObject* selfAsPython = PyObjCObject_New(self, 0, YES);
				setValue = PyObject_GetAttrString(selfAsPython, "pyobjcSetValue_");

				PyObject* v2 = PyObject_CallFunction(PyObjC_Decoder, "OO", cdr, setValue);
				Py_DECREF(cdr);
				Py_DECREF(setValue);
				Py_DECREF(selfAsPython);

				if (v2 == NULL) {
					PyObjC_GIL_FORWARD_EXC();
				}

				Py_XDECREF(value);
				value = v2;

				NSObject* proxy = PyObjC_FindObjCProxy(value);
				if (proxy == NULL) {
					PyObjC_RegisterObjCProxy(value, self);
				} else {
					[self release];
					[proxy retain];
					self = (OC_PythonString*)proxy;
				}


			PyObjC_END_WITH_GIL

			return self;

		} else {
			[NSException raise:NSInvalidArgumentException
					format:@"decoding Python objects is not supported"];
			return nil;

		}

	} else {
		[NSException raise:NSInvalidArgumentException
				format:@"encoding Python objects is not supported"];
	}
	return self;
}

-(void)encodeWithCoder:(NSCoder*)coder
{
	if (PyString_CheckExact(value)) {
		if ([coder allowsKeyedCoding]) {
			[coder encodeInt32:1 forKey:@"pytype"];
		} else {
			int v = 1;
			[coder encodeValueOfObjCType:@encode(int) at:&v];
		}
		[super encodeWithCoder:coder];
	} else {
		if ([coder allowsKeyedCoding]) {
			[coder encodeInt32:2 forKey:@"pytype"];
		} else {
			int v = 2;
			[coder encodeValueOfObjCType:@encode(int) at:&v];
		}

		PyObjC_encodeWithCoder(value, coder);

	}
}

#if 1
-(NSObject*)replacementObjectForArchiver:(NSArchiver*)archiver 
{
	(void)(archiver);
	return self;
}

-(NSObject*)replacementObjectForKeyedArchiver:(NSKeyedArchiver*)archiver
{
	(void)(archiver);
	return self;
}

-(NSObject*)replacementObjectForCoder:(NSCoder*)archiver
{
	(void)(archiver);
	return self;
}

-(NSObject*)replacementObjectForPortCoder:(NSPortCoder*)archiver
{
	(void)(archiver);
	return self;
}

-(Class)classForArchiver
{
	return [OC_PythonString class];
}

-(Class)classForKeyedArchiver
{
	return [OC_PythonString class];
}

-(Class)classForCoder
{
	return [OC_PythonString class];
}

-(Class)classForPortCoder
{
	return [OC_PythonString class];
}

/* Ensure that we can be unarchived as a generic string by pure ObjC
 * code.
 */
+classFallbacksForKeyedArchiver
{
	return [NSArray arrayWithObject:@"NSString"];
}
#endif

@end /* implementation OC_PythonString */

#endif /* !Py3k */
