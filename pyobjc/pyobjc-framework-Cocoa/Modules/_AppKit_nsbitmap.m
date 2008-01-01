#include <Python.h>
#include <AppKit/AppKit.h>
#include "pyobjc-api.h"

static PyObject* 
call_NSBitmapImageRep_getTIFFCompressionTypes_count_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	PyObject* result;
	struct objc_super super;
	NSTIFFCompression* list;
	int numTypes;

	if  (!PyArg_ParseTuple(arguments, "")) {
		return NULL;
	}

	PyObjC_DURING
		PyObjC_InitSuperCls(&super,
			PyObjCSelector_GetClass(method),
			PyObjCClass_GetClass(self));

		(void)objc_msgSendSuper(&super,
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


/* XXX: Needs looking into, argument parsing seems awfully complex */
static PyObject*
call_NSBitmapImageRep_initWithBitmap(PyObject* method, 
		PyObject* self, PyObject* arguments)
{
	PyObject* result;
	PyObject* maybeNone;
	char *dataPlanes[5];
	int garbage;
	int width, height;
	int bps, spp;
	BOOL hasAlpha, isPlanar;
	char *colorSpaceName;
	NSString *colorSpaceNameString;
	int bpr, bpp;
	NSBitmapImageRep *newImageRep;
	struct objc_super super;

	// check for five well defined read buffers in data planes argument
	if (!PyArg_ParseTuple(arguments, "(z#z#z#z#z#)iiiibbsii",
		&dataPlanes[0], &garbage,
		&dataPlanes[1], &garbage,
		&dataPlanes[2], &garbage,
		&dataPlanes[3], &garbage,
		&dataPlanes[4], &garbage,
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
	}

	colorSpaceNameString = [NSString stringWithCString: colorSpaceName];

	PyObjC_DURING
		PyObjC_InitSuper(&super,
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));
    
		newImageRep = objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method),
				dataPlanes, width, height, bps, spp, 
				hasAlpha, isPlanar, colorSpaceNameString, 
				bpr, bpp);

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
		newImageRep = nil;
	PyObjC_ENDHANDLER

	if (newImageRep == nil && PyErr_Occurred()) {
		return NULL;
	}

	result = PyObjC_IdToPython(newImageRep);

	return result;
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
    
		(void)objc_msgSendSuper(&super, 
			PyObjCSelector_GetSelector(method),
			&dataPlanes);

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
				PyObject* buffer = PyBuffer_FromReadWriteMemory(dataPlanes[i], bytesPerPlane);
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
    
		bitmapData = (unsigned char *) objc_msgSendSuper(&super, 
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

	result = PyBuffer_FromReadWriteMemory(bitmapData, bytesPerPlane);
	if (PyErr_Occurred()) {
		if (result) {
			Py_DECREF(result);
		}
		result = NULL;
	}

	return result;
}




static PyMethodDef mod_methods[] = {
	{ 0, 0, 0, 0 } /* sentinel */
};

void init_nsbitmap(void);
void init_nsbitmap(void)
{
	PyObject* m = Py_InitModule4("_nsbitmap", mod_methods, "", NULL,
			PYTHON_API_VERSION);

	PyObjC_ImportAPI(m);

	Class class_NSBitmapImageRep = objc_lookUpClass("NSBitmapImageRep");

	if (PyObjC_RegisterMethodMapping(class_NSBitmapImageRep, 
		@selector(getTIFFCompressionTypes:count:),
		call_NSBitmapImageRep_getTIFFCompressionTypes_count_,
		PyObjCUnsupportedMethod_IMP) < 0 ) {

		return;
	}

	if (PyObjC_RegisterMethodMapping(
			class_NSBitmapImageRep,
			@selector(initWithBitmapDataPlanes:pixelsWide:pixelsHigh:bitsPerSample:samplesPerPixel:hasAlpha:isPlanar:colorSpaceName:bytesPerRow:bitsPerPixel:),
			call_NSBitmapImageRep_initWithBitmap,
			PyObjCUnsupportedMethod_IMP) < 0) {

		return;
	}

	if (PyObjC_RegisterMethodMapping(
			class_NSBitmapImageRep,
			@selector(getBitmapDataPlanes:),
			call_NSBitmapImageRep_getBitmapDataPlanes_,
			PyObjCUnsupportedMethod_IMP) < 0) {

		return;
	}

	if (PyObjC_RegisterMethodMapping(
			class_NSBitmapImageRep,
			@selector(bitmapData),
			call_NSBitmapImageRep_bitmapData,
			PyObjCUnsupportedMethod_IMP) < 0) {

		return;
	}
}
