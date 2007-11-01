# $Id: Makefile,v 1.1 2001/05/14 22:55:19 twburton Exp $

# Togl - a Tk OpenGL widget
# Version 1.5
# Copyright (C) 1996-1997  Brian Paul and Ben Bederson
# See the LICENSE file for copyright details.


# $Log: Makefile,v $
# Revision 1.1  2001/05/14 22:55:19  twburton
# Add Togl
#
# Revision 1.1  1999/07/15 21:13:12  dacvs
# Togl, again!
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
COPTS = -c -O

# Shared library linker command:
SHLINK = cc -G

# Name for the shared lib:
#SH_LIB = libtogl.so.1.3
SH_LIB = 

# Where to find tcl.h, tk.h, OpenGL/Mesa headers, etc:
INCLUDES = -I/usr/local/include -I/usr/include/tcl

# Where to find libtcl.a, libtk.a, OpenGL/Mesa libraries:
LIBDIRS = -L/usr/local/lib

# Libraries to link with (-ldl for Linux only?):
LIBS = -ltk -ltcl -lGLU -lGL -L/usr/X11/lib -lX11 -lXmu -lXext -lXt -lm -ldl

TK_FLAGS =


#### Shouldn't have to change anything beyond this point ####


CFLAGS = $(COPTS) $(INCLUDES) $(TK_FLAGS)

LFLAGS = $(LIBDIRS)


DEMOS = $(SH_LIB) double texture index overlay gears


default: $(DEMOS)


# double demo
double: double.o togl.o
	$(CC) $(LFLAGS) double.o togl.o $(LIBS) -o $@

double.o: double.c togl.h
	$(CC) $(CFLAGS) double.c


# texture demo
texture: texture.o image.o togl.o
	$(CC) $(LFLAGS) texture.o image.o togl.o $(LIBS) -o $@

texture.o: texture.c togl.h
	$(CC) $(CFLAGS) texture.c

image.o: image.c
	$(CC) $(CFLAGS) image.c


# color index demo
index: index.o togl.o
	$(CC) $(LFLAGS) index.o togl.o $(LIBS) -o $@

index.o: index.c togl.h
	$(CC) $(CFLAGS) index.c


# overlay demo
overlay: overlay.o togl.o
	$(CC) $(LFLAGS) overlay.o togl.o $(LIBS) -o $@

overlay.o: overlay.c togl.h
	$(CC) $(CFLAGS) overlay.c


# gears demo
gears: gears.o togl.o
	$(CC) $(LFLAGS) gears.o togl.o $(LIBS) -o $@

gears.o: gears.c togl.h
	$(CC) $(CFLAGS) gears.c


# the togl widget
togl.o: togl.c togl.h
	$(CC) $(CFLAGS) togl.c


#$(SH_LIB): togl.o
#	$(SHLINK) $(LFLAGS) togl.o $(LIBS) -o $@ 



clean:
	-rm -f *.o *~ core

realclean:
	-rm -f *.o *~ core
	-rm -f $(DEMOS)



TOGL = Togl-1.5

FILES = \
	$(TOGL)/README		\
	$(TOGL)/Togl.html	\
	$(TOGL)/LICENSE		\
	$(TOGL)/Makefile	\
	$(TOGL)/*.[ch]		\
	$(TOGL)/*.tcl		\
	$(TOGL)/tree2.rgba	\
	$(TOGL)/ben.rgb

tar:
	cd .. ; \
	tar -cvf $(TOGL).tar $(FILES) ; \
	gzip $(TOGL).tar ; \
	mv $(TOGL).tar.gz $(TOGL)


zip:
	cd .. ; \
	zip -r $(TOGL).zip $(FILES) ; \
	mv $(TOGL).zip $(TOGL)
