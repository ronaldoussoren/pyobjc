#include "pyobjc.h"

PyObjCMethodSignature* PyObjCMethodSignature_FromSignature(
		const char* signature)
{
	int nargs;
	const char* cur;
	PyObjCMethodSignature* retval;


	/* Skip return-type */
	cur = PyObjCRT_SkipTypeSpec(signature);

	nargs = 0;
	for ( ; cur && *cur; cur = PyObjCRT_SkipTypeSpec(cur)) {
		nargs++;
	}

	retval = PyMem_Malloc(sizeof(PyObjCMethodSignature) + sizeof(char*)*nargs);
	if (retval == NULL) {
		PyErr_NoMemory();
		return NULL;
	}

	retval->nargs = nargs;
	retval->retainCount = 1;
	retval->signature = PyObjCUtil_Strdup(signature);
	if (retval->signature == NULL) {
		PyMem_Free(retval);
		return NULL;
	}

	retval->rettype = retval->signature;
	
	cur = PyObjCRT_SkipTypeSpec(retval->signature);
	nargs = 0;
	for (;cur && *cur; cur = PyObjCRT_SkipTypeSpec(cur)) {
		retval->argtype[nargs++] = cur;
	}
	return retval;
}

void PyObjCMethodSignature_Free(PyObjCMethodSignature* value)
{
	if (--value->retainCount != 0) return;

	PyMem_Free((char*)(value->signature));
	PyMem_Free(value);
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
	if (r > buflen) return NULL;

	end = (char*)PyObjCRT_SkipTypeSpec(buf);
	*end = '\0';
	buflen -= (end - buf);
	buf = end;

	for (i = 0; i < arg_count; i++) {
		r = snprintf(buf, buflen, "%s", [sig getArgumentTypeAtIndex:i]);
		if (r > buflen) return NULL;

		end = (char*)PyObjCRT_SkipTypeSpec(buf);
		buflen -= (end - buf);
		buf = end;
	}

	return result;
}
