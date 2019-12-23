from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2 ** 32:
    import Contacts

    class TestCNContactRelation(TestCase):
        @min_os_level("10.11")
        def testConstants10_11(self):
            self.assertIsInstance(Contacts.CNLabelContactRelationFather, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationMother, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationParent, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationBrother, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationSister, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationChild, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationFriend, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationSpouse, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationPartner, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationAssistant, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationManager, unicode)

        @min_os_level("10.13")
        def testConstants10_13(self):
            self.assertIsInstance(Contacts.CNLabelContactRelationSon, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationDaughter, unicode)

        @min_os_level("10.15")
        def testConstants10_15(self):
            self.assertIsInstance(Contacts.CNLabelContactRelationColleague, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationTeacher, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationSibling, unicode)
            self.assertIsInstance(
                Contacts.CNLabelContactRelationYoungerSibling, unicode
            )
            self.assertIsInstance(Contacts.CNLabelContactRelationElderSibling, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationYoungerSister, unicode)
            self.assertIsInstance(
                Contacts.CNLabelContactRelationYoungestSister, unicode
            )
            self.assertIsInstance(Contacts.CNLabelContactRelationElderSister, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationEldestSister, unicode)
            self.assertIsInstance(
                Contacts.CNLabelContactRelationYoungerBrother, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationYoungestBrother, unicode
            )
            self.assertIsInstance(Contacts.CNLabelContactRelationElderBrother, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationEldestBrother, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationMaleFriend, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationFemaleFriend, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationWife, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationHusband, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationMalePartner, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationFemalePartner, unicode)
            self.assertIsInstance(
                Contacts.CNLabelContactRelationGirlfriendOrBoyfriend, unicode
            )
            self.assertIsInstance(Contacts.CNLabelContactRelationGirlfriend, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationBoyfriend, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationGrandparent, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationGrandmother, unicode)
            self.assertIsInstance(
                Contacts.CNLabelContactRelationGrandmotherMothersMother, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationGrandmotherFathersMother, unicode
            )
            self.assertIsInstance(Contacts.CNLabelContactRelationGrandfather, unicode)
            self.assertIsInstance(
                Contacts.CNLabelContactRelationGrandfatherMothersFather, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationGrandfatherFathersFather, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationGreatGrandparent, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationGreatGrandmother, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationGreatGrandfather, unicode
            )
            self.assertIsInstance(Contacts.CNLabelContactRelationGrandchild, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationGranddaughter, unicode)
            self.assertIsInstance(
                Contacts.CNLabelContactRelationGranddaughterDaughtersDaughter, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationGranddaughterSonsDaughter, unicode
            )
            self.assertIsInstance(Contacts.CNLabelContactRelationGrandson, unicode)
            self.assertIsInstance(
                Contacts.CNLabelContactRelationGrandsonDaughtersSon, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationGrandsonSonsSon, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationGreatGrandchild, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationGreatGranddaughter, unicode
            )
            self.assertIsInstance(Contacts.CNLabelContactRelationGreatGrandson, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationParentInLaw, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationMotherInLaw, unicode)
            self.assertIsInstance(
                Contacts.CNLabelContactRelationMotherInLawWifesMother, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationMotherInLawHusbandsMother, unicode
            )
            self.assertIsInstance(Contacts.CNLabelContactRelationFatherInLaw, unicode)
            self.assertIsInstance(
                Contacts.CNLabelContactRelationFatherInLawWifesFather, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationFatherInLawHusbandsFather, unicode
            )
            self.assertIsInstance(Contacts.CNLabelContactRelationCoParentInLaw, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationCoMotherInLaw, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationCoFatherInLaw, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationSiblingInLaw, unicode)
            self.assertIsInstance(
                Contacts.CNLabelContactRelationYoungerSiblingInLaw, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationElderSiblingInLaw, unicode
            )
            self.assertIsInstance(Contacts.CNLabelContactRelationSisterInLaw, unicode)
            self.assertIsInstance(
                Contacts.CNLabelContactRelationYoungerSisterInLaw, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationElderSisterInLaw, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationSisterInLawSpousesSister, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationSisterInLawWifesSister, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationSisterInLawHusbandsSister, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationSisterInLawBrothersWife, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationSisterInLawYoungerBrothersWife, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationSisterInLawElderBrothersWife, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationYoungerBrother, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationYoungestBrother, unicode
            )
            self.assertIsInstance(Contacts.CNLabelContactRelationElderBrother, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationEldestBrother, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationMaleFriend, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationFemaleFriend, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationWife, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationHusband, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationMalePartner, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationFemalePartner, unicode)
            self.assertIsInstance(
                Contacts.CNLabelContactRelationGirlfriendOrBoyfriend, unicode
            )
            self.assertIsInstance(Contacts.CNLabelContactRelationGirlfriend, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationBoyfriend, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationGrandparent, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationGrandmother, unicode)
            self.assertIsInstance(
                Contacts.CNLabelContactRelationGrandmotherMothersMother, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationGrandmotherFathersMother, unicode
            )
            self.assertIsInstance(Contacts.CNLabelContactRelationGrandfather, unicode)
            self.assertIsInstance(
                Contacts.CNLabelContactRelationGrandfatherMothersFather, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationGrandfatherFathersFather, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationGreatGrandparent, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationGreatGrandmother, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationGreatGrandfather, unicode
            )
            self.assertIsInstance(Contacts.CNLabelContactRelationBrotherInLaw, unicode)
            self.assertIsInstance(
                Contacts.CNLabelContactRelationYoungerBrotherInLaw, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationElderBrotherInLaw, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationBrotherInLawSpousesBrother, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationBrotherInLawHusbandsBrother, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationBrotherInLawWifesBrother, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationBrotherInLawSistersHusband, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationBrotherInLawYoungerSistersHusband,
                unicode,
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationBrotherInLawElderSistersHusband, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationSisterInLawWifesBrothersWife, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationSisterInLawHusbandsBrothersWife, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationBrotherInLawWifesSistersHusband, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationBrotherInLawHusbandsSistersHusband,
                unicode,
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationCoSiblingInLaw, unicode
            )
            self.assertIsInstance(Contacts.CNLabelContactRelationCoSisterInLaw, unicode)
            self.assertIsInstance(
                Contacts.CNLabelContactRelationCoBrotherInLaw, unicode
            )
            self.assertIsInstance(Contacts.CNLabelContactRelationChildInLaw, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationDaughterInLaw, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationSonInLaw, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationCousin, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationYoungerCousin, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationElderCousin, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationMaleCousin, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationFemaleCousin, unicode)
            self.assertIsInstance(
                Contacts.CNLabelContactRelationCousinParentsSiblingsChild, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationCousinParentsSiblingsSon, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationYoungerCousinParentsSiblingsSon, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationElderCousinParentsSiblingsSon, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationCousinParentsSiblingsDaughter, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationYoungerCousinParentsSiblingsDaughter,
                unicode,
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationElderCousinParentsSiblingsDaughter,
                unicode,
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationCousinMothersSistersDaughter, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationYoungerCousinMothersSistersDaughter,
                unicode,
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationElderCousinMothersSistersDaughter,
                unicode,
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationCousinMothersSistersSon, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationYoungerCousinMothersSistersSon, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationElderCousinMothersSistersSon, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationCousinMothersBrothersDaughter, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationYoungerCousinMothersBrothersDaughter,
                unicode,
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationElderCousinMothersBrothersDaughter,
                unicode,
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationCousinMothersBrothersSon, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationYoungerCousinMothersBrothersSon, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationElderCousinMothersBrothersSon, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationCousinFathersSistersDaughter, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationYoungerCousinFathersSistersDaughter,
                unicode,
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationElderCousinFathersSistersDaughter,
                unicode,
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationCousinFathersSistersSon, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationYoungerCousinFathersSistersSon, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationElderCousinFathersSistersSon, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationCousinFathersBrothersDaughter, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationYoungerCousinFathersBrothersDaughter,
                unicode,
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationElderCousinFathersBrothersDaughter,
                unicode,
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationCousinFathersBrothersSon, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationYoungerCousinFathersBrothersSon, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationElderCousinFathersBrothersSon, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationCousinGrandparentsSiblingsChild, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationCousinGrandparentsSiblingsDaughter,
                unicode,
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationCousinGrandparentsSiblingsSon, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationYoungerCousinMothersSiblingsSonOrFathersSistersSon,
                unicode,
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationElderCousinMothersSiblingsSonOrFathersSistersSon,
                unicode,
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationYoungerCousinMothersSiblingsDaughterOrFathersSistersDaughter,
                unicode,
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationElderCousinMothersSiblingsDaughterOrFathersSistersDaughter,
                unicode,
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationParentsSibling, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationParentsYoungerSibling, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationParentsElderSibling, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationParentsSiblingMothersSibling, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationParentsSiblingMothersYoungerSibling,
                unicode,
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationParentsSiblingMothersElderSibling,
                unicode,
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationParentsSiblingFathersSibling, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationParentsSiblingFathersYoungerSibling,
                unicode,
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationParentsSiblingFathersElderSibling,
                unicode,
            )
            self.assertIsInstance(Contacts.CNLabelContactRelationAunt, unicode)
            self.assertIsInstance(
                Contacts.CNLabelContactRelationAuntParentsSister, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationAuntParentsYoungerSister, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationAuntParentsElderSister, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationAuntFathersSister, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationAuntFathersYoungerSister, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationAuntFathersElderSister, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationAuntFathersBrothersWife, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationAuntFathersYoungerBrothersWife, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationAuntFathersElderBrothersWife, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationAuntMothersSister, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationAuntMothersYoungerSister, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationAuntMothersElderSister, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationAuntMothersBrothersWife, unicode
            )
            self.assertIsInstance(Contacts.CNLabelContactRelationGrandaunt, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationUncle, unicode)
            self.assertIsInstance(
                Contacts.CNLabelContactRelationUncleParentsBrother, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationUncleParentsYoungerBrother, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationUncleParentsElderBrother, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationUncleMothersBrother, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationUncleMothersYoungerBrother, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationUncleMothersElderBrother, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationUncleMothersSistersHusband, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationUncleFathersBrother, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationUncleFathersYoungerBrother, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationUncleFathersElderBrother, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationUncleFathersSistersHusband, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationUncleFathersYoungerSistersHusband,
                unicode,
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationUncleFathersElderSistersHusband, unicode
            )
            self.assertIsInstance(Contacts.CNLabelContactRelationGranduncle, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationSiblingsChild, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationNiece, unicode)
            self.assertIsInstance(
                Contacts.CNLabelContactRelationNieceSistersDaughter, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationNieceBrothersDaughter, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationNieceSistersDaughterOrWifesSiblingsDaughter,
                unicode,
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationNieceBrothersDaughterOrHusbandsSiblingsDaughter,
                unicode,
            )
            self.assertIsInstance(Contacts.CNLabelContactRelationNephew, unicode)
            self.assertIsInstance(
                Contacts.CNLabelContactRelationNephewSistersSon, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationNephewBrothersSon, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationNephewBrothersSonOrHusbandsSiblingsSon,
                unicode,
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationNephewSistersSonOrWifesSiblingsSon,
                unicode,
            )
            self.assertIsInstance(Contacts.CNLabelContactRelationGrandniece, unicode)
            self.assertIsInstance(
                Contacts.CNLabelContactRelationGrandnieceSistersGranddaughter, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationGrandnieceBrothersGranddaughter, unicode
            )
            self.assertIsInstance(Contacts.CNLabelContactRelationGrandnephew, unicode)
            self.assertIsInstance(
                Contacts.CNLabelContactRelationGrandnephewSistersGrandson, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationGrandnephewBrothersGrandson, unicode
            )
            self.assertIsInstance(Contacts.CNLabelContactRelationStepparent, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationStepfather, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationStepmother, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationStepchild, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationStepson, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationStepdaughter, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationStepbrother, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationStepsister, unicode)
            self.assertIsInstance(
                Contacts.CNLabelContactRelationMotherInLawOrStepmother, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationFatherInLawOrStepfather, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationDaughterInLawOrStepdaughter, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationSonInLawOrStepson, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationCousinOrSiblingsChild, unicode
            )
            self.assertIsInstance(Contacts.CNLabelContactRelationNieceOrCousin, unicode)
            self.assertIsInstance(
                Contacts.CNLabelContactRelationNephewOrCousin, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationGrandchildOrSiblingsChild, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationGreatGrandchildOrSiblingsGrandchild,
                unicode,
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationDaughterInLawOrSisterInLaw, unicode
            )
            self.assertIsInstance(
                Contacts.CNLabelContactRelationSonInLawOrBrotherInLaw, unicode
            )


if __name__ == "__main__":
    main()
