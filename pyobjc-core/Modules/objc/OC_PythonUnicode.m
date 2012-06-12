#include "pyobjc.h"
#import "OC_PythonUnicode.h"

@implementation OC_PythonUnicode 

+ unicodeWithPythonObject:(PyObject*)v
{
	OC_PythonUnicode* res;

	res = [[OC_PythonUnicode alloc] initWithPythonObject:v];
	[res autorelease];
	return res;
}

- initWithPythonObject:(PyObject*)v
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



-(BOOL)supportsWeakPointers { return YES; }

-(oneway void)release
{
	/* There is small race condition when an object is almost deallocated
	 * in one thread and fetched from the registration mapping in another
	 * thread. If we don't get the GIL this object might get a -dealloc
	 * message just as the other thread is fetching us from the mapping.
	 * That's why we need to grab the GIL here (getting it in dealloc is
	 * too late, we'd already be dead).
	 */
	/* FIXME: it should be possible to grab the lock only when really
	 * needed, but the test below isn't good enough. Be heavy handed to
	 * make sure we're right, rather than crashing sometimes anyway.
	 */
	/* FIXME2: in rare occasions we're trying to acquire the GIL during 
	 * shutdown and if we're very unlucky this can happen after the 
	 * GILState machinery has shut down...
	 */
	/* FIXME3: Should switch to __weak on OSX 10.7 or later, that should
	 * fix this issue without a performance penalty.
	 */
	PyObjC_BEGIN_WITH_GIL
		[super release];
	PyObjC_END_WITH_GIL
}

-(void)dealloc
{
	PyObjC_BEGIN_WITH_GIL
		PyObjC_UnregisterObjCProxy(value, self);
#ifndef PyObjC_UNICODE_FAST_PATH
		[realObject release];
#endif /* !PyObjC_UNICODE_FAST_PATH */
		Py_XDECREF(value);
	PyObjC_END_WITH_GIL

	[super dealloc];
}

#ifdef PyObjC_UNICODE_FAST_PATH

-(NSUInteger)length
{
	return (NSUInteger)PyUnicode_GET_SIZE(value);
}

-(unichar)characterAtIndex:(NSUInteger)anIndex
{
	Py_ssize_t offset;
	if (anIndex > PY_SSIZE_T_MAX) {
		[NSException raise:@"NSRangeException" format:@"Range or index out of bounds"];
	}
	if (anIndex >= (NSUInteger)PyUnicode_GET_SIZE(value)) {
		[NSException raise:@"NSRangeException" format:@"Range or index out of bounds"];
	}

	offset = (Py_ssize_t)anIndex;
	unichar ch = PyUnicode_AS_UNICODE(value)[offset];
	return ch;
}

-(void)getCharacters:(unichar *)buffer range:(NSRange)aRange
{
	Py_ssize_t offset;
	size_t length;

	if (aRange.location + aRange.length > (NSUInteger)PyUnicode_GET_SIZE(value)) {
		[NSException raise:@"NSRangeException" format:@"Range or index out of bounds"];
	}

	offset = (Py_ssize_t)(aRange.location);
	length = (size_t)aRange.length;

	memcpy(buffer, 
	       (PyUnicode_AS_UNICODE(value)) + offset,
	       2 * length);
}

#else /* !PyObjC_UNICODE_FAST_PATH */

-(id)__realObject__
{
	if (!realObject) {
		PyObjC_BEGIN_WITH_GIL
			PyObject* utf8 = PyUnicode_AsUTF8String(value);
			if (!utf8) {
				NSLog(@"failed to encode unicode string to byte string");
				PyErr_Clear();
			} else {
				realObject = [[NSString alloc]
					initWithBytes:PyBytes_AS_STRING(utf8)
					       length:(NSUInteger)PyBytes_GET_SIZE(utf8)
					     encoding:NSUTF8StringEncoding];
				Py_DECREF(utf8);
			}
		PyObjC_END_WITH_GIL
	}
	return realObject;
}
	
-(NSUInteger)length
{
	return [((NSString *)[self __realObject__]) length];
}

-(unichar)characterAtIndex:(NSUInteger)anIndex
{

	unichar ch = [((NSString *)[self __realObject__]) characterAtIndex:anIndex];
	return ch;
}

-(void)getCharacters:(unichar *)buffer range:(NSRange)aRange
{
	[((NSString *)[self __realObject__]) getCharacters:buffer range:aRange];
}

#endif /* PyObjC_UNICODE_FAST_PATH */

/*
 * NSCoding support 
 *
 * We need explicit NSCoding support to get full fidelity, otherwise we'll
 * get archived as generic NSStrings.
 */
- (id)initWithCharactersNoCopy:(unichar *)characters 
			length:(NSUInteger)length 
		  freeWhenDone:(BOOL)flag
{
	int byteorder = 0;
	PyObjC_BEGIN_WITH_GIL
		/* Decode as a UTF-16 string in native byteorder */
		value = PyUnicode_DecodeUTF16(
				(const char*)characters,
				length * 2,
				NULL,
				&byteorder); 
		if (value == NULL) {
			PyObjC_GIL_FORWARD_EXC();
		}

	PyObjC_END_WITH_GIL;
	if (flag) {
		free(characters);
	}
	return self;
}

-initWithBytes:(void*)bytes length:(NSUInteger)length encoding:(NSStringEncoding)encoding
{
	char* py_encoding = NULL;
	int byteorder = 0;

	/* Detect some often used single-byte encodings that can be created in Python without
	 * creating an intermediate object.
	 */

	switch (encoding) {
	case NSASCIIStringEncoding: py_encoding = "ascii"; break;
	case NSUTF8StringEncoding: py_encoding = "UTF-8"; break;
	case NSISOLatin1StringEncoding: py_encoding = "latin1"; break;
	}

	if (py_encoding != NULL) {
		PyObjC_BEGIN_WITH_GIL
			value = PyUnicode_Decode(bytes, length, py_encoding, NULL);
			if (value == NULL) {
				PyObjC_GIL_FORWARD_EXC();
			}
		PyObjC_END_WITH_GIL
		return self;
	}

	/* UTF-16 encodings can also be decoded without an intermediate object */
	byteorder = 2;
	switch (encoding) {
	case NSASCIIStringEncoding: byteorder = 0; break;
	case NSUTF8StringEncoding:  byteorder = -1; break;
	case NSISOLatin1StringEncoding:  byteorder = 1; break;
	}
	if (byteorder != 2) {
		PyObjC_BEGIN_WITH_GIL
			/* Decode as a UTF-16 string in native byteorder */
			value = PyUnicode_DecodeUTF16(
					bytes,
					length,
					NULL,
					&byteorder); 
			if (value == NULL) {
				PyObjC_GIL_FORWARD_EXC();
			}

		PyObjC_END_WITH_GIL;
		return self;
	}

	/* And finally: first use the Cocoa decoder to create an NSString, copy the unichars into
	 * a temporary buffer and use that to create a Python unicode string using the UTF16 decoder.
	 *
	 * This can be slightly optimized on systems where sizeof(Py_UNICODE) == sizeof(unichar), but
	 * that's not worth the additional complexity and won't work on Python 3.3 or later anyway.
	 */

	NSString* tmpval = [[NSString alloc] initWithBytes:bytes length:length encoding:encoding];
	Py_ssize_t charcount = [tmpval length];

	/* NOTE: the malloc() call can be avoided when sizeof(unichar) == sizeof(Py_UNICODE) and
	 * we're on python 3.2 or earlier. That's not worth the added complexity.
	 */
	unichar* chars = malloc(charcount*2);

	if (chars == NULL) {
		[self release];
		return nil;
	}
	[tmpval getCharacters:chars];
	[tmpval release];

	PyObjC_BEGIN_WITH_GIL
		/* Decode as a UTF-16 string in native byteorder */
		byteorder = 0;
		value = PyUnicode_DecodeUTF16(
				(const char*)chars,
				length * 2,
				NULL,
				&byteorder); 
		free(chars);
		if (value == NULL) {
			PyObjC_GIL_FORWARD_EXC();
		}

	PyObjC_END_WITH_GIL;
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
	int ver;
	if ([coder allowsKeyedCoding]) {
		ver = [coder decodeInt32ForKey:@"pytype"];
	} else {
		[coder decodeValueOfObjCType:@encode(int) at:&ver];
	}
	if (ver == 1) {
		self = [super initWithCoder:coder];
		return self;
	} else if (ver == 2) {

		if (PyObjC_Decoder != NULL) {
			PyObjC_BEGIN_WITH_GIL
				PyObject* cdr = PyObjC_IdToPython(coder);
				if (cdr == NULL) {
					PyObjC_GIL_FORWARD_EXC();
				}

				PyObject* setValue;
				PyObject* selfAsPython = PyObjCObject_New(self, 0, YES);
				setValue = PyObject_GetAttrString(selfAsPython, "pyobjcSetValue_");

				PyObject* v = PyObject_CallFunction(PyObjC_Decoder, "OO", cdr, setValue);
				Py_DECREF(cdr);
				Py_DECREF(setValue);
				Py_DECREF(selfAsPython);

				if (v == NULL) {
					PyObjC_GIL_FORWARD_EXC();
				}

				Py_XDECREF(value);
				value = v;

				NSObject* proxy = PyObjC_FindObjCProxy(value);
				if (proxy == NULL) {
					PyObjC_RegisterObjCProxy(value, self);
				} else {
					[self release];
					[proxy retain];
					self = (OC_PythonUnicode*)proxy;
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
		return nil;
	}
}

-(void)encodeWithCoder:(NSCoder*)coder
{
	if (PyUnicode_CheckExact(value)) {
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
	return [OC_PythonUnicode class];
}

-(Class)classForKeyedArchiver
{
	return [OC_PythonUnicode class];
}

-(Class)classForCoder
{
	return [OC_PythonUnicode class];
}

-(Class)classForPortCoder
{
	return [OC_PythonUnicode class];
}

/* Ensure that we can be unarchived as a generic string by pure ObjC
 * code.
 */
+classFallbacksForKeyedArchiver
{
	return [NSArray arrayWithObject:@"NSString"];
}

#endif

@end /* implementation OC_PythonUnicode */
