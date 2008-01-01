Python Specific notes:
- ArcBall.h's function Matrix3fMulMatrix3f (A, B) uses an unusual 
convention where A' = B * A. The A matrix is changed in place. 
The python function creates a new matrix and operates as A' = A * B.
- ArcBall's math and data structures have largely been implemented
using the Numerical python package. Numerical provides fast, high 
quality, matrix operations and it allows for code that expresses 
the math more succinctly.
- Initialize () doesn't need to generate texture coordinates for 
the sphere quadric because we don't apply an texture maps in this tutorial.
- Python's modulus operator is defined to act differently for negative numbers


------------------------------------------------------------------
Specific links for downloads of Python and components (Windows).
As of July, 2004

Python 2.3 		- http://www.python.org/ftp/python/2.3.4/Python-2.3.4.exe
PyOpenGL 2.0.1	- http://sourceforge.net/project/showfiles.php?group_id=5988&package_id=6035&release_id=193380
Numerical Python v 22	- http://prdownloads.sourceforge.net/numpy/Numeric-22.0.win32-py2.2.exe?download
