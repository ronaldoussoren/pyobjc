#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
#import <CoreData/CoreData.h>

/* We include the source code here instead of
 * using the linker due to limitations in pyobjc-api.h
 */
#include "_CoreData_protocols.m"


static PyMethodDef mod_methods[] = {
    { 0, 0, 0, 0 } /* sentinel */
};


/* Python glue */
PyObjC_MODULE_INIT(_CoreData)
{
    PyObject* m;
    m = PyObjC_MODULE_CREATE(_CoreData)
    if (!m) {
        PyObjC_INITERROR();
    }

    if (PyObjC_ImportAPI(m) == -1) PyObjC_INITERROR();

    /*
     * XXX: This call is here to force some initialisation
     * that confuses PyObjC. In particular, some 'constants'
     * are nil until this calls is initialized.
     */
    [NSManagedObjectContext initialize];

    PyObjC_INITDONE();
}
