import Foundation
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestNSPredicateValidatingHelper(Foundation.NSObject):
    def visitPredicate_error_(self, a, b):
        return 1

    def visitExpression_error_(self, a, b):
        return 1

    def visitOperatorType_error_(self, a, b):
        return 1

    def visitExpressionKeyPath_scope_key_error_(self, a, b, c, d):
        return 1


class TestNSPredicateValidating(TestCase):
    @min_sdk_level("26.4")
    def test_protocols(self):
        self.assertProtocolExists("NSPredicateValidating")

    def test_protocol_methods(self):
        self.assertResultIsBOOL(TestNSPredicateValidatingHelper.visitPredicate_error_)
        self.assertArgHasType(
            TestNSPredicateValidatingHelper.visitPredicate_error_, 1, b"o^@"
        )

        self.assertResultIsBOOL(TestNSPredicateValidatingHelper.visitExpression_error_)
        self.assertArgHasType(
            TestNSPredicateValidatingHelper.visitExpression_error_, 1, b"o^@"
        )

        self.assertResultIsBOOL(
            TestNSPredicateValidatingHelper.visitOperatorType_error_
        )
        self.assertArgHasType(
            TestNSPredicateValidatingHelper.visitOperatorType_error_, 0, b"Q"
        )
        self.assertArgHasType(
            TestNSPredicateValidatingHelper.visitOperatorType_error_, 1, b"o^@"
        )

        self.assertResultIsBOOL(
            TestNSPredicateValidatingHelper.visitExpressionKeyPath_scope_key_error_
        )
        self.assertArgHasType(
            TestNSPredicateValidatingHelper.visitExpressionKeyPath_scope_key_error_,
            3,
            b"o^@",
        )
