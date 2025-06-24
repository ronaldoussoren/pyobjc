#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
#import <Security/Security.h>

static PyObject*
m_SecKeychainFindInternetPassword(PyObject* module __attribute__((__unused__)),
                                  PyObject* args)
{
    OSStatus              retval;
    id                    keychainOrArray;
    PyObject*             py_keychainOrArray;
    Py_ssize_t            serverName_length;
    const char*           serverName;
    PyObject*             py_serverName;
    int                   serverName_token;
    PyObject*             serverName_buffer = NULL;
    Py_buffer             serverName_view;
    Py_ssize_t            securityDomain_length;
    const char*           securityDomain;
    PyObject*             py_securityDomain;
    int                   securityDomain_token;
    PyObject*             securityDomain_buffer = NULL;
    Py_buffer             securityDomain_view;
    Py_ssize_t            accountName_length;
    const char*           accountName;
    PyObject*             py_accountName;
    int                   accountName_token;
    PyObject*             accountName_buffer = NULL;
    Py_buffer             accountName_view;
    Py_ssize_t            path_length;
    const char*           path;
    PyObject*             py_path;
    int                   path_token;
    PyObject*             path_buffer = NULL;
    Py_buffer             path_view;
    UInt16                port;
    SecProtocolType       protocol;
    SecAuthenticationType authenticationType;
    UInt32                password_length = 0;
    PyObject*             py_password_length;
    void*                 passwordData = NULL;
    PyObject*             py_passwordData;
    SecKeychainItemRef    itemRef = NULL;
    PyObject*             py_itemRef;
    const char            string = 't';

    if (!PyArg_ParseTuple(args, "OnOnOnOnOHIIOOO", &py_keychainOrArray,
                          &serverName_length, &py_serverName, &securityDomain_length,
                          &py_securityDomain, &accountName_length, &py_accountName,
                          &path_length, &py_path, &port, &protocol, &authenticationType,
                          &py_password_length, &py_passwordData, &py_itemRef)) {
        return NULL;
    }

    if (depythonify_python_object(py_keychainOrArray, &keychainOrArray) == -1) {
        return NULL;
    }

    serverName_token =
        PyObjC_PythonToCArray(NO, NO, &string, py_serverName, (void**)&serverName,
                              &serverName_length, &serverName_buffer, &serverName_view);
    if (serverName_token == -1) {
        return NULL;
    }

    if (py_securityDomain == Py_None || py_securityDomain == PyObjC_NULL) {
        securityDomain = NULL;

    } else {
        securityDomain_token = PyObjC_PythonToCArray(
            NO, NO, &string, py_securityDomain, (void**)&securityDomain,
            &securityDomain_length, &securityDomain_buffer, &securityDomain_view);
        if (securityDomain_token == -1) {
            PyObjC_FreeCArray(serverName_token, &serverName_view);
            Py_XDECREF(serverName_buffer);
            return NULL;
        }
    }

    if (py_accountName == Py_None || py_accountName == PyObjC_NULL) {
        accountName = NULL;
    } else {
        accountName_token = PyObjC_PythonToCArray(
            NO, NO, &string, py_accountName, (void**)&accountName, &accountName_length,
            &accountName_buffer, &accountName_view);
        if (accountName_token == -1) {
            PyObjC_FreeCArray(serverName_token, &serverName_view);
            Py_XDECREF(serverName_buffer);
            if (py_securityDomain != NULL)
                PyObjC_FreeCArray(securityDomain_token, &securityDomain_view);
            Py_XDECREF(securityDomain_buffer);
            return NULL;
        }
    }

    if (py_path == Py_None || py_path == PyObjC_NULL) {
        path = NULL;
    } else {
        path_token = PyObjC_PythonToCArray(NO, NO, &string, py_path, (void**)&path,
                                           &path_length, &path_buffer, &path_view);
        if (path_token == -1) {
            PyObjC_FreeCArray(serverName_token, &serverName_view);
            Py_XDECREF(serverName_buffer);
            if (py_securityDomain != NULL)
                PyObjC_FreeCArray(securityDomain_token, &securityDomain_view);
            Py_XDECREF(securityDomain_buffer);
            PyObjC_FreeCArray(accountName_token, &accountName_view);
            Py_XDECREF(accountName_buffer);
            return NULL;
        }
    }

    if (py_password_length != Py_None && py_password_length != PyObjC_NULL) {
        PyErr_SetString(PyExc_TypeError, "passwordLength must be None or objc.NULL");
        PyObjC_FreeCArray(serverName_token, (void*)serverName);
        Py_XDECREF(serverName_buffer);
        if (py_securityDomain != NULL)
            PyObjC_FreeCArray(securityDomain_token, &securityDomain_view);
        Py_XDECREF(securityDomain_buffer);
        PyObjC_FreeCArray(accountName_token, &accountName_view);
        Py_XDECREF(accountName_buffer);
        PyObjC_FreeCArray(path_token, &path_view);
        Py_XDECREF(path_buffer);
        return NULL;
    }

    if (py_passwordData != Py_None && py_passwordData != PyObjC_NULL) {
        PyErr_SetString(PyExc_TypeError, "passwordData must be None or objc.NULL");
        PyObjC_FreeCArray(serverName_token, &serverName_view);
        Py_XDECREF(serverName_buffer);
        if (py_securityDomain != NULL)
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
                py_password_length == Py_None ? &password_length : NULL,
                py_passwordData == Py_None ? &passwordData : NULL,
                py_itemRef == Py_None ? &itemRef : NULL);
#pragma clang diagnostic pop

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    PyObjC_FreeCArray(serverName_token, &serverName_view);
    Py_XDECREF(serverName_buffer);
    if (py_securityDomain != NULL)
        PyObjC_FreeCArray(securityDomain_token, &securityDomain_view);
    Py_XDECREF(securityDomain_buffer);
    PyObjC_FreeCArray(accountName_token, &accountName_view);
    Py_XDECREF(accountName_buffer);
    PyObjC_FreeCArray(path_token, &path_view);
    Py_XDECREF(path_buffer);

    if (PyErr_Occurred()) {
        return NULL;
    }

    if (py_passwordData == Py_None) {
        if (passwordData == NULL) {
            py_passwordData = Py_None;
            Py_INCREF(py_passwordData);
        } else {
            py_passwordData = PyBytes_FromStringAndSize(passwordData, password_length);
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
            (void)SecKeychainItemFreeContent(NULL, passwordData);
#pragma clang diagnostic pop

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
            py_itemRef = Py_None;
            Py_INCREF(Py_None);
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
m_SecKeychainFindGenericPassword(PyObject* module __attribute__((__unused__)),
                                 PyObject* args)
{
    OSStatus           retval;
    id                 keychainOrArray;
    PyObject*          py_keychainOrArray;
    Py_ssize_t         serviceName_length;
    const char*        serviceName;
    PyObject*          py_serviceName;
    int                serviceName_token;
    PyObject*          serviceName_buffer = NULL;
    Py_buffer          serviceName_view;
    Py_ssize_t         accountName_length;
    const char*        accountName;
    PyObject*          py_accountName;
    int                accountName_token;
    PyObject*          accountName_buffer = NULL;
    Py_buffer          accountName_view;
    UInt32             password_length = 0;
    PyObject*          py_password_length;
    void*              passwordData = NULL;
    PyObject*          py_passwordData;
    SecKeychainItemRef itemRef = NULL;
    PyObject*          py_itemRef;
    const char         string = 't';

    if (!PyArg_ParseTuple(args, "OnOnOOOO", &py_keychainOrArray, &serviceName_length,
                          &py_serviceName, &accountName_length, &py_accountName,
                          &py_password_length, &py_passwordData, &py_itemRef)) {
        return NULL;
    }

    if (depythonify_python_object(py_keychainOrArray, &keychainOrArray) == -1) {
        return NULL;
    }
    serviceName_token = PyObjC_PythonToCArray(NO, NO, &string, py_serviceName,
                                              (void**)&serviceName, &serviceName_length,
                                              &serviceName_buffer, &serviceName_view);
    if (serviceName_token == -1) {
        return NULL;
    }

    if (py_accountName == Py_None || py_accountName == PyObjC_NULL) {
        accountName = NULL;
    } else {
        accountName_token = PyObjC_PythonToCArray(
            NO, NO, &string, py_accountName, (void**)&accountName, &accountName_length,
            &accountName_buffer, &accountName_view);
        if (accountName_token == -1) {
            PyObjC_FreeCArray(serviceName_token, &serviceName_view);
            Py_XDECREF(serviceName_buffer);
            return NULL;
        }
    }

    if (py_password_length != Py_None && py_password_length != PyObjC_NULL) {
        PyErr_SetString(PyExc_TypeError, "passwordLength must be None or objc.NULL");
        PyObjC_FreeCArray(serviceName_token, &serviceName_view);
        Py_XDECREF(serviceName_buffer);
        PyObjC_FreeCArray(accountName_token, &accountName_view);
        Py_XDECREF(accountName_buffer);
        return NULL;
    }

    if (py_passwordData != Py_None && py_passwordData != PyObjC_NULL) {
        PyErr_SetString(PyExc_TypeError, "passwordData must be None or objc.NULL");
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
                accountName, py_password_length == Py_None ? &password_length : NULL,
                py_passwordData == Py_None ? &passwordData : NULL,
                py_itemRef == Py_None ? &itemRef : NULL);

#pragma clang diagnostic pop
        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    PyObjC_FreeCArray(serviceName_token, &serviceName_view);
    Py_XDECREF(serviceName_buffer);
    PyObjC_FreeCArray(accountName_token, &accountName_view);
    Py_XDECREF(accountName_buffer);

    if (PyErr_Occurred()) {
        return NULL;
    }

    if (py_passwordData == Py_None) {
        if (passwordData == NULL) {
            py_passwordData = Py_None;
            Py_INCREF(py_passwordData);
        } else {
            py_passwordData = PyBytes_FromStringAndSize(passwordData, password_length);
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
            (void)SecKeychainItemFreeContent(NULL, passwordData);
#pragma clang diagnostic pop

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
            py_itemRef = Py_None;
            Py_INCREF(Py_None);
        } else {
            py_itemRef = PyObjC_IdToPython((id)itemRef);
            CFRelease(itemRef);
        }
    } else {
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
        if (itemset->items == NULL) {
            PyErr_NoMemory();
            return 0;
        }

        for (i = 0; i < PyTuple_GET_SIZE(seq); i++) {
            if (PyObjC_PythonToObjC("{_AuthorizationItem=^cL^vI}",
                                    PyTuple_GET_ITEM(seq, i), itemset->items + i)
                < 0) {
                PyMem_Free(itemset->items);
                return 0;
            }
        }
    }
    return 1;
}

static PyObject*
build_itemset(AuthorizationItemSet* itemset)
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
            PyObject* t =
                PyObjC_ObjCToPython("{_AuthorizationItem=^cL^vI}", itemset->items + i);
            if (t == NULL) {
                Py_DECREF(result);
                return NULL;
            }
            PyTuple_SetItem(result, i, t);
        }
    }
    return result;
}

static PyObject*
m_AuthorizationCreate(PyObject* module __attribute__((__unused__)), PyObject* args)
{
    OSStatus                 retval;
    AuthorizationRights      rights;
    PyObject*                py_rights;
    AuthorizationEnvironment environment;
    PyObject*                py_environment;
    AuthorizationFlags       flags;
    AuthorizationRef         authorization = NULL;
    PyObject*                py_authorization;

    rights.items = environment.items = NULL;

    if (!PyArg_ParseTuple(args, "OOIO", &py_rights, &py_environment, &flags,
                          &py_authorization)) {
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

    Py_BEGIN_ALLOW_THREADS
        @try {
            retval = AuthorizationCreate(py_rights == Py_None ? NULL : &rights,
                                         py_environment == Py_None ? NULL : &environment,
                                         flags, &authorization);

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    PyMem_Free(rights.items);
    PyMem_Free(environment.items);

    if (PyErr_Occurred()) {
        return NULL;
    }

    return Py_BuildValue("iN", retval,
                         PyObjC_ObjCToPython(@encode(AuthorizationRef), &authorization));
}

static PyObject*
m_AuthorizationCopyInfo(PyObject* module __attribute__((__unused__)), PyObject* args)
{
    OSStatus              retval;
    AuthorizationRef      authorization;
    PyObject*             py_authorization;
    char*                 tag;
    PyObject*             py_tag;
    AuthorizationItemSet* info = NULL;
    PyObject*             py_info;

    if (!PyArg_ParseTuple(args, "OOO", &py_authorization, &py_tag, &py_info)) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(AuthorizationRef), py_authorization, &authorization)
        == -1) {
        return NULL;
    }

    if (py_tag == Py_None) {
        tag = NULL;

    } else if (PyBytes_Check(py_tag)) {
        tag = PyBytes_AsString(py_tag);

    } else {
        PyErr_SetString(PyExc_ValueError, "tag must be byte string or None");
        return NULL;
    }

    if (py_info != Py_None) {
        PyErr_SetString(PyExc_ValueError, "info must be None");
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            retval = AuthorizationCopyInfo(authorization, tag, &info);

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

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
m_AuthorizationCopyRights(PyObject* module __attribute__((__unused__)), PyObject* args)
{
    OSStatus                 retval;
    AuthorizationRef         authorization;
    PyObject*                py_authorization;
    AuthorizationRights      rights;
    PyObject*                py_rights;
    AuthorizationEnvironment environment;
    PyObject*                py_environment;
    AuthorizationFlags       flags;
    AuthorizationRights*     authorizedRights = NULL;
    PyObject*                py_authorizedRights;

    if (!PyArg_ParseTuple(args, "OOOIO", &py_authorization, &py_rights, &py_environment,
                          &flags, &py_authorizedRights)) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(AuthorizationRef), py_authorization, &authorization)
        == -1) {
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

    Py_BEGIN_ALLOW_THREADS
        @try {
            retval = AuthorizationCopyRights(
                authorization, py_rights == Py_None ? NULL : &rights,
                py_environment == Py_None ? NULL : &environment, flags,
                py_authorizedRights == PyObjC_NULL ? NULL : &authorizedRights);

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

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
m_AuthorizationCopyRightsAsync(PyObject* module __attribute__((__unused__)),
                               PyObject* args)
{
    AuthorizationRef         authorization;
    PyObject*                py_authorization;
    AuthorizationRights      rights;
    PyObject*                py_rights;
    AuthorizationEnvironment environment;
    PyObject*                py_environment;
    AuthorizationFlags       flags;
    PyObject*                py_callback;

    if (!PyArg_ParseTuple(args, "OOOIO", &py_authorization, &py_rights, &py_environment,
                          &flags, &py_callback)) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(AuthorizationRef), py_authorization, &authorization)
        == -1) {
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
    Py_BEGIN_ALLOW_THREADS
        @try {
            AuthorizationCopyRightsAsync(
                authorization, py_rights == Py_None ? NULL : &rights,
                py_environment == Py_None ? NULL : &environment, flags,
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
                          PyObjC_GIL_FORWARD_EXC();
                      } else if (py_result != Py_None) {
                          Py_DECREF(py_result);
                          PyErr_SetString(PyExc_TypeError,
                                          "callbackBlock returned value");
                          PyObjC_GIL_FORWARD_EXC();
                      } else {
                          Py_DECREF(py_result);
                      }

                      Py_DECREF(py_callback);
                      PyMem_Free(rights.items);
                      PyMem_Free(environment.items);

                  PyObjC_END_WITH_GIL
                });

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        Py_DECREF(py_callback);
        return NULL;
    }
    Py_INCREF(Py_None);
    return Py_None;
}

static PyObject*
m_AuthorizationExecuteWithPrivileges(PyObject* module __attribute__((__unused__)),
                                     PyObject* args)
{
    OSStatus           retval;
    AuthorizationRef   authorization;
    PyObject*          py_authorization;
    const char*        pathToTool;
    AuthorizationFlags options;
    PyObject*          py_pathToTool;
    char**             arguments;
    PyObject*          py_arguments;
    FILE*              communicationsPipe = NULL;
    PyObject*          py_communicationsPipe;
    PyObject*          seq;
    Py_ssize_t         i;

    if (!PyArg_ParseTuple(args, "OOIOO", &py_authorization, &py_pathToTool, &options,
                          &py_arguments, &py_communicationsPipe)) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(AuthorizationRef), py_authorization, &authorization)
        == -1) {
        return NULL;
    }

    if (!PyBytes_Check(py_pathToTool)) {
        PyErr_SetString(PyExc_ValueError, "pathToTool must be a bytes string");
        return NULL;
    }

    pathToTool = PyBytes_AsString(py_pathToTool);

    seq = PySequence_Tuple(py_arguments);
    if (seq == NULL) {
        return NULL;
    }

    arguments = PyMem_Malloc(sizeof(char*) * PyTuple_GET_SIZE(seq) + 1);
    if (arguments == NULL) {
        PyErr_NoMemory();
        return NULL;
    }

    if (py_communicationsPipe != Py_None && py_communicationsPipe != PyObjC_NULL) {
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
                py_communicationsPipe == PyObjC_NULL ? NULL : &communicationsPipe);

#pragma clang diagnostic pop

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    PyMem_Free(arguments);

    if (PyErr_Occurred()) {
        return NULL;
    }

    if (py_communicationsPipe == PyObjC_NULL) {
        return Py_BuildValue("iO", retval, Py_None);
    } else {
        return Py_BuildValue("iN", retval,
                             PyObjC_ObjCToPython(@encode(FILE*), &communicationsPipe));
    }
}

static PyMethodDef mod_methods[] = {
    {"SecKeychainFindInternetPassword", m_SecKeychainFindInternetPassword, METH_VARARGS,
     "SecKeychainFindInternetPassword()"},
    {"SecKeychainFindGenericPassword", m_SecKeychainFindGenericPassword, METH_VARARGS,
     "SecKeychainFindGenericPassword()"},
    {"AuthorizationCreate", m_AuthorizationCreate, METH_VARARGS, "AuthorizationCreate()"},
    {"AuthorizationCopyInfo", m_AuthorizationCopyInfo, METH_VARARGS,
     "AuthorizationCopyInfo()"},
    {"AuthorizationCopyRights", m_AuthorizationCopyRights, METH_VARARGS,
     "AuthorizationCopyRights()"},
    {"AuthorizationCopyRightsAsync", m_AuthorizationCopyRightsAsync, METH_VARARGS,
     "AuthorizationCopyRightsAsync()"},
    {"AuthorizationExecuteWithPrivileges", m_AuthorizationExecuteWithPrivileges,
     METH_VARARGS, "AuthorizationExecuteWithPrivileges()"},

    {0, 0, 0, 0} /* sentinel */
};

static int
mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) == -1)
        return -1;

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
