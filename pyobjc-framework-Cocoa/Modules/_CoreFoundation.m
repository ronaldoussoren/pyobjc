#define PY_SSIZE_T_CLEAN
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

PyObjC_MODULE_INIT(_CoreFoundation)
{
	PyObject* m;
	m = PyObjC_MODULE_CREATE(_CoreFoundation)
	if (!m) { 
		PyObjC_INITERROR();
	}

	/* Some C functions aren't available at runtime (e.g. when compiling on
	 * OS X 10.5 but running on 10.4), so we use "#pragma weak" to weakly
	 * link the functions, then we remove the corresponding Python wrappers
	 * at runtime when we detect that the underlying C functions aren't
	 * available.  It's a bit gross, but it's probably worse to try to
	 * mimic Py_InitModule*, which is "a bit of a hack" according to its
	 * source code.
	 */
	COREFOUNDATION_FILEDESCRIPTOR_AFTER_CREATE

	if (PyObjC_ImportAPI(m) == -1) PyObjC_INITERROR();

	PyObjC_INITDONE();
}
