==============
SimplePrefPane
==============

This example shows how to build preference panes in python. This example
requires a framework install of Python and the Developer Tools. 

The same technique can be used to build plugin bundles for other applications,
as long as those applications support Cocoa plugins.

To test this::

  $ python buildplugin.py build
  $ mv build/SimplePreferencePane.prefPane  \
  	~/Library/PreferencePanes/SimplePreferencePane.prefPane

The preference pane can be uninstalled by removing the bundle
``SimplePreferencePane.prefPane`` from Library/PreferencePanes in your
home directory.
