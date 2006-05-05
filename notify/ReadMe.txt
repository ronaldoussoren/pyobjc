Theses are wrappers for the notify library on Mac OS X 10.3 or later. This 
library allows processes to exchange stateless notification events.

Notifications are associated with names in a namespace shared by all
clients of the system.  Clients may post notifications for names, and
may monitor names for posted notifications.  Clients may request
notification delivery by a number of different methods.

To install::
   
   $ python setup.py install

See the ``Examples/`` directory for some examples of how to use this library.
