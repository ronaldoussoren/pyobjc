static PyObject*
call_NSBitmapImageRep_getTIFFCompressionTypes_count_(PyObject* method, PyObject* self,
                                                     PyObject* const* arguments,
                                                     size_t           nargs)
{
    PyObject*          result;
    struct objc_super  super;
    NSTIFFCompression* list     = NULL;
    NSInteger          numTypes = 0;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1) {
        return NULL;
    }

    if (arguments[0] != Py_None) {
        PyErr_SetString(PyExc_ValueError, "buffer must be None");
        return NULL;
    }
    if (arguments[1] != Py_None) {
        PyErr_SetString(PyExc_ValueError, "length must be None");
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            super.super_class =
                (Class _Nonnull)object_getClass(PyObjCSelector_GetClass(method));
            super.receiver = PyObjCClass_GetClass(self);

            ((void (*)(struct objc_super*, SEL, NSTIFFCompression**,
                       NSInteger*))objc_msgSendSuper)(
                &super, PyObjCSelector_GetSelector(method), &list, &numTypes);
        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
            list     = NULL;
            numTypes = -1;
        }
    Py_END_ALLOW_THREADS

    if (list == NULL && PyErr_Occurred()) {
        return NULL;
    }

    result = PyTuple_New(2);
    if (result == NULL) {
        return NULL;
    }

    /* XXX: Use Py_BuildValue */
    PyTuple_SetItem(result, 1, PyLong_FromLong(numTypes));
    if (PyTuple_GetItem(result, 1) == NULL) {
        Py_DECREF(result);
        return NULL;
    }

    if (numTypes < 0) {
        PyTuple_SetItem(result, 0, Py_None);
        Py_INCREF(Py_None);
    } else {
        PyObject* v = PyObjC_CArrayToPython(@encode(NSTIFFCompression), list, numTypes);
        if (v == NULL) {
            Py_DECREF(result);
            return NULL;
        }
        PyTuple_SetItem(result, 0, v);
    }

    return result;
}

static PyObject*
call_NSBitmapImageRep_initWithBitmap(PyObject* method, PyObject* self,
                                     PyObject* const* arguments, size_t nargs)
{
    const void*       dataPlanes[5] = {0};
    int               width, height;
    int               bps, spp;
    BOOL              hasAlpha, isPlanar;
    NSString*         colorSpaceNameString;
    int               bpr, bpp, i;
    NSBitmapImageRep* newImageRep;
    struct objc_super super;
    PyObject*         py_allPlanes;
    Py_buffer         planeBuffers[5];

    for (i = 0; i < 5; i++) {
        planeBuffers[i].buf = NULL;
    }

    if (PyObjC_CheckArgCount(method, 10, 10, nargs) == -1) {
        return NULL;
    }
    py_allPlanes = arguments[0];
    if (py_allPlanes != Py_None) {
        PyObject* fast_planes =
            PySequence_Fast(py_allPlanes, "Expecting a 5 tuple or None");
        if (fast_planes == NULL) {
            /* XXX: Clearer error message */
            PyErr_SetString(PyExc_TypeError,
                            "First argument must be a 5 element Tuple or None.");
            return NULL;
        }
        if (PySequence_Fast_GET_SIZE(fast_planes) != 5) {
            /* XXX: Clearer error message */
            PyErr_SetString(PyExc_TypeError,
                            "First argument must be a 5 element Tuple or None.");
            Py_DECREF(fast_planes);
            return NULL;
        }
        for (i = 0; i < 5; i++) {
            PyObject* tmp = PySequence_Fast_GET_ITEM(fast_planes, i);
            if (tmp == Py_None) {
                dataPlanes[i] = NULL;
            } else {
                int r = PyObject_GetBuffer(tmp, planeBuffers + i, PyBUF_SIMPLE);
                if (r == 0) {
                    dataPlanes[i] = planeBuffers[i].buf;
                } else {
                    goto error_cleanup;
                }
            }
        }
    }

    if (PyObjC_PythonToObjC(@encode(int), arguments[1], &width) == -1) {
        goto error_cleanup;
    }
    if (PyObjC_PythonToObjC(@encode(int), arguments[2], &height) == -1) {
        goto error_cleanup;
    }
    if (PyObjC_PythonToObjC(@encode(int), arguments[3], &bps) == -1) {
        goto error_cleanup;
    }
    if (PyObjC_PythonToObjC(@encode(int), arguments[4], &spp) == -1) {
        goto error_cleanup;
    }
    hasAlpha = (BOOL)PyObject_IsTrue(arguments[5]);
    isPlanar = (BOOL)PyObject_IsTrue(arguments[6]);
    if (PyObjC_PythonToObjC(@encode(NSString*), arguments[7], &colorSpaceNameString)
        == -1) {
        goto error_cleanup;
    }
    if (PyObjC_PythonToObjC(@encode(int), arguments[8], &bpr) == -1) {
        goto error_cleanup;
    }
    if (PyObjC_PythonToObjC(@encode(int), arguments[9], &bpp) == -1) {
        goto error_cleanup;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            super.super_class = PyObjCSelector_GetClass(method);
            super.receiver    = PyObjCObject_GetObject(self);

            newImageRep = ((id(*)(struct objc_super*, SEL, const void**, NSInteger,
                                  NSInteger, NSInteger, NSInteger, BOOL, BOOL, id,
                                  NSInteger, NSInteger))objc_msgSendSuper)(
                &super, PyObjCSelector_GetSelector(method), dataPlanes, width, height,
                bps, spp, hasAlpha, isPlanar, colorSpaceNameString, bpr, bpp);

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
            newImageRep = nil;
        }
    Py_END_ALLOW_THREADS

    for (i = 0; i < 5; i++) {
        if (planeBuffers[i].buf != NULL) {
            PyBuffer_Release(&planeBuffers[i]);
        }
    }

    if (newImageRep == nil && PyErr_Occurred()) {
        return NULL;
    }

    return PyObjC_IdToPython(newImageRep);

error_cleanup : {
    int j = i;
    for (i = 0; i < j; i++) {
        if (planeBuffers[i].buf != NULL) {
            PyBuffer_Release(&planeBuffers[i]);
        }
    }
}
    return NULL;
}

static PyObject*
call_NSBitmapImageRep_initWithBitmapFormat(PyObject* method, PyObject* self,
                                           PyObject* const* arguments, size_t nargs)
{
    PyObject*         result;
    const void*       dataPlanes[5] = {0};
    int               width, height;
    int               bps, spp;
    BOOL              hasAlpha, isPlanar;
    NSString*         colorSpaceNameString;
    int               bpr, bpp, i;
    NSBitmapImageRep* newImageRep;
    int               format;
    struct objc_super super;
    PyObject*         py_allPlanes;
    Py_buffer         planeBuffers[5];

    for (i = 0; i < 5; i++) {
        planeBuffers[i].buf = NULL;
    }

    if (PyObjC_CheckArgCount(method, 11, 11, nargs) == -1) {
        return NULL;
    }
    py_allPlanes = arguments[0];
    if (py_allPlanes != Py_None) {
        PyObject* fast_planes =
            PySequence_Fast(py_allPlanes, "Expecting a 5 tuple or None");
        if (fast_planes == NULL) {
            /* XXX: Clearer error message */
            PyErr_SetString(PyExc_TypeError,
                            "First argument must be a 5 element Tuple or None.");
            return NULL;
        }
        if (PySequence_Fast_GET_SIZE(fast_planes) != 5) {
            /* XXX: Clearer error message */
            PyErr_SetString(PyExc_TypeError,
                            "First argument must be a 5 element Tuple or None.");
            Py_DECREF(fast_planes);
            return NULL;
        }
        for (i = 0; i < 5; i++) {
            PyObject* tmp = PySequence_Fast_GET_ITEM(fast_planes, i);
            if (tmp == Py_None) {
                dataPlanes[i] = NULL;
            } else {
                int r = PyObject_GetBuffer(tmp, planeBuffers + i, PyBUF_SIMPLE);
                if (r == 0) {
                    dataPlanes[i] = planeBuffers[i].buf;
                } else {
                    goto error_cleanup;
                }
            }
        }
    }

    if (PyObjC_PythonToObjC(@encode(int), arguments[1], &width) == -1) {
        goto error_cleanup;
    }
    if (PyObjC_PythonToObjC(@encode(int), arguments[2], &height) == -1) {
        goto error_cleanup;
    }
    if (PyObjC_PythonToObjC(@encode(int), arguments[3], &bps) == -1) {
        goto error_cleanup;
    }
    if (PyObjC_PythonToObjC(@encode(int), arguments[4], &spp) == -1) {
        goto error_cleanup;
    }
    hasAlpha = (BOOL)PyObject_IsTrue(arguments[5]);
    isPlanar = (BOOL)PyObject_IsTrue(arguments[6]);
    if (PyObjC_PythonToObjC(@encode(NSString*), arguments[7], &colorSpaceNameString)
        == -1) {
        goto error_cleanup;
    }
    if (PyObjC_PythonToObjC(@encode(int), arguments[8], &format) == -1) {
        goto error_cleanup;
    }
    if (PyObjC_PythonToObjC(@encode(int), arguments[9], &bpr) == -1) {
        goto error_cleanup;
    }
    if (PyObjC_PythonToObjC(@encode(int), arguments[10], &bpp) == -1) {
        goto error_cleanup;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            super.super_class = PyObjCSelector_GetClass(method);
            super.receiver    = PyObjCObject_GetObject(self);

            newImageRep =
                ((id(*)(struct objc_super*, SEL, const void**, NSInteger, NSInteger,
                        NSInteger, NSInteger, BOOL, BOOL, id, NSBitmapFormat, NSInteger,
                        NSInteger))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), dataPlanes, width, height,
                    bps, spp, hasAlpha, isPlanar, colorSpaceNameString,
                    (NSBitmapFormat)format, bpr, bpp);

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
            result      = NULL;
            newImageRep = nil;
        }
    Py_END_ALLOW_THREADS

    for (i = 0; i < 5; i++) {
        if (planeBuffers[i].buf != NULL) {
            PyBuffer_Release(&planeBuffers[i]);
        }
    }

    if (newImageRep == nil && PyErr_Occurred()) {
        return NULL;
    }

    result = PyObjC_IdToPython(newImageRep);

    return result;

error_cleanup:
    for (i = 0; i < 5; i++) {
        if (planeBuffers[i].buf != NULL) {
            PyBuffer_Release(&planeBuffers[i]);
        }
    }
    return NULL;
}

static PyObject*
call_NSBitmapImageRep_getBitmapDataPlanes_(PyObject* method, PyObject* self,
                                           PyObject* const* arguments, size_t nargs)
{
    PyObject*         result;
    struct objc_super super;
    unsigned char*    dataPlanes[5];
    int               i;
    int               bytesPerPlane;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1) {
        return NULL;
    }

    memset(dataPlanes, 0, sizeof(dataPlanes));

    Py_BEGIN_ALLOW_THREADS
        @try {

            super.super_class = PyObjCSelector_GetClass(method);
            super.receiver    = PyObjCObject_GetObject(self);

            ((void (*)(struct objc_super*, SEL, unsigned char***))objc_msgSendSuper)(
                &super, PyObjCSelector_GetSelector(method),
                (unsigned char***)&dataPlanes);

            bytesPerPlane =
                [(NSBitmapImageRep*)PyObjCObject_GetObject(self) bytesPerPlane];

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
            result        = NULL;
            bytesPerPlane = -1;
        }
    Py_END_ALLOW_THREADS

    if (bytesPerPlane == -1)
        return NULL;

    result = PyTuple_New(5);
    if (result != NULL) {
        for (i = 0; i < 5; i++) {
            if (dataPlanes[i]) {
                Py_buffer info;
                if (PyBuffer_FillInfo(&info, NULL, dataPlanes[i], bytesPerPlane, 0,
                                      PyBUF_FULL)
                    < 0) {
                    return NULL;
                }
                PyObject* buffer = PyMemoryView_FromBuffer(&info);

                if ((!buffer) || PyErr_Occurred()) {
                    Py_DECREF(result);
                    result = NULL;
                    return NULL;
                }
                PyTuple_SetItem(result, i, buffer);
            } else {
                Py_INCREF(Py_None);
                PyTuple_SetItem(result, i, Py_None);
            }
        }
    }

    return result;
}

static PyObject*
call_NSBitmapImageRep_bitmapData(PyObject* method, PyObject* self,
                                 PyObject* const* arguments, size_t nargs)
{
    PyObject*         result;
    struct objc_super super;
    unsigned char* volatile bitmapData;
    int bytesPerPlane;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1) {
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {

            super.super_class = PyObjCSelector_GetClass(method);
            super.receiver    = PyObjCObject_GetObject(self);

            bitmapData = ((unsigned char* (*)(struct objc_super*, SEL))objc_msgSendSuper)(
                &super, PyObjCSelector_GetSelector(method));

            bytesPerPlane =
                [(NSBitmapImageRep*)PyObjCObject_GetObject(self) bytesPerPlane];

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
            result        = NULL;
            bitmapData    = NULL;
            bytesPerPlane = -1;
        }
    Py_END_ALLOW_THREADS

    if (bytesPerPlane == -1 && PyErr_Occurred()) {
        return NULL;
    }

    /* A memory view requires that the backing store implements the buffer
     * interface, therefore create a mutable bytes object to do that for us.
     */
    Py_buffer info;
    if (PyBuffer_FillInfo(&info, NULL, bitmapData, bytesPerPlane, 0, PyBUF_FULL) < 0) {
        return NULL;
    }
    result = PyMemoryView_FromBuffer(&info);

    if (result == NULL) {
        if (result) {
            Py_DECREF(result);
        }
        result = NULL;
    }

    return result;
}

static int
setup_nsbitmap(PyObject* m __attribute__((__unused__)))
{
    Class class_NSBitmapImageRep = objc_lookUpClass("NSBitmapImageRep");
    if (class_NSBitmapImageRep == NULL) {
        return 0;
    }

    if (PyObjC_RegisterMethodMapping(class_NSBitmapImageRep,
                                     @selector(getTIFFCompressionTypes:count:),
                                     call_NSBitmapImageRep_getTIFFCompressionTypes_count_,
                                     PyObjCUnsupportedMethod_IMP)
        < 0) {

        return -1;
    }

    if (PyObjC_RegisterMethodMapping(
            class_NSBitmapImageRep,
            @selector
            (initWithBitmapDataPlanes:
                           pixelsWide:pixelsHigh:bitsPerSample:samplesPerPixel:hasAlpha
                                     :isPlanar:colorSpaceName:bytesPerRow:bitsPerPixel:),
            call_NSBitmapImageRep_initWithBitmap, PyObjCUnsupportedMethod_IMP)
        < 0) {

        return -1;
    }

    if (PyObjC_RegisterMethodMapping(
            class_NSBitmapImageRep,
            @selector(initWithBitmapDataPlanes:
                                    pixelsWide:pixelsHigh:bitsPerSample:samplesPerPixel
                                              :hasAlpha:isPlanar:colorSpaceName
                                              :bitmapFormat:bytesPerRow:bitsPerPixel:),
            call_NSBitmapImageRep_initWithBitmapFormat, PyObjCUnsupportedMethod_IMP)
        < 0) {

        return -1;
    }

    if (PyObjC_RegisterMethodMapping(
            class_NSBitmapImageRep, @selector(getBitmapDataPlanes:),
            call_NSBitmapImageRep_getBitmapDataPlanes_, PyObjCUnsupportedMethod_IMP)
        < 0) {

        return -1;
    }

    if (PyObjC_RegisterMethodMapping(class_NSBitmapImageRep, @selector(bitmapData),
                                     call_NSBitmapImageRep_bitmapData,
                                     PyObjCUnsupportedMethod_IMP)
        < 0) {

        return -1;
    }

    return 0;
}
