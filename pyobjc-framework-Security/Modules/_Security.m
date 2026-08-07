#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
#import <Security/Security.h>

/*
 * XXX: Does this need to be a manual binding?
 */
static PyObject*
m_SecKeychainFindInternetPassword(PyObject* meth, PyObject* _Nonnull const* _Nonnull args,
                                  size_t    nargs)
{
    OSStatus              retval;
    id                    keychainOrArray;
    Py_ssize_t            serverName_length;
    const char*           serverName;
    int                   serverName_token;
    PyObject*             serverName_buffer = NULL;
    Py_buffer             serverName_view;
    Py_ssize_t            securityDomain_length;
    const char*           securityDomain;
    int                   securityDomain_token;
    PyObject*             securityDomain_buffer = NULL;
    Py_buffer             securityDomain_view;
    Py_ssize_t            accountName_length;
    const char*           accountName;
    int                   accountName_token;
    PyObject*             accountName_buffer = NULL;
    Py_buffer             accountName_view;
    Py_ssize_t            path_length;
    const char*           path;
    int                   path_token;
    PyObject*             path_buffer = NULL;
    Py_buffer             path_view;
    UInt16                port;
    SecProtocolType       protocol;
    SecAuthenticationType authenticationType;
    UInt32                password_length = 0;
    void*                 passwordData    = NULL;
    SecKeychainItemRef    itemRef         = NULL;

    if (PyObjC_CheckArgCount(meth, 15, 15, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC("@", args[0], &keychainOrArray) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(Py_ssize_t), args[1], &serverName_length) == -1) {
        return NULL;
    }

    serverName_token =
        PyObjC_PythonToCArray(NO, NO, "t", args[2], (void**)&serverName,
                              &serverName_length, &serverName_buffer, &serverName_view);
    if (serverName_token == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(Py_ssize_t), args[3], &securityDomain_length) == -1) {
        return NULL;
    }

    /* XXX: Is PyObjC_NULL correct here? */
    if (args[4] == Py_None || args[4] == PyObjC_NULL) {
        securityDomain = NULL;

    } else {
        securityDomain_token = PyObjC_PythonToCArray(
            NO, NO, "t", args[4], (void**)&securityDomain, &securityDomain_length,
            &securityDomain_buffer, &securityDomain_view);
        if (securityDomain_token == -1) {
            PyObjC_FreeCArray(serverName_token, &serverName_view);
            Py_XDECREF(serverName_buffer);
            return NULL;
        }
    }

    if (PyObjC_PythonToObjC(@encode(Py_ssize_t), args[5], &accountName_length) == -1) {
        PyObjC_FreeCArray(serverName_token, &serverName_view);
        Py_XDECREF(serverName_buffer);
        if (args[4] != NULL)
            PyObjC_FreeCArray(securityDomain_token, &securityDomain_view);
        Py_XDECREF(securityDomain_buffer);
        return NULL;
    }

    if (args[6] == Py_None || args[6] == PyObjC_NULL) {
        accountName = NULL;
    } else {
        accountName_token = PyObjC_PythonToCArray(
            NO, NO, "t", args[6], (void**)&accountName, &accountName_length,
            &accountName_buffer, &accountName_view);
        if (accountName_token == -1) {
            PyObjC_FreeCArray(serverName_token, &serverName_view);
            Py_XDECREF(serverName_buffer);
            if (args[4] != NULL)
                PyObjC_FreeCArray(securityDomain_token, &securityDomain_view);
            Py_XDECREF(securityDomain_buffer);
            return NULL;
        }
    }

    if (PyObjC_PythonToObjC(@encode(Py_ssize_t), args[7], &path_length) == -1) {
        PyObjC_FreeCArray(serverName_token, &serverName_view);
        Py_XDECREF(serverName_buffer);
        if (args[4] != NULL)
            PyObjC_FreeCArray(securityDomain_token, &securityDomain_view);
        Py_XDECREF(securityDomain_buffer);
        PyObjC_FreeCArray(accountName_token, &accountName_view);
        Py_XDECREF(accountName_buffer);
        return NULL;
    }

    if (args[8] == Py_None || args[8] == PyObjC_NULL) {
        path = NULL;
    } else {
        path_token = PyObjC_PythonToCArray(NO, NO, "t", args[8], (void**)&path,
                                           &path_length, &path_buffer, &path_view);
        if (path_token == -1) {
            PyObjC_FreeCArray(serverName_token, &serverName_view);
            Py_XDECREF(serverName_buffer);
            if (args[4] != NULL)
                PyObjC_FreeCArray(securityDomain_token, &securityDomain_view);
            Py_XDECREF(securityDomain_buffer);
            PyObjC_FreeCArray(accountName_token, &accountName_view);
            Py_XDECREF(accountName_buffer);
            return NULL;
        }
    }

    if (PyObjC_PythonToObjC(@encode(UInt16), args[9], &port) == -1) {
        PyObjC_FreeCArray(serverName_token, &serverName_view);
        Py_XDECREF(serverName_buffer);
        if (args[4] != NULL)
            PyObjC_FreeCArray(securityDomain_token, &securityDomain_view);
        Py_XDECREF(securityDomain_buffer);
        PyObjC_FreeCArray(accountName_token, &accountName_view);
        Py_CLEAR(accountName_buffer);
        PyObjC_FreeCArray(path_token, &path_view);
        Py_CLEAR(path_buffer);
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(SecProtocolType), args[10], &protocol) == -1) {
        PyObjC_FreeCArray(serverName_token, &serverName_view);
        Py_XDECREF(serverName_buffer);
        if (args[4] != NULL)
            PyObjC_FreeCArray(securityDomain_token, &securityDomain_view);
        Py_XDECREF(securityDomain_buffer);
        PyObjC_FreeCArray(accountName_token, &accountName_view);
        Py_XDECREF(accountName_buffer);
        PyObjC_FreeCArray(path_token, &path_view);
        Py_XDECREF(path_buffer);
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(SecAuthenticationType), args[11], &authenticationType)
        == -1) {
        PyObjC_FreeCArray(serverName_token, &serverName_view);
        Py_XDECREF(serverName_buffer);
        if (args[4] != NULL)
            PyObjC_FreeCArray(securityDomain_token, &securityDomain_view);
        Py_XDECREF(securityDomain_buffer);
        PyObjC_FreeCArray(accountName_token, &accountName_view);
        Py_XDECREF(accountName_buffer);
        PyObjC_FreeCArray(path_token, &path_view);
        Py_XDECREF(path_buffer);
        return NULL;
    }

    if (args[12] != Py_None && args[12] != PyObjC_NULL) {
        PyErr_SetString(PyExc_TypeError, "passwordLength must be None or objc.NULL");
        PyObjC_FreeCArray(serverName_token, &serverName_view);
        Py_XDECREF(serverName_buffer);
        if (args[4] != NULL)
            PyObjC_FreeCArray(securityDomain_token, &securityDomain_view);
        Py_XDECREF(securityDomain_buffer);
        PyObjC_FreeCArray(accountName_token, &accountName_view);
        Py_XDECREF(accountName_buffer);
        PyObjC_FreeCArray(path_token, &path_view);
        Py_XDECREF(path_buffer);
        return NULL;
    }

    if (args[13] != Py_None && args[13] != PyObjC_NULL) {
        PyErr_SetString(PyExc_TypeError, "passwordData must be None or objc.NULL");
        PyObjC_FreeCArray(serverName_token, &serverName_view);
        Py_XDECREF(serverName_buffer);
        if (args[4] != NULL)
            PyObjC_FreeCArray(securityDomain_token, &securityDomain_view);
        Py_XDECREF(securityDomain_buffer);
        PyObjC_FreeCArray(accountName_token, &accountName_view);
        Py_XDECREF(accountName_buffer);
        PyObjC_FreeCArray(path_token, &path_view);
        Py_XDECREF(path_buffer);
        return NULL;
    }

    if (args[14] != Py_None && args[14] != PyObjC_NULL) {
        PyErr_SetString(PyExc_TypeError, "item must be None or objc.NULL");
        PyObjC_FreeCArray(serverName_token, &serverName_view);
        Py_XDECREF(serverName_buffer);
        if (args[4] != NULL)
            PyObjC_FreeCArray(securityDomain_token, &securityDomain_view);
        Py_XDECREF(securityDomain_buffer);
        PyObjC_FreeCArray(accountName_token, &accountName_view);
        Py_XDECREF(accountName_buffer);
        PyObjC_FreeCArray(path_token, &path_view);
        Py_XDECREF(path_buffer);
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
            retval = SecKeychainFindInternetPassword(
                keychainOrArray, serverName_length, serverName, securityDomain_length,
                securityDomain, accountName_length, accountName, path_length, path, port,
                protocol, authenticationType,
                args[12] == Py_None ? &password_length : NULL,
                args[13] == Py_None ? &passwordData : NULL,
                args[14] == Py_None ? &itemRef : NULL);
#pragma clang diagnostic pop

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    PyObjC_FreeCArray(serverName_token, &serverName_view);
    Py_XDECREF(serverName_buffer);
    if (args[4] != NULL)
        PyObjC_FreeCArray(securityDomain_token, &securityDomain_view);
    Py_XDECREF(securityDomain_buffer);
    PyObjC_FreeCArray(accountName_token, &accountName_view);
    Py_XDECREF(accountName_buffer);
    PyObjC_FreeCArray(path_token, &path_view);
    Py_XDECREF(path_buffer);

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    PyObject* py_passwordData;
    if (args[13] == Py_None) {
        if (passwordData == NULL) {
            py_passwordData = Py_None;
            Py_INCREF(py_passwordData);
        } else {
            py_passwordData = PyBytes_FromStringAndSize(passwordData, password_length);
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
            (void)SecKeychainItemFreeContent(NULL, passwordData);
#pragma clang diagnostic pop

            if (py_passwordData == NULL) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                if (itemRef != NULL) {
                    CFRelease(itemRef);
                }
                return NULL;
                // LCOV_EXCL_STOP
            }
        }
    } else {
        py_passwordData = PyObjC_NULL;
        Py_INCREF(py_passwordData);
    }

    PyObject* py_itemRef;
    if (args[14] == Py_None) {
        if (itemRef == nil) {
            py_itemRef = Py_None;
            Py_INCREF(Py_None);
        } else {
            py_itemRef = PyObjC_IdToPython((id)itemRef);
            CFRelease(itemRef);
        }
    } else {
        py_itemRef = PyObjC_NULL;
        Py_INCREF(py_itemRef);
    }

    return Py_BuildValue("iINN", retval, password_length, py_passwordData, py_itemRef);
}

static PyObject*
m_SecKeychainFindGenericPassword(PyObject* meth, PyObject* _Nonnull const* _Nonnull args,
                                 size_t    nargs)
{
    OSStatus           retval;
    id                 keychainOrArray;
    Py_ssize_t         serviceName_length;
    const char*        serviceName;
    int                serviceName_token;
    PyObject*          serviceName_buffer = NULL;
    Py_buffer          serviceName_view;
    Py_ssize_t         accountName_length;
    const char*        accountName;
    int                accountName_token;
    PyObject*          accountName_buffer = NULL;
    Py_buffer          accountName_view;
    UInt32             password_length = 0;
    void*              passwordData    = NULL;
    SecKeychainItemRef itemRef         = NULL;

    if (PyObjC_CheckArgCount(meth, 8, 8, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(id), args[0], &keychainOrArray) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(Py_ssize_t), args[1], &serviceName_length) == -1) {
        return NULL;
    }

    serviceName_token = PyObjC_PythonToCArray(NO, NO, "t", args[2], (void**)&serviceName,
                                              &serviceName_length, &serviceName_buffer,
                                              &serviceName_view);
    if (serviceName_token == -1) {
        PyObjC_FreeCArray(serviceName_token, &serviceName_view);
        Py_XDECREF(serviceName_buffer);
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(Py_ssize_t), args[3], &accountName_length) == -1) {
        PyObjC_FreeCArray(serviceName_token, &serviceName_view);
        Py_XDECREF(serviceName_buffer);
        return NULL;
    }

    if (args[4] == Py_None || args[4] == PyObjC_NULL) {
        accountName = NULL;
    } else {
        accountName_token = PyObjC_PythonToCArray(
            NO, NO, "t", args[4], (void**)&accountName, &accountName_length,
            &accountName_buffer, &accountName_view);
        if (accountName_token == -1) {
            PyObjC_FreeCArray(serviceName_token, &serviceName_view);
            Py_XDECREF(serviceName_buffer);
            return NULL;
        }
    }

    if (args[5] != Py_None && args[5] != PyObjC_NULL) {
        PyErr_SetString(PyExc_TypeError, "passwordLength must be None or objc.NULL");
        PyObjC_FreeCArray(serviceName_token, &serviceName_view);
        Py_XDECREF(serviceName_buffer);
        PyObjC_FreeCArray(accountName_token, &accountName_view);
        Py_XDECREF(accountName_buffer);
        return NULL;
    }

    if (args[6] != Py_None && args[6] != PyObjC_NULL) {
        PyErr_SetString(PyExc_TypeError, "passwordData must be None or objc.NULL");
        PyObjC_FreeCArray(serviceName_token, &serviceName_view);
        Py_XDECREF(serviceName_buffer);
        PyObjC_FreeCArray(accountName_token, &accountName_view);
        Py_XDECREF(accountName_buffer);
        return NULL;
    }

    if (args[7] != Py_None && args[7] != PyObjC_NULL) {
        PyErr_SetString(PyExc_TypeError, "item must be None or objc.NULL");
        PyObjC_FreeCArray(serviceName_token, &serviceName_view);
        Py_XDECREF(serviceName_buffer);
        PyObjC_FreeCArray(accountName_token, &accountName_view);
        Py_XDECREF(accountName_buffer);
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"

            retval = SecKeychainFindGenericPassword(
                keychainOrArray, serviceName_length, serviceName, accountName_length,
                accountName, args[5] == Py_None ? &password_length : NULL,
                args[6] == Py_None ? &passwordData : NULL,
                args[7] == Py_None ? &itemRef : NULL);

#pragma clang diagnostic pop
        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    PyObjC_FreeCArray(serviceName_token, &serviceName_view);
    Py_XDECREF(serviceName_buffer);
    PyObjC_FreeCArray(accountName_token, &accountName_view);
    Py_XDECREF(accountName_buffer);

    if (PyErr_Occurred()) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    PyObject* py_passwordData;
    if (args[6] == Py_None) {
        if (passwordData == NULL) {
            py_passwordData = Py_None;
            Py_INCREF(py_passwordData);
        } else {
            py_passwordData = PyBytes_FromStringAndSize(passwordData, password_length);
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
            (void)SecKeychainItemFreeContent(NULL, passwordData);
#pragma clang diagnostic pop

            if (py_passwordData == NULL) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                if (itemRef != NULL) {
                    CFRelease(itemRef);
                }
                return NULL;
                // LCOV_EXCL_STOP
            }
        }
    } else {
        py_passwordData = PyObjC_NULL;
        Py_INCREF(py_passwordData);
    }

    PyObject* py_itemRef;
    if (args[7] == Py_None) {
        if (itemRef == nil) {
            py_itemRef = Py_None;
            Py_INCREF(Py_None);
        } else {
            py_itemRef = PyObjC_IdToPython((id)itemRef);
            CFRelease(itemRef);
        }
    } else {
        py_itemRef = PyObjC_NULL;
        Py_INCREF(py_itemRef);
    }

    return Py_BuildValue("iINN", retval, password_length, py_passwordData, py_itemRef);
}

static int
parse_itemset(PyObject* value, AuthorizationItemSet* itemset)
{
    itemset->items = NULL;

    if (value == Py_None) {
        return 1;

    } else {
        PyObject*  seq = PySequence_Tuple(value);
        Py_ssize_t i;
        if (seq == NULL) {
            return 0;
        }
        itemset->count = PyTuple_GET_SIZE(seq);
        itemset->items = PyMem_Malloc(sizeof(AuthorizationItem) * PyTuple_GET_SIZE(seq));
        if (itemset->items == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            PyErr_NoMemory();
            return 0;
            // LCOV_EXCL_STOP
        }

        for (i = 0; i < PyTuple_GET_SIZE(seq); i++) {
            PyObject* cur_seq = PySequence_Tuple(PyTuple_GET_ITEM(seq, i));
            if (cur_seq == NULL) {
                PyErr_Format(PyExc_TypeError, "items[%ld] is not a sequence", (long)i);
                PyMem_Free(itemset->items);
                return 0;
            }
            if (PyTuple_GET_SIZE(cur_seq) != 4) {
                PyErr_Format(PyExc_TypeError, "items[%ld] is not a sequence of 4 items",
                             (long)i);
                PyMem_Free(itemset->items);
                return 0;
            }

            if (!PyBytes_Check(PyTuple_GET_ITEM(cur_seq, 0))) {
                PyErr_Format(PyExc_TypeError, "items[%ld].name is not a byte string",
                             (long)i);
                PyMem_Free(itemset->items);
                return 0;
            }

            itemset->items[i].name = PyBytes_AsString(PyTuple_GET_ITEM(cur_seq, 0));

            if (PyObjC_PythonToObjC(@encode(size_t), PyTuple_GET_ITEM(cur_seq, 1),
                                    &(itemset->items[i].valueLength))
                == -1) {
                PyErr_Format(PyExc_TypeError, "items[%ld].valueLength is not an integer",
                             (long)i);
                PyMem_Free(itemset->items);
                return 0;
            }

            if (PyTuple_GET_ITEM(cur_seq, 2) == Py_None) {
                if (itemset->items[i].valueLength != 0) {
                    PyErr_Format(PyExc_TypeError,
                                 "items[%ld].value is None, valueLength != 0", (long)i);
                    PyMem_Free(itemset->items);
                    return 0;
                }

                itemset->items[i].value = NULL;

            } else {
                if (!PyBytes_Check(PyTuple_GET_ITEM(cur_seq, 2))
                    || PyBytes_Size(PyTuple_GET_ITEM(cur_seq, 2))
                           != (Py_ssize_t)itemset->items[i].valueLength) {
                    PyErr_Format(PyExc_TypeError,
                                 "items[%ld].value is not a byte string of length %ld",
                                 (long)i, (long)(itemset->items[i].valueLength));
                    PyMem_Free(itemset->items);
                    return 0;
                }

                itemset->items[i].value = PyBytes_AsString(PyTuple_GET_ITEM(cur_seq, 2));
            }

            if (PyObjC_PythonToObjC(@encode(UInt32), PyTuple_GET_ITEM(cur_seq, 3),
                                    &(itemset->items[i].flags))
                == -1) {
                PyErr_Format(PyExc_TypeError, "items[%ld].flags is not an integer",
                             (long)i);
                PyMem_Free(itemset->items);
                return 0;
            }
        }
    }
    return 1;
}

static void
free_itemset(AuthorizationItemSet* itemset)
{
    PyMem_Free(itemset->items);
}

static PyObject*
build_itemset(AuthorizationItemSet* _Nonnull itemset)
{
    PyObject* result = NULL;
    PyObject* t      = NULL;
    PyObject* o      = NULL;

    assert(itemset != NULL);

    UInt32 i;
    result = PyTuple_New(itemset->count);
    if (result == NULL) // LCOV_BR_EXCL_LINE
        return NULL;    // LCOV_EXCL_LINE

    for (i = 0; i < itemset->count; i++) {
        Py_ssize_t         packed = -1;
        AuthorizationItem* item   = itemset->items + i;

        t = PyObjC_CreateRegisteredStruct("{_AuthorizationItem=^cL^vI}",
                                          sizeof("{_AuthorizationItem=^cL^vI}") - 1, NULL,
                                          &packed);
        if (t == NULL)  // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE

        o = PyBytes_FromString(item->name);
        if (o == NULL)  // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE

        if (PySequence_SetItem(t, 0, o) == -1) // LCOV_BR_EXCL_LINE
            goto error;                        // LCOV_EXCL_LINE

        Py_CLEAR(o);

        o = PyLong_FromUnsignedLong(item->valueLength);
        if (o == NULL)  // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE

        if (PySequence_SetItem(t, 1, o) == -1) // LCOV_BR_EXCL_LINE
            goto error;                        // LCOV_EXCL_LINE

        Py_CLEAR(o);

        if (item->value == NULL) {
            o = Py_None;
            Py_INCREF(Py_None);
        } else {
            o = PyBytes_FromStringAndSize(item->value, item->valueLength);
            if (o == NULL)  // LCOV_BR_EXCL_LINE
                goto error; // LCOV_EXCL_LINE
        }

        if (PySequence_SetItem(t, 2, o) == -1) // LCOV_BR_EXCL_LINE
            goto error;                        // LCOV_EXCL_LINE

        Py_CLEAR(o);

        o = PyLong_FromUnsignedLong(item->flags);
        if (o == NULL)  // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE

        if (PySequence_SetItem(t, 3, o) == -1) // LCOV_BR_EXCL_LINE
            goto error;                        // LCOV_EXCL_LINE

        Py_CLEAR(o);

        PyTuple_SET_ITEM(result, i, t);
    }
    return result;

error:
    // LCOV_EXCL_START
    Py_CLEAR(result);
    Py_CLEAR(t);
    Py_CLEAR(o);
    return NULL;
    // LCOV_EXCL_STOP
}

static PyObject*
m_AuthorizationCreate(PyObject* meth, PyObject* _Nonnull const* _Nonnull args,
                      size_t    nargs)
{
    OSStatus                 retval;
    AuthorizationRights      rights;
    AuthorizationEnvironment environment;
    AuthorizationFlags       flags;
    AuthorizationRef         authorization = NULL;

    rights.items = environment.items = NULL;

    if (PyObjC_CheckArgCount(meth, 4, 4, nargs) == -1) {
        return NULL;
    }

    if (!parse_itemset(args[0], &rights)) {
        return NULL;
    }

    if (!parse_itemset(args[1], &environment)) {
        PyMem_Free(rights.items);
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(AuthorizationFlags), args[2], &flags) == -1) {
        PyMem_Free(rights.items);
        PyMem_Free(environment.items);
        return NULL;
    }

    if (args[3] != Py_None) {
        PyErr_SetString(PyExc_ValueError, "authorization must be None");
        PyMem_Free(rights.items);
        PyMem_Free(environment.items);
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            retval = AuthorizationCreate(args[0] == Py_None ? NULL : &rights,
                                         args[1] == Py_None ? NULL : &environment, flags,
                                         &authorization);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    free_itemset(&rights);
    free_itemset(&environment);

    if (PyErr_Occurred()) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    return Py_BuildValue("iN", retval,
                         PyObjC_ObjCToPython(@encode(AuthorizationRef), &authorization));
}

static PyObject*
m_AuthorizationCopyInfo(PyObject* meth, PyObject* _Nonnull const* _Nonnull args,
                        size_t    nargs)
{
    OSStatus              retval;
    AuthorizationRef      authorization;
    char*                 tag;
    AuthorizationItemSet* info = NULL;

    if (PyObjC_CheckArgCount(meth, 3, 3, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(AuthorizationRef), args[0], &authorization) == -1) {
        return NULL;
    }

    if (args[1] == Py_None) {
        tag = NULL;

    } else if (PyBytes_Check(args[1])) {
        tag = PyBytes_AsString(args[1]);

    } else {
        PyErr_SetString(PyExc_ValueError, "tag must be byte string or None");
        return NULL;
    }

    if (args[2] != Py_None) {
        PyErr_SetString(PyExc_ValueError, "info must be None");
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            retval = AuthorizationCopyInfo(authorization, tag, &info);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    PyObject* py_info = build_itemset(info);
    if (info != NULL) {
        AuthorizationFreeItemSet(info);
    }

    return Py_BuildValue("iN", retval, py_info);
}

static PyObject*
m_AuthorizationCopyRights(PyObject* meth, PyObject* _Nonnull const* _Nonnull args,
                          size_t    nargs)
{
    OSStatus                 retval;
    AuthorizationRef         authorization;
    AuthorizationRights      rights;
    AuthorizationEnvironment environment;
    AuthorizationFlags       flags;
    AuthorizationRights*     authorizedRights = NULL;

    if (PyObjC_CheckArgCount(meth, 5, 5, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(AuthorizationRef), args[0], &authorization) == -1) {
        return NULL;
    }

    if (!parse_itemset(args[1], &rights)) {
        return NULL;
    }
    if (!parse_itemset(args[2], &environment)) {
        PyMem_Free(rights.items);
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(AuthorizationFlags), args[3], &flags) == -1) {
        PyMem_Free(rights.items);
        PyMem_Free(environment.items);
        return NULL;
    }

    if (args[4] != PyObjC_NULL && args[4] != Py_None) {
        PyMem_Free(rights.items);
        PyMem_Free(environment.items);
        PyErr_SetString(PyExc_ValueError, "authorizedRights must be None or objc.NULL");
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            retval = AuthorizationCopyRights(
                authorization, args[1] == Py_None ? NULL : &rights,
                args[1] == Py_None ? NULL : &environment, flags,
                args[4] == PyObjC_NULL ? NULL : &authorizedRights);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    free_itemset(&rights);
    free_itemset(&environment);

    if (PyErr_Occurred()) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    PyObject* py_authorizedRights;
    if (args[4] == PyObjC_NULL) {
        py_authorizedRights = PyObjC_NULL;
        Py_INCREF(py_authorizedRights);

    } else {
        py_authorizedRights = build_itemset(authorizedRights);
        if (authorizedRights != NULL) {
            AuthorizationFreeItemSet(authorizedRights);
        }
    }

    return Py_BuildValue("iN", retval, py_authorizedRights);
}

static PyObject*
m_AuthorizationCopyRightsAsync(PyObject* meth, PyObject* _Nonnull const* _Nonnull args,
                               size_t    nargs)
{
    AuthorizationRef         authorization;
    AuthorizationRights      rights;
    AuthorizationEnvironment environment;
    AuthorizationFlags       flags;
    PyObject*                py_callback;

    if (PyObjC_CheckArgCount(meth, 5, 5, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(AuthorizationRef), args[0], &authorization) == -1) {
        return NULL;
    }

    if (!parse_itemset(args[1], &rights)) {
        return NULL;
    }
    if (!parse_itemset(args[2], &environment)) {
        PyMem_Free(rights.items);
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(AuthorizationFlags), args[3], &flags) == -1) {
        PyMem_Free(rights.items);
        PyMem_Free(environment.items);
        return NULL;
    }

    py_callback = args[4];
    if (!PyCallable_Check(py_callback)) {
        PyMem_Free(rights.items);
        PyMem_Free(environment.items);
        PyErr_SetString(PyExc_ValueError, "callback must be callable");
        return NULL;
    }

    Py_INCREF(py_callback);
    Py_BEGIN_ALLOW_THREADS
        @try {
            AuthorizationCopyRightsAsync(
                authorization, args[1] == Py_None ? NULL : &rights,
                args[2] == Py_None ? NULL : &environment, flags,
                ^(OSStatus err, AuthorizationRights* authorizedRights) {
                  PyObject* py_authorizedRights;
                  PyObject* py_result;

                  PyObjC_BEGIN_WITH_GIL

                      if (authorizedRights == NULL) {
                          py_authorizedRights = Py_None;
                          Py_INCREF(Py_None);
                      } else {
                          py_authorizedRights = build_itemset(authorizedRights);
                          if (authorizedRights != NULL) {
                              AuthorizationFreeItemSet(authorizedRights);
                          }
                      }

                      py_result = PyObject_CallFunction(py_callback, "iO", err,
                                                        py_authorizedRights);
                      if (py_result == NULL) {
                          /* Don't raise as ObjC exception, will cause hard crash */
                          PyErr_WriteUnraisable(py_callback);
                      } else if (py_result != Py_None) {
                          Py_DECREF(py_result);
                          PyErr_SetString(PyExc_TypeError,
                                          "callbackBlock returned value");
                          /* Don't raise as ObjC exception, will cause hard crash */
                          PyErr_WriteUnraisable(py_callback);
                      } else {
                          Py_DECREF(py_result);
                      }

                      Py_DECREF(py_callback);
                      PyMem_Free(rights.items);
                      PyMem_Free(environment.items);

                  PyObjC_END_WITH_GIL
                });

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(py_callback);
        return NULL;
        // LCOV_EXCL_STOP
    }
    Py_INCREF(Py_None);
    return Py_None;
}

static PyObject*
m_AuthorizationExecuteWithPrivileges(PyObject* meth,
                                     PyObject* _Nonnull const* _Nonnull args,
                                     size_t nargs)
{
    OSStatus           retval;
    AuthorizationRef   authorization;
    const char*        pathToTool;
    AuthorizationFlags options;
    char**             arguments;
    FILE*              communicationsPipe = NULL;
    PyObject*          seq;
    Py_ssize_t         i;

    if (PyObjC_CheckArgCount(meth, 5, 5, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(AuthorizationRef), args[0], &authorization) == -1) {
        return NULL;
    }

    if (!PyBytes_Check(args[1])) {
        PyErr_SetString(PyExc_ValueError, "pathToTool must be a bytes string");
        return NULL;
    }

    pathToTool = PyBytes_AsString(args[1]);

    if (PyObjC_PythonToObjC(@encode(AuthorizationFlags), args[2], &options) == -1) {
        return NULL;
    }

    seq = PySequence_Tuple(args[3]);
    if (seq == NULL) {
        return NULL;
    }

    arguments = PyMem_Malloc(sizeof(char*) * PyTuple_GET_SIZE(seq) + 1);
    if (arguments == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_NoMemory();
        return NULL;
        // LCOV_EXCL_STOP
    }

    if (args[4] != Py_None && args[4] != PyObjC_NULL) {
        PyErr_SetString(PyExc_ValueError, "communicationsPipe must be None or objc.NULL");
        return NULL;
    }

    for (i = 0; i < PyTuple_GET_SIZE(seq); i++) {
        PyObject* t = PyTuple_GET_ITEM(seq, i);

        if (!PyBytes_Check(t)) {
            PyErr_SetString(PyExc_ValueError,
                            "arguments must be a sequence of byte strings");
            PyMem_Free(arguments);
            Py_DECREF(seq);
            return NULL;
        }
        arguments[i] = PyBytes_AsString(t);
    }
    arguments[i] = NULL;
    Py_DECREF(seq);

    Py_BEGIN_ALLOW_THREADS
        @try {

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"

            retval = AuthorizationExecuteWithPrivileges(
                authorization, pathToTool, options, arguments,
                args[4] == PyObjC_NULL ? NULL : &communicationsPipe);

#pragma clang diagnostic pop

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    PyMem_Free(arguments);

    if (PyErr_Occurred()) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    if (args[4] == PyObjC_NULL) {
        return Py_BuildValue("iO", retval, Py_None);
    } else {
        return Py_BuildValue("iN", retval,
                             PyObjC_ObjCToPython(@encode(FILE*), &communicationsPipe));
    }
}

static PyMethodDef mod_methods[] = {
    {0, 0, 0, 0} /* sentinel */
};

static int
mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) == -1) // LCOV_BR_EXCL_LINE
        return -1;                 // LCOV_EXCL_LINE

    if (PyObjCRegister_FunctionCaller(SecKeychainFindInternetPassword,
                                      m_SecKeychainFindInternetPassword)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(SecKeychainFindGenericPassword,
                                      m_SecKeychainFindGenericPassword)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(AuthorizationCreate, m_AuthorizationCreate)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(AuthorizationCopyInfo, m_AuthorizationCopyInfo)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(AuthorizationCopyRights, m_AuthorizationCopyRights)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(AuthorizationCopyRightsAsync,
                                      m_AuthorizationCopyRightsAsync)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(AuthorizationExecuteWithPrivileges,
                                      m_AuthorizationExecuteWithPrivileges)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    return 0;
}

static struct PyModuleDef_Slot mod_slots[] = {
    {.slot = Py_mod_exec, .value = (void*)mod_exec_module},
#if PY_VERSION_HEX >= 0x030c0000
    {
        /* This extension does not use the CPython API other than initializing
         * the module, hence is safe with subinterpreters and per-interpreter
         * GILs
         */
        .slot  = Py_mod_multiple_interpreters,
        .value = Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED,
    },
#endif
#if PY_VERSION_HEX >= 0x030d0000
    {
        /* The code in this extension should be safe to use without the GIL */
        .slot  = Py_mod_gil,
        .value = Py_MOD_GIL_NOT_USED,
    },
#endif
    {/* Sentinel */
     .slot  = 0,
     .value = 0}};

static struct PyModuleDef mod_module = {
    .m_base     = PyModuleDef_HEAD_INIT,
    .m_name     = "_Security",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit__Security(void);

PyObject* __attribute__((__visibility__("default")))
PyInit__Security(void)
{
    return PyModuleDef_Init(&mod_module);
}
