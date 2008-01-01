#!/bin/sh
# the next line restarts using wish \
exec wish "$0" "$@"

# Togl - a Tk OpenGL widget
# Copyright (C) 1996-1997  Brian Paul and Ben Bederson
# See the LICENSE file for copyright details.


#
# Test Togl using GL Gears Demo
#
# Copyright (C) 1997 Philip Quaife
#

load [file dirname [info script]]/gears[info sharedlibextension]

proc setup {} {
    global startx starty xangle0 yangle0 xangle yangle RotCnt
    global vTime
    set RotCnt 1
    set xangle 0.0
    set yangle 0.0
    set vTime 100
    wm title . "Rotating Gear Widget Test"

    label .t -text "Click and drag to rotate image"
    pack .t -side top -padx 2 -pady 10
    frame .f
    pack .f -side top
    button .f.n1 -text "  Add " -command AutoRot
    button .f.r1 -text "Remove" -command DelRot
    button .f.b1 -text " Quit " -command exit 
    entry .f.t -width 4 -textvariable vTime
    pack .f.n1 .f.t .f.r1 .f.b1 -side left -anchor w -padx 5
    newRot .w0 10

}
proc AutoRot {} {
    global RotCnt vTime
    newRot .w$RotCnt $vTime
    set RotCnt [expr $RotCnt + 1]
}

proc DelRot {} {
    global RotCnt vTime
    if { $RotCnt != 0 } {
      set RotCnt [expr $RotCnt - 1]
      destroy .w$RotCnt
    }
}

proc newRot {win {tick 100} } {
    togl $win -width 200 -height 200  -rgba true  -double true  -depth true -privatecmap false  -time $tick
    bind $win <ButtonPress-1> {RotStart %x %y %W}
    bind $win <B1-Motion> {RotMove %x %y %W}
    pack $win -expand true -fill both
}

proc RotStart {x y W } {
    global startx starty xangle0 yangle0 xangle yangle
	set startx $x
	set starty $y
        set vPos [$W position]
	set xangle0 [lindex $vPos 0]
	set yangle0 [lindex $vPos 1]
    }

proc RotMove {x y W} {
    global startx starty xangle0 yangle0 xangle yangle
        set xangle [expr $xangle0 + ($x - $startx)  ]
        set yangle [expr $yangle0 + ($y - $starty)  ]
        $W rotate $xangle $yangle
    }

setup
