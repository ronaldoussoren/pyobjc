Final version of the Todo application from 'Learning Cocoa' (O'reilly),
translated to python.

The nib-file is unchanged from the version in the tar-archive downloaded
from the o'reilly website.

Notes:
- The code doesn't work correctly at the moment. 
  * Loading does not work. The code uses NSCoder and the methods for
    decoding C-types have not been wrapped yet. Adding this is not very 
    hard.
  * The first line in the list ToDo items doesn't show unless the field
    is selected. The objective-C version has the same problem. 

- This is a minimal translation, the application logic has not been
  'pythonified'. 

- There are two blocks of code that are not filled in in the objective-C 
  version (left as an extercise for the reader). I've not yet written those
  pieces.
