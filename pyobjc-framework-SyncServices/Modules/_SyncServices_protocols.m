/*
 * This file is generated by objective.metadata
 *
 * Last update: Wed Jan 16 13:12:13 2013
 */

#if PyObjC_BUILD_RELEASE >= 1007
#import <SyncServices/ISyncConflictPropertyType.h>
#endif

static void __attribute__((__used__)) use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
    p = PyObjC_IdToPython(@protocol(ISyncFiltering));
    Py_XDECREF(p);
#if PyObjC_BUILD_RELEASE >= 1005
    p = PyObjC_IdToPython(@protocol(ISyncSessionDriverDataSource));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSPersistentStoreCoordinatorSyncing));
    Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 1005 */
#if PyObjC_BUILD_RELEASE >= 1007
    p = PyObjC_IdToPython(@protocol(ISyncConflictPropertyType));
    Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 1007 */
}
