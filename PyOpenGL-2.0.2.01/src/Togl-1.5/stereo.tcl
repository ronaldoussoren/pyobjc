# $Id: stereo.tcl,v 1.1 2001/05/14 22:55:19 twburton Exp $

# Togl - a Tk OpenGL widget
# Copyright (C) 1996  Brian Paul and Ben Bederson
# See the LICENSE file for copyright details.


# $Log: stereo.tcl,v $
# Revision 1.1  2001/05/14 22:55:19  twburton
# Add Togl
#
# Revision 1.1  1999/07/15 21:13:12  dacvs
# Togl, again!
#
# Revision 1.1  1997/10/01 02:53:12  brianp
# Initial revision
#
#
# Revision 1.1  1997/9/28 18:54:46  Ben Evans
# Initial revision. Based on double.tcl
#


# An Tk/OpenGL widget demo with two windows, one single buffered and the
# other double buffered.



proc setup {} {
    global scale
    set scale 1.0
    wm title . "Full Screen Stereo Buffering"

    frame .f1
    togl .f1.o1 -width 200 -height 200  -rgba true  -stereo true -double true -depth true -ident "stereo buffer"

    scale  .sx   -label {X Axis} -from 0 -to 360 -command {setAngle x} -orient horizontal
    scale  .sy   -label {Y Axis} -from 0 -to 360 -command {setAngle y} -orient horizontal
    button .btn  -text Quit -command exit

    bind .f1.o1 <B1-Motion> {
	motion_event [lindex [%W config -width] 4] \
		     [lindex [%W config -height] 4] \
		     %x %y
    }

    bind .f1.o1 <ButtonPress-2> {
        set startx %x
        set starty %y
        set scale0 $scale
    }

    bind .f1.o1 <B1-B2-Motion> {
        set q [ expr ($starty - %y) / 400.0 ]
        set scale [expr $scale0 * exp($q)]
        .f1.o1 scale $scale
    }

    pack .f1.o1  -side left -padx 3 -pady 3 -fill both -expand t
    pack .f1  -fill both -expand t
    pack .sx  -fill x
    pack .sy  -fill x
    pack .btn -fill x

    puts "use /usr/gfx/setmon -n 60HZ to reset display and /usr/gfx/setmon -n STR_TOP to put in display in stereo mode"

}



# This is called when mouse button 1 is pressed and moved in either of
# the OpenGL windows.
proc motion_event { width height x y } {
    .f1.o1 setXrot [expr 360.0 * $y / $height]
    .f1.o1 setYrot [expr 360.0 * ($width - $x) / $width]

#    .sx set [expr 360.0 * $y / $height]
#    .sy set [expr 360.0 * ($width - $x) / $width]

    .sx set [getXrot]
    .sy set [getYrot]
}

# This is called when a slider is changed.
proc setAngle {axis value} {
    global xAngle yAngle zAngle

    switch -exact $axis {
	x {.f1.o1 setXrot $value}
	y {.f1.o1 setYrot $value}
    }
}

# Execution starts here!
setup
