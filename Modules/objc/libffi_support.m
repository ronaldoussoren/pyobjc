/*
 * Support for libffi (http://sources.redhat.com/libffi)
 *
 * libffi is a library that makes it possible to dynamicly create calls
 * to C functions (without knowing the signature at compile-time). It also
 * provides a way to create closures, that is dynamicly create functions with
 * a runtime specified interface.
 *
 * This file contains functions to dynamicly call objc_msgSendSuper and to
 * dynamicly create IMPs for use in Objective-C method dispatch tables. The
 * file 'register.m' contains compile-time generated equivalents of these.
 */
#include "pyobjc.h"

#include "ffi.h"

#ifndef FFI_CLOSURES
#    error "Need FFI_CLOSURES!"
#endif

#if 0 /* Usefull during debugging, only used in the debugger */
static void describe_ffitype(ffi_type* type)
{
	switch (type->type) {
	case FFI_TYPE_VOID: printf("%s", "void"); break;
	case FFI_TYPE_INT: printf("%s", "int"); break;
	case FFI_TYPE_FLOAT: printf("%s", "float"); break;
	case FFI_TYPE_DOUBLE: printf("%s", "double"); break;
	case FFI_TYPE_UINT8: printf("%s", "uint8"); break;
	case FFI_TYPE_SINT8: printf("%s", "sint8"); break;
	case FFI_TYPE_UINT16: printf("%s", "uint16"); break;
	case FFI_TYPE_SINT16: printf("%s", "sint16"); break;
	case FFI_TYPE_UINT32: printf("%s", "uint32"); break;
	case FFI_TYPE_SINT32: printf("%s", "sint32"); break;
	case FFI_TYPE_UINT64: printf("%s", "uint64"); break;
	case FFI_TYPE_SINT64: printf("%s", "sint64"); break;
	case FFI_TYPE_POINTER: printf("%s", "*"); break;
	case FFI_TYPE_STRUCT: {
			ffi_type** elems = type->elements;

			printf("%s", "struct { ");
			if (elems) {
				while (*elems) {
					describe_ffitype(*(elems++));
					printf("%s", "; ");
				}
			}
			printf("%s", "}");
		}
	       break;

	default:
	       // Don't abort, this is called from the debugger 
	       printf("?(%d)", type->type);
	}
}

static void describe_cif(ffi_cif* cif)
{
	size_t i;
	printf("<ffi_cif abi=%d nargs=%d  bytes=%d flags=%#x args=[",
		cif->abi, cif->nargs, cif->bytes, cif->flags);
	for  (i = 0; i < cif->nargs; i++) {
		describe_ffitype(cif->arg_types[i]);
		printf("%s", ", ");
	}
	printf("%s", "] rettype=");
	describe_ffitype(cif->rtype);
	printf("%s", ">\n");
}

#endif

static int align(int offset, int alignment)
{
	int rest = offset % alignment;
	if (rest == 0) return offset;
	return offset + (alignment - rest);
}

static int
count_struct(const char* argtype)
{
	int res = 0;

	if (*argtype != _C_STRUCT_B) return -1;
	while (*argtype != _C_STRUCT_E && *argtype != '=') argtype++;
	if (*argtype == _C_STRUCT_E) return 0;
	
	argtype++;
	while (*argtype != _C_STRUCT_E) {
		argtype = PyObjCRT_SkipTypeSpec(argtype);
		if (argtype == NULL) return -1;
		res ++;
	}
	return res;
}


static void
free_type(void *obj)
{
	free(((ffi_type*)obj)->elements);
	free(obj);
}

static ffi_type* signature_to_ffi_type(const char* argtype);

static ffi_type* 
array_to_ffi_type(const char* argtype)
{
static  PyObject* array_types = NULL; /* XXX: Use NSMap  */
	PyObject* v;
	ffi_type* type;
	int       field_count;
	int        i;
	const char* key = argtype;

	if (array_types == NULL) {
		array_types = PyDict_New();
		if (array_types == NULL) return NULL;
	}

	v = PyDict_GetItemString(array_types, (char*)argtype);
	if (v != NULL) {
		return (ffi_type*)PyCObject_AsVoidPtr(v);
	}

	/* We don't have a type description yet, dynamicly 
	 * create it.
	 */
	field_count = atoi(argtype+1);
			
	type = malloc(sizeof(*type));
	if (type == NULL) {
		PyErr_NoMemory();
		return NULL;
	}
	type->size = PyObjCRT_SizeOfType(argtype);
	type->alignment = PyObjCRT_AlignOfType(argtype);

	/* Libffi doesn't really know about arrays as part of larger 
	 * data-structres (e.g. struct foo { int field[3]; };). We fake it
	 * by treating the nested array as a struct. These seems to work 
	 * fine on MacOS X.
	 */
	type->type = FFI_TYPE_STRUCT;
	type->elements = malloc((1+field_count) * sizeof(ffi_type*));
	if (type->elements == NULL) {
		free(type);
		PyErr_NoMemory();
		return NULL;
	}
	
	while (isdigit(*++argtype));
	type->elements[0] = signature_to_ffi_type(argtype);
	for (i = 1; i < field_count; i++) {
		type->elements[i] = type->elements[0];
	}
	type->elements[field_count] = 0;

	v = PyCObject_FromVoidPtr(type, free_type);
	if (v == NULL) {
		free_type(type);
		return NULL;
	}

	PyDict_SetItemString(array_types, (char*)key, v);
	if (PyErr_Occurred()) {
		Py_DECREF(v);
		return NULL;
	}
	Py_DECREF(v);
	return type;
}

static ffi_type* 
struct_to_ffi_type(const char* argtype)
{
static  PyObject* struct_types = NULL; /* XXX: Use NSMap  */
	PyObject* v;
	ffi_type* type;
	int       field_count;
	const char*     curtype;

	if (struct_types == NULL) {
		struct_types = PyDict_New();
		if (struct_types == NULL) return NULL;
	}

	v = PyDict_GetItemString(struct_types, (char*)argtype);
	if (v != NULL) {
		return (ffi_type*)PyCObject_AsVoidPtr(v);
	}

	/* We don't have a type description yet, dynamicly 
	 * create it.
	 */
	field_count = count_struct(argtype);
	if (field_count == -1) {
		ObjCErr_Set(ObjCExc_internal_error,
			"Cannot determine layout of %s", argtype);
		return NULL;
	}
			
	type = malloc(sizeof(*type));
	if (type == NULL) {
		PyErr_NoMemory();
		return NULL;
	}
	type->size = PyObjCRT_SizeOfType(argtype);
	type->alignment = PyObjCRT_AlignOfType(argtype);
	type->type = FFI_TYPE_STRUCT;
	type->elements = malloc((1+field_count) * sizeof(ffi_type*));
	if (type->elements == NULL) {
		free(type);
		PyErr_NoMemory();
		return NULL;
	}
	
	field_count = 0;
	curtype = argtype+1;
	while (*curtype != _C_STRUCT_E && *curtype != '=') curtype++;
	if (*curtype == '=') {
		curtype ++;
		while (*curtype != _C_STRUCT_E) {
			type->elements[field_count] = 
				signature_to_ffi_type(curtype);
			if (type->elements[field_count] == NULL) {
				free(type->elements);
				return NULL;
			}
			field_count++;
			curtype = PyObjCRT_SkipTypeSpec(curtype);
			if (curtype == NULL) {
				free(type->elements);
				return NULL;
			}
		}
	}
	type->elements[field_count] = NULL;

	v = PyCObject_FromVoidPtr(type, free_type);
	if (v == NULL) {
		free_type(type);
		return NULL;
	}

	PyDict_SetItemString(struct_types, (char*)argtype, v);
	if (PyErr_Occurred()) {
		Py_DECREF(v);
		return NULL;
	}
	Py_DECREF(v);
	return type;
}

static ffi_type*
signature_to_ffi_return_type(const char* argtype)
{
	switch (*argtype) {
	case _C_CHR: case _C_SHT:
		return &ffi_type_sint;
	case _C_UCHR: case _C_USHT:
		return &ffi_type_uint;
#ifdef _C_BOOL
	case _C_BOOL: return &ffi_type_sint;
#endif	
	default:
		return signature_to_ffi_type(argtype);
	}
}


static ffi_type*
signature_to_ffi_type(const char* argtype)
{
	switch (*argtype) {
	case _C_VOID: return &ffi_type_void;
	case _C_ID: return &ffi_type_pointer;
	case _C_CLASS: return &ffi_type_pointer;
	case _C_SEL: return &ffi_type_pointer;
	case _C_CHR: return &ffi_type_schar;
#ifdef _C_BOOL
	case _C_BOOL: return &ffi_type_sint;
#endif	
	case _C_UCHR: return &ffi_type_uchar;
	case _C_SHT: return &ffi_type_sshort;
	case _C_USHT: return &ffi_type_ushort;
	case _C_INT: return &ffi_type_sint;
	case _C_UINT: return &ffi_type_uint;

	 /* The next to defintions are incorrect, but the correct definitions
	  * don't work (e.g. give testsuite failures). We should be fine
	  * as long as sizeof(long) == sizeof(int)
	  */
	case _C_LNG: return &ffi_type_sint;  /* ffi_type_slong */
	case _C_ULNG: return &ffi_type_uint;  /* ffi_type_ulong */
	case _C_LNGLNG: return &ffi_type_sint64;
	case _C_ULNGLNG: return &ffi_type_uint64;
	case _C_FLT: return &ffi_type_float;
	case _C_DBL: return &ffi_type_double;
	case _C_CHARPTR: return &ffi_type_pointer;
	case _C_PTR: return &ffi_type_pointer;
	case _C_ARY_B: 
		return array_to_ffi_type(argtype);
	case _C_IN: case _C_OUT: case _C_INOUT: case _C_CONST:
		return signature_to_ffi_type(argtype+1);
	case _C_STRUCT_B: 
		return struct_to_ffi_type(argtype);
	default:
		ObjCErr_Set(PyExc_NotImplementedError,
			"Type '%x' not supported", *argtype);
		return NULL;
	}
}

/*
 * arg_signature_to_ffi_type: Make the ffi_type for the call to the method IMP,
 * on MacOS X this is the same as the normal signature_to_ffi_type, but on
 * Linux/GNUstep we need a slightly different function.
 */
#ifdef MACOSX
#define arg_signature_to_ffi_type signature_to_ffi_type

#else

static inline ffi_type*
arg_signature_to_ffi_type(const char* argtype)
{
	/* NOTE: This is the minimal change to pass the unittests, it is not
	 * based on analysis of the calling conventions.
	 */
	switch (*argtype) {
	case _C_CHR: return &ffi_type_sint;
	case _C_UCHR: return &ffi_type_uint;
	case _C_SHT: return &ffi_type_sint;
	case _C_USHT: return &ffi_type_uint;
	default: return signature_to_ffi_type(argtype);
	}
}

#endif

/* This function decodes its arguments into Python values, then
 * calls the python method and finally encodes the return value
 */

typedef struct {
	PyObject* callable;
	PyObjCMethodSignature* methinfo;
} _method_stub_userdata;

static void 
method_stub(ffi_cif* cif __attribute__((__unused__)), void* resp, void** args, void* _userdata)
{
	_method_stub_userdata* userdata = (_method_stub_userdata*)_userdata;
	PyObject* callable = userdata->callable;
	PyObjCMethodSignature* methinfo = userdata->methinfo;
	int isAlloc = 0;
	int                argOffset;
	int                i;
	PyObject*          arglist;
	PyObject*          res;
	PyObject*          v;
	int                have_output = 0;
	const char*        rettype;

	PyGILState_STATE   state = PyGILState_Ensure();

	rettype = methinfo->rettype;

	if (((size_t)PyObjCRT_SizeOfType(rettype) > sizeof(id))
		 	&& *rettype != _C_DBL && *rettype != _C_FLT
		 	&& *rettype != _C_LNGLNG && *rettype != _C_ULNGLNG) {
		/* the prototype is objc_msgSend_stret(void* retbuf, ... */
		resp = *(void**)args[0];
		argOffset = 1;
	} else {
		argOffset = 0;
	}

	arglist = PyList_New(0);
	v = pythonify_c_value("@", args[0+argOffset]);
	if (v == NULL) {
		goto error;
	}
	if (PyList_Append(arglist, v) == -1) {
		goto error;
	}
	Py_DECREF(v);

	/* First translate from Objective-C to python */
	
	for (i = 2; i < methinfo->nargs; i++) {

		const char* argtype = methinfo->argtype[i];

		switch (*argtype) {
		case _C_INOUT: 
			if (argtype[1] == _C_PTR) {
				have_output ++;
			}
			/* FALL THROUGH */
		case _C_IN: case _C_CONST:
			if (argtype[1] == _C_PTR) {
				v = pythonify_c_value(argtype+2, 
						*(void**)args[i+argOffset]);
			} else {
				v = pythonify_c_value(argtype+1, 
						args[i+argOffset]);
			}
			break;
		case _C_OUT:
			/* Skip output parameter */
			if (argtype[1] == _C_PTR) {
				have_output ++;
			}
			continue;
		default:
			v = pythonify_c_value(argtype, args[i+argOffset]);
		}
		if (v == NULL) {
			Py_DECREF(arglist);
			goto error;
		}
		if (PyList_Append(arglist, v) == -1) {
			Py_DECREF(v);
			Py_DECREF(arglist);
			goto error;
		}
		Py_DECREF(v); 
	}

	v = PyList_AsTuple(arglist);
	if (v == NULL) {
		Py_DECREF(arglist);
		goto error;
	}
	Py_DECREF(arglist);
	arglist = v;

	if (!callable) {
		res = PyObjC_CallPython(*(id*)args[0+argOffset], *(SEL*)args[1+argOffset], arglist, &isAlloc);
	} else {
		if (callable != userdata->callable) abort();

		res = PyObject_Call(callable, arglist, NULL);
		isAlloc = 0;
	}
	Py_DECREF(arglist);
	if (res == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
	}

	if (!have_output) {
		int err;

		if (*rettype != _C_VOID) {
			err = depythonify_c_return_value(rettype, res, resp);

			if (isAlloc && *rettype == _C_ID) {
			   /* Must return a 'new' instead of a borrowed 
			    * reference.
			    */
			   [(*(id*)resp) retain];
			} else if (*rettype == _C_ID && res->ob_refcnt == 1) {
				/* make sure return value doesn't die before
				 * the caller can get its hands on it.
				 */
			    [[(*(id*)resp) retain] autorelease];
			}
			Py_DECREF(res);
			if (err == -1) {
				goto error;
			}
		}
	} else {
		/* We have some output parameters, locate them and encode
		 * their values
		 */
		int idx;
		PyObject* real_res;

		if (*rettype == _C_VOID && have_output == 1) {
			/* Special case: the python method returned only
			 * the return value, not a tuple.
			 */
			for (i = 2; i < methinfo->nargs; i++) {
				const char* argtype = methinfo->argtype[i];
				int err;

				switch (*argtype) {
				case _C_INOUT: case _C_OUT:
					if (argtype[1] != _C_PTR) {
						continue;
					}
					argtype += 2;
					break;
				default: continue;
				}

				err = depythonify_c_value(argtype, res, *(void**)args[i]);
				if (err == -1) {
					goto error;
				}
				if (v->ob_refcnt == 1 && argtype[0] == _C_ID) {
					/* make sure return value doesn't die before
					 * the caller can get its hands on it.
					 */
					[[**(id**)args[i] retain] autorelease];
				}

				break;
			}

			PyGILState_Release(state);
			return;
		}

		if (*rettype != _C_VOID) {
			if (!PyTuple_Check(res) || PyTuple_Size(res) != have_output+1) {
				ObjCErr_Set(PyExc_TypeError,
					"%s: Need tuple of %d arguments as result",
					PyObjCRT_SELName(*(SEL*)args[1]), have_output+1);
				Py_DECREF(res);
				goto error;
			}

			real_res = PyTuple_GET_ITEM(res, 0);
			idx = 1;
		} else {
			if (!PyTuple_Check(res) || PyTuple_Size(res) != have_output) {
				ObjCErr_Set(PyExc_TypeError,
					"%s: Need tuple of %d arguments as result",
					PyObjCRT_SELName(*(SEL*)args[1]), have_output);
				Py_DECREF(res);
				goto error;
			}
			real_res = NULL;
			idx = 0;
		}


		for (i = 2; i < methinfo->nargs; i++) {
			const char* argtype = methinfo->argtype[i];
			int err;

			switch (*argtype) {
			case _C_INOUT: case _C_OUT:
				if (argtype[1] != _C_PTR) {
					continue;
				}
				argtype += 2;
				break;
			default: continue;
			}

			v = PyTuple_GET_ITEM(res, idx++);
			err = depythonify_c_value(argtype, v, *(void**)args[i]);
			if (err == -1) {
				goto error;
			}
			if (v->ob_refcnt == 1 && argtype[0] == _C_ID) {
				/* make sure return value doesn't die before
				 * the caller can get its hands on it.
				 */
				[[**(id**)args[i] retain] autorelease];
			}
		}

		if (*rettype != _C_VOID) {
			int err = depythonify_c_return_value(rettype, 
				real_res, resp);

			if (isAlloc && *rettype == _C_ID) {
			   /* Must return a 'new' instead of a borrowed 
			    * reference.
			    */
			   [(*(id*)resp) retain];
			} else if (*rettype == _C_ID && real_res->ob_refcnt == 1) {
				/* make sure return value doesn't die before
				 * the caller can get its hands on it.
				 */
			    [[(*(id*)resp) retain] autorelease];
			}
			if (err == -1) {
				Py_DECREF(res);
				goto error;
			}
		}

		Py_DECREF(res);

	}

	PyGILState_Release(state);
	
	return;

error:
	PyObjCErr_ToObjCWithGILState(&state);
}

/* 
 * Return an IMP that is suitable for forwarding a method with the specified
 * signature from Objective-C to Python.
 */
IMP
ObjC_MakeIMPForSignature(char* signature, PyObject* callable)
{
	_method_stub_userdata* stubUserdata;
	ffi_cif           *cif;
	ffi_closure       *cl;
	ffi_type**        cl_arg_types;
	ffi_type*         cl_ret_type;
	ffi_status        rv;
	int               i;
	const char*  rettype;
	int argOffset;
	PyObjCMethodSignature* methinfo;

	/* Build FFI returntype description */
	methinfo = PyObjCMethodSignature_FromSignature(signature);
	if (methinfo == NULL) {
		return NULL;
	}
	rettype = methinfo->rettype;

	if (((size_t)PyObjCRT_SizeOfType(rettype) > sizeof(id))
		 	&& *rettype != _C_DBL && *rettype != _C_FLT
		 	&& *rettype != _C_LNGLNG && *rettype != _C_ULNGLNG) {
		/* the prototype is objc_msgSend_stret(void* retbuf, ... */
		argOffset = 1;
		cl_ret_type = &ffi_type_void;
	} else {
		argOffset = 0;
		cl_ret_type = signature_to_ffi_return_type(rettype);
		if (cl_ret_type == NULL) {
			PyObjCMethodSignature_Free(methinfo);
			return NULL;
		}
	}

	/* Build FFI argumentlist description */
	cl_arg_types = malloc(sizeof(ffi_type*) * (argOffset+methinfo->nargs));
	if (cl_arg_types == NULL) {
		PyObjCMethodSignature_Free(methinfo);
		free(cl_ret_type);
		PyErr_NoMemory();
		return NULL;
	}

	if (argOffset) {
		cl_arg_types[0] = &ffi_type_pointer;
	}

	for (i = 0; i < methinfo->nargs; i++) {
		cl_arg_types[i+argOffset] = arg_signature_to_ffi_type(
			methinfo->argtype[i]);
		if (cl_arg_types[i+argOffset] == NULL) {
			PyObjCMethodSignature_Free(methinfo);
			free(cl_arg_types);
			return NULL;
		}
	}

	/* Create the invocation description */
	cif = malloc(sizeof(*cif));
	if (cif == NULL) {
		PyObjCMethodSignature_Free(methinfo);
		free(cl_arg_types);
		PyErr_NoMemory();
		return NULL;
	}

	/*  XXX: When calling a method with a structured return-value we
	 * use objc_msgSendSuper_stret, should the method stub have a return
	 * buffer argument in those cases? Hmm, maybe libffi knows about this.
	 */
	rv = ffi_prep_cif(cif, FFI_DEFAULT_ABI, methinfo->nargs+argOffset, 
		cl_ret_type, cl_arg_types);
	if (rv != FFI_OK) {
		PyObjCMethodSignature_Free(methinfo);
		free(cl_arg_types);
		ObjCErr_Set(PyExc_RuntimeError,
			"Cannot create FFI CIF: %d", rv);
		return NULL;
	}

	/* And finally create the actual closure */
	cl = malloc(sizeof(*cl));
	if (cl == NULL) {
		PyObjCMethodSignature_Free(methinfo);
		free(cl_arg_types);
		free(cif);
		PyErr_NoMemory();
		return NULL;
	}
	stubUserdata = malloc(sizeof(*stubUserdata));
	stubUserdata->methinfo = methinfo;

	if (callable) {
		stubUserdata->callable = callable;
		Py_INCREF(stubUserdata->callable);
	} else {
		stubUserdata->callable = NULL;
	}

	rv = ffi_prep_closure(cl, cif, method_stub, (void*)stubUserdata);
	if (rv != FFI_OK) {
		PyObjCMethodSignature_Free(methinfo);
		if (stubUserdata->callable) {
			Py_DECREF(stubUserdata->callable);
		}
		free(stubUserdata);
		ObjCErr_Set(PyExc_RuntimeError,
			"Cannot create FFI closure: %d", rv);
		return NULL;
	}

	return (IMP)cl;
}

IMP
ObjC_MakeIMPForPyObjCSelector(PyObjCSelector *aSelector) 
{
	if (ObjCNativeSelector_Check(aSelector)) {
		ObjCNativeSelector *nativeSelector = 
			(ObjCNativeSelector *) aSelector;
		PyObjCRT_Method_t aMethod;

		if (nativeSelector->sel_flags & PyObjCSelector_kCLASS_METHOD) {
			aMethod = class_getClassMethod(nativeSelector->sel_class, nativeSelector->sel_selector);
		} else {
			aMethod = class_getInstanceMethod(nativeSelector->sel_class, nativeSelector->sel_selector);
		}
		return aMethod->method_imp;
	} else {
		ObjCPythonSelector *pythonSelector = (ObjCPythonSelector *) aSelector;
		return ObjC_MakeIMPForSignature(pythonSelector->sel_signature, pythonSelector->callable);
	}
}


PyObject *
ObjC_FFICaller(PyObject *aMeth, PyObject* self, PyObject *args)
{
	size_t            argbuf_len = 0;
	size_t            argbuf_cur = 0;
	unsigned char* volatile    argbuf = NULL;
	int            byref_in_count = 0;
	volatile int            byref_out_count = 0;
	int            plain_count = 0;
	size_t            py_arg;
	int               i;
	void** volatile	byref = NULL; /* offset for arguments in argbuf */
	const char* 	  rettype;
	PyObjCMethodSignature*  volatile methinfo;
	ObjCNativeSelector* meth = (ObjCNativeSelector*)aMeth;
	PyObject* volatile  objc_result = NULL;
	PyObject* volatile  result = NULL;
	id		  self_obj = nil;
	struct objc_super super;
	struct objc_super* superPtr;
	ffi_cif		  cif;
	ffi_type*	  arglist[64]; /* XX: Magic constant */
	void*             values[64];
	int               r;
	void*		  msgResult;
	int               resultSize;
	volatile int               arglistOffset;
	int		  itemSize;
	int		  itemAlign;
	void*		  arg;

	if (meth->sel_oc_signature) {
		methinfo = meth->sel_oc_signature;
	} else {
		methinfo = PyObjCMethodSignature_FromSignature(meth->sel_signature);
		if (methinfo == NULL) {
			return NULL;
		}

		meth->sel_oc_signature = methinfo;
	}
	rettype = methinfo->rettype;

	resultSize = PyObjCRT_SizeOfReturnType(rettype);
	if (resultSize == -1) {
		return NULL;
	}


	/* First count the number of by reference parameters, and the number
	 * of bytes of storage needed for them. Note that arguments 0 and 1
	 * are self and the selector, no need to count those.
	 */
	argbuf_len = resultSize;

	for (i = 2; i < methinfo->nargs; i++) {
		const char *argtype = methinfo->argtype[i];

		switch (*argtype) {
		case _C_INOUT:
			if (argtype[1] == _C_PTR) {
				byref_out_count ++;
				byref_in_count ++;
				itemAlign = PyObjCRT_AlignOfType(argtype+2);
				itemSize = PyObjCRT_SizeOfType(argtype+2);
				if (itemSize == -1) {
					return NULL;
				}
			} else {
				itemSize = PyObjCRT_SizeOfType(argtype+1);
				itemAlign = PyObjCRT_AlignOfType(argtype+1);
				if (itemSize == -1) {
					return NULL;
				}
			}
			argbuf_len = align(argbuf_len, itemAlign);
			argbuf_len += itemSize;
			break;

		case _C_IN: case _C_CONST:
			if (argtype[1] == _C_PTR) {
				byref_in_count ++;
				itemSize = PyObjCRT_SizeOfType(argtype+2);
				itemAlign = PyObjCRT_AlignOfType(argtype+2);
				if (itemSize == -1) {
					return NULL;
				}
			} else {
				plain_count ++;
				itemSize = PyObjCRT_SizeOfType(argtype+1);
				itemAlign = PyObjCRT_AlignOfType(argtype+1);
				if (itemSize == -1) {
					return NULL;
				}
			}
			argbuf_len = align(argbuf_len, itemAlign);
			argbuf_len += itemSize;
			break;

		case _C_OUT:
			if (argtype[1] == _C_PTR) {
				byref_out_count ++;
				itemSize = PyObjCRT_SizeOfType(argtype+2);
				itemAlign = PyObjCRT_AlignOfType(argtype+2);
				if (itemSize == -1) {
					return NULL;
				}
			} else {
				plain_count++;
				itemSize = PyObjCRT_SizeOfType(argtype+1);
				itemAlign = PyObjCRT_AlignOfType(argtype+1);
				if (itemSize == -1) {
					return NULL;
				}
			}
			argbuf_len = align(argbuf_len, itemAlign);
			argbuf_len += itemSize;
			break;

		case _C_STRUCT_B: case _C_UNION_B: case _C_ARY_B:
			plain_count++;
			itemSize = PyObjCRT_SizeOfType(argtype);
			itemAlign = PyObjCRT_AlignOfType(argtype);
			if (itemSize == -1) {
				return NULL;
			}
			argbuf_len = align(argbuf_len, itemAlign);
			argbuf_len += itemSize;
			break;

		default:
			itemSize = PyObjCRT_SizeOfType(argtype);
			itemAlign = PyObjCRT_AlignOfType(argtype);
			if (itemSize == -1) {
				return NULL;
			}
			argbuf_len = align(argbuf_len, itemAlign);
			argbuf_len += itemSize;
			plain_count++;
			break;
		}
	}

	/* 
	 * We need input arguments for every normal argument and for every
	 * input argument that is passed by reference.
	 */
	if (PyTuple_Size(args) != (plain_count + byref_in_count)) {
		ObjCErr_Set(PyExc_TypeError, "Need %d arguments, got %d",
			plain_count + byref_in_count, PyTuple_Size(args));
		goto error_cleanup;
	}


	argbuf = PyMem_Malloc(argbuf_len);
	if (argbuf == 0) {
		PyErr_NoMemory();
		goto error_cleanup;
	}
	byref = PyMem_Malloc(sizeof(void*) * methinfo->nargs);
	if (byref == NULL) {
		PyErr_NoMemory();
		goto error_cleanup;
	}

	/* Set 'self' argument, for class methods we use the class */ 
	if (meth->sel_flags & PyObjCSelector_kCLASS_METHOD) {
		if (PyObjCObject_Check(self)) {
			self_obj = PyObjCObject_GetObject(self);
			if (self_obj != NULL) {
				self_obj = GETISA(self_obj);
			}
		} else if (PyObjCClass_Check(self)) {
			self_obj = PyObjCClass_GetClass(self);
		} else {
			PyErr_SetString(PyExc_TypeError, 
				"Need objective-C object or class as self");
			goto error_cleanup;
		}
	} else {
		int err;
		if (PyObjCObject_Check(self)) {
			self_obj = PyObjCObject_GetObject(self);
		} else {
			err = depythonify_c_value("@", self, &self_obj);
			if (err == -1) {
				goto error_cleanup;
			}
		}
	}

	RECEIVER(super) = self_obj;
	if (meth->sel_flags & PyObjCSelector_kCLASS_METHOD) {
		super.class = GETISA(meth->sel_class);
	} else {
		super.class = meth->sel_class;
	}

#ifdef GNU_RUNTIME
	arglistOffset = 0;

#else /* !GNU_RUNTIME */
	if (*rettype == _C_DBL || *rettype == _C_FLT ||
		 *rettype == _C_LNGLNG || *rettype == _C_ULNGLNG) {

		/* Libffi knows how to pass them, and ..._stret doesn't work
		 * with these...
		 */

		arglistOffset = 0;
	} else if ((size_t)resultSize > sizeof(id)) {
		arglistOffset = 1;
		arglist[0] = &ffi_type_pointer;
		values[0] = &msgResult;
	} else {
		arglistOffset = 0;
	}
#endif
	
	superPtr = &super;
	arglist[arglistOffset + 0] = &ffi_type_pointer;
	values[arglistOffset + 0] = &superPtr;
	arglist[arglistOffset + 1] = &ffi_type_pointer;
	values[arglistOffset + 1] = &meth->sel_selector;
	msgResult = argbuf;
	argbuf_cur = resultSize;

	py_arg = 0;
	for (i = 2; i < methinfo->nargs; i++) {
		int error;
		PyObject *argument;
		const char *argtype = methinfo->argtype[i];

		if (argtype[0] == _C_OUT && argtype[1] == _C_PTR) {
			/* Just allocate room in argbuf and set that*/
			int sz;

			argbuf_cur = align(argbuf_cur, 
				PyObjCRT_AlignOfType(argtype+2));
			arg = argbuf + argbuf_cur;
			byref[i] = arg;

			arglist[arglistOffset + i] = &ffi_type_pointer;
			values[arglistOffset + i] = byref+i;

			sz = PyObjCRT_SizeOfType(argtype+2);
			argbuf_cur += sz;

			/* Clear the output buffer, just in case the called
			 * function doesn't write anything into the buffer.
			 */
			memset(arg, 0, sz);
		} else {
			/* Encode argument, maybe after allocating space */

			if (argtype[0] == _C_OUT) argtype ++;

			argument = PyTuple_GET_ITEM (args, py_arg);
			switch (*argtype) {
			case _C_STRUCT_B: case _C_ARY_B: case _C_UNION_B:
				/* Allocate space and encode */
				{
					argbuf_cur = align(argbuf_cur, 
						PyObjCRT_AlignOfType(argtype));
					arg = argbuf + argbuf_cur;
					argbuf_cur += PyObjCRT_SizeOfType(argtype);
					byref[i] = arg;
	  				error = depythonify_c_value (
						argtype, 
						argument, 
						arg);


					arglist[arglistOffset + i] = 
						signature_to_ffi_type(argtype);
					values[arglistOffset + i] = arg;
				} 
				break;
			case _C_INOUT:
			case _C_IN:
			case _C_CONST:

				if (argtype[1] == _C_PTR) {
					/* Allocate space and encode */
					argbuf_cur = align(argbuf_cur, PyObjCRT_AlignOfType(argtype+2)); 
					arg = argbuf + argbuf_cur;
					argbuf_cur += PyObjCRT_SizeOfType(argtype+2);
					byref[i] = arg;
	  				error = depythonify_c_value (
						argtype+2, 
						argument, 
						arg);

					arglist[arglistOffset + i] = &ffi_type_pointer;
					values[arglistOffset + i] = byref + i;

				} else {
					/* just encode */
					argbuf_cur = align(argbuf_cur, PyObjCRT_AlignOfType(argtype+1));
					arg = argbuf + argbuf_cur;
					argbuf_cur += PyObjCRT_SizeOfType(argtype+1);
	  				error = depythonify_c_value (
						argtype+1, 
						argument, 
						arg);

					arglist[arglistOffset + i] = signature_to_ffi_type(
						argtype+1);
					values[arglistOffset + i] = arg;

				}
				break;
			default:
				{
				argbuf_cur = align(argbuf_cur, PyObjCRT_AlignOfType(argtype));
				arg = argbuf + argbuf_cur;
				argbuf_cur += PyObjCRT_SizeOfType(argtype);

	  			error = depythonify_c_value (
					argtype, 
					argument, 
					arg);

				arglist[arglistOffset + i] = signature_to_ffi_type(argtype);
				values[arglistOffset + i] = arg;
				}
			}

			if (error == -1) {
				goto error_cleanup;
			}
			py_arg++;
		}
	}

	PyErr_Clear();
	if (arglistOffset) {
		r = ffi_prep_cif(&cif, FFI_DEFAULT_ABI, methinfo->nargs+1,
			&ffi_type_void, arglist);
	} else {
		r = ffi_prep_cif(&cif, FFI_DEFAULT_ABI, methinfo->nargs,
			signature_to_ffi_return_type(rettype), arglist);
	}
	if (r != FFI_OK) {
		ObjCErr_Set(PyExc_RuntimeError,
			"Cannot setup FFI CIF [%d]", r);
		goto error_cleanup;
	}

	NS_DURING
#ifdef GNU_RUNTIME
		/* 
		 * The GNU runtime doesn't have a objc_msgSendSuper function,
		 * and we implement it ourselves using a macro (the 'obvious'
		 * implementation using a function doesn't work). This means
		 * we have duplicate part of that implementation here.
		 *
		 * XXX: If this works correctly with proxy objects, NSInvocation
		 * and the like we might consider moving all platforms over
		 * to this structure.
		 */
		Method_t m = class_get_instance_method(super.class, 
			meth->sel_selector);

		values[0] = &super.self;
		ffi_call(&cif, FFI_FN(m->method_imp), 
			msgResult, values);

#else /* !GNU_RUNTIME */

		if (arglistOffset) {
			ffi_call(&cif, FFI_FN(objc_msgSendSuper_stret), 
				NULL, values);
		} else {
			ffi_call(&cif, FFI_FN(objc_msgSendSuper), 
				msgResult, values);

		}
#endif /* !GNU_RUNTIME */

	NS_HANDLER
		PyObjCErr_FromObjC(localException);
	NS_ENDHANDLER

	if (PyErr_Occurred()) goto error_cleanup;

	if ( (*rettype != _C_VOID) /* && ([methinfo isOneway] == NO) */ ) {
		objc_result = pythonify_c_return_value (rettype, msgResult);
	} else {
		Py_INCREF(Py_None);
		objc_result =  Py_None;
	}
	if ( (meth->sel_flags & PyObjCSelector_kRETURNS_SELF)
		&& (objc_result != self)) {

		/* meth is a method that returns a possibly reallocated
		 * version of self and self != return-value, the current
		 * value of self is assumed to be no longer valid
		 */
		if (PyObjCObject_Check(self) && PyObjCObject_Check(objc_result)
			&& (meth->sel_flags & PyObjCSelector_kINITIALIZER) &&
			(((PyObjCObject*)self)->flags & PyObjCObject_kUNINITIALIZED)) {
			[PyObjCObject_GetObject(objc_result) release];
		}
		PyObjCObject_ClearObject(self);
	}

	if (byref_out_count == 0) {
		result = objc_result;
	} else {

		if (*rettype == _C_VOID) {
			if (byref_out_count > 1) {
				result = PyTuple_New(byref_out_count);
				if (result == 0) goto error_cleanup;
			} else {
				result = NULL;
			}
			Py_DECREF(objc_result);
			py_arg = 0;
		} else {
			result = PyTuple_New(byref_out_count+1);
			if (result == 0) goto error_cleanup;
			if (PyTuple_SetItem(result, 0, objc_result) < 0) {
				goto error_cleanup;
			}
			py_arg = 1;
		}
		objc_result = NULL;

		for (i = 2; i < methinfo->nargs; i++) {
			const char *argtype = methinfo->argtype[i];
			PyObject*   v;

			switch (*argtype) {
			case _C_INOUT:
			case _C_OUT:
				if (argtype[1] == _C_PTR) {
					arg = byref[i];
					v = pythonify_c_value(argtype+2, arg);
					if (!v) goto error_cleanup;

					if (result != NULL) {
						if (PyTuple_SetItem(result, 
							py_arg++, v) < 0) {

							Py_DECREF(v);
							goto error_cleanup;
						}
					} else {
						result = v;
					}
				}
				break;
			}
		}
	}

	PyMem_Free(argbuf);
	argbuf = NULL;
	PyMem_Free(byref);
	byref = NULL;
	methinfo = NULL;

	return result;

error_cleanup:

	if (objc_result) {
		Py_DECREF(objc_result);
		objc_result = NULL;
	}
	if (result) {
		Py_DECREF(result);
		result = NULL;
	}
	if (argbuf) {
		PyMem_Free(argbuf);
		argbuf = NULL;
	}
	if (byref) {
		PyMem_Free(byref);
		byref = NULL;
	}
	return NULL;
}
