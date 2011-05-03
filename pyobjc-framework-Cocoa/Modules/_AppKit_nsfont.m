static PyObject* 
m_NSConvertGlyphsToPackedGlyphs(
	PyObject* self __attribute__((__unused__)), PyObject* arguments)
{
	PyObject* py_glBuf;
	PyObject* py_count;
	PyObject* py_packing;
	PyObject* py_packedGlyphs;

	NSGlyph* glBuf;
	int bufCode;
	PyObject* buffer = NULL;
	NSInteger count;
	Py_ssize_t c;
	NSMultibyteGlyphPacking packing;
	char* packedGlyphs;
	
	if  (!PyArg_ParseTuple(arguments, "OOOO", &py_glBuf, &py_count, &py_packing, &py_packedGlyphs)) {
		return NULL;
	}

	if (py_packedGlyphs != Py_None) {
		PyErr_SetString(PyExc_ValueError, "packedGlyphs argument must be None");
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(NSInteger), py_count, &count) == -1) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(NSMultibyteGlyphPacking), py_packing, &packing) == -1) {
		return NULL;
	}

	c = count;
	bufCode = PyObjC_PythonToCArray(NO, NO, @encode(NSGlyph), py_glBuf,
		(void**)&glBuf, &c, &buffer);
	if (bufCode == -1) {

		return NULL;
	}
	count = c;

	packedGlyphs = malloc(count*4+1);
	if (packedGlyphs == NULL) {
		PyObjC_FreeCArray(bufCode, glBuf);
		Py_XDECREF(buffer);
		PyErr_NoMemory();
		return NULL;
	}
	
	NSInteger result = -1;
	PyObjC_DURING
		result = NSConvertGlyphsToPackedGlyphs(glBuf, count, packing, packedGlyphs);
		
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	PyObjC_FreeCArray(bufCode, glBuf);
	Py_XDECREF(buffer);

	if (PyErr_Occurred()) {
		free(packedGlyphs);
		return NULL;
	}

	if (result == 0) {
		Py_INCREF(Py_None);
		return Py_None;
	}

	PyObject* pyRes;
	
	if (result == 0) {
		pyRes = Py_BuildValue("Ns#",
			PyObjC_ObjCToPython(@encode(NSInteger), &result), packedGlyphs, result-1);
	} else {
		pyRes = Py_BuildValue("Ns#",
			PyObjC_ObjCToPython(@encode(NSInteger), &result), packedGlyphs, result);
	}

	free(packedGlyphs);
	return pyRes;
}



#define APPKIT_NSFONT_METHODS \
	{							\
	   "NSConvertGlyphsToPackedGlyphs",			\
	   (PyCFunction)m_NSConvertGlyphsToPackedGlyphs,	\
	   METH_VARARGS,					\
	   0							\
	},
