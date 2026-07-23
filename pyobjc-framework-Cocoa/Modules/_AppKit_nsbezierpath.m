/*
 * Several methods of NSBezierPath cannot be handled automatically because the
 * size of a C-style array depends on the value of another argument.
 */

NS_ASSUME_NONNULL_BEGIN

#if PyObjC_BUILD_RELEASE < 1014
#define NSBezierPathElementMoveTo NSMoveToBezierPathElement
#define NSBezierPathElementLineTo NSLineToBezierPathElement
#define NSBezierPathElementCurveTo NSCurveToBezierPathElement
#define NSBezierPathElementClosePath NSClosePathBezierPathElement
#endif
#if PyObjC_BUILD_RELEASE < 1400
#define NSBezierPathElementCubicCurveTo NSBezierPathElementCurveTo
#endif

static PyObject* _Nullable call_NSBezierPath_elementAtIndex_associatedPoints_(
    PyObject* method, PyObject* self, PyObject* _Nonnull const* _Nonnull arguments,
    size_t nargs)
{
    struct objc_super   super;
    NSInteger           idx;
    int                 pointCount;
    NSPoint             points[3];
    NSBezierPathElement res;

    if (nargs == 1) {
        if (PyErr_WarnEx(PyExc_DeprecationWarning,
                         "leaving of the second argument is deprecated", 0)
            < 0) {
            return NULL;
        }
        if (PyObjC_PythonToObjC(@encode(NSInteger), arguments[0], &idx) == -1) {
            return NULL;
        }
    } else {
        if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1) {
            return NULL;
        }
        if (PyObjC_PythonToObjC(@encode(NSInteger), arguments[0], &idx) == -1) {
            return NULL;
        }
        if (arguments[1] != Py_None) {
            PyErr_SetString(PyExc_ValueError, "buffer must be None");
            return NULL;
        }
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (PyObjCIMP_Check(method)) {
                res = ((NSBezierPathElement (*)(id, SEL, NSInteger,
                                                NSPoint*))PyObjCIMP_GetIMP(method))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), idx,
                    points);
            } else {
                super.super_class = PyObjCSelector_GetClass(method);
                super.receiver    = PyObjCObject_GetObject(self);

                res = ((NSBezierPathElement (*)(struct objc_super*, SEL, NSInteger,
                                                NSPoint*))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), idx, points);
            }
        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    switch (res) { // LCOV_BR_EXCL_LINE
    case NSBezierPathElementMoveTo:
        pointCount = 1;
        break;
    case NSBezierPathElementLineTo:
        pointCount = 1;
        break;
    case NSBezierPathElementCubicCurveTo:
        pointCount = 3;
        break;
#if PyObjC_BUILD_RELEASE >= 1400
    case NSBezierPathElementQuadraticCurveTo:
        pointCount = 1;
        break;
#endif
    case NSBezierPathElementClosePath:
        pointCount = 0;
        break;
    default:
        // LCOV_EXCL_START
        PyErr_SetString(PyExc_ValueError, "ObjC returned illegal value");
        return NULL;
        // LCOV_EXCL_STOP
    }

    return Py_BuildValue("NN", PyObjC_ObjCToPython(@encode(NSBezierPathElement), &res),
                         PyObjC_CArrayToPython(@encode(NSPoint), points, pointCount));
}

static PyObject* _Nullable call_NSBezierPath_setAssociatedPoints_atIndex_(
    PyObject* method, PyObject* self, PyObject* _Nonnull const* _Nonnull arguments,
    size_t nargs)
{
    PyObject*         result;
    struct objc_super super;
    NSInteger         idx;
    NSPoint           points[3];
    PyObject*         pointList;
    PyObject*         seq;
    int               i, len;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1) {
        return NULL;
    }
    pointList = arguments[0];
    if (PyObjC_PythonToObjC(@encode(NSInteger), arguments[1], &idx) == -1) {
        return NULL;
    }

    memset(points, 0, sizeof(points));

    seq = PySequence_Tuple(pointList);
    if (seq == NULL) {
        return NULL;
    }

    len = PyTuple_GET_SIZE(seq);
    if (len > 3) {
        Py_DECREF(seq);
        PyErr_SetString(PyExc_ValueError, "Need at most 3 elements");
        return NULL;
    }

    for (i = 0; i < len; i++) {
        int err =
            PyObjC_PythonToObjC(@encode(NSPoint), PyTuple_GET_ITEM(seq, i), points + i);
        if (err == -1) {
            return NULL;
        }
    }
    Py_DECREF(seq);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (PyObjCIMP_Check(method)) {
                ((void (*)(id, SEL, NSPoint*, NSInteger))PyObjCIMP_GetIMP(method))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), points,
                    idx);
            } else {
                super.super_class = PyObjCSelector_GetClass(method);
                super.receiver    = PyObjCObject_GetObject(self);

                ((void (*)(struct objc_super*, SEL, NSPoint*,
                           NSInteger))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), points, idx);
            }

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
            result = NULL;                       // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) // LCOV_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    result = Py_None;
    Py_INCREF(result);

    return result;
}

static IMP
mkimp_NSBezierPath_elementAtIndex_associatedPoints_(PyObject* callable,
                                                    PyObject* methodsignature)
{
    Py_INCREF(callable);
    NSBezierPathElement (^block)(NSBezierPath*, NSInteger, NSPointArray) = ^(
        NSBezierPath* self, NSInteger idx, NSPointArray points) {
      PyObject*           result;
      PyObject*           seq = NULL;
      PyObject*           arglist[4];
      int                 err;
      int                 pointCount;
      int                 i;
      int                 cookie = 0;
      NSBezierPathElement element;

      PyGILState_STATE state = PyGILState_Ensure();

      arglist[0] = NULL;

      arglist[1] = PyObjCObject_NewTransient(self, &cookie);
      if (arglist[1] == NULL) // LCOV_BR_EXCL_LINE
          goto error;         // LCOV_EXCL_LINE

      arglist[2] = PyLong_FromLong(idx);
      if (arglist[2] == NULL) // LCOV_BR_EXCL_LINE
          goto error;         // LCOV_EXCL_LINE

      arglist[3] = Py_None;

      result = PyObject_Vectorcall((PyObject*)callable, arglist + 1,
                                   3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      PyObjCObject_ReleaseTransient(arglist[1], cookie);
      arglist[1] = NULL;
      Py_CLEAR(arglist[2]);
      if (result == NULL)
          goto error;

      seq = PySequence_Tuple(result);
      Py_DECREF(result);
      if (seq == NULL)
          goto error;

      if (PyTuple_GET_SIZE(seq) != 2) {
          PyErr_SetString(PyExc_ValueError, "should return tuple of length 2");
          goto error;
      }

      PyObject* v;
      v = PyTuple_GET_ITEM(seq, 0);

      err = PyObjC_PythonToObjC(@encode(NSBezierPathElement), v, &element);
      if (err == -1)
          goto error;

      v = PySequence_Tuple(PyTuple_GET_ITEM(seq, 1));

      switch (element) {
      case NSBezierPathElementMoveTo:
          pointCount = 1;
          break;
      case NSBezierPathElementLineTo:
          pointCount = 1;
          break;
      case NSBezierPathElementCubicCurveTo:
          pointCount = 3;
          break;
#if PyObjC_BUILD_RELEASE >= 1400
      case NSBezierPathElementQuadraticCurveTo:
          pointCount = 1;
          break;
#endif
      case NSBezierPathElementClosePath:
          pointCount = 0;
          break;
      default:
          PyErr_SetString(PyExc_ValueError, "Return[0] should be NS{*}PathElement");
          Py_DECREF(v);
          goto error;
      }

      if (PyTuple_GET_SIZE(v) != pointCount) {
          PyErr_Format(PyExc_ValueError, "expected %ld points, got %ld", (long)pointCount,
                       (long)PyTuple_GET_SIZE(v));
          Py_DECREF(v);
          goto error;
      }

      for (i = 0; i < pointCount; i++) {
          err = PyObjC_PythonToObjC(@encode(NSPoint), PyTuple_GET_ITEM(v, i), points + i);
          if (err == -1) {
              Py_DECREF(v);
              goto error;
          }
      }

      Py_DECREF(v);
      Py_DECREF(seq);
      PyGILState_Release(state);
      return element;

  error:
      if (arglist[1]) { // LCOV_BR_EXCL_LINE
          // LCOV_EXCL_START
          PyObjCObject_ReleaseTransient(arglist[1], cookie);
          // LCOV_EXCL_STOP
      } // LCOV_EXCL_LINE
      Py_XDECREF(seq);
      PyObjCErr_ToObjCWithGILState(&state);
      __builtin_unreachable();
    };
    return imp_implementationWithBlock(block);
}

static int
setup_nsbezierpath(PyObject* m __attribute__((__unused__)))
{
    Class cls = objc_lookUpClass("NSBezierPath");
    if (!cls) {   // LCOV_BR_EXCL_LINE
        return 0; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterMethodMapping(cls, @selector(elementAtIndex:associatedPoints:),
                                     call_NSBezierPath_elementAtIndex_associatedPoints_,
                                     mkimp_NSBezierPath_elementAtIndex_associatedPoints_)
        < 0) { // LCOV_BR_EXCL_LINE

        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterMethodMapping(cls, @selector(setAssociatedPoints:atIndex:),
                                     call_NSBezierPath_setAssociatedPoints_atIndex_,
                                     PyObjCUnsupportedMethod_IMP)
        < 0) { // LCOV_BR_EXCL_LINE

        return -1; // LCOV_EXCL_LINE
    }
    return 0;
}

NS_ASSUME_NONNULL_END
