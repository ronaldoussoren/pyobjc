static PyObject* 
call_NSBitmapImageRep_getTIFFCompressionTypes_count_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	PyObject* a1;
	PyObject* a2;
	PyObject* result;
	struct objc_super super;
	NSTIFFCompression* list;
	NSInteger numTypes;

	if  (!PyArg_ParseTuple(arguments, "OO", &a1, &a2)) {
		return NULL;
	}

	if (a1 != Py_None) {
		PyErr_SetString(PyExc_ValueError, "buffer must be None");
		return NULL;
	}
	if (a2 != Py_None) {
		PyErr_SetString(PyExc_ValueError, "length must be None");
		return NULL;
	}

	PyObjC_DURING
		PyObjC_InitSuperCls(&super,
			PyObjCSelector_GetClass(method),
			PyObjCClass_GetClass(self));

		((void(*)(struct objc_super*, SEL, NSTIFFCompression**, NSInteger*))objc_msgSendSuper)(&super,
				PyObjCSelector_GetSelector(method),
				&list, &numTypes);
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		list = NULL; numTypes = -1;
	PyObjC_ENDHANDLER

	if (list == NULL && PyErr_Occurred()) {
		return NULL;
	}

	result = PyTuple_New(2);
	if (result == NULL) {
		return NULL;
	}

	PyTuple_SET_ITEM(result, 1, PyInt_FromLong(numTypes));
	if (PyTuple_GET_ITEM(result, 1) == NULL) {
		Py_DECREF(result);
		return NULL;
	}

	if (numTypes < 0) {
		PyTuple_SET_ITEM(result, 0, Py_None);
		Py_INCREF(Py_None);
	} else {
		PyObject* v = PyObjC_CArrayToPython(
				@encode(NSTIFFCompression),
				list, numTypes);
		if (v == NULL) {
			Py_DECREF(result);
			return NULL;
		}
		PyTuple_SET_ITEM(result, 0, v);
	}

	return result;
}

static PyObject*
call_NSBitmapImageRep_initWithBitmap(PyObject* method, 
		PyObject* self, PyObject* arguments)
{
	PyObject* result;
	PyObject* maybeNone;
	const void *dataPlanes[5];
	int garbage;
	int width, height;
	int bps, spp;
	BOOL hasAlpha, isPlanar;
	char *colorSpaceName;
	NSString *colorSpaceNameString;
	int bpr, bpp, i;
	NSBitmapImageRep *newImageRep;
	struct objc_super super;
	PyObject*  py_Planes[5];
	Py_buffer  planeBuffers[5];

	for (i = 0; i < 5; i++) {
		py_Planes[i] = NULL;
		planeBuffers[i].buf = NULL;
	}

	// check for five well defined read buffers in data planes argument
	if (!PyArg_ParseTuple(arguments, "(OOOOO)iiiibbsii",
		py_Planes + 0,
		py_Planes + 1,
		py_Planes + 2,
		py_Planes + 3,
		py_Planes + 4,
		&width,
		&height,
		&bps,
		&spp,
		&hasAlpha,
		&isPlanar,
		&colorSpaceName,
		&bpr,
		&bpp)) {

		if ( !PyErr_ExceptionMatches(PyExc_TypeError) ) {
			return NULL;
		}

		PyErr_Clear();
		bzero(dataPlanes, sizeof(dataPlanes));
		bzero(py_Planes, sizeof(py_Planes));

		if (!PyArg_ParseTuple(arguments, "Oiiiibbsii",
				 &maybeNone,
				 &width,
				 &height,
				 &bps,
				 &spp,
				 &hasAlpha,
				 &isPlanar,
				 &colorSpaceName,
				 &bpr,
				 &bpp)){

			return NULL; //! any other situations that we need to parse specific args go here
		} else {
			// first arg must be none as nothing else makes sense
			if (maybeNone != Py_None) {
				PyErr_SetString(PyExc_TypeError, "First argument must be a 5 element Tuple or None.");
				return NULL;
			}
		}
	} else {
		for (i = 0; i < 5; i++) {
			if (py_Planes[i] == Py_None) {
				dataPlanes[i] = NULL;
			} else {
				int r = PyObject_GetBuffer(py_Planes[i], planeBuffers + i,
						PyBUF_SIMPLE);
				if (r == 0) {
					dataPlanes[i] = planeBuffers[i].buf;
				} else {
#if PY_MAJOR_VERSION == 2
					/* Fall back to old-style buffers, not all python 2 types 
					 * implement the newer APIs and that includes the stdlib.
					 */
					PyErr_Clear();
					void * buf;
					Py_ssize_t len;
					int r = PyObject_AsReadBuffer(py_Planes[i], 
						&buf, &len);
					if (r == -1) {
						goto error_cleanup;
					}
					dataPlanes[i] = buf;
#else
					goto error_cleanup;
#endif
				}
			}
		}
	}

	colorSpaceNameString = [NSString stringWithUTF8String: colorSpaceName];

	PyObjC_DURING
		PyObjC_InitSuper(&super,
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));
    
		newImageRep = ((id(*)(struct objc_super*, SEL, const void**, NSInteger, NSInteger, NSInteger, NSInteger, BOOL, BOOL, id, NSInteger, NSInteger))objc_msgSendSuper)(&super,
				PyObjCSelector_GetSelector(method),
				dataPlanes, width, height, bps, spp, 
				hasAlpha, isPlanar, colorSpaceNameString, 
				bpr, bpp);

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
		newImageRep = nil;
	PyObjC_ENDHANDLER

	for (i = 0; i < 5; i++) {
		if (py_Planes[i] != NULL && planeBuffers[i].buf != NULL) {
			PyBuffer_Release(&planeBuffers[i]);
		}
	}

	if (newImageRep == nil && PyErr_Occurred()) {
		return NULL;
	}

	result = PyObjC_IdToPython(newImageRep);

	return result;

error_cleanup:
	{
		int j = i;
		for (i = 0; i < j; i++) {
			if (py_Planes[i] != NULL && planeBuffers[i].buf != NULL) {
				PyBuffer_Release(&planeBuffers[i]);
			}
		}
	}
	return NULL;
}

static PyObject*
call_NSBitmapImageRep_initWithBitmapFormat(PyObject* method, 
		PyObject* self, PyObject* arguments)
{
	PyObject* result;
	PyObject* maybeNone;
	const void *dataPlanes[5];
	int garbage;
	int width, height;
	int bps, spp;
	BOOL hasAlpha, isPlanar;
	char *colorSpaceName;
	NSString *colorSpaceNameString;
	int bpr, bpp, i;
	NSBitmapImageRep *newImageRep;
	int format;
	struct objc_super super;
	PyObject*  py_Planes[5];
	Py_buffer  planeBuffers[5];

	for (i = 0; i < 5; i++) {
		py_Planes[i] = NULL;
		planeBuffers[i].buf = NULL;
	}

	// check for five well defined read buffers in data planes argument
	if (!PyArg_ParseTuple(arguments, "(OOOOO)iiiibbsiii",
		py_Planes + 0,
		py_Planes + 1,
		py_Planes + 2,
		py_Planes + 3,
		py_Planes + 4,
		&width,
		&height,
		&bps,
		&spp,
		&hasAlpha,
		&isPlanar,
		&colorSpaceName,
		&format,
		&bpr,
		&bpp)) {

		if ( !PyErr_ExceptionMatches(PyExc_TypeError) ) {
			return NULL;
		}

		PyErr_Clear();
		bzero(dataPlanes, sizeof(dataPlanes));
		bzero(py_Planes, sizeof(py_Planes));

		if (!PyArg_ParseTuple(arguments, "Oiiiibbsiii",
				 &maybeNone,
				 &width,
				 &height,
				 &bps,
				 &spp,
				 &hasAlpha,
				 &isPlanar,
				 &colorSpaceName,
				 &format,
				 &bpr,
				 &bpp)){

			return NULL; //! any other situations that we need to parse specific args go here
		} else {
			// first arg must be none as nothing else makes sense
			if (maybeNone != Py_None) {
				PyErr_SetString(PyExc_TypeError, "First argument must be a 5 element Tuple or None.");
				return NULL;
			}
		}
	} else {
		for (i = 0; i < 5; i++) {
			if (py_Planes[i] == Py_None) {
				dataPlanes[i] = NULL;
			} else {
				int r = PyObject_GetBuffer(py_Planes[i], planeBuffers + i,
						PyBUF_SIMPLE);
				if (r == 0) {
					dataPlanes[i] = planeBuffers[i].buf;
				} else {
#if PY_MAJOR_VERSION == 2
					/* Fall back to old-style buffers, not all python 2 types 
					 * implement the newer APIs and that includes the stdlib.
					 */
					PyErr_Clear();
					void * buf;
					Py_ssize_t len;
					int r = PyObject_AsReadBuffer(py_Planes[i], 
						&buf, &len);
					if (r == -1) {
						goto error_cleanup;
					}
					dataPlanes[i] = buf;
#else
					goto error_cleanup;
#endif
				}
			}
		}
	}

	colorSpaceNameString = [NSString stringWithUTF8String: colorSpaceName];

	PyObjC_DURING
		PyObjC_InitSuper(&super,
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));
    
		newImageRep = ((id(*)(struct objc_super*, SEL, const void**, NSInteger, NSInteger, NSInteger, NSInteger, BOOL, BOOL, id, NSBitmapFormat, NSInteger, NSInteger))objc_msgSendSuper)(&super,
				PyObjCSelector_GetSelector(method),
				dataPlanes, width, height, bps, spp, 
				hasAlpha, isPlanar, colorSpaceNameString, 
				(NSBitmapFormat)format, bpr, bpp);

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
		newImageRep = nil;
	PyObjC_ENDHANDLER

	for (i = 0; i < 5; i++) {
		if (py_Planes[i] != NULL && planeBuffers[i].buf != NULL) {
			PyBuffer_Release(&planeBuffers[i]);
		}
	}

	if (newImageRep == nil && PyErr_Occurred()) {
		return NULL;
	}

	result = PyObjC_IdToPython(newImageRep);

	return result;

error_cleanup:
	{
		int j = i;
		for (i = 0; i < j; i++) {
			if (py_Planes[i] != NULL && planeBuffers[i].buf != NULL) {
				PyBuffer_Release(&planeBuffers[i]);
			}
		}
	}
	return NULL;
}


static PyObject*
call_NSBitmapImageRep_getBitmapDataPlanes_(PyObject* method, 
		PyObject* self, PyObject* arguments)
{
	PyObject* result;
	struct objc_super super;
	unsigned char *dataPlanes[5];
	int i;
	int bytesPerPlane;
  
	if (!PyArg_ParseTuple(arguments, "")) {
		return NULL;
	}

	memset(dataPlanes, 0, sizeof(dataPlanes));

	PyObjC_DURING

		PyObjC_InitSuper(&super,
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));
    
		((void(*)(struct objc_super*, SEL, unsigned char***))objc_msgSendSuper)(&super, 
			PyObjCSelector_GetSelector(method),
			(unsigned char***)&dataPlanes);

		bytesPerPlane = [
			(NSBitmapImageRep*)PyObjCObject_GetObject(self) 
			bytesPerPlane];

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
		bytesPerPlane = -1;
	PyObjC_ENDHANDLER

	if (bytesPerPlane == -1) return NULL;

	result = PyTuple_New(5);
	if (result != NULL) {
		for(i=0; i<5; i++) {
			if (dataPlanes[i]) {
#if PY_MAJOR_VERSION == 2 && PY_MINOR_VERSION <= 6
				PyObject* buffer = PyBuffer_FromReadWriteMemory(dataPlanes[i], bytesPerPlane);
#else
				Py_buffer info;
				if (PyBuffer_FillInfo(&info, NULL, dataPlanes[i], bytesPerPlane, 0, PyBUF_FULL) < 0) {
					return NULL;
				}
				PyObject* buffer = PyMemoryView_FromBuffer(&info);
#endif

				if ( (!buffer) || PyErr_Occurred()) {
					Py_DECREF(result);
					result = NULL;
				}
				PyTuple_SET_ITEM(result, i, buffer);
			} else {
				Py_INCREF(Py_None);
				PyTuple_SET_ITEM(result, i, Py_None);
			}
		}
	}

	return result;
}

static PyObject*
call_NSBitmapImageRep_bitmapData(PyObject* method, 
		PyObject* self, PyObject* arguments)
{
	PyObject* result;
	struct objc_super super;
	unsigned char * volatile bitmapData;
	int bytesPerPlane;
  
	if (!PyArg_ParseTuple(arguments, "")) {
		return NULL;
	}

	PyObjC_DURING

		PyObjC_InitSuper(&super,
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));
    
		bitmapData = (unsigned char *(*)(id, SEL)) objc_msgSendSuper(&super, 
				PyObjCSelector_GetSelector(method));
			
		bytesPerPlane = [
			(NSBitmapImageRep*)PyObjCObject_GetObject(self) 
			bytesPerPlane];

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
		bitmapData = NULL;
		bytesPerPlane = -1;
	PyObjC_ENDHANDLER

	if (bytesPerPlane == -1 && PyErr_Occurred()) {
		return NULL;
	}

#if  PY_MAJOR_VERSION == 2 && PY_MINOR_VERSION <= 6
	result = PyBuffer_FromReadWriteMemory(bitmapData, bytesPerPlane);
#else

	/* A memory view requires that the backing store implements the buffer
	 * interface, therefore create a mutable bytes object to do that for us.
	 */
	Py_buffer info;
	if (PyBuffer_FillInfo(&info, NULL, bitmapData, bytesPerPlane, 0, PyBUF_FULL) < 0) {
		return NULL;
	}
	result = PyMemoryView_FromBuffer(&info);

#endif
	if (result == NULL) {
		if (result) {
			Py_DECREF(result);
		}
		result = NULL;
	}

	return result;
}




static int setup_nsbitmap(PyObject* m __attribute__((__unused__)))
{
	Class class_NSBitmapImageRep = objc_lookUpClass("NSBitmapImageRep");
	if (class_NSBitmapImageRep == NULL) {
		return 0;
	}

	if (PyObjC_RegisterMethodMapping(class_NSBitmapImageRep, 
		@selector(getTIFFCompressionTypes:count:),
		call_NSBitmapImageRep_getTIFFCompressionTypes_count_,
		PyObjCUnsupportedMethod_IMP) < 0 ) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
			class_NSBitmapImageRep,
			@selector(initWithBitmapDataPlanes:pixelsWide:pixelsHigh:bitsPerSample:samplesPerPixel:hasAlpha:isPlanar:colorSpaceName:bytesPerRow:bitsPerPixel:),
			call_NSBitmapImageRep_initWithBitmap,
			PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
			class_NSBitmapImageRep,
			@selector(initWithBitmapDataPlanes:pixelsWide:pixelsHigh:bitsPerSample:samplesPerPixel:hasAlpha:isPlanar:colorSpaceName:bitmapFormat:bytesPerRow:bitsPerPixel:),
			call_NSBitmapImageRep_initWithBitmapFormat,
			PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
			class_NSBitmapImageRep,
			@selector(getBitmapDataPlanes:),
			call_NSBitmapImageRep_getBitmapDataPlanes_,
			PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
			class_NSBitmapImageRep,
			@selector(bitmapData),
			call_NSBitmapImageRep_bitmapData,
			PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	return 0;
}
