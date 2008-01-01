# $Id: overlay.tcl,v 1.1 2001/05/14 22:55:19 twburton Exp $

# Togl - a Tk OpenGL widget
# Copyright (C) 1996  Brian Paul and Ben Bederson
# See the LICENSE file for copyright details.


# $Log: overlay.tcl,v $
# Revision 1.1  2001/05/14 22:55:19  twburton
# Add Togl
#
# Revision 1.1  1999/07/15 21:13:12  dacvs
# Togl, again!
#
# Revision 1.2  1998/01/24 14:05:50  brianp
# added quit button (Ben Bederson)
#
# Revision 1.1  1997/03/07 01:26:38  brianp
# Initial revision
#
#


# A Tk/OpenGL widget demo using an overlay.


proc setup {} {
    wm title . "Overlay demo"

    togl .win -width 200 -height 200  -rgba true -double false -overlay true
    button .btn  -text Quit -command exit

    pack .win -expand true -fill both
    pack .btn -expand true -fill both
}



# Execution starts here!
setup
