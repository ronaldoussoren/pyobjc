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
 * TODO:
 * - Extended slice interface
 * - Add more unittests 
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
	Py_XINCREF(val);
	Py_XDECREF((PyObject*)(((char*)self) + member->offset));
	*((PyObject**)(((char*)self) + member->offset)) = val;
}

/*
 * Implementation of the sequence interface.
 */

static int
struct_sq_length(PyObject* self)
{
	/* The object contains the generic PyObject header followed by an
	 * array of PyObject*-s.
	 */
	return (self->ob_type->tp_basicsize - sizeof(PyObject)) / sizeof(PyObject*);
}

static PyObject*
struct_sq_item(PyObject* self, int offset)
{
	int len = struct_sq_length(self);
	PyMemberDef* member;
	PyObject* res;

	if (offset < 0 || offset >= len) {
		PyErr_Format(PyExc_IndexError,  
				"%s index out of range",
				self->ob_type->tp_name);
		return NULL;
	} 

	member = self->ob_type->tp_members + offset;
	res = GET_FIELD(self, member);

	Py_INCREF(res);
	return res;
}

static PyObject*
struct_sq_slice(PyObject* self, int ilow, int ihigh)
{
	PyObject* result;
	int i, len;
	
	len = struct_sq_length(self);
	if (ilow < 0)  ilow = 0;
	if (ihigh > len) ihigh = len;

	result = PyTuple_New(ihigh - ilow);
	if (result == NULL) {
		return NULL;
	}

	for (i = ilow; i < ihigh; i++) {
		PyMemberDef* member = self->ob_type->tp_members + i;
		PyObject* v = GET_FIELD(self, member);
		Py_INCREF(v);
		PyTuple_SET_ITEM(result, i-ilow, v);
	}
	return result;
}

static int
struct_sq_ass_item(PyObject* self, int offset, PyObject* newVal)
{
	int len;
	PyMemberDef* member;

	if (newVal == NULL) {
		PyErr_Format(PyExc_TypeError, 
			"Cannot delete item '%d' in a %s instance",
			offset, self->ob_type->tp_name);
		return -1;
	}

	len = struct_sq_length(self);

	if ((offset < 0) || (offset >= len)) {
		PyErr_Format(PyExc_IndexError,  
				"%s index out of range",
				self->ob_type->tp_name);
		return -1;
	}
	member = self->ob_type->tp_members + offset;
	SET_FIELD(self, member, newVal);
	return 0;
}

static int
struct_sq_ass_slice(PyObject* self, int ilow, int ihigh, PyObject* v)
{
	PyObject* seq;
	int i, len;

	if (v == NULL) {
		PyErr_Format(PyExc_TypeError,
			"Cannot delete items in an %s instance",
			self->ob_type->tp_name);
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
	if (seq == NULL) return NULL;

	if (PySequence_Fast_GET_SIZE(seq) != ihigh - ilow) {
		Py_DECREF(seq);
		PyErr_Format(PyExc_TypeError,
			"slice assignment would change size of %s "
			"instance", self->ob_type->tp_name);
		return -1;
	}

	for (i = ilow; i < ihigh; i++) {
		PyObject* x;
		PyMemberDef* member = self->ob_type->tp_members + i;

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
	PyMemberDef* member = self->ob_type->tp_members;

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
	int i, len;

	len = struct_sq_length(self);
	values = PyTuple_New(len);
	if (values == NULL) return NULL;

	for (i = 0; i < len; i++) {
		PyObject* v = GET_FIELD(self, self->ob_type->tp_members + i);
		Py_INCREF(v);
		PyTuple_SET_ITEM(values, i, v);
	}

	result = Py_BuildValue("(OO)", self->ob_type, values);
	Py_DECREF(values);
	return result;
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

static PyMethodDef struct_methods[] = {
	{
		"__reduce__", 
		(PyCFunction)struct_reduce,
		METH_NOARGS, 
		NULL
	}, 
	{ NULL, NULL, NULL, NULL }
};


/*
 * Special methods
 */

static int
struct_setattro(PyObject* self, PyObject* name, PyObject* value)
{
	if (value == NULL) {
		PyErr_Format(PyExc_TypeError, "Cannot delete attributes of %s",
				self->ob_type->tp_name);
		return -1;
	}
	return PyObject_GenericSetAttr(self, name, value);
}

static void
struct_dealloc(PyObject* self)
{
	PyMemberDef* member = self->ob_type->tp_members;

	while (member && member->name) {
		Py_XDECREF(*(PyObject**)(((char*)self)+member->offset));
		member++;
	}

	PyObject_Free(self);
}

static PyObject*
struct_new(PyTypeObject* type, PyObject* args, PyObject* kwds)
{
	PyObject* result;
	PyMemberDef* member = type->tp_members;
	int r;

	result = PyObject_New(PyObject, type);
	if (result == NULL) return NULL;

	while (member && member->name) {
		if (member->type != T_OBJECT) {
			member++;
			continue;
		}
		*((PyObject**)(((char*)result) + member->offset)) = NULL;
		member++;
	}

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


static int
struct_init(PyObject* self, PyObject* args, PyObject* kwds)
{
	int setUntil = -1;

	if (args != NULL && !PyTuple_Check(args)) {
		PyErr_Format(PyExc_TypeError, 
				"%s() argument tuple is not a tuple",
				self->ob_type->tp_name);
		return -1;
	}
	if (kwds != NULL && !PyDict_Check(kwds)) {
		PyErr_Format(PyExc_TypeError, 
				"%s() keyword dict is not a dict",
				self->ob_type->tp_name);
		return -1;
	}

	if (args != NULL) {
		int i, len;

		len = PyTuple_GET_SIZE(args);
		if (len > struct_sq_length(self)) {
			PyErr_Format(PyExc_TypeError, 
				"%s() takes at most %d %sarguments (%d given)",
				self->ob_type->tp_name,
				struct_sq_length(self),
				kwds?"non-keyword ":"", len);
			return -1;
		}
		for (i = 0; i < len; i++) {
			PyObject* v = PyTuple_GET_ITEM(args, i);

			SET_FIELD(self, self->ob_type->tp_members+i, v);
		}
		setUntil = len-1;
	}

	if (kwds != NULL) {
		PyObject* keys;
		int i, len;

		keys = PyDict_Keys(kwds);
		if (keys == NULL) {
			Py_DECREF(keys);
		}

		if (!PyList_Check(keys)) {
			Py_DECREF(keys);
			PyErr_SetString(PyExc_TypeError, 
					"dict.keys didn't return a list");
			return -1;
		}

		len = PyList_GET_SIZE(keys);
		for (i = 0; i < len; i++) {
			PyMemberDef* member;
			int off;
			PyObject* k;
			PyObject* v;

			k = PyList_GET_ITEM(keys, i);
			if (!PyString_Check(k)) {
				Py_DECREF(keys);
				PyErr_Format(PyExc_TypeError,
					"%s() keywords must be strings",
					self->ob_type->tp_name);
				return -1;
			}

			off = LOCATE_MEMBER(self->ob_type, 
					PyString_AS_STRING(k));
			if (off == -1) {
				PyErr_Format(PyExc_TypeError,
					"no keyword argument: %s",
					PyString_AS_STRING(k));
				Py_DECREF(keys);
				return -1;
			}

			if (off <= setUntil) {
				PyErr_Format(PyExc_TypeError,
					"%s() got multiple values for keyword "
					"argument '%s'",
					self->ob_type->tp_name,
					PyString_AS_STRING(k));
				Py_DECREF(keys);
				return -1;
			}

			member = self->ob_type->tp_members + off;
			v = PyDict_GetItem(kwds, k);
			SET_FIELD(self, member, v);
		}
		Py_DECREF(keys);
	}

	return 0;
}

static long
struct_hash(PyObject* self)
{
	PyErr_Format(PyExc_TypeError, "%s objects are unhashable",
			self->ob_type->tp_name);
	return -1;
}

static PyObject*
struct_richcompare(PyObject* self, PyObject* other, int op)
{
	int self_len, other_len, i, len;
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
				self->ob_type->tp_name,
				other->ob_type->tp_name);
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

		self_cur = GET_FIELD(self, self->ob_type->tp_members+i);
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
	int cmp;

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

	for (member = self->ob_type->tp_members; 
				member && member->name; member++) {
		v = GET_FIELD(self, member);
		err = visit(v, arg);
		if (err) return err;
	}
	return 0;
}

static int
struct_clear(PyObject* self)
{
	PyMemberDef* member;

	for (member = self->ob_type->tp_members; 
				member && member->name; member++) {
		SET_FIELD(self, member, NULL);
	}
	return 0;
}


static PyObject*
struct_repr(PyObject* self)
{
	char buffer[128];
	int i, len;
	PyObject* cur;
	PyMemberDef* member;

	len = struct_sq_length(self);
	if (len == 0) {
		snprintf(buffer, sizeof(buffer), "<%s>", 
				self->ob_type->tp_name);
		return PyString_FromString(buffer);
	}

	i = Py_ReprEnter(self);
	if (i < 0) return NULL;
	if (i != 0) {
		/* Self-recursive struct */
		snprintf(buffer, sizeof(buffer), "<%s ...>", 
				self->ob_type->tp_name);
		return PyString_FromString(buffer);
	}

	snprintf(buffer, sizeof(buffer), "<%s", self->ob_type->tp_name);
	cur = PyString_FromString(buffer);

	member = self->ob_type->tp_members;
	while (member->name != NULL) {
		PyObject* v;

		snprintf(buffer, sizeof(buffer), " %s=", member->name);
		PyString_ConcatAndDel(&cur, PyString_FromString(buffer));
		if (cur == NULL) goto done;

		v = GET_FIELD(self, member);

		PyString_ConcatAndDel(&cur, PyObject_Repr(v));
		if (cur == NULL) goto done;
		member++;
	}

	PyString_ConcatAndDel(&cur, PyString_FromString(">"));

done:
	Py_ReprLeave(self);
	return cur;
}


/*
 * A template for the type object
 */
static PyTypeObject StructTemplate_Type = {
	PyObject_HEAD_INIT(NULL)
	0,					/* ob_size */
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
	0,					/* tp_as_mapping */
	struct_hash,				/* tp_hash */
	0,					/* tp_call */
	0,					/* tp_str */
	PyObject_GenericGetAttr,		/* tp_getattro */
	struct_setattro,			/* tp_setattro */
	0,					/* tp_as_buffer */
	Py_TPFLAGS_DEFAULT 
		| Py_TPFLAGS_HAVE_RICHCOMPARE 
		/*| Py_TPFLAGS_HAVE_GC*/, 		/* tp_flags */
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
	struct_init,				/* tp_init */
	0,					/* tp_alloc */
	struct_new,				/* tp_new */
	0,					/* tp_free */
	0,					/* tp_is_gc */
	0,					/* tp_bases */
	0,					/* tp_mro */
	0,					/* tp_cache */
	0,					/* tp_subclasses */
	0					/* tp_weaklist */
#if PY_VERSION_HEX >= 0x020300A2
	, 0,					/* tp_del */
#endif
};

PyObject* 
PyObjC_MakeStructType(
		const char* name,
		const char* doc,
		initproc tpinit,
		int numFields,
		const char** fieldnames)
{
	PyTypeObject* result;
	PyMemberDef* members;
	int i;

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
	result->ob_refcnt = 1;
	result->tp_members = members;
	result->tp_basicsize = sizeof(PyObject) + numFields*sizeof(PyObject*);
	if (tpinit) {
		result->tp_init = tpinit;
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
PyObjC_CreateRegisteredStruct(const char* signature, int len)
{
	PyTypeObject* type;
	PyObject* result;
	PyObject* v;
	PyMemberDef* member;

	if (structRegistry == NULL) return NULL;

	v = PyString_FromStringAndSize(signature, len);
	type = (PyTypeObject*)PyDict_GetItem(structRegistry, v);
	Py_DECREF(v);
	if (type == NULL) {
		PyErr_Clear();
		return NULL;
	}

	member = type->tp_members;

	result = PyObject_New(PyObject, type);
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
	return result;
}


PyObject* 
PyObjC_RegisterStructType(
		const char* signature,
		const char* name,
		const char* doc,
		initproc tpinit,
		int numFields,
		const char** fieldnames)
{
	PyObject* structType;
	int r;
	
	structType = PyObjC_MakeStructType(name, doc, tpinit, 
						numFields, fieldnames);
	if (structType == NULL) {
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

	return structType;
}
