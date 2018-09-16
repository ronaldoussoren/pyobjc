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
#if PY_MAJOR_VERSION == 3
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
#if PY_MAJOR_VERSION == 3
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

static int parse_itemset(PyObject* value, AuthorizationItemSet* itemset)
{
    itemset->items = NULL;

    if (value == Py_None) {
        return 1;

    } else {
        PyObject* seq = PySequence_Fast(value, "itemset must be a sequence or None");
        Py_ssize_t i;
        if (seq == NULL) {
            return 0;
        }
        itemset->count = PySequence_Fast_GET_SIZE(seq);
        itemset->items = PyMem_Malloc(sizeof(AuthorizationItem) * PySequence_Fast_GET_SIZE(seq));
        if (itemset->items == NULL) {
            PyErr_NoMemory();
            return 0;
        }

        for (i = 0; i < PySequence_Fast_GET_SIZE(seq); i++) {
            if (PyObjC_PythonToObjC("{_AuthorizationItem=^cL^vI}", PySequence_Fast_GET_ITEM(seq, i), itemset->items + i) < 0) {
                PyMem_Free(itemset->items);
                return 0;
            }
        }
    }
    return 1;
}

static PyObject* build_itemset(AuthorizationItemSet* itemset)
{
    PyObject* result;

    if (itemset == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    } else {
        UInt32 i;
        result = PyTuple_New(itemset->count);
        if (result == NULL) {
            return NULL;
        }

        for (i = 0; i < itemset->count; i++) {
            PyObject* t = PyObjC_ObjCToPython("{_AuthorizationItem=^cL^vI}", itemset->items + i);
            if (t == NULL) {
                Py_DECREF(result);
                return NULL;
            }
            PyTuple_SET_ITEM(result, i, t);
        }
    }
    return result;
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

    if (!parse_itemset(py_rights, &rights)) {
        return NULL;
    }

    if (!parse_itemset(py_environment, &environment)) {
        PyMem_Free(rights.items);
        return NULL;
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

#if PY_MAJOR_VERSION == 2
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

    py_info = build_itemset(info);
    if (info != NULL) {
        AuthorizationFreeItemSet(info);
    }

    return Py_BuildValue("iN", retval, py_info);
}

static PyObject*
m_AuthorizationCopyRights(
        PyObject* module __attribute__((__unused__)),
        PyObject* args)
{
    OSStatus retval;
    AuthorizationRef authorization;
    PyObject* py_authorization;
    AuthorizationRights rights;
    PyObject* py_rights;
    AuthorizationEnvironment environment;
    PyObject* py_environment;
    AuthorizationFlags flags;
    AuthorizationRights* authorizedRights = NULL;
    PyObject*  py_authorizedRights;

    if (!PyArg_ParseTuple(args, "OOOIO", &py_authorization, &py_rights, &py_environment, &flags, &py_authorizedRights)) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(AuthorizationRef), py_authorization, &authorization) == -1) {
        return NULL;
    }

    if (!parse_itemset(py_rights, &rights)) {
        return NULL;
    }
    if (!parse_itemset(py_environment, &environment)) {
        PyMem_Free(rights.items);
        return NULL;
    }
    if (py_authorizedRights != PyObjC_NULL && py_authorizedRights != Py_None) {
        PyMem_Free(rights.items);
        PyMem_Free(environment.items);
        PyErr_SetString(PyExc_ValueError, "authorizedRights must be None or objc.NULL");
        return NULL;
    }

    PyObjC_DURING
        retval = AuthorizationCopyRights(authorization,
                py_rights == Py_None?NULL:&rights,
                py_environment == Py_None?NULL:&environment,
                flags,
                py_authorizedRights == PyObjC_NULL?NULL:&authorizedRights);

    PyObjC_HANDLER
        PyObjCErr_FromObjC(localException);

    PyObjC_ENDHANDLER

    PyMem_Free(rights.items);
    PyMem_Free(environment.items);

    if (PyErr_Occurred()) {
        return NULL;
    }

    if (py_authorizedRights == PyObjC_NULL) {
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
m_AuthorizationCopyRightsAsync(
        PyObject* module __attribute__((__unused__)),
        PyObject* args)
{
    AuthorizationRef authorization;
    PyObject* py_authorization;
    AuthorizationRights rights;
    PyObject* py_rights;
    AuthorizationEnvironment environment;
    PyObject* py_environment;
    AuthorizationFlags flags;
    PyObject*  py_callback;

    if (!PyArg_ParseTuple(args, "OOOIO", &py_authorization, &py_rights, &py_environment, &flags, &py_callback)) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(AuthorizationRef), py_authorization, &authorization) == -1) {
        return NULL;
    }

    if (!parse_itemset(py_rights, &rights)) {
        return NULL;
    }
    if (!parse_itemset(py_environment, &environment)) {
        PyMem_Free(rights.items);
        return NULL;
    }
    if (!PyCallable_Check(py_callback)) {
        PyMem_Free(rights.items);
        PyMem_Free(environment.items);
        PyErr_SetString(PyExc_ValueError, "callback must be callable");
        return NULL;
    }

    Py_INCREF(py_callback);
    PyObjC_DURING
        AuthorizationCopyRightsAsync(authorization,
                py_rights == Py_None?NULL:&rights,
                py_environment == Py_None?NULL:&environment,
                flags,
                ^(OSStatus err, AuthorizationRights* authorizedRights) {
                    PyObject* py_authorizedRights;
                    PyObject* py_result;

                    PyObjC_BEGIN_WITH_GIL

                        if (authorizedRights == NULL) {
                            py_authorizedRights = Py_None; Py_INCREF(Py_None);
                        } else {
                            py_authorizedRights = build_itemset(authorizedRights);
                            if (authorizedRights != NULL) {
                                AuthorizationFreeItemSet(authorizedRights);
                            }
                        }

                        py_result = PyObject_CallFunction(py_callback, "iO", err, py_authorizedRights);
                        if (py_result == NULL) {
                            PyObjC_GIL_FORWARD_EXC();
                        } else if (py_result != Py_None) {
                            Py_DECREF(py_result);
                            PyErr_SetString(PyExc_TypeError, "callbackBlock returned value");
                            PyObjC_GIL_FORWARD_EXC();
                        } else {
                            Py_DECREF(py_result);
                        }

                        Py_DECREF(py_callback);
                        PyMem_Free(rights.items);
                        PyMem_Free(environment.items);

                    PyObjC_END_WITH_GIL
                });

    PyObjC_HANDLER
        PyObjCErr_FromObjC(localException);

    PyObjC_ENDHANDLER

    if (PyErr_Occurred()) {
        Py_DECREF(py_callback);
        return NULL;
    }
    Py_INCREF(Py_None);
    return Py_None;
}

static PyObject*
m_AuthorizationExecuteWithPrivileges(
        PyObject* module __attribute__((__unused__)),
        PyObject* args)
{
    OSStatus retval;
    AuthorizationRef authorization;
    PyObject* py_authorization;
    const char* pathToTool;
    AuthorizationFlags options;
    PyObject* py_pathToTool;
    char** arguments;
    PyObject* py_arguments;
    FILE* communicationsPipe = NULL;
    PyObject* py_communicationsPipe;
    PyObject* seq;
    Py_ssize_t i;

    if (!PyArg_ParseTuple(args, "OOIOO", &py_authorization, &py_pathToTool, &options, &py_arguments, &py_communicationsPipe)) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(AuthorizationRef), py_authorization, &authorization) == -1) {
        return NULL;
    }

#if PY_MAJOR_VERSION == 2
    if (!PyString_Check(py_pathToTool)) {
        PyErr_SetString(PyExc_ValueError, "pathToTool must be a bytes string");
        return NULL;
    }

    pathToTool = PyString_AsString(py_pathToTool);

#else
    if (!PyBytes_Check(py_pathToTool)) {
        PyErr_SetString(PyExc_ValueError, "pathToTool must be a bytes string");
        return NULL;
    }

    pathToTool = PyBytes_AsString(py_pathToTool);
#endif

    seq = PySequence_Fast(py_arguments, "arguments must be a sequence of byte strings");
    if (seq == NULL) {
        return NULL;
    }

    arguments = PyMem_Malloc(sizeof(char*) * PySequence_Fast_GET_SIZE(seq)+1);
    if (arguments == NULL) {
        PyErr_NoMemory();
        return NULL;
    }

    if (py_communicationsPipe != Py_None && py_communicationsPipe != PyObjC_NULL) {
        PyErr_SetString(PyExc_ValueError, "communicationsPipe must be None or objc.NULL");
        return NULL;
    }

    for (i = 0; i < PySequence_Fast_GET_SIZE(seq); i++) {
        PyObject* t = PySequence_Fast_GET_ITEM(seq, i);

#if PY_MAJOR_VERSION == 2
        if (!PyString_Check(t)) {
            PyErr_SetString(PyExc_ValueError, "arguments must be a sequence of byte strings");
            PyMem_Free(arguments);
            Py_DECREF(seq);
            return NULL;
        }
        arguments[i] = PyString_AsString(t);
#else
        if (!PyBytes_Check(t)) {
            PyErr_SetString(PyExc_ValueError, "arguments must be a sequence of byte strings");
            PyMem_Free(arguments);
            Py_DECREF(seq);
            return NULL;
        }
        arguments[i] = PyBytes_AsString(t);
#endif
    }
    arguments[i] = NULL;
    Py_DECREF(seq);

    PyObjC_DURING

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"

        retval = AuthorizationExecuteWithPrivileges(
                    authorization, pathToTool, options, arguments,
                    py_communicationsPipe == PyObjC_NULL?NULL:&communicationsPipe);

#pragma clang diagnostic pop

    PyObjC_HANDLER
        PyObjCErr_FromObjC(localException);

    PyObjC_ENDHANDLER

    PyMem_Free(arguments);

    if (PyErr_Occurred()) {
        return NULL;
    }

    if (py_communicationsPipe == PyObjC_NULL) {
        return Py_BuildValue("iO", retval, Py_None);
    } else {
        return Py_BuildValue("iN", retval, PyObjC_ObjCToPython(@encode(FILE*), &communicationsPipe));
    }
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
    {
        "AuthorizationCopyRights",
        m_AuthorizationCopyRights,
        METH_VARARGS,
        "AuthorizationCopyRights()"
    },
    {
        "AuthorizationCopyRightsAsync",
        m_AuthorizationCopyRightsAsync,
        METH_VARARGS,
        "AuthorizationCopyRightsAsync()"
    },
    {
        "AuthorizationExecuteWithPrivileges",
        m_AuthorizationExecuteWithPrivileges,
        METH_VARARGS,
        "AuthorizationExecuteWithPrivileges()"
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
