from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKVerifiableClinicalRecord(TestCase):
    def test_constants(self):
        self.assertIsTypedEnum(HealthKit.HKVerifiableClinicalRecordSourceType, str)

        self.assertIsInstance(
            HealthKit.HKVerifiableClinicalRecordSourceTypeSMARTHealthCard, str
        )
        self.assertIsInstance(
            HealthKit.HKVerifiableClinicalRecordSourceTypeEUDigitalCOVIDCertificate, str
        )

        self.assertIsTypedEnum(HealthKit.HKVerifiableClinicalRecordCredentialType, str)

        self.assertIsInstance(
            HealthKit.HKVerifiableClinicalRecordCredentialTypeCOVID19, str
        )
        self.assertIsInstance(
            HealthKit.HKVerifiableClinicalRecordCredentialTypeImmunization, str
        )
        self.assertIsInstance(
            HealthKit.HKVerifiableClinicalRecordCredentialTypeLaboratory, str
        )
        self.assertIsInstance(
            HealthKit.HKVerifiableClinicalRecordCredentialTypeRecovery, str
        )
