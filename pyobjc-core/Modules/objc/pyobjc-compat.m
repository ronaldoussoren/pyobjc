#include "pyobjc.h"

#if PY_MAJOR_VERSION == 2

PyObject* 
PyObjCString_InternFromStringAndSize(const char* v, Py_ssize_t l)
{
	PyObject* result;

	result = PyString_FromStringAndSize(v, l);
	if (result == NULL) {
		return NULL;
	}
	PyString_InternInPlace(&result);
	return result;
}



#ifndef PY_FORMAT_LONG_LONG 
#define   PY_FORMAT_LONG_LONG "ll"
#endif

/* 
 * This function is PyString_FromFormat from Python 2.7 + support for
 * '%R' and '%S'.
 */
static PyObject* 
PyObjCString_FromFormatV(const char* format, va_list vargs)
{
	va_list count;
	Py_ssize_t n = 0;
	const char* f;
	char *s;
	PyObject* string;
        Py_ssize_t callcount = 0;
	PyObject **callresults = NULL;
        PyObject **callresult = NULL;

#ifdef VA_LIST_IS_ARRAY
	Py_MEMCPY(count, vargs, sizeof(va_list));
#else
#ifdef  __va_copy
	__va_copy(count, vargs);
#else
	count = vargs;
#endif
#endif
	 /* step 0: count the number of %S/%R format specifications
	  * (we call PyObject_Str()/PyObject_Repr() for these
	  * objects once during step 1 and put the result in an array) 
	  */
	for (f = format; *f; f++) {
		if (*f == '%') {
			if (*(f+1)=='%')
				continue;
			if (*(f+1)=='S' || *(f+1)=='R')
				++callcount;
		 }
	}
	if (callcount) {
		callresults = PyObject_Malloc(sizeof(PyObject *)*callcount);
		if (!callresults) {
			PyErr_NoMemory();
			return NULL;
		}
		callresult = callresults;
	}

	/* step 1: figure out how large a buffer we need */
	for (f = format; *f; f++) {
		if (*f == '%') {
#ifdef HAVE_LONG_LONG
			int longlongflag = 0;
#endif
			const char* p = f;
			while (*++f && *f != '%' && !isalpha(Py_CHARMASK(*f)))
				;

			/* skip the 'l' or 'z' in {%ld, %zd, %lu, %zu} since
			 * they don't affect the amount of space we reserve.
			 */
			if (*f == 'l') {
				if (f[1] == 'd' || f[1] == 'u') {
					++f;
				}
#ifdef HAVE_LONG_LONG
				else if (f[1] == 'l' &&
					 (f[2] == 'd' || f[2] == 'u')) {
					longlongflag = 1;
					f += 2;
				}
#endif
			}
			else if (*f == 'z' && (f[1] == 'd' || f[1] == 'u')) {
				++f;
			}

			switch (*f) {
			case 'c':
				(void)va_arg(count, int);
				/* fall through... */
			case '%':
				n++;
				break;
			case 'd': case 'u': case 'i': case 'x':
				(void) va_arg(count, int);
#ifdef HAVE_LONG_LONG
				/* Need at most
				   ceil(log10(256)*SIZEOF_LONG_LONG) digits,
				   plus 1 for the sign.  53/22 is an upper
				   bound for log10(256). */
				if (longlongflag)
					n += 2 + (SIZEOF_LONG_LONG*53-1) / 22;
				else
#endif
					/* 20 bytes is enough to hold a 64-bit
					   integer.  Decimal takes the most
					   space.  This isn't enough for
					   octal. */
					n += 20;

				break;
			case 's':
				s = va_arg(count, char*);
				n += strlen(s);
				break;
			case 'p':
				(void) va_arg(count, int);
				/* maximum 64-bit pointer representation:
				 * 0xffffffffffffffff
				 * so 19 characters is enough.
				 * XXX I count 18 -- what's the extra for?
				 */
				n += 19;
				break;

			case 'R':
			{
				PyObject *obj = va_arg(count, PyObject *);
				PyObject *str;
				assert(obj);
				str = PyObject_Repr(obj);
				if (!str)
				    goto fail;
				if (!PyString_Check(str)) {
					PyErr_SetString(PyExc_TypeError,
						"repr() returned non-string");
					goto fail;
				}
				n += PyString_GET_SIZE(str);
				/* Remember the str and switch to the next slot */
				*callresult++ = str;
			}
			break;

			case 'S':
			{
				PyObject *obj = va_arg(count, PyObject *);
				PyObject *str;
				assert(obj);
				str = PyObject_Str(obj);
				if (!str)
				    goto fail;
				if (!PyString_Check(str)) {
					PyErr_SetString(PyExc_TypeError,
						"str() returned non-string");
					goto fail;
				}
				n += PyString_GET_SIZE(str);
				/* Remember the str and switch to the next slot */
				*callresult++ = str;
			}
			break;

			default:
				/* if we stumble upon an unknown
				   formatting code, copy the rest of
				   the format string to the output
				   string. (we cannot just skip the
				   code, since there's no way to know
				   what's in the argument list) */
				n += strlen(p);
				goto expand;
			}
		} else
			n++;
	}
 expand:
	/* step 2: fill the buffer */
	/* Since we've analyzed how much space we need for the worst case,
	   use sprintf directly instead of the slower PyOS_snprintf. */
	string = PyString_FromStringAndSize(NULL, n);
	if (!string)
		return NULL;

	s = PyString_AsString(string);

	callresult = callresults;
	for (f = format; *f; f++) {
		if (*f == '%') {
			const char* p = f++;
			Py_ssize_t i;
			int longflag = 0;
#ifdef HAVE_LONG_LONG
			int longlongflag = 0;
#endif
			int size_tflag = 0;
			/* parse the width.precision part (we're only
			   interested in the precision value, if any) */
			n = 0;
			while (isdigit(Py_CHARMASK(*f)))
				n = (n*10) + *f++ - '0';
			if (*f == '.') {
				f++;
				n = 0;
				while (isdigit(Py_CHARMASK(*f)))
					n = (n*10) + *f++ - '0';
			}
			while (*f && *f != '%' && !isalpha(Py_CHARMASK(*f)))
				f++;
			/* Handle %ld, %lu, %lld and %llu. */
			if (*f == 'l') {
				if (f[1] == 'd' || f[1] == 'u') {
					longflag = 1;
					++f;
				}
#ifdef HAVE_LONG_LONG
				else if (f[1] == 'l' &&
					 (f[2] == 'd' || f[2] == 'u')) {
					longlongflag = 1;
					f += 2;
				}
#endif
			}
			/* handle the size_t flag. */
			else if (*f == 'z' && (f[1] == 'd' || f[1] == 'u')) {
				size_tflag = 1;
				++f;
			}

			switch (*f) {
			case 'c':
				*s++ = va_arg(vargs, int);
				break;
			case 'd':
				if (longflag)
					sprintf(s, "%ld", va_arg(vargs, long));
#ifdef HAVE_LONG_LONG
				else if (longlongflag)
					sprintf(s, "%" PY_FORMAT_LONG_LONG "d",
						va_arg(vargs, PY_LONG_LONG));
#endif
				else if (size_tflag)
					sprintf(s, "%" PY_FORMAT_SIZE_T "d",
					        va_arg(vargs, Py_ssize_t));
				else
					sprintf(s, "%d", va_arg(vargs, int));
				s += strlen(s);
				break;
			case 'u':
				if (longflag)
					sprintf(s, "%lu",
						va_arg(vargs, unsigned long));
#ifdef HAVE_LONG_LONG
				else if (longlongflag)
					sprintf(s, "%" PY_FORMAT_LONG_LONG "u",
						va_arg(vargs, PY_LONG_LONG));
#endif
				else if (size_tflag)
					sprintf(s, "%" PY_FORMAT_SIZE_T "u",
					        va_arg(vargs, size_t));
				else
					sprintf(s, "%u",
						va_arg(vargs, unsigned int));
				s += strlen(s);
				break;
			case 'i':
				sprintf(s, "%i", va_arg(vargs, int));
				s += strlen(s);
				break;
			case 'x':
				sprintf(s, "%x", va_arg(vargs, int));
				s += strlen(s);
				break;
			case 's':
				p = va_arg(vargs, char*);
				i = strlen(p);
				if (n > 0 && i > n)
					i = n;
				Py_MEMCPY(s, p, i);
				s += i;
				break;
			case 'p':
				sprintf(s, "%p", va_arg(vargs, void*));
				/* %p is ill-defined:  ensure leading 0x. */
				if (s[1] == 'X')
					s[1] = 'x';
				else if (s[1] != 'x') {
					memmove(s+2, s, strlen(s)+1);
					s[0] = '0';
					s[1] = 'x';
				}
				s += strlen(s);
				break;

			case 'R':
			case 'S':
			   {
				/* unused, since we already have the result */
				(void) va_arg(vargs, PyObject *);

				/* FIXME: The clang analyzer thinks that 'callresult' might be 
				 * NULL here. That's wrong, this is the second loop through 
				 * the format string and on the previous loop callresults got
				 * created and filled.
				 */

				if (callresult != NULL) {
					memcpy(s, PyString_AS_STRING(*callresult),
					  PyString_GET_SIZE(*callresult));
					s += PyString_GET_SIZE(*callresult);
					Py_DECREF(*callresult); *callresult = NULL;
				}
				callresult++;
				break;
			    }

			case '%':
				*s++ = '%';
				break;
			default:
				strcpy(s, p);
				s += strlen(s);
				goto end;
			}
		} else
			*s++ = *f;
	}

 end:
	if (callresults) {
		PyObject_Free(callresults);
        }
	_PyString_Resize(&string, s - PyString_AS_STRING(string));
	return string;

 fail:
	if (callresults) {
		PyObject **callresult2 = callresults;
		while (callresult2 < callresult) {
		    Py_DECREF(*callresult2);
		    ++callresult2;
		}
		PyObject_Free(callresults);
        }
	return NULL;
}

PyObject* PyObjCErr_Format(PyObject* exception, const char* format, ...)
{
	/* This is an enhanced version of PyErr_Format for python 2.x that
	 * accept much of the format characters that are supported in python 3
	 */
	PyObject* strval;
	va_list args;
	va_start(args, format);
	strval = PyObjCString_FromFormatV(format, args);
	va_end(args);
	if (strval) {
		PyErr_SetObject(exception, strval);
		Py_DECREF(strval);
	}
	return NULL;
}

#else /* Py3k */

int PyObject_Cmp (PyObject *o1, PyObject *o2, int *result)
{
	int r;
	
	r = PyObject_RichCompareBool(o1, o2, Py_EQ);
	if (r == -1) {
		return -1;
	} else if (r == 1) {
		*result = 0;
		return 0;
	}

	r = PyObject_RichCompareBool(o1, o2, Py_LT);
	if (r == -1) {
		return -1;
	} else if (r == 1) {
		*result = -1;
		return 0;
	} 

	r = PyObject_RichCompareBool(o1, o2, Py_GT);
	if (r == -1) {
		return 1;
	} else if (r == 1) {
		*result = 1;
		return 0;
	} 

	PyErr_Format(PyExc_TypeError, "%R and %R cannot be compared",
			o1, o2);
	return -1;
}

static PyObject* registry = NULL;

PyObject* PyBytes_InternFromString(const char* v)
{
	PyObject* key;
	PyObject* value;

	if (registry == NULL) {
		registry = PyDict_New();
		if (registry == NULL) {
			return NULL;
		}
	}

	key = PyBytes_FromString(v);
	if (key == NULL) {
		return NULL;
	}
	value = PyDict_GetItem(registry, key);
	if (value == NULL) {
		int r = PyDict_SetItem(registry, key, key);
		if (r == -1) {
			Py_DECREF(key);
			return NULL;
		} else {
			return key;
		}
	} else {
		Py_DECREF(key);
		Py_INCREF(value);
		return value;
	}
}

PyObject* PyBytes_InternFromStringAndSize(const char* v, Py_ssize_t l)
{
	PyObject* key;
	PyObject* value;

	if (registry == NULL) {
		registry = PyDict_New();
		if (registry == NULL) {
			return NULL;
		}
	}

	key = PyBytes_FromStringAndSize(v, l);
	if (key == NULL) {
		return NULL;
	}
	value = PyDict_GetItem(registry, key);
	if (value == NULL) {
		int r = PyDict_SetItem(registry, key, key);
		if (r == -1) {
			Py_DECREF(key);
			return NULL;
		} else {
			return key;
		}
	} else {
		Py_DECREF(key);
		Py_INCREF(value);
		return value;
	}
}


#endif /* Py3K */

/* 
 * Helper function for making sure that we don't store duplicate data
 * for the metadata bridges.
 *
 * Interface: call on value, don't update value afterwards. Steals
 * reference to argument and returns a new reference.
 */
static	PyObject* intern_mapping = NULL;

void	  PyObjC_ClearIntern(void)
{
	Py_CLEAR(intern_mapping);
}

PyObject* PyObjC_InternValue(PyObject* orig)
{
	return orig;
}

PyObject* PyObjC_IntFromString(char* v, char**pend, int base)
{
	PyObject* r = PyInt_FromString(v, pend, base);
	if (r == NULL) {
		return NULL;
	}
	return PyObjC_InternValue(r);
}


PyObject* PyObjC_IntFromLong(long v)
{
	PyObject* r = PyInt_FromLong(v);
	if (r == NULL) {
		return NULL;
	}
	return PyObjC_InternValue(r);
}
