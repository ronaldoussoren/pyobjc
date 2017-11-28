#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
#import <Security/Security.h>

static PyObject*
m_SecKeychainFindInternetPassword(
        PyObject* module __attribute__((__unused__)),
        PyObject* args)
{
    OSStatus retval;
    id keychainOrArray;
    PyObject*  py_keychainOrArray;
    Py_ssize_t serverName_length;
    const char* serverName;
    PyObject* py_serverName;
    int serverName_token;
    PyObject* serverName_buffer = NULL;
    Py_ssize_t securityDomain_length;
    const char* securityDomain;
    PyObject* py_securityDomain;
    int securityDomain_token;
    PyObject* securityDomain_buffer = NULL;
    Py_ssize_t accountName_length;
    const char* accountName;
    PyObject* py_accountName;
    int accountName_token;
    PyObject* accountName_buffer = NULL;
    Py_ssize_t path_length;
    const char* path;
    PyObject* py_path;
    int path_token;
    PyObject* path_buffer = NULL;
    UInt16 port;
    SecProtocolType protocol;
    SecAuthenticationType authenticationType;
    UInt32 password_length = 0;
    PyObject* py_password_length;
    void* passwordData = NULL;
    PyObject* py_passwordData;
    SecKeychainItemRef itemRef = NULL;
    PyObject* py_itemRef;
    const char string = 't';

    if (!PyArg_ParseTuple(args, "OnOnOnOnOHIIOOO",
            &py_keychainOrArray,
            &serverName_length, &py_serverName,
            &securityDomain_length, &py_securityDomain,
            &accountName_length, &py_accountName,
            &path_length, &py_path,
            &port, &protocol, &authenticationType,
            &py_password_length, &py_passwordData,
            &py_itemRef)) {
        return NULL;
    }

    keychainOrArray = PyObjC_PythonToId(py_keychainOrArray);
    if (keychainOrArray == nil && PyErr_Occurred()) {
        return NULL;
    }

    serverName_token = PyObjC_PythonToCArray(NO, NO, &string, py_serverName, (void**)&serverName, &serverName_length, &serverName_buffer);
    if (serverName_token == -1) {
        return NULL;
    }

    if (py_securityDomain == Py_None) {
        securityDomain = NULL;

    } else {
        securityDomain_token = PyObjC_PythonToCArray(NO, NO, &string, py_securityDomain, (void**)&securityDomain, &securityDomain_length, &securityDomain_buffer);
        if (securityDomain_token == -1) {
            PyObjC_FreeCArray(serverName_token, (void*)serverName); Py_XDECREF(serverName_buffer);
            return NULL;
        }
    }

    if (py_accountName == Py_None) {
        accountName = NULL;
    } else {
        accountName_token = PyObjC_PythonToCArray(NO, NO, &string, py_accountName, (void**)&accountName, &accountName_length, &accountName_buffer);
        if (accountName_token == -1) {
            PyObjC_FreeCArray(serverName_token, (void*)serverName); Py_XDECREF(serverName_buffer);
            if (py_securityDomain != NULL) PyObjC_FreeCArray(securityDomain_token, (void*)securityDomain); Py_XDECREF(securityDomain_buffer);
            return NULL;
        }
    }

    if (py_path == NULL) {
        path = NULL;
    } else {
        path_token = PyObjC_PythonToCArray(NO, NO, &string, py_path, (void**)&path, &path_length, &path_buffer);
        if (path_token == -1) {
            PyObjC_FreeCArray(serverName_token, (void*)serverName); Py_XDECREF(serverName_buffer);
            if (py_securityDomain != NULL) PyObjC_FreeCArray(securityDomain_token, (void*)securityDomain); Py_XDECREF(securityDomain_buffer);
            PyObjC_FreeCArray(accountName_token, (void*)accountName); Py_XDECREF(accountName_buffer);
            return NULL;
        }
    }

    if (py_password_length != Py_None && py_password_length != PyObjC_NULL) {
        PyErr_SetString(PyExc_TypeError, "passwordLength must be None or objc.NULL");
        PyObjC_FreeCArray(serverName_token, (void*)serverName); Py_XDECREF(serverName_buffer);
        if (py_securityDomain != NULL) PyObjC_FreeCArray(securityDomain_token, (void*)securityDomain); Py_XDECREF(securityDomain_buffer);
        PyObjC_FreeCArray(accountName_token, (void*)accountName); Py_XDECREF(accountName_buffer);
        PyObjC_FreeCArray(path_token, (void*)path); Py_XDECREF(path_buffer);
        return NULL;
    }

    if (py_passwordData != Py_None && py_passwordData != PyObjC_NULL) {
        PyErr_SetString(PyExc_TypeError, "passwordData must be None or objc.NULL");
        PyObjC_FreeCArray(serverName_token, (void*)serverName); Py_XDECREF(serverName_buffer);
        if (py_securityDomain != NULL) PyObjC_FreeCArray(securityDomain_token, (void*)securityDomain); Py_XDECREF(securityDomain_buffer);
        PyObjC_FreeCArray(accountName_token, (void*)accountName); Py_XDECREF(accountName_buffer);
        PyObjC_FreeCArray(path_token, (void*)path); Py_XDECREF(path_buffer);
        return NULL;
    }

    PyObjC_DURING
        retval = SecKeychainFindInternetPassword(keychainOrArray,
                    serverName_length, serverName, securityDomain_length, securityDomain,
                    accountName_length, accountName, path_length, path,
                    port, protocol, authenticationType,
                    py_password_length == Py_None?&password_length:NULL,
                    py_passwordData == Py_None?&passwordData:NULL, py_itemRef == Py_None?&itemRef:NULL);

    PyObjC_HANDLER
        PyObjCErr_FromObjC(localException);

    PyObjC_ENDHANDLER

    PyObjC_FreeCArray(serverName_token, (void*)serverName); Py_XDECREF(serverName_buffer);
    if (py_securityDomain != NULL) PyObjC_FreeCArray(securityDomain_token, (void*)securityDomain); Py_XDECREF(securityDomain_buffer);
    PyObjC_FreeCArray(accountName_token, (void*)accountName); Py_XDECREF(accountName_buffer);
    PyObjC_FreeCArray(path_token, (void*)path); Py_XDECREF(path_buffer);

    if (PyErr_Occurred()) {
        return NULL;
    }

    if (py_passwordData == Py_None) {
        if (passwordData == NULL) {
            py_passwordData = Py_None;
            Py_INCREF(py_passwordData);
        } else {
#if Py_MAJOR == 3
            py_passwordData = PyBytes_FromStringAndSize(passwordData, password_length);
#else
            py_passwordData = PyBytes_FromStringAndSize(passwordData, password_length);
#endif
            (void)SecKeychainItemFreeContent(NULL, passwordData);

            if (py_passwordData == NULL) {
                if (itemRef != NULL) {
                    CFRelease(itemRef);
                }
                return NULL;
            }
        }
    } else {
        Py_INCREF(py_passwordData);
    }

    if (py_itemRef == Py_None) {
        if (itemRef == nil) {
            py_itemRef = Py_None; Py_INCREF(Py_None);
        } else {
            py_itemRef = PyObjC_IdToPython((id)itemRef);
            CFRelease(itemRef);
        }
    } else {
        Py_INCREF(py_itemRef);
    }

    return Py_BuildValue("iINN", retval, password_length, py_passwordData, py_itemRef);
}

static PyObject*
m_SecKeychainFindGenericPassword(
        PyObject* module __attribute__((__unused__)),
        PyObject* args)
{
    OSStatus retval;
    id keychainOrArray;
    PyObject*  py_keychainOrArray;
    Py_ssize_t serviceName_length;
    const char* serviceName;
    PyObject* py_serviceName;
    int serviceName_token;
    PyObject* serviceName_buffer = NULL;
    Py_ssize_t accountName_length;
    const char* accountName;
    PyObject* py_accountName;
    int accountName_token;
    PyObject* accountName_buffer = NULL;
    UInt32 password_length = 0;
    PyObject* py_password_length;
    void* passwordData = NULL;
    PyObject* py_passwordData;
    SecKeychainItemRef itemRef = NULL;
    PyObject* py_itemRef;
    const char string = 't';

    if (!PyArg_ParseTuple(args, "OnOnOOOO",
            &py_keychainOrArray,
            &serviceName_length, &py_serviceName,
            &accountName_length, &py_accountName,
            &py_password_length, &py_passwordData,
            &py_itemRef)) {
        return NULL;
    }

    keychainOrArray = PyObjC_PythonToId(py_keychainOrArray);
    if (keychainOrArray == nil && PyErr_Occurred()) {
        return NULL;
    }

    serviceName_token = PyObjC_PythonToCArray(NO, NO, &string, py_serviceName, (void**)&serviceName, &serviceName_length, &serviceName_buffer);
    if (serviceName_token == -1) {
        return NULL;
    }

    if (py_accountName == Py_None) {
        accountName = NULL;
    } else {
        accountName_token = PyObjC_PythonToCArray(NO, NO, &string, py_accountName, (void**)&accountName, &accountName_length, &accountName_buffer);
        if (accountName_token == -1) {
            PyObjC_FreeCArray(serviceName_token, (void*)serviceName); Py_XDECREF(serviceName_buffer);
            return NULL;
        }
    }

    if (py_password_length != Py_None && py_password_length != PyObjC_NULL) {
        PyErr_SetString(PyExc_TypeError, "passwordLength must be None or objc.NULL");
        PyObjC_FreeCArray(serviceName_token, (void*)serviceName); Py_XDECREF(serviceName_buffer);
        PyObjC_FreeCArray(accountName_token, (void*)accountName); Py_XDECREF(accountName_buffer);
        return NULL;
    }

    if (py_passwordData != Py_None && py_passwordData != PyObjC_NULL) {
        PyErr_SetString(PyExc_TypeError, "passwordData must be None or objc.NULL");
        PyObjC_FreeCArray(serviceName_token, (void*)serviceName); Py_XDECREF(serviceName_buffer);
        PyObjC_FreeCArray(accountName_token, (void*)accountName); Py_XDECREF(accountName_buffer);
        return NULL;
    }

    PyObjC_DURING
        retval = SecKeychainFindGenericPassword(keychainOrArray,
                    serviceName_length, serviceName,
                    accountName_length, accountName,
                    py_password_length == Py_None?&password_length:NULL,
                    py_passwordData == Py_None?&passwordData:NULL, py_itemRef == Py_None?&itemRef:NULL);

    PyObjC_HANDLER
        PyObjCErr_FromObjC(localException);

    PyObjC_ENDHANDLER

    PyObjC_FreeCArray(serviceName_token, (void*)serviceName); Py_XDECREF(serviceName_buffer);
    PyObjC_FreeCArray(accountName_token, (void*)accountName); Py_XDECREF(accountName_buffer);

    if (PyErr_Occurred()) {
        return NULL;
    }

    if (py_passwordData == Py_None) {
        if (passwordData == NULL) {
            py_passwordData = Py_None;
            Py_INCREF(py_passwordData);
        } else {
#if Py_MAJOR == 3
            py_passwordData = PyBytes_FromStringAndSize(passwordData, password_length);
#else
            py_passwordData = PyBytes_FromStringAndSize(passwordData, password_length);
#endif
            (void)SecKeychainItemFreeContent(NULL, passwordData);

            if (py_passwordData == NULL) {
                if (itemRef != NULL) {
                    CFRelease(itemRef);
                }
                return NULL;
            }
        }
    } else {
        Py_INCREF(py_passwordData);
    }

    if (py_itemRef == Py_None) {
        if (itemRef == nil) {
            py_itemRef = Py_None; Py_INCREF(Py_None);
        } else {
            py_itemRef = PyObjC_IdToPython((id)itemRef);
            CFRelease(itemRef);
        }
    } else {
        Py_INCREF(py_itemRef);
    }

    return Py_BuildValue("iINN", retval, password_length, py_passwordData, py_itemRef);
}

static PyObject*
m_AuthorizationCreate(
        PyObject* module __attribute__((__unused__)),
        PyObject* args)
{
    OSStatus retval;
    AuthorizationRights rights;
    PyObject* py_rights;
    AuthorizationEnvironment environment;
    PyObject* py_environment;
    AuthorizationFlags flags;
    AuthorizationRef authorization = NULL;
    PyObject* py_authorization;

    rights.items = environment.items = NULL;

    if (!PyArg_ParseTuple(args, "OOIO", &py_rights, &py_environment, &flags, &py_authorization)) {
        return NULL;
    }

    if (py_rights == Py_None) {
        /* pass */

    } else {
        PyObject* seq = PySequence_Fast(py_rights, "rights must be a sequence");
        Py_ssize_t i;
        if (seq == NULL) {
            return NULL;
        }
        rights.count = PySequence_Fast_GET_SIZE(seq);
        rights.items = PyMem_Malloc(sizeof(AuthorizationItem) * PySequence_Fast_GET_SIZE(seq));
        if (rights.items == NULL) {
            PyErr_NoMemory();
            return NULL;
        }

        for (i = 0; i < PySequence_Fast_GET_SIZE(seq); i++) {
            if (PyObjC_PythonToObjC("{_AuthorizationItem=^cL^vI}", PySequence_Fast_GET_ITEM(seq, i), rights.items + i) < 0) {
                PyMem_Free(rights.items);
                return NULL;
            }
        }
    }

    if (py_environment == Py_None) {
        /* pass */

    } else {
        PyObject* seq = PySequence_Fast(py_environment, "environment must be a sequence");
        Py_ssize_t i;
        if (seq == NULL) {
            return NULL;
        }
        environment.count = PySequence_Fast_GET_SIZE(seq);
        environment.items = PyMem_Malloc(sizeof(AuthorizationItem) * PySequence_Fast_GET_SIZE(seq));
        if (environment.items == NULL) {
            PyMem_Free(rights.items);
            PyErr_NoMemory();
            return NULL;
        }

        for (i = 0; i < PySequence_Fast_GET_SIZE(seq); i++) {
            if (PyObjC_PythonToObjC("{_AuthorizationItem=^cL^vI}", PySequence_Fast_GET_ITEM(seq, i), environment.items + i) < 0) {
                PyMem_Free(rights.items);
                PyMem_Free(environment.items);
                return NULL;
            }
        }
    }

    if (py_authorization != Py_None) {
        PyErr_SetString(PyExc_ValueError, "authorization must be None");
        PyMem_Free(rights.items);
        PyMem_Free(environment.items);
        return NULL;
    }

    PyObjC_DURING
        retval = AuthorizationCreate(
            py_rights == Py_None?NULL:&rights,
            py_environment == Py_None?NULL:&environment,
            flags,
            &authorization);

    PyObjC_HANDLER
        PyObjCErr_FromObjC(localException);

    PyObjC_ENDHANDLER

    PyMem_Free(rights.items);
    PyMem_Free(environment.items);

    if (PyErr_Occurred()) {
        return NULL;
    }

    return Py_BuildValue("iN", retval, PyObjC_ObjCToPython(@encode(AuthorizationRef), &authorization));
}

static PyObject*
m_AuthorizationCopyInfo(
        PyObject* module __attribute__((__unused__)),
        PyObject* args)
{
    OSStatus retval;
    AuthorizationRef authorization;
    PyObject* py_authorization;
    char* tag;
    PyObject* py_tag;
    AuthorizationItemSet* info = NULL;
    PyObject* py_info;

    if (!PyArg_ParseTuple(args, "OOO", &py_authorization, &py_tag, &py_info)) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(AuthorizationRef), py_authorization, &authorization) == -1) {
        return NULL;
    }

    if (py_tag == Py_None) {
        tag = NULL;

#if Py_MAJOR == 2
    } else if (PyString_Check(py_tag)) {
#else
    } else if (PyBytes_Check(py_tag)) {
#endif
        tag = PyBytes_AsString(py_tag);

    } else {
        PyErr_SetString(PyExc_ValueError, "tag must be byte string or None");
        return NULL;
    }

    if (py_info != Py_None) {
        PyErr_SetString(PyExc_ValueError, "info must be None");
        return NULL;
    }

    PyObjC_DURING
        retval = AuthorizationCopyInfo(authorization, tag, &info);

    PyObjC_HANDLER
        PyObjCErr_FromObjC(localException);

    PyObjC_ENDHANDLER

    if (PyErr_Occurred()) {
        return NULL;
    }

    if (info != NULL) {
        UInt32 i;
        py_info = PyTuple_New(info->count);
        if (py_info == NULL) {
            AuthorizationFreeItemSet(info);
            return NULL;
        }

        for (i = 0; i < info->count; i++) {
            PyObject* t = PyObjC_ObjCToPython("{_AuthorizationItem=^cL^vI}", info->items + i);
            if (t == NULL) {
                Py_DECREF(py_info);
                AuthorizationFreeItemSet(info);
            }
            PyTuple_SET_ITEM(py_info, i, t);
        }
        AuthorizationFreeItemSet(info);
    }

    return Py_BuildValue("iN", retval, py_info);
}


static PyMethodDef mod_methods[] = {
    {
        "SecKeychainFindInternetPassword",
        m_SecKeychainFindInternetPassword,
        METH_VARARGS,
        "SecKeychainFindInternetPassword()"
    },
    {
        "SecKeychainFindGenericPassword",
        m_SecKeychainFindGenericPassword,
        METH_VARARGS,
        "SecKeychainFindGenericPassword()"
    },
    {
        "AuthorizationCreate",
        m_AuthorizationCreate,
        METH_VARARGS,
        "AuthorizationCreate()"
    },
    {
        "AuthorizationCopyInfo",
        m_AuthorizationCopyInfo,
        METH_VARARGS,
        "AuthorizationCopyInfo()"
    },

    { 0, 0, 0, 0 } /* sentinel */
};


/* Python glue */
PyObjC_MODULE_INIT(_Security)
{
    PyObject* m;
    m = PyObjC_MODULE_CREATE(_Security)
    if (!m) {
        PyObjC_INITERROR();
    }

    if (PyObjC_ImportAPI(m) == -1) PyObjC_INITERROR();

    PyObjC_INITDONE();
}
