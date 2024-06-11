# This file is generated by objective.metadata
#
# Last update: Tue Jun 11 10:15:54 2024
#
# flake8: noqa

import objc, sys
from typing import NewType

if sys.maxsize > 2**32:

    def sel32or64(a, b):
        return b

else:

    def sel32or64(a, b):
        return a


if objc.arch == "arm64":

    def selAorI(a, b):
        return a

else:

    def selAorI(a, b):
        return b


misc = {}
constants = """$$"""
enums = """$ENETFSACCOUNTRESTRICTED@-5999$ENETFSNOAUTHMECHSUPP@-5997$ENETFSNOPROTOVERSSUPP@-5996$ENETFSNOSHARESAVAIL@-5998$ENETFSPWDNEEDSCHANGE@-5045$ENETFSPWDPOLICY@-5046$"""
misc.update({})
misc.update({})
misc.update(
    {
        "kNetFSMountPathKey": "MountPath",
        "kNAUIOptionNoUI": "NoUI",
        "kNetFSServerDisplayNameKey": "ServerDisplayName",
        "kNetFSAuthorityParamsKey": "AuthorityParams",
        "kNetFSMountFlagsKey": "MountFlags",
        "kNetFSSupportsKerberosKey": "SupportsKerberos",
        "kNetFSMountedMultiUserKey": "MountedMultiUser",
        "kNetFSHostKey": "Host",
        "kNetFSOpenURLMountKey": "OpenURLMount",
        "kNetFSConnectedAsUserKey": "MountedByUser",
        "kNetFSHasPasswordKey": "HasPassword",
        "kNetFSSupportsGuestKey": "SupportsGuest",
        "kNetFSAlreadyMountedKey": "AlreadyMounted",
        "kNAUIOptionAllowUI": "AllowUI",
        "kNetFSMechTypesSupportedKey": "MechTypesSupported",
        "kNetFSMountedByUserKey": "MountedByUser",
        "kNetFSMountedWithAuthenticationInfoKey": "MountedWithAuthenticationInfo",
        "kNetFSAuthenticationInfoKey": "AuthenticationInfo",
        "kNetFSNoMountAuthenticationKey": "NoMountAuthentication",
        "kNetFSPrinterShareKey": "PrinterShare",
        "kNetFSUseKerberosKey": "Kerberos",
        "kNetFSMountAtMountDirKey": "MountAtMountDir",
        "kNAUIOptionForceUI": "ForceUI",
        "kNetFSGetAccessRightsKey": "GetAccessRights",
        "kNetFSPasswordKey": "Password",
        "kNetFSMountedByKerberosKey": "MountedByKerberos",
        "kNetFSSchemeKey": "Scheme",
        "kNetFSConnectedMultiUserKey": "ConnectedMultiUser",
        "kNetFSAccessRightsKey": "AccessRights",
        "kNetFSMountedByGuestKey": "MountedByGuest",
        "kNetFSSoftMountKey": "SoftMount",
        "kNetFSChangePasswordKey": "ChangePassword",
        "kNetFSUseGuestKey": "Guest",
        "kNetFSUseAuthenticationInfoKey": "UseAuthenticationInfo",
        "kNetFSPathKey": "Path",
        "kNetFSSupportsChangePasswordKey": "SupportsChangePassword",
        "kNetFSNoUserPreferencesKey": "NoUserPreferences",
        "kNetFSForceNewSessionKey": "ForceNewSession",
        "kNAUIOptionKey": "UIOption",
        "kNetFSConnectedAsGuestKey": "MountedByGuest",
        "kNetFSConnectedWithAuthenticationInfoKey": "ConnectedWithAuthenticationInfo",
        "kNetFSDisplayNameKey": "DisplayName",
        "kNetFSAlternatePortKey": "AlternatePort",
        "kNetFSAllowLoopbackKey": "AllowLoopback",
        "kNetFSMountedURLKey": "MountedURL",
        "kNetFSGuestOnlyKey": "GuestOnly",
        "kNetFSAllowSubMountsKey": "AllowSubMounts",
        "kNetFSUserNameKey": "UserName",
        "kNetFSURLOptionsKey": "URLOptions",
        "kNetFSIsHiddenKey": "IsHidden",
    }
)
functions = {
    "NetFSMountURLProbe": (b"^{__CFString=}^{__CFString=}",),
    "NetFSMountURLAsync": (
        b"i^{__CFURL=}^{__CFURL=}^{__CFString=}^{__CFString=}^{__CFDictionary=}^{__CFDictionary=}^^v@@?",
        "",
        {
            "arguments": {
                8: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": "^v"},
                            1: {"type": "i"},
                            2: {"type": "^v"},
                            3: {"type": "@"},
                        },
                    }
                },
                6: {"type_modifier": "o"},
            }
        },
    ),
    "NetFSMountURLSync": (
        b"i^{__CFURL=}^{__CFURL=}^{__CFString=}^{__CFString=}^{__CFDictionary=}^{__CFDictionary=}^^{__CFArray=}",
        "",
        {"arguments": {6: {"type_modifier": "o"}}},
    ),
    "NetFSMountURLCancel": (b"i^v",),
    "NetFSCopyURLForRemountingVolume": (
        b"^{__CFURL=}^{__CFURL=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "NetFSCFStringtoCString": (
        b"^t^{__CFString=}",
        "",
        {"retval": {"c_array_delimited_by_null": True}},
    ),
}
expressions = {}

# END OF FILE
