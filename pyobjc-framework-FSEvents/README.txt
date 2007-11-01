Wrappers for the 'FSEvents' subsystem in Carbon. 

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

Note that an FSEventStreamRef is not a CoreFoundation type and you'll have to
maintain reference-counts yourself.
