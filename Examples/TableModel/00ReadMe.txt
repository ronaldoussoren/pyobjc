Example of how to provide a table-model from python.

Note that the abstract protocol contains a number of methods that take
plain C arguments (e.g. not 'id' values). 

Because these methods are not present in NSObject, you must explicitly 
specify the Objective-C signature of the method, hence the calls to 'selector'
