#include "pyobjc.h"
#import "OC_PythonDate.h"

static PyObject* datetime_types = NULL;

@implementation OC_PythonDate 

+ depythonifyObject:(PyObject*)object;
{
	if (datetime_types == NULL) {
		/* Initialize the mapping table, don't worry about
		 * import errors: if we're running in an Py2app application
		 * that doesn't use datetime we won't be able to import the
		 * module
		 */
		datetime_types = PyList_New(0);
		if (datetime_types == NULL) {
			return nil;
		}
		PyObject* name = PyText_FromString("datetime");
		if (name == NULL) {
			return nil;
		}
		PyObject* datetime = PyImport_Import(name);
		Py_DECREF(name); name = NULL;

		if (datetime == NULL) {
			Py_DECREF(datetime);
			PyErr_Clear();
			return nil;
		}

		PyList_Append(datetime_types,
			PyObject_GetAttrString(datetime, "date"));
		PyList_Append(datetime_types,
			PyObject_GetAttrString(datetime, "datetime"));
		if (PyErr_Occurred()) {
			Py_DECREF(datetime);
			return nil;
		}
		Py_DECREF(datetime);
	}


	if (PySequence_Contains(datetime_types, (PyObject*)(Py_TYPE(object)))) {
		return [[OC_PythonDate alloc] initWithPythonObject:object];
	}
	return nil;
}

+ dateWithPythonObject:(PyObject*)v;
{
	OC_PythonArray* res;

	res = [[OC_PythonDate alloc] initWithPythonObject:v];
	[res autorelease];
	return res;
}

- initWithPythonObject:(PyObject*)v;
{
	self = [super init];
	if (unlikely(self == nil)) return nil;

	oc_value = nil;

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
	[oc_value  release];
	oc_value = nil;

	PyObjC_BEGIN_WITH_GIL
		PyObjC_UnregisterObjCProxy(value, self);
		Py_XDECREF(value);

	PyObjC_END_WITH_GIL

	[super dealloc];
}


- (void)encodeWithCoder:(NSCoder*)coder
{
	PyObjC_encodeWithCoder(value, coder);
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
	value = NULL;

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
				self = (OC_PythonDate*)proxy;
			}


		PyObjC_END_WITH_GIL

		return self;

	} else {
		[NSException raise:NSInvalidArgumentException
				format:@"decoding Python objects is not supported"];
		return nil;

	}
}

-(NSDate*)_make_oc_value
{
	if (oc_value == nil) {
		PyObjC_BEGIN_WITH_GIL
			PyObject* v;

			v = PyObject_CallMethod(value, "strftime", "s",
				"%Y-%m-%d %H:%M:%S %z");
			if (v == NULL) {
				/* Raise ObjC exception */
			}


			oc_value = [NSDate dateWithString: PyObjC_PythonToId(v)];
			[oc_value retain];
			Py_DECREF(v);

			if (oc_value == nil) {
				/* The first try will fail when the date/datetime object
				 * isn't timezone aware, try again with a default timezone
				 */
				char buf[128];

				NSTimeZone* zone = [NSTimeZone defaultTimeZone];
				NSInteger offset = [zone secondsFromGMT];
				char posneg;
				if (offset < 0) {
					posneg = '-';
					offset = -offset;
				} else {
					posneg = '+';
				}
				offset = offset / 60; /* Seconds to minutes */

				int minutes = offset % 60;
				int hours = offset / 60;



				snprintf(buf, sizeof(buf), "%%Y-%%m-%%d %%H:%%M:%%S %c%02d%02d",
					posneg, hours, minutes);
				v = PyObject_CallMethod(value, "strftime", "s", buf);
				if (v == NULL) {
					/* Raise ObjC exception */
				}

				oc_value = [NSDate dateWithString: PyObjC_PythonToId(v)];
				[oc_value retain];
				Py_DECREF(v);
			}



		PyObjC_END_WITH_GIL
	} 
	return oc_value;
}

-(NSTimeInterval)timeIntervalSinceReferenceDate
{
	return [[self _make_oc_value] timeIntervalSinceReferenceDate];
}


- (id)addTimeInterval:(NSTimeInterval)seconds
{
	return [[self _make_oc_value] addTimeInterval:seconds];
}

- (NSComparisonResult)compare:(NSDate *)anotherDate
{
	return [[self _make_oc_value] compare:anotherDate];
}

- (NSCalendarDate *)dateWithCalendarFormat:(NSString *)formatString timeZone:(NSTimeZone *)timeZone
{
	return [[self _make_oc_value] dateWithCalendarFormat:formatString timeZone:timeZone];
}

- (NSString*)description
{
	return [[self _make_oc_value] description];
}

- (NSString *)descriptionWithCalendarFormat:(NSString *)formatString timeZone:(NSTimeZone *)aTimeZone locale:(id)localeDictionary
{
	return [[self _make_oc_value] descriptionWithCalendarFormat:formatString timeZone:aTimeZone locale:localeDictionary];
}

- (NSString *)descriptionWithLocale:(id)localeDictionary
{
	return [[self _make_oc_value] descriptionWithLocale:localeDictionary];
}

- (NSDate *)earlierDate:(NSDate *)anotherDate
{
	if ([[self _make_oc_value] earlierDate:anotherDate] == self) {
		return self;
	} else {
		return anotherDate;
	}
}


- (BOOL)isEqualToDate:(NSDate *)anotherDate
{
	return [[self _make_oc_value] isEqualToDate:anotherDate];
}


- (NSDate *)laterDate:(NSDate *)anotherDate
{
	if ([[self _make_oc_value] laterDate:anotherDate] == self) {
		return self;
	} else {
		return anotherDate;
	}
}

- (NSTimeInterval)timeIntervalSince1970
{
	return [[self _make_oc_value] timeIntervalSince1970];
}

- (NSTimeInterval)timeIntervalSinceDate:(NSDate *)anotherDate
{
	return [[self _make_oc_value] timeIntervalSinceDate:anotherDate];
}

- (NSTimeInterval)timeIntervalSinceNow
{
	return [[self _make_oc_value] timeIntervalSinceNow];
}


@end /* implementation OC_PythonDate */
