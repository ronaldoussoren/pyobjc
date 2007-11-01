#!/bin/sh
# the next line restarts using wish \
exec wish "$0" "$@"

# $Id: overlay.tcl,v 1.1 2003/02/14 20:18:20 mcfletch Exp $

# Togl - a Tk OpenGL widget
# Copyright (C) 1996  Brian Paul and Ben Bederson
# See the LICENSE file for copyright details.


# $Log: overlay.tcl,v $
# Revision 1.1  2003/02/14 20:18:20  mcfletch
# Switch to TOGL 1.6 (from CVS) which should support Tk 8.4 (and earlier versions as well)
#
# Revision 1.4  2001/12/20 13:59:31  beskow
# Improved error-handling in togl.c in case of window creation failure
# Added pkgIndex target to makefile
# Updated documentation to reflect stubs-interface (Togl.html + new README.stubs)
# Added tk8.4a3 headers
# Removed obsolete Tk internal headers
#
# Revision 1.3  2001/01/29 18:11:53  brianp
# Jonas Beskow's changes to use Tcl/Tk stub interface
#
# Revision 1.2  1998/01/24 14:05:50  brianp
# added quit button (Ben Bederson)
#
# Revision 1.1  1997/03/07 01:26:38  brianp
# Initial revision
#
#


# A Tk/OpenGL widget demo using an overlay.

load [file dirname [info script]]/overlay[info sharedlibextension]

proc setup {} {
    wm title . "Overlay demo"

    togl .win -width 200 -height 200  -rgba true -double false -overlay true
    button .btn  -text Quit -command exit

    pack .win -expand true -fill both
    pack .btn -expand true -fill both
}



# Execution starts here!
setup
