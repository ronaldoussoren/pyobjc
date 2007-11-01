Wrappers for framework 'SystemConfiguration'. 

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

NOTE: all callback registriation APIs, such as SCNetworkReachabilitySetCallback, have a 
single python object as the 'info' instead of the structure that is used in Obejctive-C

Another magic value: kSCNetworkInterfaceIPv4
