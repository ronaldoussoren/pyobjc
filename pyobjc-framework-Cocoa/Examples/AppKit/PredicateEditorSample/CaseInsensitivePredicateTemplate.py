import Cocoa
from objc import super


class CaseInsensitivePredicateTemplate(Cocoa.NSPredicateEditorRowTemplate):
    def predicateWithSubpredicates_(self, subpredicates):
        # we only make NSComparisonPredicates
        predicate = super(
            CaseInsensitivePredicateTemplate, self
        ).predicateWithSubpredicates_(subpredicates)

        # construct an identical predicate, but add the
        # NSCaseInsensitivePredicateOption flag
        return Cocoa.NSComparisonPredicate.predicateWithLeftExpression_rightExpression_modifier_type_options_(  # noqa: B950
            predicate.leftExpression(),
            predicate.rightExpression(),
            predicate.comparisonPredicateModifier(),
            predicate.predicateOperatorType(),
            predicate.options() | Cocoa.NSCaseInsensitivePredicateOption,
        )
