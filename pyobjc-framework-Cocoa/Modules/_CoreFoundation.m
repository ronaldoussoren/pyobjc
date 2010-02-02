#include <Python.h>
#include "pyobjc-api.h"

#import <CoreFoundation/CoreFoundation.h>

/* We include the source code here instead of 
 * using the linker due to limitations in pyobjc-api.h
 */
#include "_CoreFoundation_CFBag.m"
#include "_CoreFoundation_CFBinaryHeap.m"
#include "_CoreFoundation_CFBitVector.m"
#include "_CoreFoundation_CFCalendar.m"
#include "_CoreFoundation_CFDictionary.m"
#include "_CoreFoundation_CFFileDescriptor.m"
#include "_CoreFoundation_CFMachPort.m"
#include "_CoreFoundation_CFMessagePort.m"
#include "_CoreFoundation_CFNumber.m"
#include "_CoreFoundation_CFReadStream.m"
#include "_CoreFoundation_CFRunLoopObserver.m"
#include "_CoreFoundation_CFRunLoopSource.m"
#include "_CoreFoundation_CFRunLoopTimer.m"
#include "_CoreFoundation_CFSet.m"
#include "_CoreFoundation_CFSocket.m"
#include "_CoreFoundation_CFTree.m"
#include "_CoreFoundation_CFWriteStream.m"


static PyMethodDef mod_methods[] = {
	COREFOUNDATION_CFBAG_METHODS
	COREFOUNDATION_CFBINARYHEAP_METHODS
	COREFOUNDATION_BITVECTOR_METHODS
	COREFOUNDATION_CALENDAR_METHODS
	COREFOUNDATION_DICTIONARY_METHODS
#if MAC_OS_X_VERSION_10_5 <= MAC_OS_X_VERSION_MAX_ALLOWED
	COREFOUNDATION_FILEDESCRIPTOR_METHODS
#endif
	COREFOUNDATION_MACHPORT_METHODS
	COREFOUNDATION_MESSAGEPORT_METHODS
	COREFOUNDATION_NUMBER_METHODS
	COREFOUNDATION_READSTREAM_METHODS
	COREFOUNDATION_RUNLOOP_METHODS
	COREFOUNDATION_RUNLOOPSOURCE_METHODS
	COREFOUNDATION_RUNLOOPTIMER_METHODS
	COREFOUNDATION_SET_METHODS
	COREFOUNDATION_SOCKET_METHODS
	COREFOUNDATION_TREE_METHODS
	COREFOUNDATION_WRITESTREAM_METHODS

	{ 0, 0, 0, 0 } /* sentinel */
};


/* Python glue */
#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
        PyModuleDef_HEAD_INIT,
	"_CoreFoundation",
	NULL,
	0,
	mod_methods,
	NULL,
	NULL,
	NULL,
	NULL
};

#define INITERROR() return NULL
#define INITDONE() return m

PyObject* PyInit__CoreFoundation(void);

PyObject*
PyInit__CoreFoundation(void)

#else

#define INITERROR() return
#define INITDONE() return

void init_CoreFoundation(void);

void
init_CoreFoundation(void)
#endif
{
	PyObject* m;
#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("_CoreFoundation", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) { 
		INITERROR();
	}

	if (PyObjC_ImportAPI(m) == -1) INITERROR();

	INITDONE();
}
