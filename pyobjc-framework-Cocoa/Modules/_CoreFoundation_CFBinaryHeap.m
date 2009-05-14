/*
 * Manual wrappers for CFBinaryHeap
 */
#include <Python.h>
#include "pyobjc-api.h"

#import <CoreFoundation/CoreFoundation.h>
#import <Foundation/Foundation.h>

@interface NSObject (OC_Comparison)
-(NSComparisonResult)compare:(NSObject*)other;
@end


static const void *mod_retain (CFAllocatorRef allocator __attribute__((__unused__)), const void *ptr)
{
	if (ptr) {
		CFRetain(ptr);
	}
	return ptr;
}

static void mod_release (CFAllocatorRef allocator __attribute__((__unused__)), const void *ptr)
{
	if (ptr) {
		CFRelease(ptr);
	}
}

static CFStringRef mod_copydescription(const void* ptr)
{
	return CFCopyDescription(ptr);	
}

CFComparisonResult mod_compare(const void *ptr1, const void *ptr2, void *info __attribute__((__unused__)))
{
	NSObject* o1 = (NSObject*)ptr1;
	NSObject* o2 = (NSObject*)ptr2;

	NSComparisonResult result = [o1 compare:o2];
	return (CFComparisonResult)result;
}


static CFBinaryHeapCallBacks mod_NSObjectBinaryHeapCallbacks = {
	0, 
	mod_retain,
	mod_release,
	mod_copydescription,
	mod_compare
};


static PyObject* 
mod_CFBinaryHeapCreate(PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_allocator;
	Py_ssize_t count;
	CFAllocatorRef allocator;
	CFBinaryHeapRef heap;


	if (!PyArg_ParseTuple(args, "O" Py_ARG_SIZE_T, &py_allocator, &count)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), py_allocator, &allocator) < 0) {
		return NULL;
	}

	heap = CFBinaryHeapCreate(allocator, count, &mod_NSObjectBinaryHeapCallbacks, NULL);

	PyObject* result = PyObjC_ObjCToPython(@encode(CFBinaryHeapRef), &heap);
	if (heap) {
		CFRelease(heap);
	}
	return result;
}


static PyObject*
mod_CFBinaryHeapGetValues(
	PyObject* self __attribute__((__unused__)), 
	PyObject* args)
{
	PyObject* py_heap;
	CFBinaryHeapRef heap;


	if (!PyArg_ParseTuple(args, "O", &py_heap)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFBinaryHeapRef), py_heap, &heap) < 0) {
		return NULL;
	}

	CFIndex count = CFBinaryHeapGetCount(heap);
	NSObject** members = malloc(sizeof(NSObject*) * count);
	if (members == NULL) {
		PyErr_NoMemory();
		return NULL;
	}
	memset(members, 0, sizeof(NSObject*) * count);

	CFBinaryHeapGetValues(heap, (const void**)members);
	PyObject* result = PyObjC_CArrayToPython(@encode(NSObject*), members, (Py_ssize_t)count);
	free(members);
	return result;
}


static PyMethodDef mod_methods[] = {
        {
		"CFBinaryHeapCreate",
		(PyCFunction)mod_CFBinaryHeapCreate,
		METH_VARARGS,
		NULL
	},
        {
		"CFBinaryHeapGetValues",
		(PyCFunction)mod_CFBinaryHeapGetValues,
		METH_VARARGS,
		NULL
	},
	{ 0, 0, 0, 0 } /* sentinel */
};

void init_CFBinaryHeap(void);
void init_CFBinaryHeap(void)
{
	PyObject* m = Py_InitModule4("_CFBinaryHeap", mod_methods, "", NULL,
		PYTHON_API_VERSION);

	PyObjC_ImportAPI(m);
}
