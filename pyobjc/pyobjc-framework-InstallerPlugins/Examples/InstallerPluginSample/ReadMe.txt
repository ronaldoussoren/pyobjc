Install plugin sample
=====================

1. What is an Installer Plugin?
-------------------------------

An Installer Plugin extends the user experience of the Installation process by 
allowing developers to insert additional custom steps in the installation 
process of their software packages.  In the sample code provided here, a 
registration pane is built that asks users for registration information before 
installing.

Note that informed end-users can remove your package's Plugins directory 
and/or change your package's InstallerSections.plist file to remove custom 
plugins from its flow. So plugins cannot serve as effective gatekeepers to 
prevent installation.

2. Using the Sample Installer Plugin
------------------------------------

1. Take a pre-existing package (or create a new one with PackageMaker.) 

   The sample package ``InstallerPluginsTestPackage.pkg`` is provided for your 
   test use.

2. Create a ``Plugins`` directory in that Package bundle: ``InstallerPluginsTestPackage.pkg/Contents/Plugins``

3. Run the ``setup.py`` in ``Registration``

4. Copy the created bundle created into the Plugins directory of your package.

5. Copy the ``InstallerSections.plist`` file in this directory into the 
   Plugins directory of your package. The ``InstallerSections.plist`` defines 
   the order that the Installer section pane will be presented to the user, 
   and where the Registration pane will appear (following the ``License`` pane.)

6. Open the package

   It will run with the additional custom Registration plugin (and will ask
   if it is al right to run additional code before opening).
	
3. Creating Your Own Custom Installer Plugin
--------------------------------------------

Getting started
...............

* Use the provided plugin as your starting point for development.

* Custom Installer Plugins must be written in Cocoa.  They may not be written 
  in Carbon or Java, but can be written in Python (obviously).

* Review the InstallerPlugins.framework APIs.  

* Copy and update the provided ``InstallerSections.plist`` file to include 
  your plugin(s), and place them in the appropriate location in the Install 
  sequence.

* Contact the Mac OS X Installation Technology Engineering team with questions 
  by subscribing to the installer-dev mailing list (email contact information
  is provided in the 'Notes' section.)
	
Code Flow in the Plugin
.......................

* The plugin's entry point to is the method ``didEnterPane_(pane)``.

* When the user clicks the "Continue" button, method ``shouldExitPane_(dir)``
  is called. Return False from this method to prevent the user from leaving
  your plugin page. 
	
4. Notes
--------

Plugins are only supported in Mac OS X Tiger (v10.4) and later.
	
Contact: Subscribe to the installer-dev mailing list at the Apple Mailing 
Lists web page <http://lists.apple.com/mailman/listinfo>.  Select the 
"Installer-dev" list item and follow the steps on 
"Subscribing to Installer-dev".
	
Documentation:	http://developer.apple.com/documentation/DeveloperTools/Conceptual/SoftwareDistribution/index.html
