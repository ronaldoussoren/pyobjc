from Cocoa import *
from InstallerPlugins import *

import objc

# Important: be aware that informed end-users can remove your package's
# Plugins directory and/or change your package's InstallerSections.plist file
# to remove custom plugins from its flow.
# So plugins cannot serve as effective gatekeepers to prevent installation.

class RegistrationPane (InstallerPane):
    uiFirstNameField = objc.IBOutlet()
    uiLastNameField = objc.IBOutlet()
    uiOrganizationField = objc.IBOutlet()
    uiSerialNumberField = objc.IBOutlet()

    def _entriesAreValid(self):
        "test all textfields to if they all have at least one character in them"
        if (len(self.uiFirstNameField.stringValue()) == 0
                or len(self.uiLastNameField.stringValue()) == 0
                or len(self.uiOrganizationField.stringValue()) == 0
                or len(self.uiSerialNumberField.stringValue()) == 0):
            return False

        return True

    def _serialNumberIsValid(self):
        """
        perform a simple string compare to validate the serial number
        entered by the user
        """
        return self.uiSerialNumberField.stringValue() == '123-456-789'

    def _updateNextButtonState(self):
        "enable the 'Continue' button if '_entriesAreValid' returns 'True'"
        self.setNextEnabled_(self._entriesAreValid())

    def _localizedStringForKey_(self, key):
        '''
        localization helper method:  This pulls localized strings from the
        plugin's bundle
        '''
        return NSBundle.bundleForClass_(type(self
                    )).localizedStringForKey_value_table_(key, '', None)

    def title(self):
        ''' return the title of this pane '''
        return self._localizedStringForKey_("Title")

    def didEnterPane_(self, dir):
        ''' pane's entry point: code called when user enters this pane '''
        NSLog("DIDENTER")
        self._updateNextButtonState()

    def shouldExitPane_(self, dir):
        '''
        called when user clicks "Continue" -- return value indicates
        if application should exit pane
        '''
        if dir == InstallerDirectionForward and not self._serialNumberIsValid():
            self._updateNextButtonState()

            NSBeginInformationalAlertSheet(
                    None,
                    self._localizedStringForKey_("OK_BUTTON"),
                    None,
                    None,
                    self.uiFirstNameField.window(),
                    None,
                    None,
                    None,
                    0,
                    self._localizedStringForKey_("InvalidSerialNumberAlertMessage"));
            return False

        return True

    def controlTextDidChange_(self, notification):
        """
        updates the state of the next button when the contents of the
        delegate textfields change
        """
        self._updateNextButtonState()
