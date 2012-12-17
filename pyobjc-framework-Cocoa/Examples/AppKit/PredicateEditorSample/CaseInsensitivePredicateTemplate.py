from Cocoa import *

class CaseInsensitivePredicateTemplate (NSPredicateEditorRowTemplate):
    def predicateWithSubpredicates_(self, subpredicates):
        # we only make NSComparisonPredicates
        predicate = super(CaseInsensitivePredicateTemplate, self).predicateWithSubpredicates_(subpredicates)

        # construct an identical predicate, but add the
        # NSCaseInsensitivePredicateOption flag
        return NSComparisonPredicate.predicateWithLeftExpression_rightExpression_modifier_type_options_(
                    predicate.leftExpression(),
                    predicate.rightExpression(),
                    predicate.comparisonPredicateModifier(),
                    predicate.predicateOperatorType(),
                    predicate.options() | NSCaseInsensitivePredicateOption)
