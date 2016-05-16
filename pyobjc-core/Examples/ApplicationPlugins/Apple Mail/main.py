#!/usr/bin/python

import sys

from AppKit import *
from Foundation import *
import objc

MessageRuleClass = objc.lookUpClass('MessageRule')
oldPerformActionsOnMessages_destinationStores_rejectedMessages_messagesToBeDeleted_ = MessageRuleClass.instanceMethodForSelector_("performActionsOnMessages:destinationStores:rejectedMessages:messagesToBeDeleted:")

def performActionsOnMessages_destinationStores_rejectedMessages_messagesToBeDeleted_(self, messages, stores, rejectedMessages, messagesToBeDeleted):
    NSLog('yes')
    oldPerformActionsOnMessages_destinationStores_rejectedMessages_messagesToBeDeleted_(self, messages, stores, rejectedMessages, messagesToBeDeleted)
    NSLog('done')

objc.classAddMethods(MessageRuleClass,
[performActionsOnMessages_destinationStores_rejectedMessages_messagesToBeDeleted_])


class ToyMailBundle2 (objc.lookUpClass('.MVMailBundle')):
    def applicationWillTerminate_ (self, notification):
        NSLog('ToyMailBundle2 is shutting down')
        NSNotificationCenter.defaultCenter().removeObserver_name_object_(self,
None, None)

    def init (self):
        self = super(ToyMailBundle2, self).init()
        if self:
            NSLog('ToyMailBundle2 -init called')
            NSNotificationCenter.defaultCenter().addObserver_selector_name_object_(self,

            b'applicationWillTerminate:',

            NSApplicationWillTerminateNotification,

            None)
        return self

    @classmethod
    def initialize (cls):
        cls.registerBundle()
        NSLog('ToyMailBundle2 registered with Mail')
