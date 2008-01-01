/*
 * A fast parser for BridgeSupport files.
 *
 * This file is an optimized processor for the bridgesupport files containing
 * metadata about constants, functions, methods, ....
 *
 * TODO: check if we can gain further speed by moving the metadata to C
 * structs instead of Python dictionaries (less object pressure->more speed?)
 */
#include "pyobjc.h"
#include <dlfcn.h>


/* Use the libxml2 parser */

/* XXX: these are needed to avoid problems when using the system version
 * of libxml:
 */
#include <libxml/xmlversion.h>
#undef LIBXML_ICU_ENABLED
#define ID _id

#include <libxml/tree.h>
#include <libxml/parser.h>

#undef ID

static PyObject* empty = NULL;
static PyObject* default_suggestion = NULL;
static PyObject* setupCFClasses = NULL;
static PyObject* structConvenience = NULL;


/* Boolean attributes for argument/retval descriptors */
static const char* gBooleanAttributes[] = {
	"already_retained",
	"already_cfretained",
	"c_array_length_in_result",
	"c_array_delimited_by_null",
	"null_accepted', ",
	"c_array_of_variable_length",
	"unicode_string",
	"printf_format",
	NULL
};

/* Support for inlineTab lists */
typedef void(*function_pointer)(void);
struct functionlist {
	char*    name;
	function_pointer func;
};

static function_pointer find_function(struct functionlist* functions, char* name)
{
	if (functions == NULL) return NULL;
	while (functions->name != NULL) {
		if (strcmp(functions->name, name) == 0) {
			return functions->func;
		}
		functions++;
		}
	return NULL;
}

int
PyObjCXML_Init(void)
{
	/* This kinda sucks: libxml will abort when
	 * it decides it's version doesn't match our
	 * version.
	 */
	LIBXML_TEST_VERSION

	empty = PyString_FromString("");
	if (empty == NULL) {
		return -1;
	}

	default_suggestion = PyString_FromString("don't use this method");
	if (default_suggestion == NULL) {
		return -1;
	}


	return 0;
}

static inline char*
attribute_string(xmlNode* node, const char* name, char* name64
#ifndef __LP64__
	__attribute__((__unused__))
#endif
)
{
	char* value = (char*)xmlGetProp(node, (xmlChar*)name);
#ifdef __LP64__
	/* The 64-bit value defaults to the same as the 32-bit value */
	if (name64 != NULL) {
		char* value64 = (char*)xmlGetProp(node, (xmlChar*)name64);
		if (value64 != NULL) {
			if (value != NULL) {
				xmlFree(value);
			}
			value = value64;
		}
	}
#endif

	return value;
}

static inline BOOL
attribute_bool(xmlNode* node, const char* name, char* name64, BOOL dflt)
{
	char* value = attribute_string(node, name, name64);
	if (value == NULL) {
		return dflt;
	}

	if (strcmp(value, "true") == 0) {
		xmlFree(value);
		return YES;
	} else {
		xmlFree(value);
		return NO;
	}
}

static PyObject*
xmlToArgMeta(xmlNode* node, BOOL isMethod, int* argIdx)
{
	if (argIdx != NULL) {
		char* end;
		char* v = attribute_string(node, "index", NULL);
		if (v == NULL) {
			PyErr_SetString(PyExc_AttributeError, "no argument index");
			*argIdx = -1;
			return NULL;
		}
		*argIdx = strtol(v, &end, 10);
		if (end && *end != '\0') {
			PyErr_SetString(PyExc_ValueError, v);
			xmlFree(v);
		}
	}

	PyObject* result = PyDict_New();
	if (result == NULL) {
		return NULL;
	}

	PyObject* v;
	char* s;
	int r;

	s = attribute_string(node, "type", "type64");
	if (s && *s) {
		v = PyString_FromString(s);
		if (v == NULL) {
			xmlFree(s);
			Py_DECREF(result);
			return NULL;
		}
		r =  PyDict_SetItemString(result, "type", v);
		Py_DECREF(v);
		if (r == -1) {
			xmlFree(s);
			Py_DECREF(result);
			return NULL;
		}
	}
	if (s) xmlFree(s);

	s = attribute_string(node, "type_modifier", NULL);
	if (s && *s) {
		v = PyString_FromString(s);
		if (v == NULL) {
			xmlFree(s);
			Py_DECREF(result);
			return NULL;
		}
		r =  PyDict_SetItemString(result, "type_modifier", v);
		Py_DECREF(v);
		if (r == -1)  {
			xmlFree(s);
			Py_DECREF(result);
			return NULL;
		}
	}
	if (s) xmlFree(s);

	s = attribute_string(node, "sel_of_type", "sel_of_type64");
	if (s && *s) {
		v = PyString_FromString(s);
		if (v == NULL) {
			xmlFree(s);
			Py_DECREF(result);
			return NULL;
		}
		r =  PyDict_SetItemString(result, "sel_of_type", v);
		Py_DECREF(v);
		if (r == -1)  {
			xmlFree(s);
			Py_DECREF(result);
			return NULL;
		}
	}
	if (s) xmlFree(s);

	s = attribute_string(node, "c_array_of_fixed_length", NULL);
	if (s && *s) {
		char* end;
		v = PyInt_FromString(s, &end, 10);
		if (v == NULL) {
			xmlFree(s);
			Py_DECREF(result);
			return NULL;
		}
		if (end && *end != '\0') {
			PyErr_SetString(PyExc_ValueError, s);
			xmlFree(s);
			Py_DECREF(result);
			Py_DECREF(v);
			return NULL;
		}
		r =  PyDict_SetItemString(result, "c_array_of_fixed_length", v);
		Py_DECREF(v);
		if (r == -1) {
			xmlFree(s);
			Py_DECREF(result);
			return NULL;
		}
	}
	if (s) xmlFree(s);

	const char** bool_attrs = gBooleanAttributes;
	for (; *bool_attrs != NULL; bool_attrs++) {
		if (attribute_bool(node, *bool_attrs, NULL, NO)) {
			r = PyDict_SetItemString(result, *bool_attrs, Py_True);
		} else {
			r = PyDict_SetItemString(result, *bool_attrs, Py_False);
		}
		if (r == -1) {
			Py_DECREF(result);
			return NULL;
		}
	}

	/* Don't use attribute_bool because the default is non-trivial */
	s = attribute_string(node, "numeric", NULL);
	if (s && *s) {
		if (strcmp(s, "true") == 0) {
			r = PyDict_SetItemString(result, "numeric", Py_True);
		} else {
			r = PyDict_SetItemString(result, "numeric", Py_False);
		}
	}

	s = attribute_string(node, "c_array_length_in_arg", NULL);
	if (s && *s) {
		char* end = strchr(s, ',');
		
		if (end == NULL) {
			int input = strtol(s, &end, 10);
			if (end && *end != '\0') {
				PyErr_SetString(PyExc_ValueError, s);
				Py_DECREF(result);
				xmlFree(s);
				return NULL;
			}

			if (isMethod) {
				v = PyInt_FromLong(input + 2);
			} else {
				v = PyInt_FromLong(input);
			}
			if (v == NULL) {
				Py_DECREF(result);
				xmlFree(s);
				return NULL;
			}

			r = PyDict_SetItemString(result, "c_array_length_in_arg", v);
			Py_DECREF(v);
			if (r == -1) {
				Py_DECREF(result);
				xmlFree(s);
				return NULL;
			}
		} else {
			int input, output;
			char* x;

			input = strtol(s, &x, 10);
			if (x != end) {
				PyErr_SetString(PyExc_ValueError, s);
				Py_DECREF(result);
				xmlFree(s);
				return NULL;
			}
			output = strtol(end+1, &x, 10);
			if (*x != '\0') {
				PyErr_SetString(PyExc_ValueError, s);
				Py_DECREF(result);
				xmlFree(s);
				return NULL;
			}

			if (isMethod) {
				v = Py_BuildValue("ii", input+2, output+2);
			} else {
				v = Py_BuildValue("ii", input, output);
			}
			if (v == NULL) {
				Py_DECREF(result);
				xmlFree(s);
				return NULL;
			}

			r = PyDict_SetItemString(result, "c_array_length_in_arg", v);
			Py_DECREF(v);
			if (r == -1) {
				Py_DECREF(result);
				xmlFree(s);
				return NULL;
			}
		}
			
	}
	if (s) xmlFree(s);

	if (attribute_bool(node, "function_pointer", NULL, NO)) {
		/* Function argument is a function pointer, there are
		 * subelements describing the full type
		 */
		v = PyBool_FromLong(
				attribute_bool(node, "function_pointer_retained", NULL, YES));
		if (v == NULL) {
			Py_DECREF(result);
			return NULL;
		}
		r = PyDict_SetItemString(result, "callable_retained", v);
		if (r == -1) {
			Py_DECREF(result);
			return NULL;
		}

		PyObject* meta = PyDict_New();
		if (meta == NULL) {
			Py_DECREF(result);
			return NULL;
		}
		r = PyDict_SetItemString(result, "callable", meta);
		Py_DECREF(meta);
		if (r == -1) {
			Py_DECREF(result);
			return NULL;
		}

		PyObject* arguments = PyDict_New();
		if (arguments == NULL) {
			Py_DECREF(result);
			return NULL;
		}
		r = PyDict_SetItemString(meta, "arguments", arguments);
		Py_DECREF(arguments);
		if (r == -1) {
			Py_DECREF(result);
			return NULL;
		}
		
		xmlNode* al;
		int idx = 0;
		for (al = node->children; al != NULL; al = al->next) {
			if (al->type != XML_ELEMENT_NODE)  {
				continue;
			}
			if (strcmp((char*)al->name, "arg") == 0) {
				PyObject* d = xmlToArgMeta(al, NO, NULL);
				if (d == NULL) {
					Py_DECREF(result);
					return NULL;
				}
				v = PyInt_FromLong(idx++);
				if (v == NULL) {
					Py_DECREF(d);
					Py_DECREF(v);
					Py_DECREF(result);
					return NULL;
				}

				r = PyDict_SetItem(arguments, v, d);
				Py_DECREF(v); Py_DECREF(d);
				if (r == -1) {
					Py_DECREF(result);
					return NULL;
				}
			} else if (strcmp((char*)al->name, "retval") == 0) {
				PyObject* d = xmlToArgMeta(al, NO, NULL);
				if (d == NULL) {
					Py_DECREF(result);
					return NULL;
				}
				r = PyDict_SetItemString(meta, "retval", d);
				Py_DECREF(d);
				if (r == -1) {
					Py_DECREF(result);
					return NULL;
				}
			}
		}	
	}

	return result;
}

static inline int
handle_opaque(xmlNode* cur_node, PyObject* globalDict)
{
	char* name = attribute_string(cur_node, "name", NULL);
	char* type = attribute_string(cur_node, "type", "type64");

	if (name != NULL && type != NULL && *type != '\0' ) {
		/* We've found a valid opaque type */
		PyObject* value = PyObjCCreateOpaquePointerType(
			name, type, "");
		if (value == NULL) {
			if (name) xmlFree(name);
			if (type) xmlFree(type);
			return -1;
		}

		int r = PyDict_SetItemString(globalDict, name, value);
		Py_DECREF(value);
		if (r == -1) {
			if (name) xmlFree(name);
			if (type) xmlFree(type);
			return -1;
		}
	}
	if (name) xmlFree(name);
	if (type) xmlFree(type);
	return 0;
}

static inline int
handle_constant(xmlNode* cur_node, PyObject* globalDict)
{
	char* name = attribute_string(cur_node, "name", NULL);
	char* type = attribute_string(cur_node, "type", "type64");

	if (name != NULL && type != NULL && *type != '\0' ) {
		if (type[0] == _C_STRUCT_B) {
			/*
			 * We do not yet correctly handle structs with embedded
			 * function pointers, this check locates those (and
			 * some more).
			 */
			char* e = strchr(type, '=');
			if (e != NULL && strchr(e, '?') != NULL) {
				if (name) xmlFree(name);
				if (type) xmlFree(type);
				return 0;
			}
		}
				
		BOOL magic = attribute_bool(cur_node, "magic_cookie", NULL, NO);

		void* buf = dlsym(RTLD_DEFAULT, name);

		PyObject* v;
		if (buf != NULL) {
			if (magic) {
				v = PyObjCCF_NewSpecial(type, buf);
			} else {
				v = pythonify_c_value(type, buf);
			}

			if (v == NULL) {
				if (name) xmlFree(name);
				if (type) xmlFree(type);
				return -1;
			}

			int r = PyDict_SetItemString(globalDict, name, v);
			if (r == -1) {
				if (name) xmlFree(name);
				if (type) xmlFree(type);
				return -1;
			}
		}
	}
	if (name) xmlFree(name);
	if (type) xmlFree(type);
	return 0;
}

static inline int
handle_string_constant(xmlNode* cur_node, PyObject* globalDict)
{
	char* name = attribute_string(cur_node, "name", NULL);
	char* value = attribute_string(cur_node, "value", "value64");

	if (name != NULL && value != NULL && *value != '\0') {
		size_t i, len = strlen(value);

		PyObject* v = NULL;
		for (i = 0; i < len; i++) {
			if (((unsigned char)value[i]) > 127) {
				v = PyUnicode_DecodeUTF8(value, len, "strict");
				if (v == NULL) {
					if (name) xmlFree(name);
					if (value) xmlFree(value);
					return -1;
				}
				break;
			}
		}
		if (v == NULL) {
			v = PyString_FromStringAndSize(value, len);
		}
		if (v == NULL) {
			if (name) xmlFree(name);
			if (value) xmlFree(value);
			return -1;
		}

		int r = PyDict_SetItemString(globalDict, name, v);
		Py_DECREF(v);
		if (r == -1) {
			if (name) xmlFree(name);
			if (value) xmlFree(value);
			return -1;
		}
	}

	if (name) xmlFree(name);
	if (value) xmlFree(value);
	return 0;
}

static inline int
handle_enum(xmlNode* cur_node, PyObject* globalDict)
{
	char* name = attribute_string(cur_node, "name", NULL);
	char* value = attribute_string(cur_node, "value", "value64");

	if (value == NULL) {
#ifdef __BIGENDIAN__
		value = attribute_string(cur_node, "be_value", NULL);
#else
		value = attribute_string(cur_node, "le_value", NULL);
#endif
	}

	if (name != NULL && value != NULL && *value != '\0') {
		PyObject* v;
		char* end;

		if (strchr(value, '.') != NULL) {
			/* floating point literal */
			PyObject* s = PyString_FromString(value);
			if (s == NULL) {
				v = NULL;

			} else {
				v = PyFloat_FromString(s, &end);
				Py_DECREF(s);
			}
		} else {
			/* integer literal */
			v = PyInt_FromString(value, &end, 10);
		}

		if (v == NULL) {
			if (name) xmlFree(name);
			if (value) xmlFree(value);
			return -1;
		}
		if (end && *end != '\0') {
			/* Junk at the end of the literal */
			PyErr_SetString(PyExc_ValueError,
				"Junk in enum value");
			if (name) xmlFree(name);
			if (value) xmlFree(value);
			Py_DECREF(v);
			return -1;
		}

		int r  = PyDict_SetItemString(globalDict, name, v);
		Py_DECREF(v);
		if (r == -1) {
			if (name) xmlFree(name);
			if (value) xmlFree(value);
			return -1;
		}
	}

	if (name) xmlFree(name);
	if (value) xmlFree(value);
	return 0;
}

static inline int
handle_null_const(xmlNode* cur_node, PyObject* globalDict)
{
	char* name = attribute_string(cur_node, "name", NULL);

	if (name != NULL) {
		int r  = PyDict_SetItemString(globalDict, name, Py_None);
		if (r == -1) {
			if (name) xmlFree(name);
			return -1;
		}
	}

	if (name) xmlFree(name);
	return 0;
}

static inline int
handle_function_pointer(xmlNode* cur_node, PyObject* func_aliases)
{
	char* name = attribute_string(cur_node, "name", NULL);
	char* original = attribute_string(cur_node, "original", NULL);

	if (name != NULL && original != NULL) {
		PyObject* v = Py_BuildValue("ss", name, original);
		if (v == NULL) {
			if (name) xmlFree(name);
			if (original) xmlFree(original);
			return -1;
		}
		int r = PyList_Append(func_aliases, v);
		Py_DECREF(v);
		if (r == -1) {
			if (name) xmlFree(name);
			if (original) xmlFree(original);
			return -1;
		}
	}
	
	if (name) xmlFree(name);
	if (original) xmlFree(original);
	return 0;
}


static inline int
handle_cftype(xmlNode* cur_node, PyObject* globalDict, PyObject* cftypes)
{
	char* name = attribute_string(cur_node, "name", NULL);
	char* type = attribute_string(cur_node, "type", "type64");
	char* funcname = attribute_string(cur_node, "gettypeid_func", NULL);
	char* tollfree = attribute_string(cur_node, "tollfree", NULL);
	int retval = -1;
	PyObject* v;


	if (name == NULL || type == NULL || *type == '\0') {
		retval = 0;
		goto end;
	}

	if (tollfree != NULL) {
		Class cls = objc_lookUpClass(tollfree);
		if (cls == NULL) {
			//PyErr_SetString(PyObjCExc_NoSuchClassError,
			//	tollfree);
			retval = 0;
			goto end;
		}
		if (PyObjCPointerWrapper_RegisterID(type) == -1) {
			goto end;
		}
		v = PyObjCClass_New(cls);

	} else {
		CFTypeID (*getfunc)(void) = NULL;

		if (funcname != NULL) {
			getfunc = dlsym(RTLD_DEFAULT, funcname);
		}

		if (getfunc == NULL) {
			/* Annoyingly enough not all public CFTypes have
			 * a GetTypeID function, proxy all those using
			 * the generic cftype wrapper.
			 */
			Class cls = objc_lookUpClass("NSCFType");
			if (cls == NULL) {
				PyErr_SetString(PyObjCExc_NoSuchClassError,
					tollfree);
				goto end;
			}
			if (PyObjCPointerWrapper_RegisterID(type) == -1) {
				goto end;
			}
			v = PyObjCClass_New(cls);
		} else {
			CFTypeID typeid = getfunc();

			v = PyInt_FromLong(typeid);
			if (v == NULL) {
				goto end;
			}
			int r = PyDict_SetItemString(PyObjC_TypeStr2CFTypeID, type, v);
			Py_DECREF(v);
			if (r == -1) {
				goto end;
			}

			v = PyObjCCFType_New(name, type, typeid);

			if (v != NULL && cftypes != NULL) {
				PyObject* e = Py_BuildValue("ss", name, type);
				if (e != NULL) {
					PyList_Append(cftypes, e);
					Py_DECREF(e);
				}

				// Ignore errors while building this list.
				PyErr_Clear();
			}

		}
	}

	if (v != NULL) {
		retval = PyDict_SetItemString(globalDict, name, v);
		Py_DECREF(v);
	}


	retval = 0;	
end:
	if (name) xmlFree(name);
	if (type) xmlFree(type);
	if (funcname) xmlFree(funcname);
	if (tollfree) xmlFree(tollfree);
	return retval;
}

static inline int
handle_class(xmlNode* cur_node)
{
	int r;
	char* classname = attribute_string(cur_node, "name", NULL);
	PyObject* pyClassname = NULL;
	if (classname == NULL) return 0;

	xmlNode* method;
	for (method = cur_node->children; method != NULL; method = method->next) {
		if (method->type != XML_ELEMENT_NODE)  {
			continue;
		}
		if (strcmp((char*)method->name, "method") != 0) {
			/* Ignore other elements */
			continue;
		}


		char* selname = attribute_string(method, "selector", NULL);
		if (selname == NULL) continue;

		BOOL variadic = attribute_bool(method, "variadic", NULL, NO);
		BOOL c_array = attribute_bool(method, "c_array_delimited_by_null", NULL, NO);
		BOOL ignore = attribute_bool(method, "ignore", NULL, NO);

		PyObject* metadata = PyDict_New();
		if (metadata == NULL) {
			Py_XDECREF(pyClassname);
			xmlFree(selname);
			xmlFree(classname);
			return -1;
		}

		if (ignore) {
			char* suggestion = attribute_string(method, "suggestion", NULL);
			if (suggestion == NULL) {
				r = PyDict_SetItemString(metadata, "suggestion", default_suggestion);
				if (r == -1) {
					Py_DECREF(metadata);
					Py_XDECREF(pyClassname);
					xmlFree(selname);
					xmlFree(classname);
					return -1;
				}

			} else {
				PyObject* v = PyString_FromString(suggestion);
				xmlFree(suggestion);

				r = PyDict_SetItemString(metadata, "suggestion", v);
				Py_DECREF(v);
				if (r == -1) {
					Py_DECREF(metadata);
					Py_XDECREF(pyClassname);
					xmlFree(selname);
					xmlFree(classname);
					return -1;
				}
			}
		}

		PyObject* v = PyBool_FromLong(variadic);
		if (v == NULL) {
			Py_DECREF(metadata);
			Py_XDECREF(pyClassname);
			xmlFree(selname);
			xmlFree(classname);
			return -1;
		}
		r = PyDict_SetItemString(metadata, "variadic", v);
		Py_DECREF(v);
		if (r == -1) {
			Py_DECREF(metadata);
			Py_XDECREF(pyClassname);
			xmlFree(selname);
			xmlFree(classname);
			return -1;
		}

		if (variadic) {
			v = PyBool_FromLong(c_array);
			if (v == NULL) {
				Py_DECREF(metadata);
				Py_XDECREF(pyClassname);
				xmlFree(selname);
				xmlFree(classname);
				return -1;
			}
			r = PyDict_SetItemString(metadata, "c_array_delimited_by_null", v);
			if (r == -1) {
				Py_DECREF(metadata);
				Py_XDECREF(pyClassname);
				xmlFree(selname);
				xmlFree(classname);
				return -1;
			}
		}

		PyObject* arguments = PyDict_New();
		if (arguments == NULL) {
			Py_DECREF(metadata);
			Py_XDECREF(pyClassname);
			xmlFree(selname);
			xmlFree(classname);
			return -1;
		}
		r = PyDict_SetItemString(metadata, "arguments", arguments);
		Py_DECREF(arguments);
		if (r == -1) {
			Py_DECREF(metadata);
			Py_XDECREF(pyClassname);
			xmlFree(selname);
			xmlFree(classname);
			return -1;
		}

		xmlNode* al;
		for (al = method->children; al != NULL; al = al->next) {
			if (al->type != XML_ELEMENT_NODE)  {
				continue;
			}

			if (strcmp((char*)al->name, "arg") == 0) {
				int argIdx;
				PyObject* d = xmlToArgMeta(al, YES, &argIdx);
				if (d == NULL) {
					Py_DECREF(metadata);
					Py_XDECREF(pyClassname);
					xmlFree(selname);
					xmlFree(classname);
					return -1;
				}
				
				PyObject* idx = PyInt_FromLong(argIdx+2);
				if (idx == NULL) {
					Py_DECREF(d);
					Py_DECREF(metadata);
					Py_XDECREF(pyClassname);
					xmlFree(selname);
					xmlFree(classname);
					return -1;
				}

				r = PyDict_SetItem(arguments, idx, d);
				Py_DECREF(idx);
				Py_DECREF(d);
				if (r == -1) {
					Py_DECREF(metadata);
					Py_XDECREF(pyClassname);
					xmlFree(selname);
					xmlFree(classname);
					return -1;
				}

			} else if (strcmp((char*)al->name, "retval") == 0) {
				PyObject* d = xmlToArgMeta(al, YES, NULL);
				if (d == NULL) {
					Py_DECREF(metadata);
					Py_XDECREF(pyClassname);
					xmlFree(selname);
					xmlFree(classname);
					return -1;
				}

				r = PyDict_SetItemString(metadata, "retval", d);
				Py_DECREF(d);
				if (r == -1) {
					Py_DECREF(metadata);
					Py_XDECREF(pyClassname);
					xmlFree(selname);
					xmlFree(classname);
					return -1;
				}
			}
		}

		/* Complete metadata for a method, register it */
		if (pyClassname == NULL) {
			pyClassname = PyString_FromString(classname);
			if (pyClassname == NULL) {
				Py_DECREF(metadata);
				xmlFree(selname);
				xmlFree(classname);
				return -1;
			}
		}

		PyObject* pySelector = PyString_FromString(selname);
		if (pySelector == NULL) {
			Py_DECREF(pyClassname);
			Py_DECREF(metadata);
			xmlFree(selname);
			xmlFree(classname);
			return -1;
		}

		r = PyObjC_registerMetaData(pyClassname, pySelector, metadata);
		Py_DECREF(pySelector);
		Py_DECREF(metadata);

		if (r < 0) {
			xmlFree(selname);
			xmlFree(classname);
			return -1;
		}
	}

	Py_XDECREF(pyClassname);
	xmlFree(classname);
	return 0;
}

static inline int
handle_function(xmlNode* cur_node, PyObject* globalDict, struct functionlist* inlineTab)
{
	char* name = attribute_string(cur_node, "name", NULL);
	if (name == NULL) return 0;

	void* function = dlsym(RTLD_DEFAULT, name);
	if (function == NULL) {
		/* Look in the inlineTab if we have one */
		function = find_function(inlineTab, name);
		if (function == NULL) {
			/* Function doesn't exist, don't bother to process
			 * metadata for it.
			 */
			return 0;
		}
	}

	BOOL ignore = attribute_bool(cur_node, "ignore", NULL, NO);
	if (ignore) {
		/* Function should be ignored */
		if (PyDict_GetItemString(globalDict, name)) {
			PyDict_DelItemString(globalDict, name);
		}
		xmlFree(name);
		return 0;
	}


	/* Build the metadata for the function:
	 * - metdata is the actual metadata list
	 * - siglist is a list with signature elements
	 *   (retval, arg1, arg2, ...)
	 */
	
	PyObject* metadata = PyDict_New();
	if (metadata == NULL) {
		xmlFree(name);
		return -1;
	}
	PyObject* arguments = PyDict_New();
	if (arguments == NULL) {
		xmlFree(name);
		Py_DECREF(metadata);
		return -1;
	}
	if (PyDict_SetItemString(metadata, "arguments", arguments) < 0)  {
		xmlFree(name);
		Py_DECREF(metadata);
		Py_DECREF(arguments);
		return -1;
	}

	BOOL variadic = attribute_bool(cur_node, "variadic", NULL, NO);
	PyObject* v = PyBool_FromLong(variadic);
	if (v == NULL) {
		xmlFree(name);
		Py_DECREF(metadata);
		Py_DECREF(arguments);
		return -1;
	}

	if (PyDict_SetItemString(metadata, "variadic", v) < 0)  {
		xmlFree(name);
		Py_DECREF(metadata);
		Py_DECREF(v);
		return -1;
	}
	Py_DECREF(v);

	if (variadic) {
		v = PyBool_FromLong(
			attribute_bool(cur_node, "c_array_delimited_by_null", NULL, NO));
		if (v == NULL) {
			xmlFree(name);
			Py_DECREF(metadata);
			Py_DECREF(arguments);
			return -1;
		}

		if (PyDict_SetItemString(metadata, "c_array_delimited_by_null", v) < 0)  {
			xmlFree(name);
			Py_DECREF(metadata);
			Py_DECREF(v);
			return -1;
		}
		Py_DECREF(v);
	}

	PyObject* siglist = PyList_New(0);
	if (siglist == NULL) {
		Py_DECREF(metadata);
		Py_DECREF(arguments);
		xmlFree(name);
		return -1;
	}

	/* Set the default result type to 'v' */
	v = PyString_FromString("v");
	if (v == NULL) goto error;

	int r = PyList_Append(siglist, v);
	Py_DECREF(v);
	if (r == -1) goto error;

	/* Now walk the children of this mode, that is the
	 * argument and retval definitions.
	 */
	xmlNode* al;
	for (al = cur_node->children; al != NULL; al = al->next) {
		if (al->type != XML_ELEMENT_NODE)  {
			continue;
		}

		if (strcmp((char*)al->name, "arg") == 0) {
			PyObject* d = xmlToArgMeta(al, NO, NULL);
			if (d == NULL) {
				goto error;
			}

			PyObject* s = PyDict_GetItemString(d, "type");
			if (s == NULL) {
				Py_DECREF(d);
				goto error;
			}

			if (PyList_Append(siglist, s) < 0) {
				Py_DECREF(d);
				goto error;
			}

			PyObject* argIdx = PyInt_FromLong(PyList_Size(siglist)-2);
			if (argIdx == NULL) {
				Py_DECREF(d);
				goto error;
			}

			if (PyDict_SetItem(arguments, argIdx, d) < 0) {
				Py_DECREF(d);
				Py_DECREF(argIdx);
				goto error;
			}
			Py_DECREF(d);
			Py_DECREF(argIdx);

		} else if (strcmp((char*)al->name, "retval") == 0) {

			PyObject* d = xmlToArgMeta(al, NO, NULL);
			if (d == NULL) {
				goto error;
			}

			PyObject* s = PyDict_GetItemString(d, "type");
			if (s == NULL) {
				Py_DECREF(d);
				goto error;
			}

			if (PyList_SetItem(siglist, 0, s) < 0) {
				Py_DECREF(d);
				goto error;
			}
			Py_INCREF(s); /* SetItem steals a reference */

			if (PyDict_SetItemString(metadata, "retval", d) < 0) {
				Py_DECREF(d);
				goto error;
			}
			Py_DECREF(d);
		}
		/* else: ignore */
	}


	/* We have the complete metadata, now build the proxy object for it */
	PyObject* signature = PyObject_CallMethod(empty, "join", "O", siglist);
	if (signature == NULL) {
		goto error;
	}

	PyObject* nm = PyString_FromString(name);
	if (nm == NULL) {
		goto error;
	}
	v = PyObjCFunc_New(nm, function, PyString_AsString(signature), Py_None, metadata);

	Py_DECREF(nm);
	Py_DECREF(metadata);
	Py_DECREF(arguments);
	Py_DECREF(siglist);

	if (v == NULL) {
		xmlFree(name);
		return -1;
	}

	if (PyDict_SetItemString(globalDict, name, v) < 0) {
		Py_DECREF(v);
		xmlFree(name);
		return -1;
	}
	Py_DECREF(v);
	xmlFree(name);
	return 0;

error:
	Py_DECREF(siglist);
	Py_DECREF(arguments);
	Py_DECREF(metadata);
	xmlFree(name);
	return -1;
}

static inline int
handle_informal_protocol(xmlNode* cur_node, const char* framework, PyObject* globalDict)
{
	char* name = attribute_string(cur_node, "name", NULL);
	PyObject* methodList = NULL;

	if (name == NULL) {
		return 0;
	}

	xmlNode* method;

	for (method = cur_node->children; method != NULL; method = method->next) {
		if (method->type != XML_ELEMENT_NODE)  {
			continue;
		}

		char* selector = attribute_string(method, "selector", NULL);
		char* type = attribute_string(method, "type", "type64");
		BOOL isClassMethod = attribute_bool(method, "classmethod", NULL, NO);

		if (selector != NULL && type != NULL) {
			if (methodList == NULL) {
				methodList = PyList_New(0);
				if (methodList == NULL) {
					xmlFree(name);
					return -1;
				}
			}

			PyObject* m = PyObjCSelector_New(Py_None, sel_getUid(selector),
				type, isClassMethod, NULL);
			if (m == NULL) {
				Py_DECREF(methodList);
				xmlFree(name);
				return -1;
			}
			int r = PyList_Append(methodList, m);
			Py_DECREF(m);
			if (r == -1) {
				Py_DECREF(methodList);
				xmlFree(name);
				return -1;
			}
		}

		if (selector) xmlFree(selector);
		if (type) xmlFree(type);
	}

	if (methodList != NULL && PyList_Size(methodList) != 0) {
		PyObject* proto = PyObject_CallFunction(
				(PyObject*)&PyObjCInformalProtocol_Type,
				"sO",
				name, methodList);
		if (proto == NULL) {
			Py_DECREF(methodList);
			xmlFree(name);
			return -1;
		}


		PyObject* module;
		module = PyDict_GetItemString(globalDict, "protocols");

		if (module == NULL) {
			char buf[1024];
			snprintf(buf, sizeof(buf), "%s.protocols", framework);
			PyObject* mod_name = PyString_FromString(buf);
			if (mod_name == NULL) {
				Py_DECREF(proto);
				Py_DECREF(methodList);
				xmlFree(name);
				return -1;
			}


			module = PyModule_New(buf);
			if (module == NULL) {
				Py_DECREF(mod_name);
				Py_DECREF(proto);
				Py_DECREF(methodList);
				xmlFree(name);
				return -1;
			}
			
			int r = PyDict_SetItemString(globalDict,
					"protocols", module);
			if (r == -1) {
				Py_DECREF(mod_name);
				Py_DECREF(proto);
				Py_DECREF(methodList);
				xmlFree(name);
				return -1;
			}

			/* Add to sys.modules as well */
			PyObject* sysmod = PyImport_GetModuleDict();
			if (sysmod == NULL) {
				Py_DECREF(mod_name);
				Py_DECREF(proto);
				Py_DECREF(methodList);
				xmlFree(name);
				return -1;
			}
			r = PyDict_SetItem(sysmod, mod_name, module);
			Py_DECREF(mod_name);
			if (r == -1) {
				Py_DECREF(proto);
				Py_DECREF(methodList);
				xmlFree(name);
				return -1;
			}
			Py_DECREF(module);
		}

		int r = PyObject_SetAttrString(module, name, proto);
		Py_DECREF(proto);
		if (r == -1) {
			Py_DECREF(methodList);
			xmlFree(name);
			return -1;
		}
	}

	xmlFree(name);
	Py_XDECREF(methodList);
	return 0;
}

static inline int
handle_struct(xmlNode* cur_node, PyObject* globalDict)
{
	char* name = attribute_string(cur_node, "name", NULL);
	char* type = attribute_string(cur_node, "type", "type64");

	if (name != NULL && type != NULL && *type != '\0') {
		PyObject* v = PyObjC_RegisterStructType(
				PyObjCUtil_Strdup(type), 
				PyObjCUtil_Strdup(name), 
				"", NULL, -1, NULL);

		if (v == NULL) {
			if (name) xmlFree(name);
			if (type) xmlFree(type);
			return -1;
		}

		if (structConvenience != NULL) {
			PyObject* o = PyObject_CallFunction(
					structConvenience, 
					"ss", name, type);
			Py_XDECREF(o);
			PyErr_Clear();
		}

		int r = PyDict_SetItemString(globalDict, name, v);
		Py_DECREF(v);
		if (r == -1) {
			if (name) xmlFree(name);
			if (type) xmlFree(type);
			return -1;
		}
	}

	if (name) xmlFree(name);
	if (type) xmlFree(type);
	return 0;
}

static int 
expand_aliases(PyObject* globalDict, PyObject* func_aliases)
{
	Py_ssize_t i, len;

	len = PyList_Size(func_aliases);

	for (i = 0; i < len; i++) {
		PyObject* v = PyList_GET_ITEM(func_aliases, i);
		PyObject* name;
		PyObject* orig;

		name = PyTuple_GET_ITEM(v, 0);
		orig = PyTuple_GET_ITEM(v, 1);

		v = PyDict_GetItem(globalDict, orig);
		if (v != NULL) {
			int r = PyDict_SetItem(globalDict, name, v);
			Py_DECREF(v);
			if (r == -1) {
				PyErr_Clear();
			}
		}
	}
	return 0;
}


PyObject*
PyObjC_SetSetupCFClasses(PyObject* self __attribute__((__unused__)), PyObject* arg)
{
	Py_INCREF(arg);
	Py_XDECREF(setupCFClasses);
	setupCFClasses = arg;
	Py_INCREF(Py_None);
	return Py_None;
}

PyObject*
PyObjC_SetStructConvenience(PyObject* self __attribute__((__unused__)), PyObject* arg)
{
	Py_INCREF(arg);
	Py_XDECREF(structConvenience);
	structConvenience = arg;
	Py_INCREF(Py_None);
	return Py_None;
}


int
PyObjC_ProcessXML(char* data, int length, PyObject* globalDict, const char* dylibPath, const char* framework, PyObject* _inlineTab)
{
	PyObject* value;	
	PyObject* func_aliases = NULL;
	PyObject* cftypes = NULL;

	if (setupCFClasses) {
		cftypes = PyList_New(0);
		if (cftypes == NULL) {
			return -1;
		}
	}


	xmlDoc* doc = xmlReadMemory(data, length,
		"noname.xml", NULL, 0 /*XML_PARSE_COMPACT*/);
	if (doc == NULL) {
		PyErr_SetString(PyObjCExc_Error, "invalid bridgesupport file");
		return -1;
	}

	struct functionlist* inlineTab = NULL;
	if (_inlineTab != NULL && PyCObject_Check(_inlineTab)) {
		inlineTab = PyCObject_AsVoidPtr(_inlineTab);
		if (inlineTab == NULL) {
			PyErr_Clear();
		}
	}

	/* Process document here */
	xmlNode* root = xmlDocGetRootElement(doc);
	xmlNode* cur_node;
	if (root->type != XML_ELEMENT_NODE || strcmp((char*)root->name, "signatures") != 0) {
		PyErr_SetString(PyObjCExc_Error, "invalid root node in bridgesupport file");
		return -1;
	}

	if (dylibPath) {
		dlopen(dylibPath, RTLD_LAZY);
	}

	func_aliases = PyList_New(0);
	if (func_aliases == NULL) {
		return -1;
	}

	PyObjC_UpdatingMetaData = YES;

	for (cur_node = root->children; cur_node != NULL; cur_node = cur_node->next) {
		if (cur_node->type != XML_ELEMENT_NODE)  {
			/* We're only interested in actual elements */
			continue;
		}
		char* tag = (char*)cur_node->name;
		value = NULL;
		int r = 1;

		/* Use a basic one-level tree to quickly dispatch to the right
		 * handler.
		 */
		switch (tag[0]) {
		case 'c':
			if (strcmp(tag, "cftype") == 0) {
				r = handle_cftype(cur_node, globalDict, cftypes);
			} else if (strcmp(tag, "constant") == 0) {
				r = handle_constant(cur_node, globalDict);
			} else if (strcmp(tag, "class") == 0) {
				r = handle_class(cur_node);
			}
			break;

		case 'e':
			if (strcmp(tag, "enum") == 0) {
				r = handle_enum(cur_node, globalDict);
			}
			break;

		case 'f':
			if (strcmp(tag, "function") == 0) {
				r = handle_function(cur_node, globalDict, inlineTab);
			} else if (strcmp(tag, "function_pointer") == 0) {
				r = handle_function_pointer(cur_node, func_aliases);
			}
			break;

		case 'i': 
			if (strcmp(tag, "informal_protocol") == 0) {
				r = handle_informal_protocol(cur_node, framework, globalDict);
			}
			break;

		case 'n':
			if (strcmp(tag, "null_const") == 0) {
				r = handle_null_const(cur_node, globalDict);
			}
			break;

		case 'o':
			if (strcmp(tag, "opaque") == 0) {
				r = handle_opaque(cur_node, globalDict);
			}
			break;

		case 's':
			if (strcmp(tag, "struct") == 0) {
				r = handle_struct(cur_node, globalDict);
			} else if (strcmp(tag, "string_constant") == 0) {
				r = handle_string_constant(cur_node, globalDict);
			}
			break;

		}

		if (r == 1) {
			/* Unknown tag, ignore these to avoid breaking when 
			 * the metadata format is upgraded.
			 */
		} else if (r == -1) {
			goto end;
		}
	}

	if (PyList_Size(func_aliases) != 0) {
		expand_aliases(globalDict, func_aliases);
	}

	if (setupCFClasses) {
		PyObject* o = PyObject_CallFunction(setupCFClasses, "OO",
			globalDict, cftypes);
		Py_XDECREF(o);
		PyErr_Clear();
	}

end:
	PyObjC_UpdatingMetaData = NO;
	PyObjC_MappingCount ++;

	Py_XDECREF(cftypes); cftypes = NULL;

	Py_DECREF(func_aliases);
	xmlFreeDoc(doc);
	if (PyErr_Occurred()) {
		return -1;
	} else {
		return 0;
	}
}
