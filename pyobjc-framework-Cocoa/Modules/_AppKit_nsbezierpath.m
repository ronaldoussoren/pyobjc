/*
 * Several methods of NSBezierPath cannot be handled automatically because the
 * size of a C-style array depends on the value of another argument.
 */

#if PyObjC_BUILD_RELEASE < 1014
#define NSBezierPathElementMoveTo NSMoveToBezierPathElement
#define NSBezierPathElementLineTo NSLineToBezierPathElement
#define NSBezierPathElementCurveTo NSCurveToBezierPathElement
#define NSBezierPathElementClosePath NSClosePathBezierPathElement
#endif
#if PyObjC_BUILD_RELEASE < 1400
#define NSBezierPathElementCubicCurveTo NSBezierPathElementCurveTo
#endif

static PyObject*
call_NSBezierPath_elementAtIndex_associatedPoints_(PyObject* method, PyObject* self,
                                                   PyObject* const* arguments,
                                                   size_t           nargs)
{
    PyObject*           result;
    PyObject*           v;
    struct objc_super   super;
    NSInteger           idx;
    int                 pointCount;
    NSPoint             points[3];
    NSBezierPathElement res;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(NSInteger), arguments[0], &idx) == -1) {
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (PyObjCIMP_Check(method)) {
                res = ((NSBezierPathElement(*)(id, SEL, NSInteger,
                                               NSPoint*))PyObjCIMP_GetIMP(method))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), idx,
                    points);
            } else {
                super.super_class = PyObjCSelector_GetClass(method);
                super.receiver    = PyObjCObject_GetObject(self);

                res = ((NSBezierPathElement(*)(struct objc_super*, SEL, NSInteger,
                                               NSPoint*))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), idx, points);
            }
        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    switch (res) {
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
        PyErr_SetString(PyExc_ValueError, "ObjC returned illegal value");
        return NULL;
    }

    result = PyTuple_New(2);
    if (result == NULL)
        return NULL;

    v = PyObjC_ObjCToPython(@encode(NSBezierPathElement), &res);
    if (v == NULL) {
        Py_DECREF(result);
        return NULL;
    }

    PyTuple_SetItem(result, 0, v);

    v = PyObjC_CArrayToPython(@encode(NSPoint), points, pointCount);
    if (v == NULL) {
        Py_DECREF(result);
        return NULL;
    }
    PyTuple_SetItem(result, 1, v);

    return result;
}

static PyObject*
call_NSBezierPath_setAssociatedPoints_atIndex_(PyObject* method, PyObject* self,
                                               PyObject* const* arguments, size_t nargs)
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

    seq = PySequence_Fast(pointList, "points is not a sequence");
    if (seq == NULL) {
        return NULL;
    }

    len = PySequence_Fast_GET_SIZE(seq);
    if (len > 3) {
        Py_DECREF(seq);
        PyErr_SetString(PyExc_ValueError, "Need at most 3 elements");
        return NULL;
    }

    for (i = 0; i < len; i++) {
        int err = PyObjC_PythonToObjC(@encode(NSPoint), PySequence_Fast_GET_ITEM(seq, i),
                                      points + i);
        if (err == -1) {
            return NULL;
        }
    }

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

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
            result = NULL;
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred())
        return NULL;

    result = Py_None;
    Py_INCREF(result);

    return result;
}

static IMP
mkimp_NSBezierPath_elementAtIndex_associatedPoints_(PyObject* callable,
                                                    PyObject* methodsignature)
{
    Py_INCREF(callable);
    NSBezierPathElement (^block)(NSBezierPath*, NSInteger, NSPointArray) =
        ^(NSBezierPath* self, NSInteger idx, NSPointArray points) {
          PyObject*           result;
          PyObject*           seq     = NULL;
          PyObject*           arglist = NULL;
          PyObject*           v;
          int                 err;
          int                 pointCount;
          int                 i;
          PyObject*           pyself = NULL;
          int                 cookie = 0;
          NSBezierPathElement element;

          PyGILState_STATE state = PyGILState_Ensure();

          arglist = PyTuple_New(2);
          if (arglist == NULL)
              goto error;

          pyself = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL)
              goto error;
          PyTuple_SetItem(arglist, 0, pyself);
          Py_INCREF(pyself);

          v = PyLong_FromLong(idx);
          if (v == NULL)
              goto error;
          PyTuple_SetItem(arglist, 1, v);

          result = PyObject_Call((PyObject*)callable, arglist, NULL);
          Py_DECREF(arglist);
          arglist = NULL;
          PyObjCObject_ReleaseTransient(pyself, cookie);
          pyself = NULL;
          if (result == NULL)
              goto error;

          seq = PySequence_Fast(result, "should return tuple of length 2");
          Py_DECREF(result);
          if (seq == NULL)
              goto error;

          if (PySequence_Fast_GET_SIZE(seq) != 2) {
              PyErr_SetString(PyExc_ValueError, "should return tuple of length 2");
              goto error;
          }

          v = PySequence_Fast_GET_ITEM(seq, 0);

          err = PyObjC_PythonToObjC(@encode(NSBezierPathElement), v, &element);
          if (err == -1)
              goto error;

          v = PySequence_Fast(PySequence_Fast_GET_ITEM(seq, 1),
                              "result[1] should be a sequence");
          if (v == NULL)
              goto error;

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

          if (PySequence_Fast_GET_SIZE(v) != pointCount) {
              PyErr_SetString(PyExc_ValueError, "wrong number of points");
              Py_DECREF(v);
              goto error;
          }

          for (i = 0; i < pointCount; i++) {
              err = PyObjC_PythonToObjC(@encode(NSPoint), PySequence_Fast_GET_ITEM(v, i),
                                        points + i);
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
          Py_XDECREF(arglist);
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }
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
    if (!cls) {
        return 0;
    }

    if (PyObjC_RegisterMethodMapping(cls, @selector(elementAtIndex:associatedPoints:),
                                     call_NSBezierPath_elementAtIndex_associatedPoints_,
                                     mkimp_NSBezierPath_elementAtIndex_associatedPoints_)
        < 0) {

        return -1;
    }

    if (PyObjC_RegisterMethodMapping(cls, @selector(setAssociatedPoints:atIndex:),
                                     call_NSBezierPath_setAssociatedPoints_atIndex_,
                                     PyObjCUnsupportedMethod_IMP)
        < 0) {

        return -1;
    }
    return 0;
}
