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
 *
 * NOTES:
 * - libffi support is optionial because it is highly experimental. To avoid
 *   code duplication it is my (Ronald's) intention to move to a situation 
 *   where libffi support is required. This should also make it possible to
 *   simplify some code. 
 * - If libffi stays optional, we should refactor ObjC_FFICaller (in this file)
 *   and execute_and_pythonify_objc_method (in objc_support.m): These are
 *   almost identical.
 */
#ifndef OC_WITH_LIBFFI

static int OBJC_FFI_SUPPORT_dummy = 0;

#warning "No FFI support"

#else /* OC_WITH_LIBFFI */

#include "ffi.h"
#include "pyobjc.h"
#include "objc_support.h"

#ifndef FFI_CLOSURES
#    error "Need FFI_CLOSURES!"
#endif

static int
count_struct(const char* argtype)
{
	int res = 0;

	if (*argtype != _C_STRUCT_B) return -1;
	while (*argtype != _C_STRUCT_E && *argtype != '=') argtype++;
	if (*argtype == _C_STRUCT_E) return 0;
	
	argtype++;
	while (*argtype != _C_STRUCT_E) {
		argtype = objc_skip_typespec(argtype);
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
struct_to_ffi_type(const char* argtype)
{
static  PyObject* struct_types = NULL;
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
	if (field_count == -1) abort();
	type = malloc(sizeof(*type));
	if (type == NULL) {
		PyErr_NoMemory();
		return NULL;
	}
	type->size = 0;
	type->alignment = 0;
	type->type = FFI_TYPE_STRUCT;
	type->elements = malloc((1+field_count) * sizeof(*type->elements));
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
				abort();
				free(type->elements);
				return NULL;
			}
			field_count++;
			curtype = objc_skip_typespec(curtype);
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
	return type;
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
	case _C_UCHR: return &ffi_type_uchar;
	case _C_SHT: return &ffi_type_sshort;
	case _C_USHT: return &ffi_type_ushort;
	case _C_INT: return &ffi_type_sint;
	case _C_UINT: return &ffi_type_uint;
	case _C_LNG: return &ffi_type_slong;
	case _C_ULNG: return &ffi_type_ulong;
	case _C_LNGLNG: return &ffi_type_sint64;
	case _C_ULNGLNG: return &ffi_type_uint64;
	case _C_FLT: return &ffi_type_float;
	case _C_DBL: return &ffi_type_double;
	case _C_CHARPTR: return &ffi_type_pointer;
	case _C_PTR: return &ffi_type_pointer;
	case _C_ARY_B: return &ffi_type_pointer;
	case _C_IN: case _C_OUT: case _C_INOUT: case _C_CONST:
		return signature_to_ffi_type(argtype+1);
	case _C_STRUCT_B: 
		return struct_to_ffi_type(argtype);
	case 0:
		abort();
	default:
		ObjCErr_Set(PyExc_NotImplementedError,
			"Type '%x' not supported", *argtype);
		return NULL;
	}
}

/* This function decodes its arguments into Python values, then
 * calls the python method and finally encodes the return value
 *
 * TODO: Check that this implements the reverse of ObjC_FFICaller
 * TODO2: Do not use NSMethodSignature
 */
static void 
method_stub(ffi_cif* cif, void* resp, void** args, void* userdata)
{
	NSMethodSignature* methinfo = (NSMethodSignature*)userdata;
	int                objc_argcount;
	int                i;
	PyObject*          arglist;
	PyObject*          res;
	PyObject*          v;
	int                have_output = 0;

	objc_argcount = [methinfo numberOfArguments];

	arglist = PyList_New(0);
	PyList_Append(arglist, pythonify_c_value("@", args[0]));

	/* First translate from Objective-C to python */
	for (i = 2; i < objc_argcount; i++) {
		const char* argtype = [methinfo getArgumentTypeAtIndex:i];

		switch (*argtype) {
		case _C_PTR:
			have_output ++;
			v = pythonify_c_value(argtype+1, *(void**)args[i]);
			break;
		case _C_INOUT: 
			if (argtype[1] == _C_PTR) {
				have_output ++;
			}
			/* FALL THROUGH */
		case _C_IN: case _C_CONST:
			if (argtype[1] == _C_PTR) {
				v = pythonify_c_value(argtype+2, *(void**)args[i]);
			} else {
				v = pythonify_c_value(argtype+2, args[i]);
			}
			break;
		case _C_OUT:
			/* Skip output parameter */
			if (argtype[1] == _C_PTR) {
				have_output ++;
			}
			continue;
		default:
			v = pythonify_c_value(argtype, args[i]);
		}
		if (v == NULL) {
			Py_DECREF(arglist);
			ObjCErr_ToObjC();
			return;
		}
		PyList_Append(arglist, v);
	}

	v = PyList_AsTuple(arglist);
	if (v == NULL) {
		Py_DECREF(arglist);
		ObjCErr_ToObjC();
		return;
	}
	Py_DECREF(arglist);
	arglist = v;

	res = ObjC_call_to_python(*(id*)args[0], *(SEL*)args[1], arglist);
	Py_DECREF(arglist);

	if (!have_output) {
		const char* err;

		err = depythonify_c_value([methinfo methodReturnType],
			res, resp);
		Py_DECREF(res);
		if (err) {
			ObjCErr_Set(PyExc_TypeError,
				"%s: Cannot encode return value: %s\n",
				SELNAME(*(SEL*)args[1]), err);
			ObjCErr_ToObjC();
		}
	} else {
		/* We have some output parameters, locate them and encode
		 * their values
		 */
		int idx;
		PyObject* real_res;
		
		if (!PyTuple_Check(res) || PyTuple_Size(res) != have_output+1) {
			ObjCErr_Set(PyExc_TypeError,
				"%s: Need tuple of %d arguments as result",
				SELNAME(*(SEL*)args[1]), have_output+1);
			ObjCErr_ToObjC();
		}

		real_res = PyTuple_GET_ITEM(res, 0);
		idx = 1;
		for (i = 2; i < objc_argcount; i++) {
			const char* argtype = [methinfo 
				getArgumentTypeAtIndex:i];
			const char* err;

			switch (*argtype) {
			case _C_PTR: 
				argtype ++;
				break;
			case _C_INOUT: case _C_OUT:
				if (argtype[1] != _C_PTR) {
					continue;
				}
				argtype += 2;
				break;
			default: continue;
			}

			v = PyTuple_GET_ITEM(res, idx++);
			err = depythonify_c_value(argtype, v, args[i]);
			Py_DECREF(res);
			if (err) {
				ObjCErr_Set(PyExc_TypeError,
					"%s: Cannot encode output argument "
					" %d: %s",
					SELNAME(*(SEL*)args[1]), i,
					err);
				ObjCErr_ToObjC();
			}
		}

	}
}

/* 
 * Return an IMP that is suitable for forwarding a method with the specified
 * signature from Objective-C to Python.
 *
 * TODO: Do not use NSMethodSignature
 */
IMP
ObjC_MakeIMPForSignature(char* signature)
{
	NSMethodSignature* methinfo;
	int               objc_argcount;
	ffi_cif           *cif;
	ffi_closure       *cl;
	ffi_type**        cl_arg_types;
	ffi_type*         cl_ret_type;
	ffi_status        rv;
	int               i;

	methinfo = [NSMethodSignature signatureWithObjCTypes:signature];

	/* Build FFI returntype description */
	cl_ret_type = signature_to_ffi_type([methinfo methodReturnType]);
	if (cl_ret_type == NULL) {
		[methinfo release];
		return NULL;
	}

	/* Build FFI argumentlist description */
	objc_argcount = [methinfo numberOfArguments];

	cl_arg_types = malloc(sizeof(ffi_type*) * objc_argcount);
	if (cl_arg_types == NULL) {
		free(cl_ret_type);
		PyErr_NoMemory();
		return NULL;
	}

	for (i = 0; i < objc_argcount; i++) {
		cl_arg_types[i] = signature_to_ffi_type(
				[methinfo getArgumentTypeAtIndex:i]);
		if (cl_arg_types[i] == NULL) {
			[methinfo release];
			free(cl_arg_types);
			return NULL;
		}
	}

	/* Create the invocation description */
	cif = malloc(sizeof(*cif));
	if (cif == NULL) {
		free(cl_arg_types);
		[methinfo release];
		PyErr_NoMemory();
		return NULL;
	}
	rv = ffi_prep_cif(cif, FFI_DEFAULT_ABI, objc_argcount, 
		cl_ret_type, cl_arg_types);
	if (rv != FFI_OK) {
		free(cl_arg_types);
		[methinfo release];
		ObjCErr_Set(PyExc_RuntimeError,
			"Cannot create FFI CIF: %d", rv);
		return NULL;
	}

	/* And finally create the actual closure */
	cl = malloc(sizeof(*cl));
	if (cl == NULL) {
		free(cl_arg_types);
		free(cif);
		[methinfo release];
		PyErr_NoMemory();
		return NULL;
	}
	rv = ffi_prep_closure(cl, cif, method_stub, methinfo);
	if (rv != FFI_OK) {
		[methinfo release];
		ObjCErr_Set(PyExc_RuntimeError,
			"Cannot create FFI closure: %d", rv);
		return NULL;
	}

	return (IMP)cl;
}


/* FIXME:
 *   This is a clone of execute_and_pythonify_objc_method in objc_support.m
 *   Need to either abstract away differences or remove one of these...
 *
 * Changes w.r.t. execute_and_...
 * - All arguments are stored in 'argbuf', not only the structs
 * - libffi support
 */
PyObject *
ObjC_FFICaller(PyObject *aMeth, PyObject* self, PyObject *args)
{
	size_t            argbuf_len = 0;
	size_t            argbuf_cur = 0;
	unsigned char*    argbuf = NULL;	/* by-reference arguments */
	size_t            byref_in_count = 0;
	size_t            byref_out_count = 0;
	size_t            plain_count = 0;
	size_t            objc_argcount;
	size_t            py_arg;
	int               i;
	int*		  byref = NULL; /* offset for arguments in argbuf */
	const char* 	  rettype;
	NSMethodSignature*  methinfo;
	ObjCNativeSelector* meth = (ObjCNativeSelector*)aMeth;
	PyObject*	  objc_result = NULL;
	PyObject*	  result = NULL;
	id		  self_obj = nil;
	struct objc_super super;
	struct objc_super* superPtr;
	ffi_cif		  cif;
	ffi_type*	  arglist[64]; /* XX: Magic constant */
	void*             values[64];
	int               r;
	void*		  msgResult;
	int               resultSize;
	int               arglistOffset;

	if (meth->sel_oc_signature) {
		methinfo = meth->sel_oc_signature;
	} else {
		methinfo = [NSMethodSignature signatureWithObjCTypes:meth->sel_signature];
		meth->sel_oc_signature = methinfo;
	}
	objc_argcount = [methinfo numberOfArguments];
	resultSize = objc_sizeof_type([methinfo methodReturnType]);

	/* First count the number of by reference parameters, and the number
	 * of bytes of storage needed for them. Note that arguments 0 and 1
	 * are self and the selector, no need to count counted or checked those.
	 */
	for (i = 2; i < objc_argcount; i++) {
		const char *argtype = [methinfo getArgumentTypeAtIndex:i];

		switch (*argtype) {
		case _C_PTR: 
			byref_in_count ++;
			byref_out_count ++;
			argbuf_len += objc_sizeof_type(argtype+1);
			break;

		case _C_INOUT:
			if (argtype[1] == _C_PTR) {
				byref_out_count ++;
				byref_in_count ++;
				argbuf_len += objc_sizeof_type(argtype+2);
			} else {
				argbuf_len += objc_sizeof_type(argtype+1);
			}
			break;

		case _C_IN: case _C_CONST:
			if (argtype[1] == _C_PTR) {
				byref_in_count ++;
				argbuf_len += objc_sizeof_type(argtype+2);
			} else {
				argbuf_len += objc_sizeof_type(argtype+1);
			}
			break;

		case _C_OUT:
			if (argtype[1] == _C_PTR) {
				byref_out_count ++;
				argbuf_len += objc_sizeof_type(argtype+2);
			} else {
				argbuf_len += objc_sizeof_type(argtype+1);
			}
			break;

		case _C_STRUCT_B: case _C_UNION_B: case _C_ARY_B:
			plain_count++;
			argbuf_len += objc_sizeof_type(argtype);
			break;

		default:
			argbuf_len += objc_sizeof_type(argtype);
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

	argbuf_len += resultSize;

	argbuf = PyMem_Malloc(argbuf_len);
	if (argbuf == 0) {
		PyErr_NoMemory();
		goto error_cleanup;
	}
	byref = PyMem_Malloc(sizeof(int) * objc_argcount);
	if (byref == NULL) {
		PyErr_NoMemory();
		goto error_cleanup;
	}
	memset(byref, 0, sizeof(int) * objc_argcount);

	/* Set 'self' argument, for class methods we use the class */ 
	if (meth->sel_flags & ObjCSelector_kCLASS_METHOD) {
		if (ObjCObject_Check(self)) {
			self_obj = ObjCObject_GetObject(self);
			if (self_obj != NULL) {
				self_obj = GETISA(self_obj);
			}
		} else if (ObjCClass_Check(self)) {
			self_obj = ObjCClass_GetClass(self);
		} else {
			PyErr_SetString(PyExc_TypeError, 
				"Need objective-C object or class as self");
			goto error_cleanup;
		}
	} else {
		const char* err;
		if (ObjCObject_Check(self)) {
			self_obj = ObjCObject_GetObject(self);
		} else {
			err = depythonify_c_value("@", self, &self_obj);
			if (err) {
				PyErr_SetString(PyExc_TypeError, 
					"Need objective-C object as self");
				goto error_cleanup;
			}
		}
	}

	super.receiver = self_obj;
	if (meth->sel_flags & ObjCSelector_kCLASS_METHOD) {
		super.class = GETISA(meth->sel_class);
	} else {
		super.class = meth->sel_class;
	}

	if (sizeof(id) >= resultSize) {
		arglistOffset = 0;
	} else {
		arglistOffset = 1;
		arglist[0] = &ffi_type_pointer;
		values[0] = argbuf;
	}
	
	superPtr = &super;
	arglist[arglistOffset + 0] = &ffi_type_pointer;
	values[arglistOffset + 0] = &superPtr;
	arglist[arglistOffset + 1] = &ffi_type_pointer;
	values[arglistOffset + 1] = &meth->sel_selector;
	msgResult = argbuf;
	argbuf_cur = resultSize;

	py_arg = 0;
	for (i = 2; i < objc_argcount; i++) {
		const char* error;
		PyObject *argument;
		const char *argtype = [methinfo getArgumentTypeAtIndex:i];

		if (argtype[0] == _C_OUT && argtype[1] == _C_PTR) {
			/* Just allocate room in argbuf and set that*/
			void* arg;
			byref[i] = argbuf_cur;
			arg = argbuf + argbuf_cur;

			arglist[arglistOffset + i] = &ffi_type_pointer;
			values[arglistOffset + i] = arg;

			argbuf_cur += objc_sizeof_type(argtype+2);
		} else {
			/* Encode argument, maybe after allocating space */

			if (argtype[0] == _C_OUT) argtype ++;

			argument = PyTuple_GET_ITEM (args, py_arg);
			switch (*argtype) {
			case _C_STRUCT_B: case _C_ARY_B: case _C_UNION_B:
				/* Allocate space and encode */
				{
					void* arg = argbuf + argbuf_cur;
					argbuf_cur += objc_sizeof_type(argtype);
					byref[i] = argbuf_cur;
	  				error = depythonify_c_value (
						argtype, 
						argument, 
						arg);


					arglist[arglistOffset + i] = signature_to_ffi_type(
					 	argtype);
					values[arglistOffset + i] = arg;
				} 
				break;

			case _C_PTR:
				/* Allocate space and encode */
				{
					void* arg = argbuf + argbuf_cur;
					argbuf_cur += objc_sizeof_type(argtype+1);
					byref[i] = argbuf_cur;
	  				error = depythonify_c_value (
						argtype+1, 
						argument, 
						arg);

					arglist[arglistOffset + i] = &ffi_type_pointer;
					values[arglistOffset + i] = arg;
				} 
				break;

			case _C_INOUT:
			case _C_IN:
			case _C_CONST:

				if (argbuf[1] == _C_PTR) {
					/* Allocate space and encode */
					void* arg = argbuf + argbuf_cur;
					argbuf_cur += objc_sizeof_type(argtype+2);
					byref[i] = argbuf_cur;
	  				error = depythonify_c_value (
						argtype+2, 
						argument, 
						arg);

					arglist[arglistOffset + i] = &ffi_type_pointer;
					values[arglistOffset + i] = arg;

				} else {
					/* just encode */
					void* arg = argbuf + argbuf_cur;
					argbuf_cur += objc_sizeof_type(argtype+1);
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
				void* arg = argbuf + argbuf_cur;
				argbuf_cur += objc_sizeof_type(argtype);

	  			error = depythonify_c_value (
					argtype, 
					argument, 
					arg);

				arglist[arglistOffset + i] = signature_to_ffi_type(argtype);
				values[arglistOffset + i] = arg;
				}
			}

			if (error) {
				const char* typeend = objc_skip_typespec(argtype);
				ObjCErr_Set(PyExc_TypeError,
					"expected %s for argument %d: its "
					"typespec is '%.*s'",
					error, py_arg+1, typeend-argtype, argtype);
				goto error_cleanup;
			}
			py_arg++;
		}
	}

	PyErr_Clear();
	if (arglistOffset) {
		r = ffi_prep_cif(&cif, FFI_DEFAULT_ABI, objc_argcount,
			&ffi_type_void, arglist);
	} else {
		r = ffi_prep_cif(&cif, FFI_DEFAULT_ABI, objc_argcount,
			&ffi_type_pointer, arglist);
	}
	if (r != FFI_OK) {
		ObjCErr_Set(PyExc_RuntimeError,
			"Cannot setup FFI CIF [%d]", r);
		goto error_cleanup;
	}

	/* XXX This only works for short return values! */
	NS_DURING
		if (arglistOffset) {
			ffi_call(&cif, FFI_FN(objc_msgSendSuper), NULL, values);
		} else {
			ffi_call(&cif, FFI_FN(objc_msgSendSuper), msgResult, values);
		}
	NS_HANDLER
		ObjCErr_FromObjC(localException);
	NS_ENDHANDLER
	if (PyErr_Occurred()) goto error_cleanup;

	rettype = [methinfo methodReturnType];
	if ( (*rettype != _C_VOID) && ([methinfo isOneway] == NO) )
	{
		objc_result = pythonify_c_value (
			[methinfo methodReturnType], msgResult);
	} else {
		Py_INCREF(Py_None);
		objc_result =  Py_None;
	}
	if ( (meth->sel_flags & ObjCSelector_kRETURNS_SELF)
		&& (objc_result != self)) {

		/* meth is a method that returns a possibly reallocated
		 * version of self and self != return-value, the current
		 * value of self is assumed to be no longer valid
		 */
		ObjCObject_ClearObject(self);
	}

	if (byref_out_count == 0) {
		result = objc_result;
	} else {
		result = PyTuple_New(byref_out_count+1);
		if (result == 0) goto error_cleanup;

		if (PyTuple_SetItem(result, 0, objc_result) < 0) {
			goto error_cleanup;
		}
		objc_result = NULL;

		py_arg = 1;
		for (i = 2; i < objc_argcount; i++) {
			const char *argtype = [methinfo 
						getArgumentTypeAtIndex:i];
			void*       arg;
			PyObject*   v;

			switch (*argtype) {
			case _C_PTR: 
				arg = argbuf + byref[i];
				v = pythonify_c_value(argtype+1, arg);
				if (!v) goto error_cleanup;
				if (PyTuple_SetItem(result, py_arg++, v) < 0) {
					Py_DECREF(v);
					goto error_cleanup;
				}
				break;

			case _C_INOUT:
			case _C_OUT:
				if (argtype[1] == _C_PTR) {
					arg = argbuf + byref[i];
					v = pythonify_c_value(argtype+2, arg);
					if (!v) goto error_cleanup;
					if (PyTuple_SetItem(result, 
							py_arg++, v) < 0) {
						Py_DECREF(v);
						goto error_cleanup;
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
	[methinfo release];
	methinfo = nil;
	
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
	if (methinfo) {
		[methinfo release];
		methinfo = nil;
	}
	return NULL;
}



#endif /* OC_WITH_LIBFFI */
