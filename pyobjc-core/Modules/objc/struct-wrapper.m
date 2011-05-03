/*
 * Wrappers for C structs
 *
 * Structs are represented as instance-like objects, with normal field access
 * (e.g. myRect.size), but can also be accessed like read-write tuples (e.g.
 * myRect[0]).
 *
 * Instances consist of the generic PyObject header followed by an array of 
 * fields. 
 *
 * NOTE: The basic implementation is quite generic, but the end of this file
 * is only usefull for PyObjC.
 */
#include "pyobjc.h"

/*
 * First some helpers: easy access to the actual fields
 */
static inline PyObject*
GET_FIELD(PyObject* self, PyMemberDef* member)
{
	PyObject* v; 

	v =  *(PyObject**)(((char*)self) + member->offset);
	if (v == NULL) {
		return Py_None;
	} else {
		return v;
	}
}

static inline void
SET_FIELD(PyObject* self, PyMemberDef* member, PyObject* val)
{
	PyObject* tmp;
	Py_XINCREF(val);
	
	tmp = *(PyObject**)(((char*)self) + member->offset);
	*((PyObject**)(((char*)self) + member->offset)) = val;
	Py_XDECREF(tmp);
}

/*
 * Implementation of the sequence interface.
 */

static Py_ssize_t
struct_sq_length(PyObject* self)
{
	/* The object contains the generic PyObject header followed by an
	 * array of PyObject*-s.
	 */
	return (Py_TYPE(self)->tp_basicsize - sizeof(PyObject)) / sizeof(PyObject*);
}

static PyObject*
struct_sq_item(PyObject* self, Py_ssize_t offset)
{
	Py_ssize_t len = struct_sq_length(self);
	PyMemberDef* member;
	PyObject* res;

	if (offset < 0 || offset >= len) {
		PyErr_Format(PyExc_IndexError,  
				"%s index out of range",
				Py_TYPE(self)->tp_name);
		return NULL;
	} 

	member = Py_TYPE(self)->tp_members + offset;
	res = GET_FIELD(self, member);

	Py_INCREF(res);
	return res;
}

static PyObject*
struct_sq_slice(PyObject* self, Py_ssize_t ilow, Py_ssize_t ihigh)
{
	PyObject* result;
	Py_ssize_t i, len;
	
	len = struct_sq_length(self);
	if (ilow < 0)  ilow = 0;
	if (ihigh > len) ihigh = len;

	result = PyTuple_New(ihigh - ilow);
	if (result == NULL) {
		return NULL;
	}

	for (i = ilow; i < ihigh; i++) {
		PyMemberDef* member = Py_TYPE(self)->tp_members + i;
		PyObject* v = GET_FIELD(self, member);
		Py_INCREF(v);
		PyTuple_SET_ITEM(result, i-ilow, v);
	}
	return result;
}

static int
struct_sq_ass_item(PyObject* self, Py_ssize_t offset, PyObject* newVal)
{
	Py_ssize_t len;
	PyMemberDef* member;

	if (newVal == NULL) {
		PyErr_Format(PyExc_TypeError, 
			"Cannot delete item '%"PY_FORMAT_SIZE_T"d' in a %s instance",
			offset, Py_TYPE(self)->tp_name);
		return -1;
	}

	len = struct_sq_length(self);

	if ((offset < 0) || (offset >= len)) {
		PyErr_Format(PyExc_IndexError,  
				"%s index out of range",
				Py_TYPE(self)->tp_name);
		return -1;
	}
	member = Py_TYPE(self)->tp_members + offset;
	SET_FIELD(self, member, newVal);
	return 0;
}

static int
struct_sq_ass_slice(PyObject* self, Py_ssize_t ilow, Py_ssize_t ihigh, PyObject* v)
{
	PyObject* seq;
	Py_ssize_t i, len;

	if (v == NULL) {
		PyErr_Format(PyExc_TypeError,
			"Cannot delete items in an %s instance",
			Py_TYPE(self)->tp_name);
		return -1;
	}

	
	len = struct_sq_length(self);
	if (ilow < 0)  {
		ilow = 0;
	} else if (ilow > len) {
		ilow = len;
	}

	if (ihigh < ilow) {
		ihigh = ilow;
	} else if (ihigh > len) {
		ihigh = len;
	}

	seq = PySequence_Fast(v, "must assign sequence to slice");
	if (seq == NULL) return -1;

	if (PySequence_Fast_GET_SIZE(seq) != ihigh - ilow) {
		Py_DECREF(seq);
		PyErr_Format(PyExc_TypeError,
			"slice assignment would change size of %s "
			"instance", Py_TYPE(self)->tp_name);
		return -1;
	}

	for (i = ilow; i < ihigh; i++) {
		PyObject* x;
		PyMemberDef* member = Py_TYPE(self)->tp_members + i;

		x = PySequence_Fast_GET_ITEM(seq, i-ilow);
		if (x == NULL) {
			Py_DECREF(seq);
			return -1;
		}
		SET_FIELD(self, member, x);
	}
	Py_DECREF(seq);
	return 0;
}

static int
struct_sq_contains(PyObject* self, PyObject* value)
{
	PyMemberDef* member = Py_TYPE(self)->tp_members;

	while (member && member->name) {
		int r;
		PyObject* cur = GET_FIELD(self, member);

		r = PyObject_RichCompareBool(cur, value, Py_EQ);
		if (r == -1) {
			PyErr_Clear();
		} else if (r) {
			return 1;
		}
	}
	return 0;
}

static PyObject*
struct_reduce(PyObject* self)
{
	PyObject* result;
	PyObject* values;
	Py_ssize_t i, len;

	len = struct_sq_length(self);
	values = PyTuple_New(len);
	if (values == NULL) return NULL;

	for (i = 0; i < len; i++) {
		PyObject* v = GET_FIELD(self, Py_TYPE(self)->tp_members + i);
		Py_INCREF(v);
		PyTuple_SET_ITEM(values, i, v);
	}

	result = Py_BuildValue("(OO)", Py_TYPE(self), values);
	Py_DECREF(values);
	return result;
}

static PyObject*
struct_copy(PyObject* self)
{
	PyObject* result;
	PyMemberDef* member = Py_TYPE(self)->tp_members;
	
	result = PyObject_GC_New(PyObject, Py_TYPE(self));
	if (result == NULL) {
		return NULL;
	}

	while (member && member->name) {
		if (member->type != T_OBJECT) {
			member++;
			continue;
		}
		*((PyObject**)(((char*)result) + member->offset)) = NULL;
		PyObject* t = GET_FIELD(self, member);

		if (t != NULL) {
			PyObject* m = PyObject_GetAttrString(t, "__pyobjc_copy__");
			if (m == NULL) {
				PyErr_Clear();
				SET_FIELD(result, member, t);
			} else {
				PyObject* c = PyObject_CallObject(m, NULL);
				Py_DECREF(m);
				if (c == NULL) {
					Py_DECREF(result);
					return NULL;
				}
				SET_FIELD(result, member, c);
				Py_DECREF(c);
			}
		}

		member++;
	}

	PyObject_GC_Track(result);
	return result;
}

static PyObject*
struct_mp_subscript(PyObject* self, PyObject* item)
{
	if (PyIndex_Check(item)) {
		Py_ssize_t i;
		i = PyNumber_AsSsize_t(item, PyExc_IndexError);
		if (i == -1 && PyErr_Occurred()) {
			return NULL;
		} 
		if (i < 0) {
			i += struct_sq_length(self);
		}
		return struct_sq_item(self, i);
	} else if (PySlice_Check(item)) {
		Py_ssize_t start, stop, step, slicelength, cur, i;
		PyObject* result;
		PyObject* it;

		if (PySlice_GetIndicesEx((PySliceObject*)item, 
				struct_sq_length(self),
				&start, &stop, &step, &slicelength) < 0) {
			return NULL;
		}

		if (slicelength <= 0) {
			return PyTuple_New(0);
		} else if (step == 1) {
			return struct_sq_slice(self, start, stop);
		} else {
			result = PyTuple_New(slicelength);
			if (result == NULL) {
				return NULL;
			}

			for (cur = start, i = 0; i < slicelength; 
						cur += step, i++) {
				it = struct_sq_item(self, cur);
				PyTuple_SET_ITEM(result, i, it);
			}
			return result;
		}

	} else {
		PyErr_Format(PyExc_TypeError,
			"struct indices must be integers, not %.200s",
			Py_TYPE(item)->tp_name);
		return NULL;
	}
}

static int
struct_mp_ass_subscript(PyObject* self, PyObject* item, PyObject* value)
{
	if (PyIndex_Check(item)) {
		Py_ssize_t i = PyNumber_AsSsize_t(item, PyExc_IndexError);
		if (i == -1 && PyErr_Occurred()) {
			return -1;
		} 
		if (i < 0) {
			i += struct_sq_length(self);
		}
		return struct_sq_ass_item(self, i, value);
	} else if (PySlice_Check(item)) {
		Py_ssize_t start, stop, step, slicelength;

		if (PySlice_GetIndicesEx((PySliceObject*)item, 
				struct_sq_length(self), &start, &stop,
				&step, &slicelength) < 0) {
			return -1;
		}
		if (step == 1) {
			return struct_sq_ass_slice(self, start, stop, value);
		}

		if (value == NULL) {
			PyErr_Format(PyExc_TypeError,
				"Cannot delete items in an %s instance",
				Py_TYPE(self)->tp_name);
			return -1;
		}

		PyObject* seq = PySequence_Fast(value, 
				"must assign sequence to slice");
		if (seq == NULL) return -1;

		if (PySequence_Fast_GET_SIZE(seq) != slicelength) {
			Py_DECREF(seq);
			PyErr_Format(PyExc_TypeError,
				"slice assignment would change size of %s "
				"instance", Py_TYPE(self)->tp_name);
			return -1;
		}

		Py_ssize_t cur, i;
		for (cur = start, i = 0; i < slicelength; cur += step, i++) {
			int r = struct_sq_ass_item(self, cur, 
				PySequence_Fast_GET_ITEM(seq, i));
			if (r == -1) {
				Py_DECREF(seq);
				return -1;
			}
		}

		Py_DECREF(seq);
		return 0;
	} else {
		PyErr_Format(PyExc_TypeError,
			"struct indices must be integers, not %.200s",
			Py_TYPE(item)->tp_name);
		return -1;
	}
}


static PySequenceMethods struct_as_sequence = {
	struct_sq_length,	/* sq_length */
	NULL,			/* sq_concat */
	NULL,			/* sq_repeat */
	struct_sq_item,		/* sq_item */
	struct_sq_slice,	/* sq_slice */
	struct_sq_ass_item,	/* sq_ass_item */
	struct_sq_ass_slice,	/* sq_ass_slice */
	struct_sq_contains,	/* sq_contains */
	NULL,			/* sq_inplace_concat */
	NULL			/* sq_inplace_repeat */
};

static PyMappingMethods struct_as_mapping = {
	struct_sq_length,
	struct_mp_subscript,
	struct_mp_ass_subscript,
};

static PyMethodDef struct_methods[] = {
	{
		"__reduce__", 
		(PyCFunction)struct_reduce,
		METH_NOARGS, 
		NULL
	}, 
	{
		"copy",
		(PyCFunction)struct_copy,
		METH_NOARGS,
		"Return a copy of the struct",
	},
	{
		"__pyobjc_copy__",
		(PyCFunction)struct_copy,
		METH_NOARGS,
		NULL,
	},
	{ NULL, NULL, 0, NULL }
};


/*
 * Special methods
 */

static int
struct_setattro(PyObject* self, PyObject* name, PyObject* value)
{
	if (value == NULL) {
		PyErr_Format(PyExc_TypeError, "Cannot delete attributes of %s",
				Py_TYPE(self)->tp_name);
		return -1;
	}
	return PyObject_GenericSetAttr(self, name, value);
}

static void
struct_dealloc(PyObject* self)
{
	PyMemberDef* member = Py_TYPE(self)->tp_members;

	PyObject_GC_UnTrack(self);

	while (member && member->name) {
		Py_XDECREF(*(PyObject**)(((char*)self)+member->offset));
		member++;
	}

	PyObject_GC_Del(self);
}

static PyObject*
struct_new(PyTypeObject* type, PyObject* args, PyObject* kwds)
{
	PyObject* result;
	PyMemberDef* member = type->tp_members;
	int r;

	result = PyObject_GC_New(PyObject, type);
	if (result == NULL) return NULL;

	while (member && member->name) {
		if (member->type != T_OBJECT) {
			member++;
			continue;
		}
		*((PyObject**)(((char*)result) + member->offset)) = NULL;
		member++;
	}
	PyObject_GC_Track(result);

	r = type->tp_init(result, args, kwds);
	if (r == -1) {
		Py_DECREF(result);
		return NULL;
	}
	return result;
}

static int LOCATE_MEMBER(PyTypeObject* type, const char* name)
{
	int i = 0;
	PyMemberDef* member;

	for (i = 0,  member = type->tp_members; 
			member->name != NULL; i++, member++) {
		if (strcmp(member->name, name) == 0) {
			return i;
		}
	}
	return -1;
}

static int set_defaults(PyObject* self, const char* typestr)
{
	Py_ssize_t i = 0;
	int r;
	PyObject* v;

	while(*typestr != _C_STRUCT_E && *typestr++ != '=');
	while(typestr && *typestr != _C_STRUCT_E) {
		const char* next;

		if (*typestr == '"') {
			/* embedded field names */
			typestr = strchr(typestr+1, '"');
			if (typestr) {
				typestr++;
			} else {
				break;
			}
		}
		next = PyObjCRT_SkipTypeSpec(typestr);
		switch (*typestr) {
#ifdef _C_BOOL
		case _C_BOOL: 
			v = PyBool_FromLong(0);
			break;
#endif
		case _C_NSBOOL:
			v = PyBool_FromLong(0);
			break;

		case _C_CHAR_AS_TEXT:
			{
				char ch = 0;
				v = PyText_FromStringAndSize(&ch, 1);
			}
			break;

		case _C_UNICHAR:
			{
				Py_UNICODE ch = 0;
				v = PyUnicode_FromUnicode(&ch, 1);
			}
			break;

		case _C_CHAR_AS_INT:
		case _C_CHR: case _C_UCHR:
		case _C_SHT: case _C_USHT:
		case _C_INT: case _C_UINT:
		case _C_LNG: case _C_ULNG:
		case _C_LNG_LNG: case _C_ULNG_LNG:
			v = PyInt_FromLong(0);
			break;

		case _C_FLT: case _C_DBL:
			v = PyFloat_FromDouble(0.0);
			break;

		case _C_STRUCT_B:
			v = PyObjC_CreateRegisteredStruct(typestr, next-typestr, NULL);
			if (v != NULL) {
				/* call init */
				r = Py_TYPE(v)->tp_init(v, NULL, NULL);
				if (r == -1) {
					Py_DECREF(v);
					return -1;
				}
			} else if (!PyErr_Occurred()) {
				/* this is a struct-type without a struct
				 * wrapper. Default to None
				 */
				v = Py_None;
				Py_INCREF(Py_None);
			}
				

			break;

		default:
			v = Py_None;
			Py_INCREF(Py_None);
		}

		if (v == NULL) {
			return -1;
		}

		r = PySequence_SetItem(self, i++, v);
		Py_DECREF(v);
		if (r != 0) {
			return -1;
		}

		typestr = next;
	}

	return 0;
}


static void
struct_init(
	ffi_cif* cif __attribute__((__unused__)),
	void* retval,
	void** cargs,
	void* userdata
	   ) 
{
	PyObject* self = *(PyObject**)cargs[0];
	PyObject* args = *(PyObject**)cargs[1];
	PyObject* kwds = *(PyObject**)cargs[2];
	const char* typestr = (char*)userdata;
	Py_ssize_t setUntil = -1;
	int r;

	if (self == NULL) {
		*(int**)retval = 0;
		return;
	}

	if (args != NULL && !PyTuple_Check(args)) {
		PyErr_Format(PyExc_TypeError, 
				"%s() argument tuple is not a tuple",
				Py_TYPE(self)->tp_name);
		*(int*)retval = -1;
		return;
	}
	if (kwds != NULL && !PyDict_Check(kwds)) {
		PyErr_Format(PyExc_TypeError, 
				"%s() keyword dict is not a dict",
				Py_TYPE(self)->tp_name);
		*(int*)retval = -1;
		return;
	}

	r = set_defaults(self, typestr);
	if (r != 0) {
		*(int*)retval = r;
		return;
	}

	if (args != NULL) {
		Py_ssize_t i, len;

		len = PyTuple_GET_SIZE(args);
		if (len > struct_sq_length(self)) {
			PyErr_Format(PyExc_TypeError, 
				"%s() takes at most %"PY_FORMAT_SIZE_T"d %sarguments (%"PY_FORMAT_SIZE_T"d given)",
				Py_TYPE(self)->tp_name,
				struct_sq_length(self),
				kwds?"non-keyword ":"", len);
			*(int*)retval = -1;
			return;
		}
		for (i = 0; i < len; i++) {
			PyObject* v = PyTuple_GET_ITEM(args, i);

			SET_FIELD(self, Py_TYPE(self)->tp_members+i, v);
		}
		setUntil = len-1;
	}

	if (kwds != NULL) {
		PyObject* keys;
		int i, len;

		keys = PyDict_Keys(kwds);
		if (keys == NULL) {
			*(int*)retval = -1;
			return;
		}

		if (!PyList_Check(keys)) {
			Py_DECREF(keys);
			PyErr_SetString(PyExc_TypeError, 
					"dict.keys didn't return a list");
			*(int*)retval = -1;
			return;
		}

		len = PyList_GET_SIZE(keys);
		for (i = 0; i < len; i++) {
			PyMemberDef* member;
			Py_ssize_t off;
			PyObject* k;
			PyObject* v;
			PyObject* k_bytes = NULL;

			k = PyList_GET_ITEM(keys, i);
			if (PyUnicode_Check(k)) {
				k_bytes = PyUnicode_AsEncodedString(k, NULL, NULL);
				if (k_bytes == NULL) {
					*(int*)retval = -1;
					return;
				}
#if PY_MAJOR_VERSION == 2
			} else if (PyString_Check(k)) {
				k_bytes = k; Py_INCREF(k_bytes);
#endif
			} else {
				Py_DECREF(keys);
				PyErr_Format(PyExc_TypeError,
					"%s() keywords must be strings",
					Py_TYPE(self)->tp_name);
				*(int*)retval = -1;
				return;
			}


			off = LOCATE_MEMBER(Py_TYPE(self),
					PyBytes_AS_STRING(k_bytes));
			if (off == -1) {
				PyErr_Format(PyExc_TypeError,
					"no keyword argument: %s",
					PyBytes_AS_STRING(k_bytes));
				Py_DECREF(k_bytes);
				Py_DECREF(keys);
				*(int*)retval = -1;
				return;
			}

			if (off <= setUntil) {
				PyErr_Format(PyExc_TypeError,
					"%s() got multiple values for keyword "
					"argument '%s'",
					Py_TYPE(self)->tp_name,
					PyBytes_AS_STRING(k_bytes));
				Py_DECREF(k_bytes);
				Py_DECREF(keys);
				*(int*)retval = -1;
				return;
			}
			Py_DECREF(k_bytes);

			member = Py_TYPE(self)->tp_members + off;
			v = PyDict_GetItem(kwds, k);
			SET_FIELD(self, member, v);
		}
		Py_DECREF(keys);
	}

	*(int*)retval = 0;
	return;
}

static initproc
make_init(const char* typestr)
{
static 	ffi_cif* init_cif = NULL;
	ffi_closure* cl = NULL;
	ffi_status rv;

	if (init_cif == NULL) {
		PyObjCMethodSignature* signature;
		signature = PyObjCMethodSignature_FromSignature("i^v^v^v", YES);
		init_cif = PyObjCFFI_CIFForSignature(signature);
		Py_DECREF(signature);
		if (init_cif == NULL) {
			return NULL;
		}
	}

	cl = PyObjC_malloc_closure();
	if (cl == NULL) {
		return NULL;
	}

	rv = ffi_prep_closure(cl, init_cif, struct_init, (char*)typestr);
	if (rv != FFI_OK) {
		PyObjC_free_closure(cl);
		PyErr_Format(PyExc_RuntimeError,
			"Cannot create FFI closure: %d", rv);
		return NULL;
	}

	return (initproc)cl;
}



static long
struct_hash(PyObject* self)
{
	PyErr_Format(PyExc_TypeError, "%s objects are unhashable",
			Py_TYPE(self)->tp_name);
	return -1;
}

static PyObject*
struct_richcompare(PyObject* self, PyObject* other, int op)
{
	Py_ssize_t self_len, other_len, i, len;
	int cmp;
	PyObject* self_cur;
	PyObject* other_cur;

	if (!PySequence_Check(other)) {
		if (op == Py_EQ) {
			Py_INCREF(Py_False);
			return Py_False;
		} else if (op == Py_NE) {
			Py_INCREF(Py_True);
			return Py_True;
		} else {
			PyErr_Format(PyExc_TypeError,
				"Cannot compare instances of %s and %s",
				Py_TYPE(self)->tp_name,
				Py_TYPE(other)->tp_name);
			return NULL;
		}
	}

	self_len = struct_sq_length(self);
	other_len = PySequence_Length(other);
	len = self_len;
	if (other_len < len) {
		len = other_len;
	}

	if (self_len != other_len && (op == Py_EQ || op == Py_NE)){
		/* Shortcut comparison for non-equals lengths */
		if (op == Py_EQ) {
			Py_INCREF(Py_False);
			return Py_False;
		} else {
			Py_INCREF(Py_True);
			return Py_True;
		}
	}

	for (i = 0; i < len; i ++) {
		int k;

		self_cur = GET_FIELD(self, Py_TYPE(self)->tp_members+i);
		other_cur = PySequence_GetItem(other, i);
		if (other_cur == NULL) return NULL;

		k = PyObject_RichCompareBool(self_cur, other_cur, Py_EQ);
		if (k < 0) {
			Py_DECREF(other_cur);
			return NULL;
		}

		if (!k) {
			/* Not equal, result is the comparison of the last
			 * item, we can do better for '==' and '!='.
			 */
			PyObject* v;

			if (op == Py_EQ) {
				Py_INCREF(Py_False);
				return Py_False;
			} else if (op == Py_NE) {
				Py_INCREF(Py_True);
				return Py_True;
			}
			v = PyObject_RichCompare(self_cur, other_cur, op);
			Py_DECREF(other_cur);
			return v;
		}
		Py_DECREF(other_cur);
	}

	/* All items are equal, compare using sizes */
	switch (op) {
	case Py_LT: cmp = self_len < other_len; break;
	case Py_LE: cmp = self_len <= other_len; break;
	case Py_EQ: cmp = self_len == other_len; break;
	case Py_NE: cmp = self_len != other_len; break;
	case Py_GE: cmp = self_len >= other_len; break;
	case Py_GT: cmp = self_len > other_len; break;
	default: 
		    /* Should never happen */
		    PyErr_SetString(PyExc_TypeError, "Invalid comparion");
		    return NULL;
	}
	if (cmp) {
		Py_INCREF(Py_True);
		return Py_True;
	} else {
		Py_INCREF(Py_False);
		return Py_False;
	}
}

static int
struct_traverse(PyObject* self, visitproc visit, void* arg)
{
	PyMemberDef* member;
	PyObject* v;
	int err;

	for (member = Py_TYPE(self)->tp_members; 
				member && member->name; member++) {
		v = GET_FIELD(self, member);
		if (v == NULL) continue;
		err = visit(v, arg);
		if (err) return err;
	}
	return 0;
}

static int
struct_clear(PyObject* self)
{
	PyMemberDef* member;

	for (member = Py_TYPE(self)->tp_members; 
				member && member->name; member++) {
		SET_FIELD(self, member, NULL);
	}
	return 0;
}



static PyObject*
struct_repr(PyObject* self)
{
	Py_ssize_t i, len;
	PyObject* cur;
	PyMemberDef* member;

	len = struct_sq_length(self);
	if (len == 0) {
		return PyText_FromFormat("<%s>",
				Py_TYPE(self)->tp_name);
	}

	i = Py_ReprEnter(self);
	if (i < 0) {
		return NULL;
	} else if (i != 0) {
		/* Self-recursive struct */
		return PyText_FromFormat("<%s ...>",
				Py_TYPE(self)->tp_name);
	}

	cur = PyText_FromFormat("<%s", Py_TYPE(self)->tp_name);

	member = Py_TYPE(self)->tp_members;
	while (member->name != NULL) {
		PyObject* v;

		PyText_Append(&cur, 
			PyText_FromFormat(" %s=", member->name));
		if (cur == NULL) goto done;

		v = GET_FIELD(self, member);

		PyText_Append(&cur, PyObject_Repr(v));
		if (cur == NULL) goto done;
		member++;
	}

	PyText_Append(&cur, PyText_FromString(">"));

done:
	Py_ReprLeave(self);
	return cur;
}


/*
 * A template for the type object
 */
static PyTypeObject StructTemplate_Type = {
	PyVarObject_HEAD_INIT(NULL, 0)
	"objc.StructTemplate",			/* tp_name */
	sizeof (PyObject*),			/* tp_basicsize */
	0,					/* tp_itemsize */
  
	/* methods */
	struct_dealloc,				/* tp_dealloc */
	0,					/* tp_print */
	0,					/* tp_getattr */
	0,					/* tp_setattr */
	0,					/* tp_compare */
	struct_repr,				/* tp_repr */
	0,					/* tp_as_number */
	&struct_as_sequence,			/* tp_as_sequence */
	&struct_as_mapping,			/* tp_as_mapping */
	struct_hash,				/* tp_hash */
	0,					/* tp_call */
	0,					/* tp_str */
	PyObject_GenericGetAttr,		/* tp_getattro */
	struct_setattro,			/* tp_setattro */
	0,					/* tp_as_buffer */
	Py_TPFLAGS_DEFAULT 
#if PY_MAJOR_VERSION == 2
		| Py_TPFLAGS_HAVE_RICHCOMPARE 
#endif
		| Py_TPFLAGS_HAVE_GC, 		/* tp_flags */
	0,					/* tp_doc */
	struct_traverse,			/* tp_traverse */
	struct_clear,				/* tp_clear */
	struct_richcompare,			/* tp_richcompare */
	0,					/* tp_weaklistoffset */
	0,					/* tp_iter */
	0,					/* tp_iternext */
	struct_methods,				/* tp_methods */
	0,					/* tp_members */
	0,					/* tp_getset */
	0,					/* tp_base */
	0,					/* tp_dict */
	0,					/* tp_descr_get */
	0,					/* tp_descr_set */
	0,					/* tp_dictoffset */
	0,					/* tp_init */
	0,					/* tp_alloc */
	struct_new,				/* tp_new */
	0,					/* tp_free */
	0,					/* tp_is_gc */
	0,					/* tp_bases */
	0,					/* tp_mro */
	0,					/* tp_cache */
	0,					/* tp_subclasses */
	0,					/* tp_weaklist */
	0					/* tp_del */
#if PY_VERSION_HEX >= 0x02060000
	, 0                                     /* tp_version_tag */
#endif

};

PyObject* 
PyObjC_MakeStructType(
		const char* name,
		const char* doc,
		initproc tpinit,
		Py_ssize_t numFields,
		const char** fieldnames,
		const char* typestr)
{
	PyTypeObject* result;
	PyMemberDef* members;
	Py_ssize_t i;

	members = PyMem_Malloc(sizeof(PyMemberDef) * (numFields+1));
	if (members == NULL) {
		PyErr_NoMemory();
		return NULL;
	}
	for (i = 0; i < numFields; i++) {
		members[i].name = (char*)fieldnames[i];
		members[i].type = T_OBJECT;
		members[i].offset = sizeof(PyObject) + i*sizeof(PyObject*);
		members[i].flags = 0; /* A read-write field */
		members[i].doc = NULL;
	}
	members[numFields].name = NULL;

	result = PyMem_Malloc(sizeof(PyTypeObject));
	if (result == NULL) {
		PyMem_Free(members);
		PyErr_NoMemory();
		return NULL;
	}

	*result = StructTemplate_Type;
	result->tp_name = (char*)name;
	result->tp_doc = (char*)doc;
	result->tp_dict = PyDict_New();
	if (result->tp_dict == NULL) {
		PyMem_Free(members);
		PyMem_Free(result);
		return NULL;
	}
	Py_REFCNT(result) = 1;
	result->tp_members = members;
	result->tp_basicsize = sizeof(PyObject) + numFields*sizeof(PyObject*);
	if (tpinit) {
		result->tp_init = tpinit;
	} else {
		result->tp_init = make_init(typestr);
		if (result->tp_init == NULL) {
			PyMem_Free(members);
			PyMem_Free(result);
			return NULL;
		}
	}

	if (PyType_Ready(result) == -1) {
		/* Is freeing save? */
		PyMem_Free(result);
		PyMem_Free(members);
		return NULL;
	}
	return (PyObject*)result;
}

/*
 * This is the start of PyObjC specific code
 */

static PyObject* structRegistry = NULL;

PyObject* 
PyObjC_CreateRegisteredStruct(const char* signature, Py_ssize_t len, const char** objc_encoding)
{
	PyTypeObject* type;
	PyObject* result;
	PyObject* v;
	PyMemberDef* member;

	if (structRegistry == NULL) return NULL;

	v = PyText_FromStringAndSize(signature, len);
	type = (PyTypeObject*)PyDict_GetItem(structRegistry, v);
	Py_DECREF(v);
	if (type == NULL) {
		PyErr_Clear();
		return NULL;
	}

	member = type->tp_members;

	result = PyObject_GC_New(PyObject, type);
	if (result == NULL) {
		PyErr_Clear();
		return NULL;
	}

	while (member && member->name) {
		if (member->type != T_OBJECT) {
			member++;
			continue;
		}
		*((PyObject**)(((char*)result) + member->offset)) = NULL;
		member++;
	}

	PyObject_GC_Track(result);

	if (objc_encoding) {
		PyObject* typestr = PyDict_GetItemString(type->tp_dict, "__typestr__");
		if (typestr != NULL) {
			*objc_encoding = PyBytes_AsString(typestr);
		} else {
			*objc_encoding = signature;
		}
	}
	return result;
}


PyObject* 
PyObjC_RegisterStructType(
		const char* signature,
		const char* name,
		const char* doc,
		initproc tpinit,
		Py_ssize_t numFields,
		const char** fieldnames)
{
	PyObject* structType;
	PyObject* v;
	int r;
	int freeNames = 0;

	if (numFields == -1) {
		/* XXX: extract me into a seperate function, 
		 * and improve error checking/recovery.
		 */
		/* Don't use fieldnames, but extract the names
		 * from the type signature.
		 */
		const char* sigcur = signature;
		const char* fieldstart;

		if (*sigcur != _C_STRUCT_B) {
			PyErr_SetString(PyExc_ValueError, "invalid signature");
			return NULL;
		}


		while (*sigcur && *sigcur != _C_STRUCT_E && *sigcur != '=') sigcur++;

		if (!*sigcur || *sigcur == _C_STRUCT_E) {
			PyErr_SetString(PyExc_ValueError, "invalid signature");
			return NULL;
		}

		fieldstart = ++sigcur;
		numFields = 0;

		while (*sigcur != _C_STRUCT_E) {
			numFields ++;
			if (*sigcur == '"') {
				sigcur++;
				sigcur = strchr(sigcur, '"');
				if (sigcur == NULL) {
					PyErr_SetString(PyExc_ValueError, "invalid signature");
					return NULL;
				}
				sigcur++;
			} else {
				PyErr_SetString(PyExc_ValueError, "invalid signature");
				return NULL;
			}
			if (*sigcur == _C_STRUCT_E) break;
			sigcur = PyObjCRT_NextField(sigcur);
			if (sigcur == NULL) {
				return NULL;
			}
		}

		fieldnames = PyMem_Malloc((numFields + 1) * sizeof(char*));
		numFields = 0;

		sigcur = fieldstart;
		while (*sigcur != _C_STRUCT_E) {
			if (*sigcur == '"') {
				char* end;
				sigcur++;
				end = strchr(sigcur, '"');

				if (end == NULL) {
					PyErr_SetString(PyExc_ValueError, "invalid signature");
					return NULL;
				}
				fieldnames[numFields] = PyMem_Malloc(end - sigcur + 1);
				memcpy((char*)fieldnames[numFields], sigcur, end-sigcur);
				((char*)fieldnames[numFields])[end-sigcur] = '\0';
				sigcur = end + 1;
			}
			numFields ++;
			sigcur = PyObjCRT_NextField(sigcur);
		}
		fieldnames[numFields] = NULL;
		freeNames = 1;

		/* 
		 * The signature string still contains embedded field names,
		 * remove those.
		 */
		char* sigtmp = PyMem_Malloc(strlen(signature)+20);
		if (sigtmp == NULL) {
			PyErr_NoMemory();
			return NULL;
		}
		if (PyObjCRT_RemoveFieldNames(sigtmp, signature) == NULL) {
			PyMem_Free(sigtmp);
			return NULL;
		}
		signature = sigtmp;
	}


	structType = PyObjC_MakeStructType(name, doc, tpinit, 
				numFields, fieldnames, signature);
	if (structType == NULL) {
		if (freeNames) {
			int i;
			PyMem_Free((char*)signature);
			for (i = 0; i < numFields; i++) {
				PyMem_Free((char*)fieldnames[i]);
			}
			PyMem_Free(fieldnames);
		}
		return NULL;
	}

	v = PyBytes_FromString(signature);
	if (v == NULL) {
		Py_DECREF(structType);
		return NULL;
	}

	r = PyDict_SetItemString(((PyTypeObject*)structType)->tp_dict, "__typestr__", v);
	Py_DECREF(v);
	if (r == -1) {
		Py_DECREF(structType);
		return NULL;
	}

	if (structRegistry == NULL) {
		structRegistry = PyDict_New();
		if (structRegistry == NULL) {
			/* This leaks some memory, but we cannot safely
			 * deallocate the type
			 */
			return NULL;
		}
	}

	r = PyDict_SetItemString(structRegistry, signature, structType);
	if (r == -1) {
		/* This leaks some memory, but we cannot safely
		 * deallocate the type
		 */
		return NULL;
	}

	/* Register again using the typecode used in the ObjC runtime */
	PyObjC_RemoveInternalTypeCodes((char*)signature);
	r = PyDict_SetItemString(structRegistry, signature, structType);
	if (r == -1) {
		return NULL;
	}

	return structType;
}

int 
PyObjC_RegisterStructAlias(const char* signature, PyObject* structType)
{
	char buf[1024];
	int r;

	if (strlen(signature) > 1023) {
		PyErr_SetString(PyExc_ValueError, "typestr too long");
		return -1;
	}
	if (PyObjCRT_RemoveFieldNames(buf, signature) == NULL) {
		return -1;
	}

	if (structRegistry == NULL) {
		structRegistry = PyDict_New();
		if (structRegistry == NULL) {
			return -1;
		}
	}

	r = PyDict_SetItemString(structRegistry, buf, structType);
	if (r == -1) {
		return -1;
	}

	/* Register again using the typecode used in the ObjC runtime */
	PyObjC_RemoveInternalTypeCodes(buf);
	r = PyDict_SetItemString(structRegistry, buf, structType);
	if (r == -1) {
		return -1;
	}

	return 0;
}
