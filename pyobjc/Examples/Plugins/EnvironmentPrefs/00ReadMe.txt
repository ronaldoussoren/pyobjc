===============
EnvironmentPane
===============

This example shows how to build preference panes in python. This example
requires a framework install of Python and the Developer Tools. 

Note that is a fully functional and usefull preference pane, this pane
allows you to change the default environment for all your processes. Changes
to the environment will only be effective after you logout and login again.

The same technique can be used to build plugin bundles for other applications,
as long as those applications support Cocoa plugins.

To test this::

  $ python buildplugin.py build
  $ mv build/EnvironmentPane.prefPane  \
  	~/Library/PreferencePanes/EnvironmentPane.prefPane

The preference pane can be uninstalled by removing the bundle
``EnvironmentPane.prefPane`` from Library/PreferencePanes in your
home directory.

NOTE: You can also add a symlink to ~/Library/Preferences. If you modify
the meta information of the pane (mostly its icon and label) you should
recreate the link, otherwise System Preferences won't reread the information.
