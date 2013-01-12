#include "pyobjc.h"

static PyObjCMethodSignature* new_methodsignature(const char*);

static PyObject*
sig_str(PyObject* _self)
{
	PyObjCMethodSignature* self = (PyObjCMethodSignature*)_self;
	PyObject* v = PyObjCMethodSignature_AsDict(self);
	if (v == NULL) {
		PyErr_Clear();
		return PyText_FromString(self->signature);
	} else {
		PyObject* r = PyObject_Repr(v);
		Py_DECREF(v);
		return r;
	}
}

static void
sig_dealloc(PyObject* _self)
{
	PyObjCMethodSignature* self = (PyObjCMethodSignature*)_self;
	Py_ssize_t i;

	if (self->signature) {
		PyMem_Free((char*)self->signature);
	}

	if (self->rettype.typeOverride) {
		PyMem_Free((char*)self->rettype.type);
	}
	for (i = 0; i < Py_SIZE(self); i++) {
		if (self->argtype[i].typeOverride) {
			PyMem_Free((char*)self->argtype[i].type);
		}
		if (self->argtype[i].sel_type != NULL) {
			PyMem_Free((char*)self->argtype[i].sel_type);
		}
	}
	PyObject_Free(self);
}


PyTypeObject PyObjCMethodSignature_Type = {
	PyVarObject_HEAD_INIT(NULL, 0)
	"objc._method_signature",		/* tp_name */
	sizeof(PyObjCMethodSignature),		/* tp_basicsize */
	sizeof(struct _PyObjC_ArgDescr),	/* tp_itemsize */
	/* methods */
	sig_dealloc,				/* tp_dealloc */
	0,					/* tp_print */
	0,					/* tp_getattr */
	0,					/* tp_setattr */
	0,					/* tp_compare */
	sig_str,				/* tp_repr */
	0,					/* tp_as_number */
	0,					/* tp_as_sequence */
	0,		       			/* tp_as_mapping */
	0,					/* tp_hash */
	0,					/* tp_call */
	sig_str,				/* tp_str */
	PyObject_GenericGetAttr,		/* tp_getattro */
	0,					/* tp_setattro */
	0,					/* tp_as_buffer */
	Py_TPFLAGS_DEFAULT,			/* tp_flags */
 	0,					/* tp_doc */
 	0,					/* tp_traverse */
 	0,					/* tp_clear */
	0,					/* tp_richcompare */
	0,					/* tp_weaklistoffset */
	0,					/* tp_iter */
	0,					/* tp_iternext */
	0,					/* tp_methods */
	0,					/* tp_members */
	0,					/* tp_getset */
	0,					/* tp_base */
	0,					/* tp_dict */
	0,					/* tp_descr_get */
	0,					/* tp_descr_set */
	0,					/* tp_dictoffset */
	0,					/* tp_init */
	0,					/* tp_alloc */
	0,					/* tp_new */
	0,		        		/* tp_free */
	0,					/* tp_is_gc */
	0,                                      /* tp_bases */
	0,                                      /* tp_mro */
	0,                                      /* tp_cache */
	0,                                      /* tp_subclasses */
	0,                                      /* tp_weaklist */
	0                                       /* tp_del */
#if PY_VERSION_HEX >= 0x02060000
	, 0                                     /* tp_version_tag */
#endif

};


static PyObjCMethodSignature* new_methodsignature(
		const char* signature)
{
	Py_ssize_t nargs;
	const char* cur;
	PyObjCMethodSignature* retval;

	/* Skip return-type */
	cur = PyObjCRT_SkipTypeSpec(signature);

	nargs = 0;
	for ( ; cur && *cur; cur = PyObjCRT_SkipTypeSpec(cur)) {
		nargs++;
	}
	retval = PyObject_NewVar(PyObjCMethodSignature, 
			&PyObjCMethodSignature_Type, nargs+1);

	if (retval == NULL) {
		PyErr_NoMemory();
		return NULL;
	}

	Py_SIZE(retval) = nargs;
	retval->suggestion = NULL;
	retval->variadic = NO;
	retval->free_result = NO;
	retval->null_terminated_array = NO;
	retval->signature = PyObjCUtil_Strdup(signature);
	if (retval->signature == NULL) {
		Py_DECREF(retval);
		return NULL;
	}

	retval->rettype.type = retval->signature;
	retval->rettype.typeOverride = NO;
	retval->rettype.ptrType = PyObjC_kPointerPlain;
	retval->rettype.allowNULL = YES;
	retval->rettype.arraySizeInRetval = NO;
	retval->rettype.printfFormat = NO;
	retval->rettype.alreadyRetained = NO;
	retval->rettype.alreadyCFRetained = NO;
	retval->rettype.callableRetained = NO;
	retval->rettype.callable = NULL;
	retval->rettype.sel_type = NULL;

	/* Ignore type specifiers for methods returning void. Mostly needed
	 * to avoid crapping out one (oneway void) methods.
	 */
	cur = PyObjCRT_SkipTypeQualifiers(retval->rettype.type);
	if (*cur == _C_VOID) {
		retval->rettype.type = cur;
	}

	cur = PyObjCRT_SkipTypeSpec(retval->signature);
	nargs = 0;
	for (;cur && *cur; cur = PyObjCRT_SkipTypeSpec(cur)) {
		retval->argtype[nargs].type = cur;
		retval->argtype[nargs].ptrType = PyObjC_kPointerPlain;
		retval->argtype[nargs].allowNULL = YES;
		retval->argtype[nargs].typeOverride = NO;
		retval->argtype[nargs].arraySizeInRetval = NO;
		retval->argtype[nargs].printfFormat = NO;
		retval->argtype[nargs].alreadyRetained = NO;
		retval->argtype[nargs].alreadyCFRetained = NO;
		retval->argtype[nargs].callableRetained = NO;
		retval->argtype[nargs].callable = NULL;
		retval->argtype[nargs].sel_type = NULL;
		nargs++;
	}
	Py_SIZE(retval) = nargs;
	

	return retval;
}

	


/* XXX: Oh joy, on GNUstep [sig methodReturnType] and 
 * [sig getArgumentTypeAtIndex:] return the actual string-value
 * followed by the rest of the signature. MacOS X returns a buffer
 * that contains only the requested signature.
 */
char*
PyObjC_NSMethodSignatureToTypeString(
		NSMethodSignature* sig, char* buf, size_t buflen)
{
	char* result = buf;
	char* end;
	int arg_count = [sig numberOfArguments];
	int i;
	size_t r;


	r = snprintf(buf, buflen, "%s", [sig methodReturnType]);
	if (r > buflen) {
		return NULL;
	}

	end = (char*)PyObjCRT_SkipTypeSpec(buf);
	*end = '\0';
	buflen -= (end - buf);
	buf = end;

	for (i = 0; i < arg_count; i++) {
		r = snprintf(buf, buflen, "%s", [sig getArgumentTypeAtIndex:i]);
		if (r > buflen) {
			return NULL;
		}

		end = (char*)PyObjCRT_SkipTypeSpec(buf);
		buflen -= (end - buf);
		buf = end;
	}

	return result;
}

static PyObject* registry = NULL;

int
PyObjC_registerMetaData(PyObject* class_name, PyObject* selector, 
							PyObject* metadata)
{
	if (registry == NULL) {
		registry = PyObjC_NewRegistry();
		if (registry == NULL) {
			return -1;
		}
	}
	return PyObjC_AddToRegistry(registry, class_name, selector, metadata);
}


static int setup_meta(struct _PyObjC_ArgDescr* descr, PyObject* meta, BOOL is_native)
{
	PyObject* d;
	char typeModifier = 0;

	if (meta == Py_None) {
		return 0;
	}

	if (meta != NULL && !PyDict_Check(meta)) {
		PyObject* r = PyObject_Repr(meta);
		if (r == NULL) {
			return -1;
		}
		PyErr_Format(PyExc_TypeError, "metadata of type %s: %s",
				Py_TYPE(meta)->tp_name,
				PyText_AsString(r));
		Py_DECREF(r);

		return -1;
	}

	descr->allowNULL = YES;
	if (meta) {
		d = PyDict_GetItemString(meta, "null_accepted");
		if (d == NULL || PyObject_IsTrue(d)) {
			descr->allowNULL = YES;
		} else {
			descr->allowNULL = NO;
		}
	}

	if (meta) {
		d = PyDict_GetItemString(meta, "already_retained");
		if (d && PyObject_IsTrue(d)) {
			descr->alreadyRetained = YES;
		} else {
			descr->alreadyRetained = NO;
		}
	}

	if (meta) {
		d = PyDict_GetItemString(meta, "already_cfretained");
		if (d && PyObject_IsTrue(d)) {
			descr->alreadyCFRetained = YES;
		} else {
			descr->alreadyCFRetained = NO;
		}
	}

	if (meta) {
		d = PyDict_GetItemString(meta, "callable_retained");
		if (d == NULL || PyObject_IsTrue(d)) {
			descr->callableRetained = YES;
		} else {
			descr->callableRetained = NO;
		}
	}

	if (meta) {
		d = PyDict_GetItemString(meta, "sel_of_type");
		if (d) {
			if (PyUnicode_Check(d)) {
				PyObject* bytes = PyUnicode_AsEncodedString(d, NULL, NULL);
				if (bytes == NULL) {
					return -1;
				}
				descr->sel_type = PyObjCUtil_Strdup(PyBytes_AsString(bytes));
				Py_DECREF(bytes);
				if (descr->sel_type == NULL) {
					return -1;
				}
			} else if (PyBytes_Check(d)) {
				descr->sel_type = PyObjCUtil_Strdup(PyBytes_AsString(d));
				if (descr->sel_type == NULL) {
					return -1;
				}
			}
		}
	}

	if (meta) {
		d = PyDict_GetItemString(meta, "callable");
		if (d) {
			/* Make up a dummy signature, will be overridden bij
			 * the metadata.
			 */
			char buffer[64];
			PyObject* a = PyDict_GetItemString(d, "arguments");
			if (a != NULL) {
				Py_ssize_t i, len = PyDict_Size(a);
				if (len == -1) {
					return -1;
				}

				for (i = 0; i < len; i++) {
					buffer[i] = _C_ID;
				}
				buffer[len] = _C_ID;
				buffer[len+1] = '\0';
			} else {
				buffer[0] = _C_ID;
				buffer[1] = '\0';
			}
			descr->callable = PyObjCMethodSignature_WithMetaData(buffer, d, NO);
			if (descr->callable == NULL) {
				return -1;
			}
		}
	}

	if (meta) {
		d = PyDict_GetItemString(meta, "c_array_length_in_result");
		if (d != NULL && PyObject_IsTrue(d)) {
			descr->arraySizeInRetval = YES;
		}
	}

	if (meta) {
		d = PyDict_GetItemString(meta, "printf_format");
		if (d != NULL && PyObject_IsTrue(d)) {
			descr->printfFormat = YES;
		}
	}

	if (meta) {
		d = PyDict_GetItemString(meta, "c_array_delimited_by_null");
		if (d != NULL && PyObject_IsTrue(d)) {
			descr->ptrType = PyObjC_kNullTerminatedArray;
		}
	}

	if (meta) {
		d = PyDict_GetItemString(meta, "c_array_of_fixed_length");
		if (d != NULL) {
			if (PyLong_Check(d)) {
				descr->ptrType = PyObjC_kFixedLengthArray;
				descr->arrayArg = PyLong_AsLong(d);
				descr->arrayArgOut = descr->arrayArg;
				if (PyErr_Occurred()) {
					return -1;
				}
			}
#if PY_MAJOR_VERSION == 2
			else if (PyInt_Check(d)) {
				descr->ptrType = PyObjC_kFixedLengthArray;
				descr->arrayArg = PyInt_AsLong(d);
				descr->arrayArgOut = descr->arrayArg;
			}
#endif
		}
	}

	if (meta) {
		d = PyDict_GetItemString(meta, "c_array_of_variable_length");
		if (d != NULL && PyObject_IsTrue(d)) {
			descr->ptrType = PyObjC_kVariableLengthArray;
			descr->arrayArg = 0;
			descr->arrayArg = 0;
		}
	}

	if (meta) {
		d = PyDict_GetItemString(meta, "c_array_length_in_arg");
		if (d != NULL) {
			if (PyLong_Check(d)) {
				descr->ptrType = PyObjC_kArrayCountInArg;
				descr->arrayArg = PyLong_AsLong(d);
				if (PyErr_Occurred()) {
					return -1;
				}
				descr->arrayArgOut = descr->arrayArg;
					
#if PY_MAJOR_VERSION == 2
			} else if (PyInt_Check(d)) {
				descr->ptrType = PyObjC_kArrayCountInArg;
				descr->arrayArg = PyInt_AsLong(d);
				descr->arrayArgOut = descr->arrayArg;
#endif
			} else if (PyTuple_Check(d)) {
				if (PyTuple_GET_SIZE(d) == 1) {
					descr->ptrType = PyObjC_kArrayCountInArg;
					if (PyLong_Check(PyTuple_GET_ITEM(d, 0))) {
						descr->arrayArg = PyLong_AsLong(PyTuple_GET_ITEM(d, 0));
					} else {
#if PY_MAJOR_VERSION == 2
						descr->arrayArg = PyInt_AsLong(PyTuple_GET_ITEM(d, 0));
#else
						PyErr_SetString(PyExc_TypeError, "array_out argument not integer");
#endif
					}
					if (PyErr_Occurred()) {
						return -1;
					}
					descr->arrayArgOut = descr->arrayArg;
				} else if (PyTuple_GET_SIZE(d) >= 2) {
					descr->ptrType = PyObjC_kArrayCountInArg;
					if (PyLong_Check(PyTuple_GET_ITEM(d, 0))) {
						descr->arrayArg = PyLong_AsLong(PyTuple_GET_ITEM(d, 0));
					} else {
#if PY_MAJOR_VERSION == 2
						descr->arrayArg = PyInt_AsLong(PyTuple_GET_ITEM(d, 0));
#else
						PyErr_SetString(PyExc_TypeError, "array_out argument not integer");
#endif
					}

					if (PyErr_Occurred()) {
						return -1;
					}

					if (PyLong_Check(PyTuple_GET_ITEM(d, 1))) {
						descr->arrayArgOut = PyLong_AsLong(PyTuple_GET_ITEM(d, 1));
					} else {
#if PY_MAJOR_VERSION == 2
						descr->arrayArgOut = PyInt_AsLong(PyTuple_GET_ITEM(d, 1));
#else
						PyErr_SetString(PyExc_TypeError, "array_out argument not integer");
#endif
					}
					if (PyErr_Occurred()) {
						return -1;
					}
				}
			}
		}
	}

	if (meta) {
		d = PyDict_GetItemString(meta, "type_modifier");
		if (d != NULL) {
			if (PyUnicode_Check(d)) {
				PyObject* bytes = PyUnicode_AsEncodedString(d, NULL, NULL);
				if (bytes == NULL) {
					return -1;
				}
				typeModifier = *PyBytes_AsString(bytes);
				Py_DECREF(bytes);
#if PY_MAJOR_VERSION == 2
			} else if (PyString_Check(d)) {
				typeModifier = *PyString_AsString(d);
#else
			} else if (PyBytes_Check(d)) {	
				typeModifier = *PyBytes_AsString(d);
#endif
			}
		}
	}

	if (meta) {
		d = PyDict_GetItemString(meta, "type");
	} else {
		d = NULL;
	}

	if (d 
		&& (
#if PY_MAJOR_VERSION == 2
		  PyString_Check(d) ||
#else
		  PyBytes_Check(d) ||
#endif
		  PyUnicode_Check(d))
		) {
		PyObject* bytes = NULL;

		if (PyUnicode_Check(d)) {
			bytes = PyUnicode_AsEncodedString(d, NULL, NULL);
			if (bytes == NULL) {
				return -1;
			}
#if PY_MAJOR_VERSION == 2
		} else if (PyString_Check(d)) {
			bytes = d; Py_INCREF(bytes);
#else
		} else if (PyBytes_Check(d)) {
			bytes = d; Py_INCREF(bytes);

#endif
		} else {
			PyErr_SetString(PyExc_SystemError, "Inconsistent if-case");
			return -1;
		}

		const char* type = PyBytes_AsString(bytes);

		if (is_native && !PyObjC_signatures_compatible(descr->type, type)) {
			/* The new signature is not compatible enough, ignore the 
			 * override.
			 */
			type = descr->type;
		}

		char* tp = PyMem_Malloc(strlen(type)+2);
		if (tp == NULL) {
			Py_XDECREF(bytes);
			PyErr_NoMemory();
			return -1;
		}

		const char* withoutModifiers = PyObjCRT_SkipTypeQualifiers(type);
		if (*withoutModifiers == _C_ARY_B) {
			/* See below */
			descr->ptrType = PyObjC_kFixedLengthArray;
			descr->arrayArg = 0;
			const char* c = withoutModifiers + 1;
			while (isdigit(*c)) {
				descr->arrayArg *= 10;
				descr->arrayArg += *c - '0';
				c++;
			}

			if (typeModifier) {
				tp[0] = typeModifier;
				tp[1] = _C_PTR;
				strcpy(tp+2, c);
			} else if (type != withoutModifiers) {
				memcpy(tp, type, withoutModifiers - type);
				tp[withoutModifiers - type] = _C_PTR;
				strcpy(tp + 1 + (withoutModifiers - type), c);

			} else {
				tp[0] = _C_IN;
				tp[1] = _C_PTR;
				strcpy(tp+2, c);
			}

		} else if (typeModifier != '\0') {
			/* Skip existing modifiers, we're overriding those */
			strcpy(tp+1, withoutModifiers);
			tp[0] = typeModifier;
		} else {
			strcpy(tp, type);
		}
		descr->typeOverride = YES;
		descr->type = tp;
		Py_XDECREF(bytes);

	} else {
		const char* withoutModifiers = PyObjCRT_SkipTypeQualifiers(descr->type);
		if (*withoutModifiers == _C_ARY_B) {
			/* translate an explicit array definition to the metadata 
			 * equivalent, keeps the rest of the code a lot simpler.
			 */
			char* tp = PyMem_Malloc(strlen(descr->type) + 2);
			if (tp == NULL) {
				PyErr_NoMemory();
				return -1;
			}

			descr->ptrType = PyObjC_kFixedLengthArray;
			descr->arrayArg = 0;
			const char* c = withoutModifiers + 1;
			while (isdigit(*c)) {
				descr->arrayArg *= 10;
				descr->arrayArg += *c - '0';
				c++;
			}

			if (typeModifier != '\0') {
				tp[0] = typeModifier;
				tp[1] = _C_PTR;
				strcpy(tp+2, c);
			} else if (descr->type != withoutModifiers) {
				memcpy(tp, descr->type, withoutModifiers - descr->type);
				tp[withoutModifiers - descr->type] = _C_PTR;
				strcpy(tp + 1 + (withoutModifiers - descr->type), c);
			} else {
				tp[0] = _C_IN;
				tp[1] = _C_PTR;
				strcpy(tp+2, c);
			}

			descr->typeOverride = YES;
			descr->type = tp;

		} else if (descr->type[0] == _C_PTR && descr->type[1] == _C_VOID &&
				descr->ptrType == PyObjC_kPointerPlain) {

			/* Plain old void*, ignore type modifiers */

		} else if (typeModifier != '\0') {

			char* tp = PyMem_Malloc(strlen(descr->type)+2);
			if (tp == NULL) {
				PyErr_NoMemory();
				return -1;
			}

			/* Skip existing modifiers, we're overriding those */
			strcpy(tp+1, withoutModifiers);
			tp[0]  = typeModifier;
			descr->typeOverride = YES;
			descr->type = tp;
		}
	}

	return 0;
}

PyObjCMethodSignature* 
PyObjCMethodSignature_WithMetaData(const char* signature, PyObject* metadata, BOOL is_native)
{
	PyObjCMethodSignature* methinfo;
	PyObject* v;
	ssize_t i;

	//methinfo = PyObjCMethodSignature_FromSignature(signature);
	methinfo = new_methodsignature(signature);
	if (methinfo == NULL) {
		return NULL;
	}

	if (metadata != NULL && !PyDict_Check(metadata)) {
		metadata = NULL;
	}


	if (metadata) {
		PyObject* retval = PyDict_GetItemString(metadata, "retval");
		if (setup_meta(&methinfo->rettype, retval, is_native) == -1) {
			Py_DECREF(methinfo);
			return NULL;
		}

		if (retval != NULL) {
			PyObject* av = PyDict_GetItemString(metadata, "free_result");
			if (av && PyObject_IsTrue(av)) {
				methinfo->free_result = YES;
			}
			Py_XDECREF(av);
		}
	}


	PyObject* args = NULL;
	if (metadata) {
		args = PyDict_GetItemString(metadata, "arguments");
	}
	if (args != NULL && !PyDict_Check(args)) {
		args = NULL;
	}

	for (i = 0; i < Py_SIZE(methinfo); i++) {
		PyObject* k = PyInt_FromLong(i);
		PyObject* d;

		if (args) {
			d = PyDict_GetItem(args, k);
		} else {
			d = NULL;
		}
		if (setup_meta(methinfo->argtype + i, d, is_native) == -1) {
			Py_DECREF(k);
			Py_DECREF(methinfo);
			return NULL;
		}

		Py_DECREF(k);
	}

	if (!metadata) {
		return methinfo;
	}


	v = PyDict_GetItemString(metadata, "suggestion");
	if (v) {
		methinfo->suggestion = v;
		Py_INCREF(v);
	}

	methinfo->null_terminated_array = NO;
	v = PyDict_GetItemString(metadata, "c_array_delimited_by_null");
	if (v && PyObject_IsTrue(v)) {
		methinfo->null_terminated_array = YES;
	}

	methinfo->arrayArg = -1;
	v = PyDict_GetItemString(metadata, "c_array_length_in_arg");
	if (v) {
		if (PyLong_Check(v)) {
			methinfo->arrayArg = PyLong_AsLong(v);
			if (PyErr_Occurred()) {
				return NULL;
			}
		}
#if PY_MAJOR_VERSION == 2
		else if (PyInt_Check(v)) {
			methinfo->arrayArg = PyInt_AsLong(v);
		}
#endif
	}

	methinfo->variadic = NO;
	v = PyDict_GetItemString(metadata, "variadic");
	if (v && PyObject_IsTrue(v)) {
		methinfo->variadic = YES;

		if ((methinfo->suggestion == NULL)
					&& (!methinfo->null_terminated_array)
					&& (methinfo->arrayArg == -1)) {
			for (i = 0; i < Py_SIZE(methinfo); i++) {
				if (methinfo->argtype[i].printfFormat) {
					return methinfo;
				}
			}

			/* No printf-format argument, therefore the method is 
			 * not supported
			 */
			methinfo->suggestion = PyText_FromString("Variadic functions/methods are not supported");
			if (methinfo->suggestion == NULL) {
				Py_DECREF(methinfo);
				return NULL;
			}
		}
	}

	return methinfo;
}


PyObjCMethodSignature* PyObjCMethodSignature_ForSelector(
		Class cls, BOOL isClassMethod, SEL sel, const char* signature,
		BOOL is_native)
{
	PyObjCMethodSignature* methinfo;
	PyObject* metadata;

	metadata = PyObjC_FindInRegistry(registry, cls, sel);

	methinfo =  PyObjCMethodSignature_WithMetaData(signature, metadata, is_native);
	if (isClassMethod) {
		const char* nm  = sel_getName(sel);
		if (strncmp(nm, "new", 3) == 0 && ((nm[3] == 0) || isupper(nm[3]))) {
			methinfo->rettype.alreadyRetained = YES;
		}
	}
	Py_XDECREF(metadata);
	return methinfo;
}

static PyObject*
argdescr2dict(struct _PyObjC_ArgDescr* descr)
{
	PyObject* result;
	PyObject* v;
	const char*     end;
	int r;

	result  = PyDict_New();
	if (result == NULL) return NULL;

	/* 
	 * FromStringAndSize because the type is a segment of the full
	 * method signature. 
	 */
	end = PyObjCRT_SkipTypeSpec(descr->type) - 1;
	while ((end != descr->type) && isdigit(*end)) {
		end --;
	}
	end ++;
	v = PyBytes_FromStringAndSize(descr->type,  end - descr->type);
	if (v == NULL) goto error;
	r = PyDict_SetItemString(result, "type", v);
	Py_DECREF(v);
	if (r == -1) goto error;

	if (descr->printfFormat) {
		v = PyBool_FromLong(descr->printfFormat);
		if (v == NULL) goto error;
		r = PyDict_SetItemString(result, "printf_format", v);
		Py_DECREF(v);
		if (r == -1) goto error;
	}
	
	if (descr->sel_type) {
		v = PyBytes_FromString(descr->sel_type);
		if (v == NULL) goto error;
		r = PyDict_SetItemString(result, "sel_of_type", v);
		Py_DECREF(v);
		if (r == -1) goto error;
	}

	v = PyBool_FromLong(descr->alreadyRetained);
	if (v == NULL) goto error;
	r = PyDict_SetItemString(result, "already_retained", v);
	Py_DECREF(v);
	if (r == -1) goto error;

	v = PyBool_FromLong(descr->alreadyCFRetained);
	if (v == NULL) goto error;
	r = PyDict_SetItemString(result, "already_cfretained", v);
	Py_DECREF(v);
	if (r == -1) goto error;

	if (descr->callable) {
		v = PyObjCMethodSignature_AsDict(descr->callable);
		if (v == NULL) goto error;
		r = PyDict_SetItemString(result, "callable", v);
		Py_DECREF(v);
		if (r == -1) goto error;

		v = PyBool_FromLong(descr->callableRetained);
		if (v == NULL) goto error;
		r = PyDict_SetItemString(result, "callable_retained", v);
		Py_DECREF(v);
		if (r == -1) goto error;
	}

	switch (descr->ptrType) {
	case PyObjC_kPointerPlain: break;
	case PyObjC_kNullTerminatedArray:
		r = PyDict_SetItemString(result, "c_array_delimited_by_null",
				Py_True);
		if (r == -1) goto error;
		break;
	case PyObjC_kArrayCountInArg:
		if (descr->arrayArg == descr->arrayArgOut) {
			v = PyInt_FromLong(descr->arrayArg);
		} else {
			v = Py_BuildValue("ii", descr->arrayArg, descr->arrayArgOut);
		}
		if (v == NULL) goto error;
		r = PyDict_SetItemString(result, "c_array_length_in_arg", v);
		Py_DECREF(v);
		if (r == -1) goto error;
		break;
	case PyObjC_kFixedLengthArray:
		v = PyInt_FromLong(descr->arrayArg);
		if (v == NULL) goto error;
		r = PyDict_SetItemString(result, "c_array_of_fixed_length", v);
		Py_DECREF(v);
		if (r == -1) goto error;
		break;
	case PyObjC_kVariableLengthArray:
		r = PyDict_SetItemString(result, "c_array_of_variable_length",
				Py_True);
		if (r == -1) goto error;

	}

	if (descr->ptrType != PyObjC_kPointerPlain) {
		v = PyBool_FromLong(descr->arraySizeInRetval);
		if (v == NULL) goto error;
		r = PyDict_SetItemString(result, "c_array_length_in_result", v);
		Py_DECREF(v);
		if (r == -1) goto error;
	}

	if (*PyObjCRT_SkipTypeQualifiers(descr->type) == _C_PTR) {
		v = PyBool_FromLong(descr->allowNULL);
		if (v == NULL) goto error;
		r = PyDict_SetItemString(result, "null_accepted", v);
		Py_DECREF(v);
		if (r == -1) goto error;
	}

	return result;

error:
	Py_DECREF(result);
	return NULL;
}

PyObject* 
PyObjCMethodSignature_AsDict(PyObjCMethodSignature* methinfo)
{
	PyObject* result;
	PyObject* v;
	int r;
	Py_ssize_t i;

	result = PyDict_New();
	if (result == NULL) {
		return NULL;
	}
	v = PyBool_FromLong(methinfo->variadic);
	if (v == NULL) goto error;
	r = PyDict_SetItemString(result, "variadic", v);
	Py_DECREF(v);
	if (r == -1) goto error;

	if (methinfo->variadic && methinfo->null_terminated_array) {
		v = PyBool_FromLong(methinfo->null_terminated_array);
		if (v == NULL) goto error;
		r = PyDict_SetItemString(result, "c_array_delimited_by_null", v);
		Py_DECREF(v);
		if (r == -1) goto error;
	}
	if (methinfo->variadic && methinfo->arrayArg != -1) {
		v = PyInt_FromLong(methinfo->arrayArg);
		if (v == NULL) goto error;
		r = PyDict_SetItemString(result, "c_array_length_in_arg", v);
		Py_DECREF(v);
		if (r == -1) goto error;
	}

	if (methinfo->suggestion) {
		r = PyDict_SetItemString(result, "suggestion", 
				methinfo->suggestion);
		if (r == -1) goto error;
	}

	v = argdescr2dict(&methinfo->rettype);
	if (v == NULL) goto error;
	r = PyDict_SetItemString(result, "retval", v);
	Py_DECREF(v);
	if (r == -1) goto error;

	v = PyTuple_New(Py_SIZE(methinfo));
	if (v == NULL) goto error;
	r = PyDict_SetItemString(result, "arguments", v);
	Py_DECREF(v);
	if (r == -1) goto error;
	
	for (i = 0; i < Py_SIZE(methinfo); i++) {
		PyObject* t;

		t = argdescr2dict(methinfo->argtype + i);
		if (t == NULL) goto error;

		PyTuple_SET_ITEM(v, i, t);
	}

	return result;

error:
	Py_XDECREF(result);
	return NULL;
}
