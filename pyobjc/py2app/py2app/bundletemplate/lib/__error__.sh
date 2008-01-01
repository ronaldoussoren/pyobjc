#!/bin/sh
#
# This is the default bundletemplate error script
# Note that this DOES NOT present a GUI dialog, because
# it has no output on stdout, and has a return value of 0.
#
if ( test -n "$2" ) ; then
	echo "[$1] Unexpected Exception:" 1>&2
	echo "$2: $3" 1>&2
else
	echo "[$1] Could not find a suitable Python runtime" 1>&2
fi
