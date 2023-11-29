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

NS_ASSUME_NONNULL_BEGIN

static char      Decimal_Encoding[sizeof(@encode(NSDecimal)) + 32];
static size_t    Decimal_Encoding_Len   = 0;
static PyObject* _NSDecimalNumber_Class = NULL;

typedef struct {
    PyObject_HEAD
    NSDecimal value;
    NSDecimalNumber* _Nullable objc_value;
} DecimalObject;

#define Decimal_Value(v) ((DecimalObject*)(v))->value

static PyObject* _Nullable Decimal_New(const NSDecimal* aDecimal);
static PyObject* _Nullable decimal_repr(PyObject* self);
static PyObject* _Nullable decimal_richcompare(PyObject* self, PyObject* other, int type);
static void decimal_dealloc(PyObject* self);
static int  decimal_init(PyObject* self, PyObject* _Nullable args,
                         PyObject* _Nullable kwds);
static PyObject* _Nullable decimal_new(PyTypeObject* type, PyObject* _Nullable args,
                                       PyObject* _Nullable kwds);
static PyObject* _Nullable decimal_asint(PyObject* self);
static PyObject* _Nullable decimal_asfloat(PyObject* self);
static PyObject* _Nullable decimal_add(PyObject* left, PyObject* right);
static PyObject* _Nullable decimal_subtract(PyObject* left, PyObject* right);
static PyObject* _Nullable decimal_multiply(PyObject* left, PyObject* right);
static PyObject* _Nullable decimal_divide(PyObject* left, PyObject* right);
static PyObject* _Nullable decimal_floordivide(PyObject* left, PyObject* right);
static PyObject* _Nullable decimal_power(PyObject* left, PyObject* right,
                                         PyObject* power);
static int decimal_nonzero(PyObject* self);
static int decimal_coerce(PyObject* _Nonnull* l, PyObject* _Nonnull* r);
static int decimal_coerce_compare(PyObject* _Nonnull* l, PyObject* _Nonnull* r);
static PyObject* _Nullable decimal_positive(PyObject* self);
static PyObject* _Nullable decimal_negative(PyObject* self);
static PyObject* _Nullable decimal_absolute(PyObject* self);
static PyObject* _Nullable decimal_round(PyObject* self, PyObject* _Nullable args,
                                         PyObject* _Nullable kwds);
static Py_hash_t decimal_hash(PyObject* o);

static NSDecimalNumber*
Decimal_ObjCValue(PyObject* self)
{
    DecimalObject*   pyself = (DecimalObject*)self;
    NSDecimalNumber* res    = pyself->objc_value;

    if (!res) {
        res = pyself->objc_value =
            [[NSDecimalNumber alloc] initWithDecimal:Decimal_Value(self)];
    }
    return res;
}

static PyObject* _Nullable decimal_get__pyobjc_object__(PyObject* self, void* closure
                                                        __attribute__((__unused__)))
{
    return PyObjCObject_New(Decimal_ObjCValue(self), 0, YES);
}

static PyGetSetDef decimal_getset[] = {{
                                           .name = "__pyobjc_object__",
                                           .get  = (getter)decimal_get__pyobjc_object__,
                                           .doc  = "NSDecimalNumber instance",
                                       },
                                       {
                                           .name = NULL /* SENTINEL */
                                       }};

static PyMethodDef decimal_methods[] = {{.ml_name  = "as_int",
                                         .ml_meth  = (PyCFunction)decimal_asint,
                                         .ml_flags = METH_NOARGS,
                                         .ml_doc   = "Convert decimal to a Python int"},
                                        {.ml_name  = "as_float",
                                         .ml_meth  = (PyCFunction)decimal_asfloat,
                                         .ml_flags = METH_NOARGS,
                                         .ml_doc   = "Convert decimal to a Python float"},
                                        {.ml_name  = "__round__",
                                         .ml_meth  = (PyCFunction)decimal_round,
                                         .ml_flags = METH_VARARGS | METH_KEYWORDS},
                                        {
                                            .ml_name = NULL /* SENTINEL */
                                        }};

static PyObject*
decimal_getattro(PyObject* o, PyObject* attr_name)
{
    return PyObject_GenericGetAttr(o, attr_name);
}

static PyObject* Decimal_Type;

PyDoc_STRVAR(decimal_cls_doc, "NSDecimal wrapper");

static PyType_Slot decimal_slots[] = {
    {.slot = Py_tp_dealloc, .pfunc = (void*)&decimal_dealloc},
    {.slot = Py_tp_repr, .pfunc = (void*)&decimal_repr},
    {.slot = Py_tp_str, .pfunc = (void*)&decimal_repr},
    {.slot = Py_tp_hash, .pfunc = (void*)&decimal_hash},
    {.slot = Py_tp_getattro, .pfunc = (void*)&decimal_getattro},
    {.slot = Py_tp_setattro, .pfunc = (void*)&PyObject_GenericSetAttr},
    {.slot = Py_tp_doc, .pfunc = (void*)&decimal_cls_doc},
    {.slot = Py_tp_richcompare, .pfunc = (void*)&decimal_richcompare},
    {.slot = Py_tp_methods, .pfunc = (void*)&decimal_methods},
    {.slot = Py_tp_getset, .pfunc = (void*)&decimal_getset},
    {.slot = Py_tp_new, .pfunc = (void*)&decimal_new},
    {.slot = Py_nb_add, .pfunc = (void*)&decimal_add},
    {.slot = Py_nb_subtract, .pfunc = (void*)&decimal_subtract},
    {.slot = Py_nb_multiply, .pfunc = (void*)&decimal_multiply},
    {.slot = Py_nb_power, .pfunc = (void*)&decimal_power},
    {.slot = Py_nb_negative, .pfunc = (void*)&decimal_negative},
    {.slot = Py_nb_positive, .pfunc = (void*)&decimal_positive},
    {.slot = Py_nb_absolute, .pfunc = (void*)&decimal_absolute},
    {.slot = Py_nb_bool, .pfunc = (void*)&decimal_nonzero},
    {.slot = Py_nb_floor_divide, .pfunc = (void*)&decimal_floordivide},
    {.slot = Py_nb_true_divide, .pfunc = (void*)&decimal_divide},

    {0, NULL} /* sentinel */
};

static PyType_Spec decimal_spec = {
    .name      = "objc.NSDecimal",
    .basicsize = sizeof(DecimalObject),
    .itemsize  = 0,
#if PY_VERSION_HEX >= 0x030a0000
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE | Py_TPFLAGS_IMMUTABLETYPE,
#else
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE,
#endif
    .slots = decimal_slots,
};

#define Decimal_Check(obj) PyObject_TypeCheck(obj, (PyTypeObject*)Decimal_Type)

static void
DecimalFromString(NSDecimal* aDecimal, NSString* aString,
                  void* _Nullable locale __attribute__((__unused__)))
{
    NSDecimalNumber* num;

    num       = [[NSDecimalNumber alloc] initWithString:aString];
    *aDecimal = [num decimalValue];
    [num release];
}

static void
DecimalFromComponents(NSDecimal* aDecimal, unsigned long long mantissa,
                      unsigned short exponent, BOOL negative)
{
    NSDecimalNumber* num;

    num = [[NSDecimalNumber alloc] initWithMantissa:mantissa
                                           exponent:exponent
                                         isNegative:negative];

    *aDecimal = [num decimalValue];
    [num release];
}

static PyObject*
decimal_new(PyTypeObject* type __attribute__((__unused__)), PyObject* _Nullable args,
            PyObject* _Nullable kwds)
{
    DecimalObject* self;

    self = PyObject_New(DecimalObject, (PyTypeObject*)Decimal_Type);
    if (self == NULL) {          // LCOV_BR_EXCL_LINE
        return PyErr_NoMemory(); // LCOV_EXCL_LINE
    }

    memset(&self->value, 0, sizeof(self->value));
    self->objc_value = nil;
    if ((args == NULL || PyTuple_Size(args) == 0)
        && (kwds == NULL || PyDict_Size(kwds) == 0)) {
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
    [((DecimalObject*)self)->objc_value release];
#if PY_VERSION_HEX >= 0x030a0000
    PyTypeObject* tp = Py_TYPE(self);
#endif
    PyObject_Free(self);
#if PY_VERSION_HEX >= 0x030a0000
    Py_DECREF(tp);
#endif
}

int
PyObjC_number_to_decimal(PyObject* pyValue, NSDecimal* outResult)
{
    BOOL               negative;
    unsigned long long mantissa;
    short int          exponent;

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

    } else if (PyFloat_Check(pyValue)) {
        /* Explicit conversion from float to NSDecimal
         * first convert the float to a string using repr, that
         * is easier than extracting the components of the
         * float.
         *
         * Previous versions converted to NSString through
         * PyObject_Repr(), but that might give an incorrect
         * value for float subclasses with an overridden __repr__,
         * which includes for example a float enum:
         *
         *     class FloatEnum(float, enum.Enum): ...
         */
        NSString* stringVal;
        stringVal = [[NSString alloc] initWithFormat:@"%.*g",
#ifdef DBL_DECIMAL_DIG
                                                     DBL_DECIMAL_DIG,
#elif defined(__DBL_DECIMAL_DIG__)
                                                     /* With Xcode 7.3 (macOS 10.11) the
                                                        public macro is not available */
                                                     __DBL_DECIMAL_DIG__,
#else
                                                     __DECIMAL_DIG__,
#endif
                                                     PyFloat_AsDouble(pyValue)];
        if (stringVal == nil) {
            PyErr_SetString(PyObjCExc_Error, "Converting double to NSString failed");
            return -1;
        }

        @try {
            DecimalFromString(outResult, stringVal, NULL);

            // LCOV_EXCL_START
            /* Experiments show that DecimalFromString won't raise, but
             * returns a NaN value if the input cannot be parsed.
             */
        } @catch (NSObject* localException) {
            PyObjCErr_FromObjC(localException);
        }
        // LCOV_EXCL_STOP

        [stringVal release];

        if (PyErr_Occurred()) // LCOV_BR_EXCL_LINE
            return -1;        // LCOV_EXCL_LINE
        return 0;
    }

    if (_NSDecimalNumber_Class == NULL) {
        _NSDecimalNumber_Class = PyObjCClass_New([NSDecimalNumber class]);
        if (_NSDecimalNumber_Class == NULL) { // LCOV_BR_EXCL_LINE
            PyErr_Clear();                    // LCOV_EXCL_LINE
        }
    }

    if (_NSDecimalNumber_Class != NULL
        && PyObject_IsInstance(pyValue, _NSDecimalNumber_Class)) {
        NSDecimalNumber* val = PyObjCObject_GetObject(pyValue);
        *outResult           = [val decimalValue];
        return 0;
    }

    PyErr_Format(PyExc_TypeError, "cannot convert instance of %s to NSDecimal",
                 pyValue->ob_type->tp_name);
    return -1;
}

/* NOTE: This is intentionally not in the tp_init slot, that would make NSDecimal
 * objects mutable.
 */
static int
decimal_init(PyObject* self, PyObject* _Nullable args, PyObject* _Nullable kwds)
{
    static char*       keywords[]  = {"mantissa", "exponent", "isNegative", NULL};
    static char*       keywords2[] = {"string", NULL};
    PyObject*          pyMantissa;
    PyObject*          pyExponent;
    PyObject*          pyNegative;
    BOOL               negative;
    unsigned long long mantissa;
    short int          exponent;

    ((DecimalObject*)self)->objc_value = nil;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "OOO", keywords, &pyMantissa,
                                     &pyExponent, &pyNegative)) {
        PyObject* pyValue;

        PyErr_Clear();
        if (!PyArg_ParseTupleAndKeywords(args, kwds, "O", keywords2, &pyValue)) {
            PyErr_SetString(
                PyExc_TypeError,
                "NSDecimal(value) or NSDecimal(mantissa, exponent, isNegative)");
            return -1;
        }

        if (PyObjCObject_Check(pyValue)) {
            NSObject* value;

            if (depythonify_python_object(pyValue, &value) == -1) {
                return -1;
            }

            if ([value isKindOfClass:[NSDecimalNumber class]]) {
                ((DecimalObject*)self)->value = [(NSDecimalNumber*)value decimalValue];

                ((DecimalObject*)self)->objc_value = (NSDecimalNumber*)value;
                [value retain];
                return 0;
            }

            PyErr_Format(PyExc_TypeError, "cannot convert instance of %s to NSDecimal",
                         pyValue->ob_type->tp_name);
            return -1;

        } else if (PyUnicode_Check(pyValue)) {

            NSString* stringVal;

            if (depythonify_python_object(pyValue, &stringVal) == -1) {
                return -1;
            }
            Py_BEGIN_ALLOW_THREADS
                @try {
                    DecimalFromString(&Decimal_Value(self), stringVal, NULL);

                    // LCOV_EXCL_START
                    // DecimalFromString does not raise, but returns a NaN on
                    // invalid values.
                } @catch (NSObject* localException) {
                    PyObjCErr_FromObjC(localException);
                }
                // LCOV_EXCL_STOP
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred()) // LCOV_BR_EXCL_LINE
                return -1;        // LCOV_EXCL_LINE
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

    DecimalFromComponents(&Decimal_Value(self), mantissa, exponent, negative);

    return 0;
}

static Py_hash_t
decimal_hash(PyObject* self)
{
    NSString*  strrepr = NSDecimalString(&Decimal_Value(self), nil);
    NSUInteger hash    = [strrepr hash];

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

        PyErr_Format(PyExc_TypeError, "Cannot compare NSDecimal and %s",
                     other->ob_type->tp_name);
        return NULL;
    }

    if (PyErr_Occurred()) {
        return NULL;
    }

    res = NSDecimalCompare(&Decimal_Value(self), &Decimal_Value(other));

    switch (type) {
    case Py_LT:
        return PyBool_FromLong(res == NSOrderedAscending);
    case Py_LE:
        return PyBool_FromLong(res != NSOrderedDescending);
    case Py_EQ:
        return PyBool_FromLong(res == NSOrderedSame);
    case Py_NE:
        return PyBool_FromLong(res != NSOrderedSame);
    case Py_GE:
        return PyBool_FromLong(res != NSOrderedAscending);
    case Py_GT:
        return PyBool_FromLong(res == NSOrderedDescending);
    default:
        // LCOV_EXCL_START
        PyErr_SetString(PyExc_TypeError, "Bad comparison arg");
        return NULL;
        // LCOV_EXCL_STOP
    }
}

static PyObject*
decimal_asint(PyObject* self)
{
    NSDecimalNumber* tmp = Decimal_ObjCValue(self);
    return PyLong_FromLong([tmp longValue]);
}

static PyObject*
decimal_asfloat(PyObject* self)
{
    NSDecimalNumber* tmp = Decimal_ObjCValue(self);
    return PyFloat_FromDouble([tmp doubleValue]);
}

static PyObject*
decimal_power(PyObject* left __attribute__((__unused__)),
              PyObject* right __attribute__((__unused__)),
              PyObject* extra __attribute__((__unused__)))
{
    PyErr_SetString(PyExc_TypeError, "pow() and ** are not supported for NSDecimal");
    return NULL;
}

static PyObject* _Nullable decimal_result_to_python(NSCalculationError status,
                                                    NSDecimal* value, bool round_down)
{
    /* XXX: Need tests that trigger these errors, including the loss of precision one */
    NSDecimal value2;
    switch (status) {
    case NSCalculationOverflow:
        PyErr_SetString(PyExc_OverflowError, "Numeric overflow");
        return NULL;
    case NSCalculationUnderflow:
        PyErr_SetString(PyExc_OverflowError, "Numeric underflow");
        return NULL;
    case NSCalculationDivideByZero:
        PyErr_SetString(PyExc_ZeroDivisionError, "Division by zero");
        return NULL;
    /*
     * Ignore these:
     */
    case NSCalculationLossOfPrecision:
    case NSCalculationNoError:
        break;
    }

    if (round_down) {
        NSDecimalRound(&value2, value, 0, NSRoundDown);
        NSDecimalCompact(&value2);
        return Decimal_New(&value2);
    } else {
        NSDecimalCompact(value);
        return Decimal_New(value);
    }
}

#define TRY_COERCE(left, right)                                                          \
    int r = decimal_coerce(&left, &right);                                               \
    if (r == 1) {                                                                        \
        Py_INCREF(Py_NotImplemented);                                                    \
        return Py_NotImplemented;                                                        \
    }

#define DECIMAL_OPERATOR(py_function, nsdecimal_function)                                \
    static PyObject* py_function(PyObject* left, PyObject* right)                        \
    {                                                                                    \
        NSDecimal          result;                                                       \
        NSCalculationError err;                                                          \
                                                                                         \
        TRY_COERCE(left, right);                                                         \
                                                                                         \
        err = nsdecimal_function(&result, &Decimal_Value(left), &Decimal_Value(right),   \
                                 NSRoundPlain);                                          \
        return decimal_result_to_python(err, &result, false);                            \
    }

DECIMAL_OPERATOR(decimal_add, NSDecimalAdd)
DECIMAL_OPERATOR(decimal_subtract, NSDecimalSubtract)
DECIMAL_OPERATOR(decimal_multiply, NSDecimalMultiply)
DECIMAL_OPERATOR(decimal_divide, NSDecimalDivide)

static PyObject*
decimal_floordivide(PyObject* left, PyObject* right)
{
    NSDecimal          result;
    NSCalculationError err;

    TRY_COERCE(left, right);

    err = NSDecimalDivide(&result, &Decimal_Value(left), &Decimal_Value(right),
                          NSRoundPlain);
    return decimal_result_to_python(err, &result, true);
}

static int
decimal_nonzero(PyObject* self)
{
    NSDecimal zero;

    DecimalFromComponents(&zero, 0, 0, 0);

    return NSDecimalCompare(&zero, &Decimal_Value(self)) != NSOrderedSame;
}

static PyObject*
decimal_positive(PyObject* self)
{
    Py_INCREF(self);
    return self;
}

static PyObject*
decimal_negative(PyObject* self)
{
    NSDecimal          result;
    NSCalculationError err;
    NSDecimal          zero;
    DecimalFromComponents(&zero, 0, 0, 0);

    err = NSDecimalSubtract(&result, &zero, &Decimal_Value(self), NSRoundPlain);
    return decimal_result_to_python(err, &result, false);
}

static PyObject*
decimal_absolute(PyObject* self)
{
    NSDecimal          result;
    NSCalculationError err;
    NSDecimal          zero;
    DecimalFromComponents(&zero, 0, 0, 0);

    switch (NSDecimalCompare(&zero, &Decimal_Value(self))) {
    case NSOrderedSame:
    case NSOrderedAscending:
        /* self >= 0 */
        Py_INCREF(self);
        return self;

    case NSOrderedDescending:;
    }

    err = NSDecimalSubtract(&result, &zero, &Decimal_Value(self), NSRoundPlain);
    return decimal_result_to_python(err, &result, false);
}

static PyObject* _Nullable decimal_round(PyObject* self, PyObject* _Nullable args,
                                         PyObject* _Nullable kwds)
{
    static char* keywords[] = {"digits", NULL};
    Py_ssize_t   digits     = 0;
    NSDecimal    result;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|n", keywords, &digits)) {
        return NULL;
    }

    NSDecimalRound(&result, &Decimal_Value(self), digits, NSRoundPlain);
    NSDecimalCompact(&result);
    return Decimal_New(&result);
}

/* XXX: Can 'l' ever be something else than NSDecimal? */
static int
decimal_coerce(PyObject** l, PyObject** r)
{
    PyObject* right = NULL;
    PyObject* left  = NULL;
    PyObject* args  = NULL;
    int       res;

    if (Decimal_Check(*l) && Decimal_Check(*r)) {
        Py_INCREF(*l);
        Py_INCREF(*r);
        return 0;
    }

    if (!Decimal_Check(*l)) {
        /* The test is needed to avoid silently converting strings */
        if (PyBytes_Check(*l) || PyUnicode_Check(*l) || PyFloat_Check(*l))
            goto error;

        left = (PyObject*)PyObject_New(DecimalObject, (PyTypeObject*)Decimal_Type);
        if (left == NULL) // LCOV_BR_EXCL_LINE
            goto error;   // LCOV_EXCL_LINE

        args = Py_BuildValue("(O)", *l); /* XXX: really? */
        if (args == NULL)                // LCOV_BR_EXCL_LINE
            goto error;                  // LCOV_EXCL_LINE

        res = decimal_init(left, args, NULL);
        if (res == -1)
            goto error;

        Py_DECREF(args);
        args = NULL;
    }

    if (!Decimal_Check(*r)) {
        /* The test is needed to avoid silently converting strings */
        if (PyBytes_Check(*r) || PyUnicode_Check(*r) || PyFloat_Check(*r))
            goto error;

        right = (PyObject*)PyObject_New(DecimalObject, (PyTypeObject*)Decimal_Type);
        if (right == NULL) // LCOV_BR_EXCL_LINE
            goto error;    // LCOV_EXCL_LINE

        args = Py_BuildValue("(O)", *r); /* XXX: really? */
        if (args == NULL)                // LCOV_BR_EXCL_LINE
            goto error;                  // LCOV_EXCL_LINE

        res = decimal_init(right, args, NULL);
        if (res == -1)
            goto error;

        Py_DECREF(args);
        args = NULL;
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

static int
decimal_coerce_compare(PyObject** l, PyObject** r)
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
    PyObject* tmp = id_to_python(val);
    if (tmp == NULL) { // LCOV_BR_EXCL_START
        return NULL;   // LCOV_EXCL_STOP
    }
    PyObject* repr = PyObject_Str(tmp);
    Py_XDECREF(tmp);
    return repr;
}

static inline int
Decimal_Convert(PyObject* self, void* val)
{
    if (Decimal_Check(self)) {
        *(NSDecimal**)val = &Decimal_Value(self);
        return 1;
    }
    PyErr_Format(PyExc_TypeError, "Expecting an NSDecimal, got instance of '%s'",
                 Py_TYPE(self)->tp_name);
    return 0;
}

static PyObject*
Decimal_New(const NSDecimal* aDecimal)
{
    DecimalObject* result;

    result = PyObject_New(DecimalObject, (PyTypeObject*)Decimal_Type);
    if (result == NULL) // LCOV_BR_EXCL_LINE
        return NULL;    // LCOV_EXCL_LINE

    result->objc_value = nil;
    result->value      = *aDecimal;
    return (PyObject*)result;
}

PyObject*
pythonify_nsdecimal(const void* value)
{
    PyObject* v;
    v = Decimal_New((const NSDecimal*)value);
    return v;
}

int
depythonify_nsdecimal(PyObject* value, void* ptr)
{
    if (Decimal_Check(value)) {
        *(NSDecimal*)ptr = Decimal_Value(value);
        return 0;

    } else {
        PyErr_Format(PyExc_TypeError, "Expecting an NSDecimal, got instance of '%s'",
                     Py_TYPE(value)->tp_name);
        return -1;
    }
}

int
IS_DECIMAL(const char* typestr)
{
    return (strncmp(typestr, @encode(NSDecimal), sizeof(@encode(NSDecimal)) - 1) == 0)
           || (Decimal_Encoding_Len != 0
               && strncmp(typestr, Decimal_Encoding, Decimal_Encoding_Len) == 0);
}

static PyObject* _Nullable call_NSDecimalNumber_decimalNumberWithDecimal_(
    PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    NSDecimal*        aDecimal;
    id                res;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (Decimal_Check(arguments[0])) {
        aDecimal = &Decimal_Value(arguments[0]);
    } else {
        PyErr_Format(PyExc_TypeError, "Expecting an NSDecimal, got instance of '%s'",
                     Py_TYPE(arguments[0])->tp_name);
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            super.super_class = object_getClass(PyObjCSelector_GetClass(method));
            super.receiver    = object_getClass(PyObjCClass_GetClass(self));

            res = ((id(*)(struct objc_super*, SEL, NSDecimal))objc_msgSendSuper)(
                &super, PyObjCSelector_GetSelector(method), *aDecimal);
            // LCOV_EXCL_START
            // AFAIK the method won't raise.
        } @catch (NSObject* localException) {
            PyObjCErr_FromObjC(localException);
            res = nil;
        }
        // LCOV_EXCL_STOP
    Py_END_ALLOW_THREADS

    if (res == nil && PyErr_Occurred()) {
        return NULL;
    }

    return id_to_python(res);
}

static PyObject* _Nullable call_NSDecimalNumber_initWithDecimal_(
    PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    NSDecimal*        aDecimal;
    id                res;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (Decimal_Check(arguments[0])) {
        aDecimal = &Decimal_Value(arguments[0]);
    } else {
        PyErr_Format(PyExc_TypeError, "Expecting an NSDecimal, got instance of '%s'",
                     Py_TYPE(arguments[0])->tp_name);
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            super.super_class = PyObjCSelector_GetClass(method);
            super.receiver    = PyObjCObject_GetObject(self);

            res = ((id(*)(struct objc_super*, SEL, NSDecimal))objc_msgSendSuper)(
                &super, PyObjCSelector_GetSelector(method), *aDecimal);
            // LCOV_EXCL_START
            // AFAIK the method won't raise.
        } @catch (NSObject* localException) {
            PyObjCErr_FromObjC(localException);
            res = nil;
        }
        // LCOV_EXCL_STOP
    Py_END_ALLOW_THREADS

    if (res == nil && PyErr_Occurred()) {
        return NULL;
    }

    return id_to_python(res);
}

static IMP
mkimp_NSDecimalNumber_initWithDecimal_(PyObject* callable, PyObjCMethodSignature* methinfo
                                       __attribute__((__unused__)))
{
    Py_INCREF(callable);
    NSDecimalNumber* (^block)(NSDecimalNumber*, NSDecimal) =
        ^(NSDecimalNumber* _Nullable self, NSDecimal aDecimal) {
          NSDecimalNumber* rv;
          PyObject*        result = NULL;
          PyObject*        v      = NULL;
          PyObject*        pyself = NULL;
          int              cookie = 0;

          PyGILState_STATE state = PyGILState_Ensure();

          pyself = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL)
              goto error;

          v = Decimal_New(&aDecimal);
          if (v == NULL)
              goto error;

          PyObject* arglist[3] = {NULL, pyself, v};
          result               = PyObject_Vectorcall((PyObject*)callable, arglist + 1,
                                                     2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          Py_DECREF(v);
          v = NULL;
          PyObjCObject_ReleaseTransient(pyself, cookie);
          pyself = NULL;
          if (result == NULL) {
              goto error;
          }

          if (depythonify_python_object(result, &rv) == -1) {
              Py_DECREF(result);
              goto error;
          }
          Py_DECREF(result);
          PyGILState_Release(state);
          return rv;

      error:
          Py_XDECREF(v);
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }
          PyObjCErr_ToObjCWithGILState(&state);
          return (NSDecimalNumber*)nil;
        };
    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_NSDecimalNumber_decimalValue(PyObject*        method,
                                                             PyObject*        self,
                                                             PyObject* const* arguments
                                                             __attribute__((__unused__)),
                                                             size_t nargs)
{
    struct objc_super super;
    NSDecimal         aDecimal;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    Py_BEGIN_ALLOW_THREADS
        @try {
            super.super_class = PyObjCSelector_GetClass(method);
            super.receiver    = PyObjCObject_GetObject(self);

#if defined(__arm64__)
            aDecimal = ((NSDecimal(*)(struct objc_super*, SEL))objc_msgSendSuper)(
                &super, PyObjCSelector_GetSelector(method));
#else
            ((void (*)(void*, struct objc_super*, SEL))objc_msgSendSuper_stret)(
                &aDecimal, &super, PyObjCSelector_GetSelector(method));
#endif

        } @catch (NSObject* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return Decimal_New(&aDecimal);
}

static IMP
mkimp_NSDecimalNumber_decimalNumberWithDecimal_(PyObject*              callable,
                                                PyObjCMethodSignature* methinfo
                                                __attribute__((__unused__)))
{
    Py_INCREF(callable);
    NSDecimalNumber* (^block)(Class, NSDecimal) =
        ^(Class _Nullable self, NSDecimal aDecimal) {
          NSDecimalNumber* rv;
          PyObject*        result = NULL;
          PyObject*        v      = NULL;
          PyObject*        pyself = NULL;

          PyGILState_STATE state = PyGILState_Ensure();

          pyself = PyObjCClass_New(self);
          if (pyself == NULL)
              goto error;

          v = Decimal_New(&aDecimal);
          if (v == NULL)
              goto error;

          PyObject* arglist[3] = {NULL, pyself, v};

          result = PyObject_Vectorcall((PyObject*)callable, arglist + 1,
                                       2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          Py_DECREF(v);
          v = NULL;
          Py_DECREF(pyself);
          pyself = NULL;
          if (result == NULL) {
              goto error;
          }

          if (depythonify_python_object(result, &rv) == -1) {
              Py_DECREF(result);
              goto error;
          }
          Py_DECREF(result);
          PyGILState_Release(state);
          return rv;

      error:
          Py_XDECREF(v);
          Py_XDECREF(pyself);
          PyObjCErr_ToObjCWithGILState(&state);
          return (NSDecimalNumber*)nil;
        };
    return imp_implementationWithBlock(block);
}

static IMP
mkimp_NSDecimalNumber_decimalValue(PyObject* callable, PyObjCMethodSignature* methinfo
                                   __attribute__((__unused__)))
{
    Py_INCREF(callable);

    NSDecimal (^block)(id) = ^(id _Nullable self) {
      NSDecimal* res = NULL;

      PyObject* result = NULL;
      PyObject* v      = NULL;

      PyGILState_STATE state = PyGILState_Ensure();

      v = id_to_python(self);
      if (v == NULL)
          goto error;

      PyObject* arglist[2] = {NULL, v};
      result               = PyObject_Vectorcall((PyObject*)callable, arglist + 1,
                                                 1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      Py_DECREF(v);
      v = NULL;
      if (result == NULL)
          goto error;

      Decimal_Convert(result, &res);
      if (res == NULL) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      PyGILState_Release(state);
      return *res;

  error:
      Py_XDECREF(v);
      PyObjCErr_ToObjCWithGILState(&state);
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wunreachable-code"

      __builtin_unreachable(); // LCOV_EXCL_LINE
#pragma clang diagnostic pop
    };
    return imp_implementationWithBlock(block);
}

int
PyObjC_setup_nsdecimal(PyObject* m)
{
    Decimal_Type = PyType_FromSpec(&decimal_spec);
    if (Decimal_Type == NULL) { // LCOV_BR_EXCL_LINE
        return -1;              // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, "NSDecimal", Decimal_Type) == -1) { // LCOV_BR_EXCL_LINE
        return -1;                                                // LCOV_EXCL_LINE
    }
    Py_INCREF(Decimal_Type);

    if (@encode(NSDecimal)[1] == '?') {
        Decimal_Encoding[0] = '{';
        strcpy(Decimal_Encoding + 1, "_NSDecimal");
        strcpy(Decimal_Encoding + 11, @encode(NSDecimal) + 2);
        Decimal_Encoding_Len = strlen(Decimal_Encoding);
    }

    Class classNSDecimalNumber = objc_lookUpClass("NSDecimalNumber");
    Class classNSNumber        = objc_lookUpClass("NSNumber");

    if (PyObjC_RegisterMethodMapping( // LCOV_BR_EXCL_LINE
            classNSDecimalNumber, @selector(initWithDecimal:),
            call_NSDecimalNumber_initWithDecimal_, mkimp_NSDecimalNumber_initWithDecimal_)
        < 0) {
        return -1; // LCOV_EXCL_LINE
    }

    Class classNSDecimalNumberPlaceholder =
        objc_lookUpClass("NSDecimalNumberPlaceholder");
    if (classNSDecimalNumberPlaceholder != nil) { // LCOV_BR_EXCL_LINE
        if (PyObjC_RegisterMethodMapping(classNSDecimalNumberPlaceholder,
                                         @selector(initWithDecimal:),
                                         call_NSDecimalNumber_initWithDecimal_,
                                         mkimp_NSDecimalNumber_initWithDecimal_)
            < 0) {

            return -1; // LCOV_EXCL_LINE
        }
    }

    if (PyObjC_RegisterMethodMapping(classNSDecimalNumber, // LCOV_BR_EXCL_LINE
                                     @selector(decimalNumberWithDecimal:),
                                     call_NSDecimalNumber_decimalNumberWithDecimal_,
                                     mkimp_NSDecimalNumber_decimalNumberWithDecimal_)
        < 0) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterMethodMapping( // LCOV_BR_EXCL_LINE
            classNSNumber, @selector(decimalValue), call_NSDecimalNumber_decimalValue,
            mkimp_NSDecimalNumber_decimalValue)
        < 0) {
        return -1; // LCOV_EXCL_LINE
    }

    return 0;
}

NS_ASSUME_NONNULL_END
