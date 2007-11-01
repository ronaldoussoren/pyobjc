#!/bin/sh
#
# This is the default apptemplate error script
#
if ( test -n "$2" ) ; then 
	echo "$1 Error"
	echo "An unexpected error has occurred during execution of the main script"
	echo ""
	echo "$2: $3"
	echo ""
	echo "See the Console for a detailed traceback."
else
	echo "$1 Error"
	echo "MacPython 2.3 is required to run this application.";
	echo "ERRORURL: http://homepages.cwi.nl/~jack/macpython/index.html Visit the MacPython Website";
fi
