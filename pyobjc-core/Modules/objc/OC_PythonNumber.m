#include "pyobjc.h"

@implementation OC_PythonNumber

+ (instancetype)numberWithPythonObject:(PyObject*)v
{
	OC_PythonNumber* res;

	res = [[OC_PythonNumber alloc] initWithPythonObject:v];
	[res autorelease];
	return res;
}

- (id)initWithPythonObject:(PyObject*)v
{
	self = [super init];
	if (unlikely(self == nil)) return nil;

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
	/* See comment in OC_PythonUnicode */
	PyObjC_BEGIN_WITH_GIL
		[super release];
	PyObjC_END_WITH_GIL
}

-(void)dealloc
{
	PyObjC_BEGIN_WITH_GIL
		PyObjC_UnregisterObjCProxy(value, self);
		Py_XDECREF(value);

	PyObjC_END_WITH_GIL

	[super dealloc];
}

-(const char*)objCType
{
	PyObjC_BEGIN_WITH_GIL
		if (PyBool_Check(value)) {
			PyObjC_GIL_RETURN(@encode(BOOL));
		} else if (PyFloat_Check(value)) {
			PyObjC_GIL_RETURN(@encode(double));
#if PY_MAJOR_VERSION == 2
		} else if (PyInt_Check(value)) {
			PyObjC_GIL_RETURN(@encode(long));
#endif
		} else if (PyLong_Check(value)) {
			PyObjC_GIL_RETURN(@encode(long long));
		} 
	PyObjC_END_WITH_GIL
	[NSException raise:NSInvalidArgumentException 
		    format:@"Cannot determine objective-C type of this number"];
	return @encode(char);
}

-(void)getValue:(void*)buffer
{
	const char* encoded = [self objCType];
	int r;
	PyObjC_BEGIN_WITH_GIL
		r = depythonify_c_value(encoded, value, buffer);
		if (r == -1) {
			PyObjC_GIL_FORWARD_EXC();
		}
	PyObjC_END_WITH_GIL
}

/* TODO:
-(BOOL)isEqualToValue:(NSValue*)other
  // convert other to Python, then use python's comparison operators to
  // check for equality.
}
*/


-(BOOL)boolValue
{
	return (BOOL)PyObject_IsTrue(value);
}

-(char)charValue
{
	return (char)[self longLongValue];
}

-(NSDecimal)decimalValue
{
	NSDecimal result;
	NSDecimalNumber* num;

	unsigned long long mantissa = 0;
	unsigned short exponent = 0;
	BOOL negative = NO;

	PyObjC_BEGIN_WITH_GIL
#if PY_MAJOR_VERSION == 2
		if (PyInt_Check(value)) {
			long lng = PyInt_AsLong(value);
			if (lng < 0) {
				mantissa = -lng;
				exponent = 0;
				negative = YES;
			} else {
				mantissa = lng;
				exponent = 0;
				negative = NO;
			}

		} else 
#endif
		if (PyLong_Check(value)) {
			mantissa = PyLong_AsUnsignedLongLong(value);
			if (PyErr_Occurred()) {
				long long lng;
				PyErr_Clear();
				lng = PyLong_AsLongLong(value);
				if (PyErr_Occurred()) {
					PyObjC_GIL_FORWARD_EXC();
				}

				if (lng < 0) {
					mantissa = -lng;
					exponent = 0;
					negative = YES;
				} else {
					mantissa = lng;
					exponent = 0;
					negative = NO;
				}
			} else {
				exponent = 0;
				negative = NO;
			}

		} else if (PyFloat_Check(value)) {
			PyObject* strVal = PyObject_Repr(value);
			PyObject* uniVal = NULL;

			if (strVal == NULL) {
				PyObjC_GIL_FORWARD_EXC();
			}

			uniVal = PyUnicode_FromEncodedObject(strVal, "ascii", "strict");
			Py_DECREF(strVal);
			if (uniVal == NULL) {
				PyObjC_GIL_FORWARD_EXC();
			}

			NSString* stringVal = PyObjC_PythonToId(uniVal);
			Py_DECREF(uniVal);
			
			num = [[NSDecimalNumber alloc] initWithString:stringVal];
			result = [num decimalValue];
			[num release];
			PyObjC_GIL_RETURN(result);

		} else {
			PyErr_Format(PyExc_TypeError, "cannot convert object of %s to NSDecimal",
					Py_TYPE(value)->tp_name);
			PyObjC_GIL_FORWARD_EXC();
		}

	PyObjC_END_WITH_GIL



	num = [[NSDecimalNumber alloc] 
		initWithMantissa:mantissa
			exponent:exponent
		      isNegative:negative];
	result = [num decimalValue];
	[num release];
	return result;
}

-(double)doubleValue
{
	PyObjC_BEGIN_WITH_GIL
		if (PyFloat_Check(value)) {
			PyObjC_GIL_RETURN(PyFloat_AsDouble(value));
		} 
	PyObjC_END_WITH_GIL
	return (double)[self longLongValue];
}

-(float)floatValue
{
	return (float)[self doubleValue];
}

-(NSInteger)integerValue
{
	return (NSInteger)[self longLongValue];
}

-(int)intValue
{
	return (int)[self longLongValue];
}


-(long)longValue
{
	return (long)[self longLongValue];
}

-(short)shortValue
{
	return (short)[self longLongValue];
}


-(unsigned char)unsignedCharValue
{
	return (unsigned char)[self unsignedLongLongValue];
}
-(NSUInteger)unsignedIntegerValue
{
	return (NSUInteger)[self unsignedLongLongValue];
}
-(unsigned int)unsignedIntValue
{
	return (unsigned int)[self unsignedLongLongValue];
}
-(unsigned long)unsignedLongValue
{
	return (unsigned long)[self unsignedLongLongValue];
}
-(unsigned short)unsignedShortValue
{
	return (unsigned short)[self unsignedLongLongValue];
}

-(long long)longLongValue
{
	long long result;

	PyObjC_BEGIN_WITH_GIL
#if PY_MAJOR_VERSION == 2
		if (PyInt_Check(value)) {
			result =  PyInt_AsLong(value);
			PyObjC_GIL_RETURN(result);
		} else 
#endif
		if (PyFloat_Check(value)) {
			result =  (long long)PyFloat_AsDouble(value);
			PyObjC_GIL_RETURN(result);
		} else if (PyLong_Check(value)) {
			result =  PyLong_AsUnsignedLongLongMask(value);
			PyObjC_GIL_RETURN(result);
		}
	PyObjC_END_WITH_GIL

	[NSException raise:NSInvalidArgumentException 
		    format:@"Cannot determine objective-C type of this number"];
	return -1;
}

-(unsigned long long)unsignedLongLongValue
{
	unsigned long long result;

	PyObjC_BEGIN_WITH_GIL
		if (PyLong_Check(value)) {
			result =  PyLong_AsUnsignedLongLongMask(value);
			PyObjC_GIL_RETURN(result);
#if PY_MAJOR_VERSION == 2
		} else if (PyInt_Check(value)) {
			result =  (unsigned long long)PyInt_AsLong(value);
			PyObjC_GIL_RETURN(result);
#endif
		} else if (PyFloat_Check(value)) {
			double temp = PyFloat_AsDouble(value);
			if (temp < 0) {
				/* Conversion of negative numbers to
				 * unsigned long long is undefined behaviour,
				 * the code below seems to get the behaviour
				 * we'd like: casting to unsigned long long
				 * behaves simular to casting a signed integer
				 * to undefined.
				 */
				long long t = (long long)temp;
				result = (unsigned long long)t;
			} else {
				result =  (unsigned long long)temp;
			}
			PyObjC_GIL_RETURN(result);
		}
	PyObjC_END_WITH_GIL

	[NSException raise:NSInvalidArgumentException 
		    format:@"Cannot determine objective-C type of this number"];
	return -1;
}

-(NSString*)description
{
	return [self stringValue];
}

-(NSString*)descriptionWithLocale:(NSObject*)locale
{
	/* FIXME: use locale information to format */
	 /* TODO: compare with regular NSNumber */
	(void)locale;
	return [self stringValue];
}

-(NSString*)stringValue
{
	PyObject* repr;
	NSObject* result = nil;

	PyObjC_BEGIN_WITH_GIL
		repr = PyObject_Repr(value);
		if (repr == NULL) {
			PyObjC_GIL_FORWARD_EXC();
		}

#if PY_MAJOR_VERSION == 2
		PyObject* uniVal = PyUnicode_FromEncodedObject(repr, "ascii", "strict");
		Py_DECREF(repr);
		if (PyErr_Occurred()) {
			PyObjC_GIL_FORWARD_EXC();
		}
	
		result = PyObjC_PythonToId(uniVal);
		Py_DECREF(uniVal);
		if (PyErr_Occurred()) {
			PyObjC_GIL_FORWARD_EXC();
		}
#else
		result = PyObjC_PythonToId(repr);
		Py_DECREF(repr);
		if (PyErr_Occurred()) {
			PyObjC_GIL_FORWARD_EXC();
		}
#endif


	PyObjC_END_WITH_GIL
	return (NSString*)result;
}

/* NSCoding support */

- (void)encodeWithCoder:(NSCoder*)coder
{
	int use_super = 0;

	PyObjC_BEGIN_WITH_GIL
		if (PyFloat_CheckExact(value)) {
			/* Float is a C double and can be roundtripped using 
			 * NSNumber.
			 */
			use_super = 1;

#if PY_MAJOR_VERSION == 2
		} else if (PyInt_CheckExact(value)) {
			/* Int is a C double and can be roundtripped using 
			 * NSNumber.
			 */
			use_super = 1;
#endif
		} else if (PyLong_CheckExact(value)) {
			/* Long object that fits in a long long */
			(void)PyLong_AsLongLong(value);
			if (PyErr_Occurred()) {
				PyErr_Clear();
				use_super = 0;
			} else {
				use_super = 1;
			}
		}
	PyObjC_END_WITH_GIL

	if (use_super) {
		[super encodeWithCoder:coder];
	} else {
		PyObjC_encodeWithCoder(value, coder);
	}
}


/* 
 * Helper method for initWithCoder, needed to deal with
 * recursive objects (e.g. o.value = o)
 */
-(void)pyobjcSetValue:(NSObject*)other
{
	PyObjC_BEGIN_WITH_GIL
		PyObject* v = PyObjC_IdToPython(other);
		Py_XDECREF(value);
		value = v;
	PyObjC_END_WITH_GIL
}

- (id)initWithCoder:(NSCoder*)coder
{
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
				self = (OC_PythonNumber*)proxy;
			}


		PyObjC_END_WITH_GIL

		return self;

	} else {
		[NSException raise:NSInvalidArgumentException
				format:@"decoding Python objects is not supported"];
		return nil;

	}
}

- (NSComparisonResult)compare:(NSNumber *)aNumber
{
	/* Rely on -[NSNumber compare:] when the other value
	 * is a number and we're not a python int that doesn't
	 * fit into a 'long long'.
	 *
	 * In all other cases use Python's comparison semantics.
	 */
	if ([aNumber isKindOfClass:[NSNumber class]] && ![aNumber isMemberOfClass: [OC_PythonNumber class]]) {
		if (PyLong_Check(value)) {
			PY_LONG_LONG r;
			r = PyLong_AsLongLong(value);
			if (r == -1 && PyErr_Occurred()) {
				PyErr_Print();
				PyErr_Clear();
			} else {
			     return [super compare:aNumber];
			}
		} else {
			return [super compare:aNumber];
		}
	} 

	PyObjC_BEGIN_WITH_GIL
		PyObject* other = PyObjC_IdToPython(aNumber);
		if (other == NULL) {
			PyObjC_GIL_FORWARD_EXC();
		}

		int r;
		int ok = PyObject_Cmp(value, other, &r);
		Py_DECREF(other);
		if (ok == -1) {
			PyObjC_GIL_FORWARD_EXC();
		}

		if (r < 0) {
			PyObjC_GIL_RETURN(NSOrderedAscending);
		} else if (r > 0) {
			PyObjC_GIL_RETURN(NSOrderedDescending);
		} else {
			PyObjC_GIL_RETURN(NSOrderedSame);
		}


	PyObjC_END_WITH_GIL
}


#define COMPARE_METHOD(NAME, OPERATOR) \
	-(BOOL)NAME:(NSObject*)aNumber \
{ \
	PyObjC_BEGIN_WITH_GIL \
		PyObject* other = PyObjC_IdToPython(aNumber); \
		if (other == NULL) { \
			PyObjC_GIL_FORWARD_EXC(); \
		} \
 \
		int r = PyObject_RichCompareBool(value, other, OPERATOR); \
		Py_DECREF(other); \
		if (r == -1) { \
			PyObjC_GIL_FORWARD_EXC(); \
		} \
 \
		if (r) { \
			PyObjC_GIL_RETURN(YES); \
		} else { \
			PyObjC_GIL_RETURN(NO); \
		} \
 \
	PyObjC_END_WITH_GIL \
}

COMPARE_METHOD(isEqualTo, Py_EQ)
COMPARE_METHOD(isNotEqualTo, Py_NE)
COMPARE_METHOD(isGreaterThan, Py_GT)
COMPARE_METHOD(isGreaterThanOrEqualTo, Py_GE)
COMPARE_METHOD(isLessThan, Py_LT)
COMPARE_METHOD(isLessThanOrEqualTo, Py_LE)


-(BOOL)isEqualToNumber:(NSNumber*)aNumber
{
	return [self isEqualTo:aNumber];
}




#if 1

-(NSObject*)replacementObjectForArchiver:(NSArchiver*)archiver
{
	(void)archiver;
	return (NSObject*)self;
}

-(NSObject*)replacementObjectForKeyedArchiver:(NSKeyedArchiver*)archiver
{
	(void)archiver;
	return (NSObject*)self;
}

-(NSObject*)replacementObjectForCoder:(NSCoder*)archiver
{
	(void)archiver;
	return (NSObject*)self;
}

-(NSObject*)replacementObjectForPortCoder:(NSPortCoder*)archiver
{
	(void)archiver;
	return (NSObject*)self;
}

-(Class)classForArchiver
{
	PyObjC_BEGIN_WITH_GIL
		if (PyFloat_CheckExact(value)) {
			/* Float is a C double and can be roundtripped using 
			 * NSNumber.
			 */
			PyObjC_GIL_RETURN([NSNumber class]);

#if PY_MAJOR_VERSION == 2
		} else if (PyInt_CheckExact(value)) {
			/* Int is a C double and can be roundtripped using 
			 * NSNumber.
			 */
			PyObjC_GIL_RETURN([NSNumber class]);
#endif
		} else if (PyLong_CheckExact(value)) {
			/* Long object that fits in a long long */
			(void)PyLong_AsLongLong(value);
			if (PyErr_Occurred()) {
				PyErr_Clear();
				PyObjC_GIL_RETURN([OC_PythonNumber class]);
			} else {
				PyObjC_GIL_RETURN([NSNumber class]);
			}

		} else {
			PyObjC_GIL_RETURN([OC_PythonNumber class]);
		}
	PyObjC_END_WITH_GIL
}

-(Class)classForKeyedArchiver
{
	return [self classForArchiver];
}

+(Class)classForUnarchiver
{
	return [OC_PythonNumber class];
}

+(Class)classForKeyedUnarchiver
{
	return [OC_PythonNumber class];
}

-(Class)classForCoder
{
	return [self classForArchiver];
}

-(Class)classForPortCoder
{
	return [self classForArchiver];
}

-(id)copy
{
	return [self copyWithZone:0];
}

-(id)copyWithZone:(NSZone*)zone
{
	(void)zone;
	[self retain];
	return self;
}


#endif
@end
