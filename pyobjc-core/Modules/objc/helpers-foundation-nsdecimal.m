/*
 * Minimal support for the C-type NSDecimal
 *
 * There is no implicit conversion to/from Python numbers, because NSDecimal
 * numbers behave differently from Python numbers (explicit rounding)
 *
 * - number methods
 *   NSDecimal objects support +, -, *, /, +=, -=, *= and /=, which directly
 *   correspond with NSDecimal* functions with the NSRoundPlain argument.
 *   They also support unary -, unary + and abs, with the obvious semantics.
 */
#include "pyobjc.h"

static char Decimal_Encoding[sizeof(@encode(NSDecimal)) + 32];
static size_t Decimal_Encoding_Len = 0;
static PyObject* _NSDecimalNumber_Class = NULL;

typedef struct {
    PyObject_HEAD
    NSDecimal value;
    NSDecimalNumber *objc_value;
} DecimalObject;

#define Decimal_Value(v) ((DecimalObject*)(v))->value

static PyObject* Decimal_New(NSDecimal* aDecimal);
static PyObject* decimal_repr(PyObject* self);
static PyObject* decimal_richcompare(PyObject* self, PyObject* other, int type);
static void decimal_dealloc(PyObject* self);
static int decimal_init(PyObject* self, PyObject* args, PyObject* kwds);
static PyObject* decimal_new(PyTypeObject* type, PyObject* args, PyObject* kwds);
static PyObject* decimal_asint(PyObject* self);
static PyObject* decimal_asfloat(PyObject* self);
static PyObject* decimal_add(PyObject* left, PyObject* right);
static PyObject* decimal_subtract(PyObject* left, PyObject* right);
static PyObject* decimal_multiply(PyObject* left, PyObject* right);
static PyObject* decimal_divide(PyObject* left, PyObject* right);
static PyObject* decimal_floordivide(PyObject* left, PyObject* right);
static PyObject* decimal_power(PyObject* left, PyObject* right, PyObject* power);
static int decimal_nonzero(PyObject* self);
static int decimal_coerce(PyObject** l, PyObject** r);
static int decimal_coerce_compare(PyObject** l, PyObject** r);
static PyObject* decimal_positive(PyObject* self);
static PyObject* decimal_negative(PyObject* self);
static PyObject* decimal_absolute(PyObject* self);
static PyObject* decimal_round(PyObject* self, PyObject* args, PyObject* kwds);
static Py_hash_t decimal_hash(PyObject* o);

static PyNumberMethods decimal_asnumber = {
    .nb_add             = decimal_add,
    .nb_subtract        = decimal_subtract,
    .nb_multiply        = decimal_multiply,
    .nb_power           = decimal_power,
    .nb_negative        = decimal_negative,
    .nb_positive        = decimal_positive,
    .nb_absolute        = decimal_absolute,
#if PY_MAJOR_VERSION == 2
    .nb_nonzero         = decimal_nonzero,
#else /* PY_MAJOR_VERSION == 3 */
    .nb_bool            = decimal_nonzero,
#endif /* PY_MAJOR_VERSION == 3 */
    .nb_floor_divide    = decimal_floordivide,
    .nb_true_divide     = decimal_divide,

#if PY_MAJOR_VERSION == 2
    .nb_divide          = decimal_divide,
    .nb_coerce          = decimal_coerce,

#endif /* PY_MAJOR_VERSION == 2 */
};

static NSDecimalNumber *
Decimal_ObjCValue(PyObject *self) {
    DecimalObject *pyself = (DecimalObject *)self;
    NSDecimalNumber *res = pyself->objc_value;

    if (!res) {
        res = pyself->objc_value = [[NSDecimalNumber alloc] initWithDecimal:Decimal_Value(self)];
    }
    return res;
}

static PyObject *
decimal_get__pyobjc_object__(PyObject *self, void *closure __attribute__((__unused__))) {
    PyObject *rval = PyObjCObject_New(Decimal_ObjCValue(self), 0, YES);
    return rval;
}

static PyGetSetDef decimal_getseters[] = {
    {
        .name   = "__pyobjc_object__",
        .get    = (getter)decimal_get__pyobjc_object__,
        .doc    = "NSDecimalNumber instance",
    },
    {
        .name   = NULL /* SENTINEL */
    }
};

static PyMethodDef decimal_methods[] = {
    {
        .ml_name    = "as_int",
        .ml_meth    = (PyCFunction)decimal_asint,
        .ml_flags   = METH_NOARGS,
        .ml_doc     = "Convert decimal to a Python int"
    },
    {
        .ml_name    = "as_float",
        .ml_meth    = (PyCFunction)decimal_asfloat,
        .ml_flags   = METH_NOARGS,
        .ml_doc     = "Convert decimal to a Python float"
    },
    {
        .ml_name    = "__round__",
        .ml_meth    = (PyCFunction)decimal_round,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS
    },
    {
        .ml_name    = NULL /* SENTINEL */
    }
};

static PyObject*
decimal_getattro(PyObject *o, PyObject *attr_name)
{
    return PyObject_GenericGetAttr(o, attr_name);
}

static PyTypeObject Decimal_Type = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0)
    .tp_name        = "Foundation.NSDecimal",
    .tp_basicsize   = sizeof (DecimalObject),
    .tp_itemsize    = 0,
    .tp_dealloc     = decimal_dealloc,
    .tp_repr        = decimal_repr,
    .tp_str         = decimal_repr,
    .tp_as_number   = &decimal_asnumber,
    .tp_hash        = decimal_hash,
    .tp_getattro    = decimal_getattro,
    .tp_setattro    = PyObject_GenericSetAttr,
#if PY_MAJOR_VERSION == 2
    .tp_flags       = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HAVE_RICHCOMPARE,
#else /* PY_MAJOR_VERSION == 3 */
    .tp_flags       = Py_TPFLAGS_DEFAULT,
#endif /* PY_MAJOR_VERSION == 3 */
    .tp_doc         = "NSDecimal wrapper",
    .tp_richcompare = decimal_richcompare,
    .tp_methods     = decimal_methods,
    .tp_getset      = decimal_getseters,
    .tp_new         = decimal_new,
};

#define Decimal_Check(obj) PyObject_TypeCheck(obj, &Decimal_Type)

static void
DecimalFromString(NSDecimal* aDecimal, NSString* aString, void* locale __attribute__((__unused__)))
{
    NSDecimalNumber* num;

    num = [[NSDecimalNumber alloc] initWithString:aString];
    *aDecimal = [num decimalValue];
    [num release];
}

static void
DecimalFromComponents(NSDecimal* aDecimal, unsigned long long mantissa, unsigned short exponent, BOOL negative)
{
    NSDecimalNumber* num;

    num = [[NSDecimalNumber alloc]
            initWithMantissa:mantissa
            exponent:exponent
            isNegative:negative];

    *aDecimal = [num decimalValue];
    [num release];
}

static PyObject*
decimal_new(PyTypeObject* type __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
    DecimalObject* self;


    self = PyObject_New(DecimalObject, &Decimal_Type);
    if (self == NULL) {
        return PyErr_NoMemory();
    }

    memset(&self->value, 0, sizeof(self->value));
    self->objc_value = nil;
    if ((args == NULL || PyTuple_Size(args) == 0) && (kwds == NULL || PyDict_Size(kwds) == 0)) {
        DecimalFromComponents(&self->value, 0, 0, 0);
        return (PyObject*)self;
    }

    if (decimal_init((PyObject*)self, args, kwds) == -1) {
        Py_DECREF(self);
        self = NULL;
        return NULL;
    }

    return (PyObject*)self;
}

static void
decimal_dealloc(PyObject* self)
{
    [((DecimalObject *)self)->objc_value release];
    PyObject_Free(self);
}

int
PyObjC_number_to_decimal(PyObject* pyValue, NSDecimal* outResult)
{
    BOOL negative;
    unsigned long long mantissa;
    short int exponent;

    if (PyLong_Check(pyValue)) {
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

            DecimalFromComponents(outResult, mantissa, exponent, negative);
            return 0;

        } else {
            DecimalFromComponents(outResult, mantissa, 0, NO);
            return 0;
        }

#if PY_MAJOR_VERSION == 2
    } else if (PyInt_Check(pyValue)) {
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

        DecimalFromComponents(outResult, mantissa, exponent, negative);
        return 0;
#endif
    } else if (PyFloat_Check(pyValue)) {
        /* Explicit conversion from float to NSDecimal
         * first convert the float to a string using repr, that
         * is easier than extracting the components of the
         * float.
         */
        NSString* stringVal;
#if PY_MAJOR_VERSION == 2
        PyObject* strVal = PyObject_Repr(pyValue);
        PyObject* uniVal = NULL;

        if (strVal == NULL) return -1;

        uniVal = PyUnicode_FromEncodedObject(strVal, "ascii", "strict");
        Py_DECREF(strVal);

#else /* PY_MAJOR_VERSION == 2 */
        PyObject* uniVal = PyObject_Repr(pyValue);
        if (uniVal == NULL) return -1;
#endif /* PY_MAJOR_VERSION == 2 */

        if (uniVal == NULL) return -1;

        stringVal = PyObjC_PythonToId(uniVal);
        Py_DECREF(uniVal);

        PyObjC_DURING
            DecimalFromString(outResult, stringVal, NULL);

        PyObjC_HANDLER
            PyObjCErr_FromObjC(localException);

        PyObjC_ENDHANDLER

        if (PyErr_Occurred()) return -1;
        return 0;

    }

    if (_NSDecimalNumber_Class == NULL) {
        _NSDecimalNumber_Class = PyObjCClass_New([NSDecimalNumber class]);
        if (_NSDecimalNumber_Class == NULL) {
            PyErr_Clear();
        }
    }

    if (_NSDecimalNumber_Class != NULL && PyObject_IsInstance(pyValue, _NSDecimalNumber_Class)) {
        NSDecimalNumber* val = PyObjCObject_GetObject(pyValue);
        *outResult = [val decimalValue];
        return 0;
    }

    PyErr_Format(PyExc_TypeError, "cannot convert object of %s to NSDecimal", pyValue->ob_type->tp_name);
    return -1;
}

/* NOTE: This is intentionally not in the tp_init slot, that would make NSDecimal
 * objects mutable.
 */
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

    ((DecimalObject*)self)->objc_value = nil;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "OOO", keywords, &pyMantissa, &pyExponent, &pyNegative)) {
        PyObject* pyValue;

        PyErr_Clear();
        if (!PyArg_ParseTupleAndKeywords(args, kwds, "O", keywords2, &pyValue)) {
            PyErr_SetString(PyExc_TypeError,
                "NSDecimal(value) or NSDecimal(mantissa, exponent, isNegative)");
            return -1;
        }

        if (PyObjCObject_Check(pyValue)) {
            NSObject* value = PyObjC_PythonToId(pyValue);

            if ([value isKindOfClass:[NSDecimalNumber class]]) {
                ((DecimalObject*)self)->value = [
                    (NSDecimalNumber*)value decimalValue
                ];

                ((DecimalObject*)self)->objc_value =
                    (NSDecimalNumber*)value;
                [value retain];
                return 0;
            }

            PyErr_Format(PyExc_TypeError, "cannot convert object of %s to NSDecimal", pyValue->ob_type->tp_name);
            return -1;

        } else if (
#if PY_MAJOR_VERSION == 2
                PyString_Check(pyValue) ||
#endif /* PY_MAJOR_VERSION == 2 */
                PyUnicode_Check(pyValue)) {

            NSString* stringVal;

            stringVal = PyObjC_PythonToId(pyValue);
            PyObjC_DURING
                DecimalFromString(&Decimal_Value(self), stringVal, NULL);
            PyObjC_HANDLER
                PyObjCErr_FromObjC(localException);
            PyObjC_ENDHANDLER

            if (PyErr_Occurred()) return -1;
            return 0;

        } else {
            return PyObjC_number_to_decimal(pyValue, &Decimal_Value(self));
        }
    }

    negative = PyObject_IsTrue(pyNegative);
    if (depythonify_c_value(@encode(short int), pyExponent, &exponent) == -1) {
        return -1;
    }

    if (depythonify_c_value(@encode(unsigned long long), pyMantissa, &mantissa) == -1) {
        return -1;
    }

    DecimalFromComponents(&Decimal_Value(self),
        mantissa,
        exponent,
        negative);

    return 0;
}


static Py_hash_t
decimal_hash(PyObject* self)
{
    NSString* strrepr = NSDecimalString(&Decimal_Value(self), nil);
    NSUInteger hash = [strrepr hash];

    if ((Py_hash_t)hash == (Py_hash_t)-1) {
        /* hash -1 is not used by Python */
        return -2;
    } else {
        return hash;
    }
}


static PyObject*
decimal_richcompare(PyObject* self, PyObject* other, int type)
{
    NSComparisonResult res;
    (void)decimal_coerce_compare(&self, &other);

    if (!Decimal_Check(other)) {
        if (type == Py_EQ) {
            if (PyErr_Occurred()) {
                PyErr_Clear();
            }
            return PyBool_FromLong(0);

        } else if (type == Py_NE) {
            if (PyErr_Occurred()) {
                PyErr_Clear();
            }
            return PyBool_FromLong(1);
        }

        PyErr_Format(PyExc_TypeError,
            "Cannot compare NSDecimal and %s",
            other->ob_type->tp_name);
        return NULL;
    }

    if (PyErr_Occurred()) {
        return NULL;
    }

    res = NSDecimalCompare(&Decimal_Value(self), &Decimal_Value(other));

    switch (type) {
    case Py_LT: return PyBool_FromLong(res == NSOrderedAscending);
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
    NSDecimalNumber* tmp = Decimal_ObjCValue(self);
    return PyInt_FromLong([tmp longValue]);
}

static PyObject* decimal_asfloat(PyObject* self)
{
    NSDecimalNumber* tmp = Decimal_ObjCValue(self);
    return PyFloat_FromDouble([tmp doubleValue]);
}

static PyObject* decimal_power(
    PyObject* left __attribute__((__unused__)),
    PyObject* right __attribute__((__unused__)),
    PyObject* extra __attribute__((__unused__)))
{
    PyErr_SetString(PyExc_TypeError,
        "pow() and ** are not supported for NSDecimal");
    return NULL;
}


#if PY_MAJOR_VERSION == 3
#   define  TRY_COERCE(left, right) \
        int r = decimal_coerce(&left, &right);  \
        if (r == 1) {                           \
            Py_INCREF(Py_NotImplemented);       \
            return Py_NotImplemented;           \
        }

#else /* PY_MAJOR_VERSION == 2 */

#   define  TRY_COERCE(left, right)

#endif /* PY_MAJOR_VERSION == 2 */

#define DECIMAL_OPERATOR(py_function, nsdecimal_function) \
            static PyObject* py_function(PyObject* left, PyObject* right)                                       \
            {                                                                                                   \
                NSDecimal  result;                                                                              \
                NSCalculationError err;                                                                         \
                                                                                                                \
                TRY_COERCE(left, right);                                                                        \
                                                                                                                \
                err = nsdecimal_function(&result, &Decimal_Value(left), &Decimal_Value(right), NSRoundPlain);   \
                if (err == NSCalculationOverflow) {                                                             \
                    PyErr_SetString(PyExc_OverflowError, "Numeric overflow");                                   \
                    return NULL;                                                                                \
                                                                                                                \
                } else if (err == NSCalculationUnderflow) {                                                     \
                    PyErr_SetString(PyExc_OverflowError, "Numeric underflow");                                  \
                    return NULL;                                                                                \
                                                                                                                \
                } else  {                                                                                       \
                    NSDecimalCompact(&result);                                                                  \
                    return Decimal_New(&result);                                                                \
                }                                                                                               \
            }

DECIMAL_OPERATOR(decimal_add, NSDecimalAdd)
DECIMAL_OPERATOR(decimal_subtract, NSDecimalSubtract)
DECIMAL_OPERATOR(decimal_multiply, NSDecimalMultiply)
DECIMAL_OPERATOR(decimal_divide, NSDecimalDivide)

static PyObject* decimal_floordivide(PyObject* left, PyObject* right)
{
    NSDecimal  result, result2;
    NSCalculationError err;

    TRY_COERCE(left, right);

    err = NSDecimalDivide(&result,
            &Decimal_Value(left),
            &Decimal_Value(right),
            NSRoundPlain);
    if (err == NSCalculationOverflow) {
        PyErr_SetString(PyExc_OverflowError, "Numeric overflow");
        return NULL;

    } else if (err == NSCalculationUnderflow) {
        PyErr_SetString(PyExc_OverflowError, "Numeric underflow");
        return NULL;
    }

    NSDecimalRound(&result2, &result, 0, NSRoundDown);
    NSDecimalCompact(&result2);
    return Decimal_New(&result2);
}

static int decimal_nonzero(PyObject* self)
{
    NSDecimal zero;

    DecimalFromComponents(&zero, 0, 0, 0);

    return NSDecimalCompare(&zero, &Decimal_Value(self)) == NSOrderedSame;
}

static PyObject* decimal_positive(PyObject* self)
{
    Py_INCREF(self);
    return self;
}

static PyObject* decimal_negative(PyObject* self)
{
    NSDecimal result;
    NSCalculationError err;
    NSDecimal zero;
    DecimalFromComponents(&zero, 0, 0, 0);

    err = NSDecimalSubtract(&result, &zero, &Decimal_Value(self), NSRoundPlain);

    if (err == NSCalculationOverflow) {
        PyErr_SetString(PyExc_OverflowError, "Numeric overflow");
        return NULL;

    } else if (err == NSCalculationUnderflow) {
        PyErr_SetString(PyExc_OverflowError, "Numeric underflow");
        return NULL;

    } else {
        NSDecimalCompact(&result);
        return Decimal_New(&result);
    }
}

static PyObject* decimal_absolute(PyObject* self)
{
    NSDecimal result;
    NSCalculationError err;
    NSDecimal zero;
    DecimalFromComponents(&zero, 0, 0, 0);


    switch (NSDecimalCompare(&zero, &Decimal_Value(self))) {
    case NSOrderedSame:
    case NSOrderedAscending:
        /* self >= 0 */
        Py_INCREF(self);
        return self;

    case NSOrderedDescending: ;
    }


    err = NSDecimalSubtract(&result,
            &zero,
            &Decimal_Value(self),
            NSRoundPlain);
    if (err == NSCalculationOverflow) {
        PyErr_SetString(PyExc_OverflowError, "Numeric overflow");
        return NULL;

    } else if (err == NSCalculationUnderflow) {
        PyErr_SetString(PyExc_OverflowError, "Numeric underflow");
        return NULL;

    } else {
        NSDecimalCompact(&result);
        return Decimal_New(&result);
    }
}

static PyObject* decimal_round(PyObject* self, PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "digits", NULL };
    Py_ssize_t digits = 0;
    NSDecimal result;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|n", keywords, &digits)) {
        return NULL;
    }

    NSDecimalRound(&result, &Decimal_Value(self), digits, NSRoundPlain);
    NSDecimalCompact(&result);
    return Decimal_New(&result);
}


static int decimal_coerce(PyObject** l, PyObject** r)
{
    PyObject* right = NULL;
    PyObject* left = NULL;
    PyObject* args = NULL;
    int res;

    if (Decimal_Check(*l) && Decimal_Check(*r)) {
        Py_INCREF(*l);
        Py_INCREF(*r);
        return 0;
    }

    if (!Decimal_Check(*l)) {
        /* The test is needed to avoid silently converting strings */
        if (PyBytes_Check(*l) || PyUnicode_Check(*l) || PyFloat_Check(*l)) goto error;

        left = (PyObject*)PyObject_New(DecimalObject, &Decimal_Type);
        if (left == NULL) goto error;

        args = Py_BuildValue("(O)", *l);
        if (args == NULL) goto error;

        res = decimal_init(left, args, NULL);
        if (res == -1) goto error;

        Py_DECREF(args); args = NULL;
    }

    if (!Decimal_Check(*r)) {
        /* The test is needed to avoid silently converting strings */
        if (PyBytes_Check(*r) || PyUnicode_Check(*r) || PyFloat_Check(*r)) goto error;

        right = (PyObject*)PyObject_New(DecimalObject, &Decimal_Type);
        if (right == NULL) goto error;

        args = Py_BuildValue("(O)", *r);
        if (args == NULL) goto error;

        res = decimal_init(right, args, NULL);
        if (res == -1) goto error;

        Py_DECREF(args); args = NULL;
    }

    if (left != NULL) {
        *l = left;
    } else {
        Py_INCREF(*l);
    }

    if (right != NULL) {
        *r = right;
    } else {
        Py_INCREF(*r);
    }

    return 0;

error:
    Py_XDECREF(args);
    Py_XDECREF(left);
    Py_XDECREF(right);
    return 1;
}

static int decimal_coerce_compare(PyObject** l, PyObject** r)
{
    if (PyFloat_Check(*l)) {
        NSDecimal tmp;
        PyObjC_number_to_decimal(*l, &tmp);
        if (PyObjC_number_to_decimal(*r, &tmp) == -1) {
            return 1;
        }
        *l = Decimal_New(&tmp);
    }
    if (PyFloat_Check(*r)) {
        NSDecimal tmp;
        if (PyObjC_number_to_decimal(*r, &tmp) == -1) {
            return 1;
        }
        *r = Decimal_New(&tmp);
    }
    return decimal_coerce(l, r);
}

static PyObject*
decimal_repr(PyObject* self)
{
    NSString* val = NSDecimalString(&Decimal_Value(self), NULL);
    PyObject* tmp = PyObjC_IdToPython(val);
    PyObject* repr = PyObject_Str(tmp);
    Py_DECREF(tmp);
    return repr;
}

static inline int
Decimal_Convert(PyObject* self, void* val)
{
    if (Decimal_Check(self)) {
         *(NSDecimal**)val = &Decimal_Value(self);
         return 1;
    }
    PyErr_Format(PyExc_TypeError, "Expecting an NSDecimal, got instance of '%s'", Py_TYPE(self)->tp_name);
    return 0;
}


static PyObject*
Decimal_New(NSDecimal* aDecimal)
{
    DecimalObject* result;

    result = PyObject_New(DecimalObject, &Decimal_Type);
    if (result == NULL) return NULL;

    result->objc_value = nil;
    result->value = *aDecimal;
    return (PyObject*)result;
}

PyObject*
pythonify_nsdecimal(void* value)
{
    PyObject* v;
    v = Decimal_New((NSDecimal*)value);
    return v;
}

int
depythonify_nsdecimal(PyObject* value, void* ptr)
{
    if (Decimal_Check(value)) {
        *(NSDecimal*)ptr = Decimal_Value(value);
        return 0;

    } else {
        PyErr_Format(PyExc_TypeError, "Expecting an NSDecimal, got instance of '%s'", Py_TYPE(value)->tp_name);
        return -1;
    }
}

int IS_DECIMAL(const char* typestr)
{
    return (strncmp(typestr, @encode(NSDecimal), sizeof(@encode(NSDecimal))-1) == 0) || (
            Decimal_Encoding_Len != 0 && strncmp(typestr, Decimal_Encoding, Decimal_Encoding_Len) == 0);
}

static PyObject*
call_NSDecimalNumber_decimalNumberWithDecimal_(
    PyObject* method, PyObject* self, PyObject* arguments)
{
    struct objc_super super;
    NSDecimal* aDecimal;
    id res;

    if (!PyArg_ParseTuple(arguments, "O&", Decimal_Convert, &aDecimal)) {
        return NULL;
    }

    PyObjC_DURING
        objc_superSetReceiver(super, object_getClass(PyObjCClass_GetClass(self)));
        objc_superSetClass(super, object_getClass(PyObjCSelector_GetClass(method)));

        res = objc_msgSendSuper(&super,
                PyObjCSelector_GetSelector(method),
                *aDecimal);
    PyObjC_HANDLER
        PyObjCErr_FromObjC(localException);
        res = nil;
    PyObjC_ENDHANDLER

    if (res == nil && PyErr_Occurred()) {
        return NULL;
    }

    return PyObjC_IdToPython(res);
}

static PyObject*
call_NSDecimalNumber_initWithDecimal_(
    PyObject* method, PyObject* self, PyObject* arguments)
{
    struct objc_super super;
    NSDecimal* aDecimal;
    id res;

    if (!PyArg_ParseTuple(arguments, "O&", Decimal_Convert, &aDecimal)) {
        return NULL;
    }

    PyObjC_DURING
        objc_superSetReceiver(super, PyObjCObject_GetObject(self));
        objc_superSetClass(super, PyObjCSelector_GetClass(method));

        res = objc_msgSendSuper(&super,
                PyObjCSelector_GetSelector(method),
                *aDecimal);
    PyObjC_HANDLER
        PyObjCErr_FromObjC(localException);
        res = nil;
    PyObjC_ENDHANDLER

    if (res == nil && PyErr_Occurred()) {
        return NULL;
    }

    return PyObjC_IdToPython(res);
}

static void
imp_NSDecimalNumber_initWithDecimal_(
    ffi_cif* cif __attribute__((__unused__)),
    void* resp,
    void** args,
    void* callable)
{
    id self = *(id*)args[0];
    NSDecimal aDecimal = *(NSDecimal*)args[2];
    id* pretval = (id*)resp;

    PyObject* result = NULL;
    PyObject* arglist = NULL;
    PyObject* v = NULL;
    PyObject* pyself = NULL;
    int cookie = 0;

    PyGILState_STATE state = PyGILState_Ensure();

    arglist = PyTuple_New(2);
    if (arglist == NULL) goto error;

    pyself = PyObjCObject_NewTransient(self, &cookie);
    if (pyself == NULL) goto error;
    PyTuple_SetItem(arglist, 0, pyself);
    Py_INCREF(pyself);

    v = Decimal_New(&aDecimal);
    if (v == NULL) goto error;
    PyTuple_SetItem(arglist, 1, v);

    result = PyObject_Call((PyObject*)callable, arglist, NULL);
    Py_DECREF(arglist); arglist = NULL;
    PyObjCObject_ReleaseTransient(pyself, cookie); pyself = NULL;
    if (result == NULL) goto error;

    *pretval = PyObjC_PythonToId(result);
    Py_DECREF(result);
    PyGILState_Release(state);
    return;

error:
    *pretval = nil;
    Py_XDECREF(arglist);
    if (pyself) {
        PyObjCObject_ReleaseTransient(pyself, cookie);
    }
    PyObjCErr_ToObjCWithGILState(&state);
}

static PyObject*
call_NSDecimalNumber_decimalValue(
    PyObject* method, PyObject* self, PyObject* arguments)
{
    struct objc_super super;
    NSDecimal aDecimal;
    if (!PyArg_ParseTuple(arguments, "")) {
        return NULL;
    }

    PyObjC_DURING
        objc_superSetReceiver(super, PyObjCObject_GetObject(self));
        objc_superSetClass(super, PyObjCSelector_GetClass(method));

#if defined(__i386__)
        /* The call below doesn't work on i386, I'm not sure why.
         * Because nobody will every subclass NSDecimalNumber this is not
         * really a problem.
         */
        aDecimal = [PyObjCObject_GetObject(self) decimalValue];
#else
        ((void(*)(void*, struct objc_super*, SEL))objc_msgSendSuper_stret)(&aDecimal, &super,
                PyObjCSelector_GetSelector(method));
#endif

    PyObjC_HANDLER
        PyObjCErr_FromObjC(localException);
    PyObjC_ENDHANDLER

    if (PyErr_Occurred()) {
        return NULL;
    }

    return Decimal_New(&aDecimal);
}

static void
imp_NSDecimalNumber_decimalNumberWithDecimal_(
    ffi_cif* cif __attribute__((__unused__)),
    void* resp,
    void** args,
    void* callable)
{
    Class self = *(id*)args[0];
    NSDecimal aDecimal = *(NSDecimal*)args[2];
    id* pretval = (id*)resp;

    PyObject* result = NULL;
    PyObject* arglist = NULL;
    PyObject* v = NULL;
    PyObject* pyself = NULL;
    int cookie = 0;

    PyGILState_STATE state = PyGILState_Ensure();

    arglist = PyTuple_New(2);
    if (arglist == NULL) goto error;

    pyself = PyObjCClass_New(self);
    if (pyself == NULL) goto error;
    PyTuple_SetItem(arglist, 0, pyself);
    Py_INCREF(pyself);

    v = Decimal_New(&aDecimal);
    if (v == NULL) goto error;
    PyTuple_SetItem(arglist, 1, v);

    result = PyObject_Call((PyObject*)callable, arglist, NULL);
    Py_DECREF(arglist); arglist = NULL;
    Py_DECREF(pyself); pyself = NULL;
    if (result == NULL) goto error;

    *pretval = PyObjC_PythonToId(result);
    Py_DECREF(result);
    PyGILState_Release(state);
    return;

error:
    *pretval = nil;
    Py_XDECREF(arglist);
    if (pyself) {
        PyObjCObject_ReleaseTransient(pyself, cookie);
    }
    PyObjCErr_ToObjCWithGILState(&state);
}

static void
imp_NSDecimalNumber_decimalValue(
    ffi_cif* cif __attribute__((__unused__)),
    void* resp,
    void** args,
    void* callable)
{
    id self = *(id*)args[0];
    NSDecimal* pretval = (NSDecimal*)resp;
    NSDecimal* res = NULL;

    PyObject* result = NULL;
    PyObject* arglist = NULL;
    PyObject* v = NULL;
    PyObject* pyself = NULL;
    int cookie = 0;

    PyGILState_STATE state = PyGILState_Ensure();

    arglist = PyTuple_New(1);
    if (arglist == NULL) goto error;

    v = PyObjC_IdToPython(self);
    if (v == NULL) goto error;
    PyTuple_SetItem(arglist, 0, v);

    result = PyObject_Call((PyObject*)callable, arglist, NULL);
    Py_DECREF(arglist); arglist = NULL;
    PyObjCObject_ReleaseTransient(pyself, cookie); pyself = NULL;
    if (result == NULL) goto error;

    Decimal_Convert(result, &res);
    if (res == NULL) {
        Py_DECREF(result);
        goto error;
    }

    *pretval = *res;
    Py_DECREF(result);
    PyGILState_Release(state);
    return;

error:
    Py_XDECREF(arglist);
    if (pyself) {
        PyObjCObject_ReleaseTransient(pyself, cookie);
    }
    PyObjCErr_ToObjCWithGILState(&state);
}


int
PyObjC_setup_nsdecimal(PyObject* m)
{
    PyType_Ready(&Decimal_Type);

    if (PyModule_AddObject(m, "NSDecimal", (PyObject*)&Decimal_Type) == -1) {
        return -1;
    }

    if (@encode(NSDecimal)[1] == '?') {
        Decimal_Encoding[0] = '{';
        strcpy(Decimal_Encoding + 1, "_NSDecimal");
        strcpy(Decimal_Encoding + 11, @encode(NSDecimal) + 2);
        Decimal_Encoding_Len = strlen(Decimal_Encoding);
    }

    PyType_Ready(&Decimal_Type);

    if (PyModule_AddObject(m, "NSDecimal", (PyObject*)&Decimal_Type) == -1) {
        return -1;
    }

    Class classNSDecimalNumber = objc_lookUpClass("NSDecimalNumber");
    Class classNSNumber = objc_lookUpClass("NSNumber");

    if (PyObjC_RegisterMethodMapping(
            classNSDecimalNumber,
            @selector(initWithDecimal:),
            call_NSDecimalNumber_initWithDecimal_,
            imp_NSDecimalNumber_initWithDecimal_) < 0) {
        return -1;
    }

    Class classNSDecimalNumberPlaceholder = objc_lookUpClass("NSDecimalNumberPlaceholder");
    if (classNSDecimalNumberPlaceholder != nil) {
        if (PyObjC_RegisterMethodMapping(
            classNSDecimalNumberPlaceholder,
            @selector(initWithDecimal:),
            call_NSDecimalNumber_initWithDecimal_,
            imp_NSDecimalNumber_initWithDecimal_) < 0) {

            return -1;
        }
    }

    if (PyObjC_RegisterMethodMapping(
            classNSDecimalNumber,
            @selector(decimalNumberWithDecimal:),
            call_NSDecimalNumber_decimalNumberWithDecimal_,
            imp_NSDecimalNumber_decimalNumberWithDecimal_) < 0) {
        return -1;
    }

    if (PyObjC_RegisterMethodMapping(
            classNSNumber,
            @selector(decimalValue),
            call_NSDecimalNumber_decimalValue,
            imp_NSDecimalNumber_decimalValue) < 0) {
        return -1;
    }

    return 0;
}
