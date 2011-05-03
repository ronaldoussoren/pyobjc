PredicateEditorSample
=====================

"PredicateEditorSample" is a Cocoa application that demonstrates how to use 
the ``NSPredicateEditor`` class.  The ``NSPredicateEditor`` class is a 
subclass of ``NSRuleEditor`` that is specialized for editing ``NSPredicate`` 
objects.  This sample is intended to show how to use the many different 
features and aspects of this control and leverages Spotlight to search your 
Address Book.

It shows how to manage this control inside your window along with an 
``NSTableView``, build Spotlight friendly queries based on ``NSPredicate`` and 
``NSCompountPredicate``, build search results based on ``NSMetadataQuery`` object.

Using the Sample
----------------

Simply build the example using the supplied ``setup.py`` file.  Enter 
query information pertaining to your Address Book.  The application will 
display matches in its table view.

Note that this sample uses Interface Builder 3.0 to build the 
``NSPredicateEditorRowTemplates`` that make up the control's interface.

AddressBook searches are achieved by specifically requesting the "kind" of data to search via the ``kMDItemKind`` key constant.  This is the metadata attribute key that tells Spotlight to search for address book data only.  Together along with the other predicates from the ``NSPredicateEditor`` class we form a "compound predicate" and start the query.  The code snippet below found in this sample shows how this is done::

   # always search for items in the Address Book
   addrBookPredicate = NSPredicate.predicateWithFormat_("(kMDItemKind = 'Address Book Person Data')")
   predicate = NSCompoundPredicate.andPredicateWithSubpredicates_([addrBookPredicate, predicate])

   query.setPredicate_(predicate)
   query.startQuery()
