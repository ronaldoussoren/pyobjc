// LCOV_EXCL_START
// This function is only present to ensure protocols are
// available at runtime.

#import <SyncServices/ISyncConflictPropertyType.h>

static void __attribute__((__used__))
use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
    p = PyObjC_IdToPython(@protocol(ISyncFiltering));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(ISyncSessionDriverDataSource));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSPersistentStoreCoordinatorSyncing));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(ISyncConflictPropertyType));
    Py_XDECREF(p);
}

// LCOV_EXCL_STOP
