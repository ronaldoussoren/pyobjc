/*
 * Minimal support for the C-type NSDecimal
 *
 * This file provides *very* minimal support for NSDecimal values. A major
 * problem is that the C API does not have a function to initialise these
 * objects (you can create them through NSDecimalNumber instances).
 *
 * There is no implicit conversion to/from Python numbers, because NSDecimal
 * numbers behave differently from Python numbers (explicit rounding)
 *
 * - number methods
 */

typedef struct {
	PyObject_HEAD
	NSDecimal value;
} DecimalObject;

#define Decimal_Value(v) ((DecimalObject*)(v))->value

static PyObject* decimal_repr(PyObject* self);
static PyObject* decimal_richcompare(PyObject* self, PyObject* other, int type);
static void decimal_dealloc(PyObject* self);
static int decimal_init(PyObject* self, PyObject* args, PyObject* kwds);
static PyObject* decimal_new(PyTypeObject* type, PyObject* args, PyObject* kwds);
static PyObject* decimal_asint(PyObject* self);
static PyObject* decimal_asfloat(PyObject* self);

static PyMethodDef decimal_methods[] = {
	{
		"as_int",
		(PyCFunction)decimal_asint,
		METH_NOARGS,
		"Convert decimal to a Python int"
	},
	{
		"as_float",
		(PyCFunction)decimal_asfloat,
		METH_NOARGS,
		"Convert decimal to a Python float"
	},
	{
		NULL,
		NULL,
		0,
		NULL
	}
};


static PyTypeObject Decimal_Type = {
	PyObject_HEAD_INIT(NULL)
	0,					/* ob_size */
	"Foundation.NSDecimal",			/* tp_name */
	sizeof (DecimalObject),			/* tp_basicsize */
	0,					/* tp_itemsize */
  
	/* methods */
	decimal_dealloc,			/* tp_dealloc */
	0,					/* tp_print */
	0,					/* tp_getattr */
	0,					/* tp_setattr */
	0,					/* tp_compare */
	decimal_repr,				/* tp_repr */
	0,					/* tp_as_number */
	0,					/* tp_as_sequence */
	0,					/* tp_as_mapping */
	0,					/* tp_hash */
	0,					/* tp_call */
	decimal_repr,				/* tp_str */
	PyObject_GenericGetAttr,		/* tp_getattro */
	PyObject_GenericSetAttr,		/* tp_setattro */
	0,					/* tp_as_buffer */
	Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HAVE_RICHCOMPARE, /* tp_flags */
	"NSDecimal wrapper",			/* tp_doc */
	0,					/* tp_traverse */
	0,					/* tp_clear */
	decimal_richcompare,			/* tp_richcompare */
	0,					/* tp_weaklistoffset */
	0,					/* tp_iter */
	0,					/* tp_iternext */
	decimal_methods,			/* tp_methods */
	0,					/* tp_members */
	0,					/* tp_getset */
	0,					/* tp_base */
	0,					/* tp_dict */
	0,					/* tp_descr_get */
	0,					/* tp_descr_set */
	0,					/* tp_dictoffset */
	0,					/* tp_init */
	0,					/* tp_alloc */
	decimal_new,				/* tp_new */
	0,					/* tp_free */
	0,					/* tp_is_gc */
	0,					/* tp_bases */
	0,					/* tp_mro */
	0,					/* tp_cache */
	0,					/* tp_subclasses */
	0					/* tp_weaklist */
#if PY_VERSION_HEX >= 0x020300A2
	, 0,					/* tp_del */
#endif
};

#define Decimal_Check(obj) PyObject_TypeCheck(obj, &Decimal_Type)

#ifdef MACOSX

static void DecimalFromString(NSDecimal* aDecimal, NSString* aString, void* locale __attribute__((__unused__)))
{
	NSDecimalNumber* num;

	num = [[NSDecimalNumber alloc] initWithString:aString];
	*aDecimal = [num decimalValue];
	[num release];
}

static void DecimalFromComponents(NSDecimal* aDecimal, unsigned long long mantissa, unsigned short exponent, BOOL negative)
{
	NSDecimalNumber* num;

	num = [[NSDecimalNumber alloc] 
			initWithMantissa:mantissa
			exponent:exponent
			isNegative:negative];

	*aDecimal = [num decimalValue];
	[num release];
}

#else

#define DecimalFromString NSDecimalFromString
#define DecimalFromComponents NSDecimalFromComponents

#endif

static PyObject*
decimal_new(PyTypeObject* type __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
	DecimalObject* self;

	
	self = PyObject_New(DecimalObject, &Decimal_Type);
	if (self != NULL) {
		memset(&self->value, 0, sizeof(self->value));
	}
	if ((args == NULL || PyTuple_Size(args) == 0) && (kwds == NULL || PyDict_Size(kwds) == 0)) {
		DecimalFromComponents(&self->value, 0, 0, 0);
		return (PyObject*)self;
	}
	if (decimal_init((PyObject*)self, args, kwds) == -1) {
		Py_DECREF(self);
		return NULL;
	}
	return (PyObject*)self;
}

static void
decimal_dealloc(PyObject* self)
{
	PyObject_Free(self);
}


static int
decimal_init(PyObject* self, PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "mantissa", "exponent", "isNegative", NULL };
static char* keywords2[] = { "string", NULL };
	PyObject* pyMantissa;
	PyObject* pyExponent;
	PyObject* pyNegative;
	BOOL negative;
	unsigned long long mantissa;
	short int exponent;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "OOO", keywords, &pyMantissa, &pyExponent, &pyNegative)) {
		PyObject* pyValue;
		NSString* stringVal;

		PyErr_Clear();
		if (!PyArg_ParseTupleAndKeywords(args, kwds, "O", keywords2, &pyValue)) {
			PyErr_SetString(PyExc_TypeError,
			    "NSDecimal(stringValue) or NSDecimal(mantissa, exponent, isNegative)");
			return -1;
		}
		if (PyInt_Check(pyValue)) {
			long lng = PyInt_AsLong(pyValue);
			if (lng < 0) {
				mantissa = -lng;
				exponent = 0;
				negative = YES;
			} else{
				mantissa = lng;
				exponent = 0;
				negative = NO;
			}
				
			DecimalFromComponents(&Decimal_Value(self),
				mantissa, exponent, negative);
			return 0;
		} else if (PyLong_Check(pyValue)) {
			mantissa = PyLong_AsUnsignedLongLong(pyValue);
			if (PyErr_Occurred()) {
				long long lng;
				PyErr_Clear();
				lng = PyLong_AsLongLong(pyValue);
				if (PyErr_Occurred()) {
					return -1;
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
				DecimalFromComponents(&Decimal_Value(self),
					mantissa, exponent, negative);
				return 0;
			} else {
				DecimalFromComponents(&Decimal_Value(self),
					mantissa, 0, NO);
				return 0;
			}
		} else if (!PyString_Check(pyValue) && !PyUnicode_Check(pyValue)) {
			PyErr_Format(PyExc_TypeError, "cannot convert object of %s to NSDecimal", pyValue->ob_type->tp_name);
			return -1;
		}

		stringVal = PyObjC_PythonToId(pyValue);
		NS_DURING
			DecimalFromString(&Decimal_Value(self), stringVal, NULL);
		NS_HANDLER
			PyObjCErr_FromObjC(localException);
		NS_ENDHANDLER

		if (PyErr_Occurred()) return -1;
		return 0;

	}

	negative = PyObject_IsTrue(pyNegative);
	if (PyObjC_PythonToObjC(@encode(short int), pyExponent, &exponent) == -1) {
		return -1;
	}

	if (PyObjC_PythonToObjC(@encode(unsigned long long), pyMantissa, &mantissa) == -1) {
		return -1;
	}


	DecimalFromComponents(&Decimal_Value(self),
		mantissa,
		exponent,
		negative);

	return 0;
}

static PyObject* 
decimal_richcompare(PyObject* self, PyObject* other, int type)
{
	NSComparisonResult res;

	if (!Decimal_Check(other)) {
		if (type == Py_EQ) {
			return PyBool_FromLong(0);
		}
		PyErr_Format(PyExc_TypeError,
			"Cannot compare NSDecimal and %s", 
			other->ob_type->tp_name);
		return NULL;
	}

	res = NSDecimalCompare(&Decimal_Value(self), &Decimal_Value(other));

	switch (type) {
	case Py_LT: return PyBool_FromLong(res ==  NSOrderedAscending);
	case Py_LE: return PyBool_FromLong(res != NSOrderedDescending);
	case Py_EQ: return PyBool_FromLong(res == NSOrderedSame);
	case Py_NE: return PyBool_FromLong(res != NSOrderedSame);
	case Py_GE: return PyBool_FromLong(res != NSOrderedAscending);
	case Py_GT: return PyBool_FromLong(res == NSOrderedDescending);
	default: 
		    PyErr_SetString(PyExc_TypeError,
				  "Bad comparison arg");
		    return NULL;
	}
}


static PyObject* decimal_asint(PyObject* self)
{
	NSDecimalNumber* tmp = [[NSDecimalNumber alloc] initWithDecimal:Decimal_Value(self)];
	long retval = [tmp longValue];
	[tmp release];

	return PyInt_FromLong(retval);
}

static PyObject* decimal_asfloat(PyObject* self)
{
	NSDecimalNumber* tmp = [[NSDecimalNumber alloc] initWithDecimal:Decimal_Value(self)];
	double retval = [tmp doubleValue];
	[tmp release];

	return PyFloat_FromDouble(retval);
}

static PyObject*
decimal_repr(PyObject* self)
{
	NSString* val = NSDecimalString(&Decimal_Value(self), NULL);
	return PyObjC_IdToPython(val);
}

static inline int
Decimal_Convert(PyObject* self, void* val)
{
	if (Decimal_Check(self)) {
		 *(NSDecimal**)val = &Decimal_Value(self);
		 return 1;
	}
	PyErr_SetString(PyExc_TypeError, "Expecting an NSDecimal");
	return 0;
}


static inline PyObject*
Decimal_New(NSDecimal* aDecimal)
{
	DecimalObject* result;

	result = PyObject_New(DecimalObject, &Decimal_Type);
	if (result == NULL) return NULL;

	result->value = *aDecimal;
	return (PyObject*)result;
}

static int install_decimal(PyObject* module);
static int install_decimal(PyObject* module)
{
	PyType_Ready(&Decimal_Type);
	PyModule_AddObject(module, "NSDecimal", (PyObject*)&Decimal_Type);
	return 0;
}
