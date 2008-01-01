# $Id: double.tcl,v 1.1 2001/05/14 22:55:19 twburton Exp $

# Togl - a Tk OpenGL widget
# Copyright (C) 1996  Brian Paul and Ben Bederson
# See the LICENSE file for copyright details.


# $Log: double.tcl,v $
# Revision 1.1  2001/05/14 22:55:19  twburton
# Add Togl
#
# Revision 1.1  1999/07/15 21:13:12  dacvs
# Togl, again!
#
# Revision 1.3  1998/03/12 03:52:31  brianp
# now sharing display lists between the widgets
#
# Revision 1.2  1996/10/23 23:31:56  brianp
# added -ident options to togl calls
#
# Revision 1.1  1996/10/23 23:17:22  brianp
# Initial revision
#


# An Tk/OpenGL widget demo with two windows, one single buffered and the
# other double buffered.



proc setup {} {
    wm title . "Single vs Double Buffering"

    frame .f1

    # create first Togl widget
    togl .f1.o1 -width 200 -height 200  -rgba true  -double false -depth true -ident Single

    # create second Togl widget, share display lists with first widget
    togl .f1.o2 -width 200 -height 200  -rgba true  -double true -depth true -ident Double -sharelist Single

    scale  .sx   -label {X Axis} -from 0 -to 360 -command {setAngle x} -orient horizontal
    scale  .sy   -label {Y Axis} -from 0 -to 360 -command {setAngle y} -orient horizontal
    button .btn  -text Quit -command exit

    bind .f1.o1 <B1-Motion> {
	motion_event [lindex [%W config -width] 4] \
		     [lindex [%W config -height] 4] \
		     %x %y
    }

    bind .f1.o2 <B1-Motion> {
	motion_event [lindex [%W config -width] 4] \
		     [lindex [%W config -height] 4] \
		     %x %y
    }

    pack .f1.o1 .f1.o2  -side left -padx 3 -pady 3 -fill both -expand t
    pack .f1  -fill both -expand t
    pack .sx  -fill x
    pack .sy  -fill x
    pack .btn -fill x
}



# This is called when mouse button 1 is pressed and moved in either of
# the OpenGL windows.
proc motion_event { width height x y } {
    .f1.o1 setXrot [expr 360.0 * $y / $height]
    .f1.o2 setXrot [expr 360.0 * $y / $height]
    .f1.o1 setYrot [expr 360.0 * ($width - $x) / $width]
    .f1.o2 setYrot [expr 360.0 * ($width - $x) / $width]

#    .sx set [expr 360.0 * $y / $height]
#    .sy set [expr 360.0 * ($width - $x) / $width]

    .sx set [getXrot]
    .sy set [getYrot]
}

# This is called when a slider is changed.
proc setAngle {axis value} {
    global xAngle yAngle zAngle

    switch -exact $axis {
	x {.f1.o1 setXrot $value
	   .f1.o2 setXrot $value}
	y {.f1.o1 setYrot $value
	   .f1.o2 setYrot $value}
    }
}

# Execution starts here!
setup
