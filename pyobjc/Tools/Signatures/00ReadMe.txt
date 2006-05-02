This tool can be used to find methods that have signatures that PyObjC isn't
able to bridge without further help.

Run this tool every time Apple releases a new version of Xcode to check which
methods need work (either an updated signature string or manual wrapping).

To use: start the Signatures application and select the Scan button. You can
either view all methods that were found and have a signature that needs help,
or only those that haven't been reviewed/fixed yet. The latter is usually the
best.

Press the 'Generate' button to create python files that set the rigth signature
at runtime.

Note: this will use the installed copy of PyObjC to actually find signatures!

TODO:
- The application should either save automaticly, or warn about unsaved
  changes.
- There is no undo.
- merge results of scan with xml signatures list (test)
- somehow deal with items where the origSignature has changed
- change pyobjc source to use import _signatures instead of 
  import _FrameworkSignatures. Do this for *all* wrapped frameworks.
- can we scan the wrapper sources for manual wrappers? 
  -> add markup
  -> add menu item for generating stub manual wrapper
