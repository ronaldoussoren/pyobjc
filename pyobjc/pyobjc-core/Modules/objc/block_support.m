/*
 * This file implements support for the "Blocks" feature of Objective-C
 *
 * Most of the code in this file implements a single manually coded block that
 * is manipulated at runtime, basicly simularly to how method descriptors are
 * manipulated by pyobjc.
 *
 * WARNING: The blocks implementation is technically private, the interfaces we
 * use here are extracted from the Blocks implementation documentation from clang.
 */
#import "pyobjc.h"

/*
 * Definitions for block functions. These definitions are technically
 * private, but are the only way to interact with the block machinary.
 *
 * Definitions are copied from the clang documentation on blocks.
 */

#if 0
  /* Full definition, contains bits we don't need at this point in time */

#if MAC_OS_X_VERSION_MIN_REQUIRED < 1060
#define BLOCK_FUNC_ATTRIBUTE __attribute__((__weak_import__))
#else
#define BLOCK_FUNC_ATTRIBUTE 
#endif

enum {    
    BLOCK_FIELD_IS_OBJECT   =  3,  // id, NSObject, __attribute__((NSObject)), block, ...
    BLOCK_FIELD_IS_BLOCK    =  7,  // a block variable
    BLOCK_FIELD_IS_BYREF    =  8,  // the on stack structure holding the __block variable
    BLOCK_FIELD_IS_WEAK     = 16,  // declared __weak
    BLOCK_BYREF_CALLER      = 128, // called from byref copy/dispose helpers
};

enum {
    BLOCK_HAS_COPY_DISPOSE =  (1 << 25),
    BLOCK_HAS_CTOR =          (1 << 26), // helpers have C++ code
    BLOCK_IS_GLOBAL =         (1 << 28),
    BLOCK_HAS_DESCRIPTOR =    (1 << 29), // interim until complete world build is accomplished
};


void _Block_object_assign(void *destAddr, const void *object, const int flags) BLOCK_FUNC_ATTRIBUTE;
void _Block_object_dispose(const void *object, const int flags) BLOCK_FUNC_ATTRIBUTE;

#else
	/* minimal definition, only contains the definitions we actually use */

enum {
	BLOCK_HAS_COPY_DISPOSE =  (1 << 25)
};

#endif

/*
 * End of definitions.
 */

static Class gStackBlockClass = nil;

struct block_descriptor {
	unsigned long int reserved;
	unsigned long int size;
	void (*copy_helper)(void* dst, void*src);
	void (*dispose_helper)(void* src);
};

struct block_literal {
	void* isa;
	int   flags;
	int   reserved;
	void (*invoke)(void*, ...);
	struct block_descriptor* descriptor;
	PyObject* invoke_cleanup;
};

/* 
 * FIXME: keep track of the refcount on the invoke function
 * as well, deconstruct it when it is no longer needed.
 */
static void 
oc_copy_helper(void* _dst, void* _src)
{
	struct block_literal* dst = (struct block_literal*)_dst;
	struct block_literal* src = (struct block_literal*)_src;

	PyGILState_STATE   state = PyGILState_Ensure();
	{
		dst->invoke_cleanup = src->invoke_cleanup;
		Py_XINCREF(dst->invoke_cleanup);
		
	}
	if (!PyErr_Occurred())  {
		PyGILState_Release(state);
	} else {
		PyObjCErr_ToObjCWithGILState(&state);
	}

}

static void
oc_dispose_helper(void* _src)
{
	struct block_literal* src = (struct block_literal*)_src;

	PyGILState_STATE   state = PyGILState_Ensure();
	{
		Py_CLEAR(src->invoke_cleanup);
	}
	if (!PyErr_Occurred())  {
		PyGILState_Release(state);
	} else {
		PyObjCErr_ToObjCWithGILState(&state);
	}
}

static struct block_descriptor gDescriptorTemplate = {
	0,
	sizeof(struct block_literal),
	oc_copy_helper,
	oc_dispose_helper
};

static struct block_literal gLiteralTemplate = {
	0, 	/* ISA */
	BLOCK_HAS_COPY_DISPOSE,
	0,
	0,
	&gDescriptorTemplate,
	0
};	

static inline Py_ssize_t align(Py_ssize_t offset, Py_ssize_t alignment)
{
	Py_ssize_t rest = offset % alignment;
	if (rest == 0) return offset;
	return offset + (alignment - rest);
}


PyObject* 
PyObjCBlock_Call(PyObject* module __attribute__((__unused__)), PyObject* func_args)
{
	PyObject*  self;
	PyObjCMethodSignature*  signature;
	PyObject*  args;
	PyObject*  kwds;
	NSObject*  block_ptr;
	_block_func_ptr call_func;
	Py_ssize_t	byref_in_count;
	Py_ssize_t	byref_out_count;
	Py_ssize_t	plain_count;
	Py_ssize_t	argbuf_len;
	int		cif_arg_count;
	BOOL		variadicAllArgs = NO;
	int 		r;
	unsigned char*	argbuf = NULL;
	ffi_type*	arglist[64];
	void*		values[64];
	void** 		byref = NULL;
	struct byref_attr* byref_attr = NULL;
	ffi_cif		cif;
	PyObject* retval;

	if (!PyArg_ParseTuple(func_args, "OOOO", &self, &signature, &args, &kwds)) {
		return NULL;
	}
	if (!PyObjCObject_Check(self) || !PyObjCObject_IsBlock(self)) {
		PyErr_SetString(PyExc_TypeError, "object is not a block");
		return NULL;
	}
	if ((PyObject*)signature == Py_None) {
		PyErr_SetString(PyExc_TypeError, "cannot call block without a signature");
		return NULL;
	}
	if (!PyObjCMethodSignature_Check(signature)) {
		PyErr_SetString(PyExc_TypeError, "signature is not a signature object");
		return NULL;
	}
	if (kwds != NULL && (!PyDict_Check(kwds) || PyDict_Size(kwds) != 0)) {
		PyErr_SetString(PyExc_TypeError, "keyword arguments not supported");
		return NULL;
	}


	block_ptr = PyObjCObject_GetObject(self);
	call_func = PyObjCBlock_GetFunction(block_ptr);

	argbuf_len = PyObjCRT_SizeOfReturnType(signature->rettype.type);
	argbuf_len = align(argbuf_len, sizeof(void*));

	argbuf_len += sizeof(void*); /* Argument 0: the block itself */
	r = PyObjCFFI_CountArguments(
		signature, 1,
		&byref_in_count, &byref_out_count, &plain_count,
		&argbuf_len, &variadicAllArgs);
	if (r == -1) {
		return NULL;
	}

	variadicAllArgs |= signature->variadic && (signature->null_terminated_array || signature->arrayArg != -1);

	if (variadicAllArgs) {
		if (byref_in_count != 0 || byref_out_count != 0) {
			PyErr_Format(PyExc_TypeError, "Sorry, printf format with by-ref args not supported");
			return NULL;
		}
		if (PyTuple_Size(args) < signature->ob_size - 1) {
			PyErr_Format(PyExc_TypeError, "Need %"PY_FORMAT_SIZE_T"d arguments, got %"PY_FORMAT_SIZE_T"d",
			signature->ob_size - 2, PyTuple_Size(args));
			return NULL;
		}
	} else if (PyTuple_Size(args) != signature->ob_size - 1) {
		PyErr_Format(PyExc_TypeError, "Need %"PY_FORMAT_SIZE_T"d arguments, got %"PY_FORMAT_SIZE_T"d",
		signature->ob_size, PyTuple_Size(args));
		return NULL;
	}

	argbuf = PyMem_Malloc(argbuf_len);
	if (argbuf == NULL) {
		PyErr_NoMemory();
		return NULL;
	}
	if (variadicAllArgs) {
		if (PyObjCFFI_AllocByRef(signature->ob_size + PyTuple_Size(args), &byref, &byref_attr) < 0) {
			goto error;
		}
	} else {
		if (PyObjCFFI_AllocByRef(signature->ob_size, &byref, &byref_attr) < 0) {
			goto error;
		}
	}
	cif_arg_count = PyObjCFFI_ParseArguments(
		signature, 1, args, 
		align(PyObjCRT_SizeOfReturnType(signature->rettype.type), sizeof(void*))+sizeof(void*),
		argbuf, argbuf_len, byref, byref_attr, arglist, values);
	if (cif_arg_count == -1) {
		goto error;
	}
	arglist[0] = &ffi_type_pointer;
	values[0] = &block_ptr;

	r = ffi_prep_cif(&cif, FFI_DEFAULT_ABI, cif_arg_count, 
			signature_to_ffi_return_type(signature->rettype.type), arglist);
	if (r != FFI_OK) {
		PyErr_Format(PyExc_RuntimeError, "Cannot setup FFI CIF [%d]", r);
		goto error;
	}
	
	PyObjC_DURING
		ffi_call(&cif, FFI_FN(call_func), argbuf, values);

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		goto error;
	}

	retval = PyObjCFFI_BuildResult(signature, 1, argbuf, byref, 
			byref_attr, byref_out_count, NULL, 0, values);

	if (variadicAllArgs) {
		if (PyObjCFFI_FreeByRef(signature->ob_size+PyTuple_Size(args), byref, byref_attr) < 0) {
			byref = NULL; byref_attr = NULL;
			goto error;
		}
	} else {
		if (PyObjCFFI_FreeByRef(signature->ob_size, byref, byref_attr) < 0) {
			byref = NULL; byref_attr = NULL;
			goto error;
		}
	}
	PyMem_Free(argbuf); argbuf = NULL;
	return retval;

error:
	if (variadicAllArgs) {
		PyObjCFFI_FreeByRef(signature->ob_size+PyTuple_Size(args), byref, byref_attr);
	} else {
		PyObjCFFI_FreeByRef(signature->ob_size, byref, byref_attr);
	}
	if (argbuf) {
		PyMem_Free(argbuf);
	}
	return NULL;
}


void*
PyObjCBlock_Create(PyObjCMethodSignature* signature, PyObject* callable)
{
	if (gStackBlockClass == NULL) {
		PyErr_SetString(PyObjCExc_Error, "Blocks not supported on this platform");
		return NULL;
	}
	struct block_literal* block = PyMem_Malloc(sizeof(struct block_literal));
	if (block == NULL) {
		PyErr_NoMemory();
		return NULL;
	}

	*block = gLiteralTemplate;
	block->isa = gStackBlockClass;
	block->invoke = PyObjCFFI_MakeBlockFunction(signature, callable);
	if (block->invoke == NULL) {
		PyMem_Free(block);
		return NULL;
	}
	block->invoke_cleanup = PyCObject_FromVoidPtr(block->invoke, (void(*)(void*))PyObjCFFI_FreeBlockFunction);
	if (block->invoke_cleanup == NULL) {
		PyObjCFFI_FreeBlockFunction(block->invoke);
		PyMem_Free(block);
		return NULL;
	}
	return (void*)block;	
}

void
PyObjCBlock_Release(void* _block)
{
	struct block_literal* block = (struct block_literal*)_block;
	Py_CLEAR(block->invoke_cleanup);
	PyMem_Free(block);
}


int
PyObjCBlock_Setup(void)
{
	gStackBlockClass = objc_lookUpClass("__NSGlobalBlock__");

	return 0;
}

_block_func_ptr
PyObjCBlock_GetFunction(void* block)
{
	return ((struct block_literal*)block)->invoke;
}
