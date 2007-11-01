# $Id: Makefile,v 1.1 2003/02/14 20:18:20 mcfletch Exp $

# Togl - a Tk OpenGL widget
# Version 1.6
# Copyright (C) 1996-1997  Brian Paul and Ben Bederson
# See the LICENSE file for copyright details.


# $Log: Makefile,v $
# Revision 1.1  2003/02/14 20:18:20  mcfletch
# Switch to TOGL 1.6 (from CVS) which should support Tk 8.4 (and earlier versions as well)
#
# Revision 1.20  2001/12/20 13:59:31  beskow
# Improved error-handling in togl.c in case of window creation failure
# Added pkgIndex target to makefile
# Updated documentation to reflect stubs-interface (Togl.html + new README.stubs)
# Added tk8.4a3 headers
# Removed obsolete Tk internal headers
#
# Revision 1.19  2001/01/29 18:11:53  brianp
# Jonas Beskow's changes to use Tcl/Tk stub interface
#
# Revision 1.18  2000/12/02 18:37:44  brianp
# updates from Bruce Cameron
#
# Revision 1.17  2000/01/05 19:38:39  brianp
# added more include and lib paths for X11
#
# Revision 1.16  1999/05/16 15:10:15  brianp
# added Windows-related files to FILES list
#
# Revision 1.15  1998/10/14 01:27:52  brianp
# bumped version to 1.6
#
# Revision 1.14  1998/03/12 04:11:13  brianp
# updated LIBS for RedHat Linux 5.0
#
# Revision 1.13  1998/03/12 03:08:43  brianp
# added gears demo
#
# Revision 1.12  1997/12/11 02:21:41  brianp
# updated version to 1.5
#
# Revision 1.11  1997/09/18 03:43:00  brianp
# added zip archive target
#
# Revision 1.10  1997/09/17 02:51:45  brianp
# updated tar file list
#
# Revision 1.9  1997/09/17 02:46:01  brianp
# updated for version 1.4
#
# Revision 1.8  1997/03/07 01:25:42  brianp
# added overlay demo
#
# Revision 1.7  1997/02/16 10:03:19  brianp
# updated for version 1.3
#
# Revision 1.6  1996/12/13 21:23:41  brianp
# added -L/usr/X11/lib to LIBS
#
# Revision 1.5  1996/11/05 02:38:30  brianp
# added -f flag to rm commands
# added Togl.html to tar file
#
# Revision 1.4  1996/10/25 03:45:18  brianp
# changed tar commands
#
# Revision 1.3  1996/10/25 00:46:29  brianp
# added SHLINK and SH_LIB stuff
#
# Revision 1.2  1996/10/25 00:43:12  brianp
# misc cleanups
#
# Revision 1.1  1996/10/23 23:15:09  brianp
# Initial revision
#



# Makefile for Togl demos
# You'll probably have to tinker with these macros:


# The C compiler:
CC = cc

# Compiler options:
# for DEC
#COPTS = -c -g -signed -DALPHA
# for HP
#COPTS = -c -g -Ae +z -Wl,+s,+b:,-B immediate  +DAportable -DHP
# for IBM
#COPTS = -c -g -qchars=signed -DIBM
# for PC_LINUX
COPTS = -c -g -fPIC -mcpu=i586 -DPC_LINUX -DDEBUG -DUSE_TCL_STUBS -DUSE_TK_STUBS -DUSE_LOCAL_TK_H
# for SGI
#COPTS = -c -g -n32 -signed -DSGI
# for SUN
#COPTS = -c -g -Xc -mt -DSUN


# Shared library linker command:
SHLINK = cc -shared


# Where to find tcl.h, tk.h, OpenGL/Mesa headers, etc:

TCL_PREFIX = /usr/local
TCL_VER = 8.3

# uncomment exactly one
TCL_INCLUDE = -I$(TCL_PREFIX)/include
#TCL_INCLUDE = -I/pkg/tcl-tk/8.3.0/include
# for DEC
#INCLUDES = $(TCL_INCLUDE)
# for HP
#INCLUDES = -I/opt/graphics/OpenGL/include $(TCL_INCLUDE)
# for IBM
#INCLUDES = -I/usr/lpp/OpenGL/include $(TCL_INCLUDE)
# for PC_LINUX
INCLUDES = -I/usr/X11R6/include $(TCL_INCLUDE)
# for SGI
#INCLUDES = $(TCL_INCLUDE)
# for SUN
#INCLUDES = -I/usr/openwin/include $(TCL_INCLUDE)


# Where to find libtcl.a, libtk.a, OpenGL/Mesa libraries:
# uncomment exactly one
TCL_LIB = -L$(TCL_PREFIX)/lib
# for DEC
#LIBDIRS =  $(TCL_LIB)
# for HP
#LIBDIRS = -L/opt/graphics/OpenGL/lib $(TCL_LIB)
# for IBM
#LIBDIRS = -L/usr/lpp/OpenGL/lib $(TCL_LIB)
# for PC_LINUX
LIBDIRS = $(TCL_LIB) -L/usr/X11R6/lib -Xlinker -rpath -Xlinker $(TCL_PREFIX)/lib
# for SGI
#LIBDIRS = $(TCL_LIB)
# for SUN
#LIBDIRS = -L/usr/openwin/lib $(TCL_LIB)

TCL_LIBS = -ltcl$(TCL_VER) -ltk$(TCL_VER)
TCL_STUB_LIBS = -ltclstub$(TCL_VER) -ltkstub$(TCL_VER)

# Libraries to link with (-ldl for Linux only?):
# NOTE: use -ltcl8.1 -ltk8.1 for Tcl/Tk version 8.1
LIBS = $(TCL_LIBS) -lGLU -lGL -L/usr/X11/lib -lX11 -lXmu -lXext -lXt -lm -ldl
STUB_LIBS = $(TCL_STUB_LIBS) -lGLU -lGL -L/usr/X11/lib -lX11 -lXmu -lXext -lXt -lm -ldl

TK_FLAGS =


#### Shouldn't have to change anything beyond this point ####


CFLAGS = $(COPTS) $(INCLUDES) $(TK_FLAGS)

LFLAGS = $(LIBDIRS)


all: togl.so double.so texture.so index.so overlay.so gears.so pkgIndex

# the togl widget
togl.o: togl.c togl.h
	$(CC) $(CFLAGS) togl.c

togl.so: togl.o
	$(SHLINK) $(LFLAGS) togl.o $(STUB_LIBS) -o $@ 

# double demo
double.so: double.o togl.o
	$(SHLINK) $(LFLAGS) double.o togl.o $(STUB_LIBS) -o $@

double.o: double.c togl.h
	$(CC) $(CFLAGS) double.c


# texture demo
texture.so: texture.o image.o togl.o
	$(SHLINK) $(LFLAGS) texture.o image.o togl.o $(STUB_LIBS) -o $@

texture.o: texture.c togl.h
	$(CC) $(CFLAGS) texture.c

image.o: image.c
	$(CC) $(CFLAGS) image.c


# color index demo
index.so: index.o togl.o
	$(SHLINK) $(LFLAGS) index.o togl.o $(STUB_LIBS) -o $@

index.o: index.c togl.h
	$(CC) $(CFLAGS) index.c


# overlay demo
overlay.so: overlay.o togl.o
	$(SHLINK) $(LFLAGS) overlay.o togl.o $(STUB_LIBS) -o $@

overlay.o: overlay.c togl.h
	$(CC) $(CFLAGS) overlay.c


# gears demo
gears.so: gears.o togl.o
	$(SHLINK) $(LFLAGS) gears.o togl.o $(STUB_LIBS) -o gears.so

gears.o: gears.c togl.h
	$(CC) $(CFLAGS) gears.c


clean:
	-rm -f *.o *.so *~ core

realclean:
	-rm -f *.o *~ core
	-rm -f $(DEMOS)


TOGL_VERSION = $(shell grep TOGL_VERSION togl.h | cut -f 3 -d " ")
#TOGL = Togl-$(TOGL_VERSION)
TOGL = Togl
ARCH = $(shell uname -s)

FILES = \
	$(TOGL)/Togl.html	\
	$(TOGL)/LICENSE		\
	$(TOGL)/Makefile	\
	$(TOGL)/Makefile.vc	\
	$(TOGL)/*.[ch]		\
	$(TOGL)/*.tcl		\
	$(TOGL)/tree2.rgba	\
	$(TOGL)/ben.rgb

pkgIndex:
	echo 'puts [pkg::create -name Togl -version $(TOGL_VERSION) -load togl[info sharedlibextension]]' | tclsh > pkgIndex.tcl 

tar:
	cd .. ; \
	tar -cvf $(TOGL).tar $(FILES) ; \
	gzip $(TOGL).tar ; \
	mv $(TOGL).tar.gz $(TOGL)


zip:
	cd .. ; \
	zip -r $(TOGL).zip $(FILES) ; \
	mv $(TOGL).zip $(TOGL)

binpkg: togl.so pkgIndex
	rm -rf $(TOGL)-$(TOGL_VERSION)
	mkdir $(TOGL)-$(TOGL_VERSION)
	mkdir $(TOGL)-$(TOGL_VERSION)/demos
	cp togl.so pkgIndex.tcl $(TOGL)-$(TOGL_VERSION)
	cp gears.so texture.so double.so $(TOGL)-$(TOGL_VERSION)/demos
	cp gears.tcl texture.tcl double.tcl $(TOGL)-$(TOGL_VERSION)/demos
	tar -cvf - $(TOGL)-$(TOGL_VERSION) $(TOGL)-$(TOGL_VERSION)-$(ARCH).tar.gz | gzip > $(TOGL)-$(TOGL_VERSION)-$(ARCH).tar.gz

