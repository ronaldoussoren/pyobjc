/*
 * Mapping of static items in the AddressBook framework
 */
#include <Python.h>

#import <SecurityInterface/SFAuthorizationView.h>
#import <SecurityInterface/SFChooseIdentityPanel.h>
#import <SecurityInterface/SFCertificatePanel.h>
#import <SecurityInterface/SFKeychainSavePanel.h>
#import <SecurityInterface/SFCertificateTrustPanel.h>
#import <SecurityInterface/SFKeychainSettingsPanel.h>
#import <SecurityInterface/SFCertificateView.h>

#import <CoreFoundation/CoreFoundation.h>

#include "pyobjc-api.h"
#include "wrapper-const-table.h"

static PyMethodDef sec_methods[] = {
	{ 0, 0, 0, 0 }
};


PyDoc_STRVAR(sec_doc,
"Cocoa._SecurityInterface defines constants, types and global functions used by "
"Cocoa.SecurityInterface."
);


#include "_SecInt_Enum.inc"
#include "_SecInt_Str.inc"

void init_SecurityInterface(void);
void init_SecurityInterface(void)
{
	PyObject *m, *d;
	CFBundleRef bundle;

	m = Py_InitModule4("_SecurityInterface", sec_methods, 
		sec_doc, NULL, PYTHON_API_VERSION);
	if (!m) return;

	d = PyModule_GetDict(m);
	if (!d) return;

	if (PyObjC_ImportAPI(m) < 0) {
		return;
	}

	/* SecurityFoundation.framework has no @constant values to bring in... */
	bundle = CFBundleGetBundleWithIdentifier(CFSTR("com.apple.securityinterface"));

	if (register_ints(d, enum_table) < 0) return;
	if (register_variableList(d, bundle, string_table, 
		(sizeof(string_table)/sizeof(string_table[0])-1)) < 0) return;

	//CFRelease(bundle);
}
