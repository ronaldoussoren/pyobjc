This is a version of the TableModel example that shows mutating the model data.

Note that the model data is stored in an NSMutableArray instead of a Python
list. That is necessary to make sure that the right events get fired 
automaticly. The alternative is to generate those events manually, which would
make bindings much less useful.
