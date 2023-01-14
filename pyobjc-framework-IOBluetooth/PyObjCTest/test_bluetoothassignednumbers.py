from PyObjCTools.TestSupport import TestCase, fourcc

import IOBluetooth


class TestBluetoothAssignedNumbers(TestCase):
    def test_constants(self):
        self.assertIsEnumType(IOBluetooth.BluetoothCompanyIdentifers)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferEricssonTechnologyLicensing, 0
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferNokiaMobilePhones, 1)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferIntel, 2)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferIBM, 3)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferToshiba, 4)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentifer3Com, 5)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferMicrosoft, 6)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferLucent, 7)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferMotorola, 8)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferInfineonTechnologiesAG, 9
        )
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferCambridgeSiliconRadio, 10
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferSiliconWave, 11)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferDigianswerAS, 12)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferTexasInstruments, 13)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferParthusTechnologies, 14)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferBroadcom, 15)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferMitelSemiconductor, 16)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferWidcomm, 17)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferZeevo, 18)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferAtmel, 19)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferMistubishiElectric, 20)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferRTXTelecom, 21)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferKCTechnology, 22)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferNewlogic, 23)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferTransilica, 24)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferRohdeandSchwarz, 25)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferTTPCom, 26)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferSigniaTechnologies, 27)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferConexantSystems, 28)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferQualcomm, 29)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferInventel, 30)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferAVMBerlin, 31)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferBandspeed, 32)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferMansella, 33)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferNEC, 34)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferWavePlusTechnology, 35)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferAlcatel, 36)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferPhilipsSemiconductor, 37)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferCTechnologies, 38)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferOpenInterface, 39)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferRFCMicroDevices, 40)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferHitachi, 41)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferSymbolTechnologies, 42)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferTenovis, 43)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferMacronixInternational, 44
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferGCTSemiconductor, 45)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferNorwoodSystems, 46)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferMewTelTechnology, 47)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferSTMicroelectronics, 48)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferSynopsys, 49)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferRedMCommunications, 50)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferCommil, 51)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferCATC, 52)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferEclipse, 53)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferRenesasTechnology, 54)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferMobilian, 55)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferTerax, 56)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferIntegratedSystemSolution, 57
        )
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferMatsushitaElectricIndustrial, 58
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferGennum, 59)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferResearchInMotion, 60)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferIPextreme, 61)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferSystemsAndChips, 62)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferBluetoothSIG, 63)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferSeikoEpson, 64)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferIntegratedSiliconSolution, 65
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferCONWISETechnology, 66)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferParrotSA, 67)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferSocketCommunications, 68)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferAtherosCommunications, 69
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferMediaTek, 70)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferBluegiga, 71)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferMarvellTechnologyGroup, 72
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentifer3DSP, 73)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferAccelSemiconductor, 74)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferContinentialAutomotiveSystems, 75
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferApple, 76)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferStaccatoCommunications, 77
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferAvagoTechnologies, 78)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferAPT, 79)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferSiRFTechnology, 80)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferTZeroTechnologies, 81)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferJandM, 82)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferFree2Move, 83)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentifer3DiJoy, 84)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferPlantronics, 85)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferSonyEricssonMobileCommunications, 86
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferHarmonInternational, 87)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferVisio, 88)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferNordicSemiconductor, 89)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferEMMicroElectronicMarin, 90
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferRalinkTechnology, 91)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferBelkinInternational, 92)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferRealtekSemiconductor, 93)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferStonestreetOne, 94)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferWicentric, 95)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferRivieraWaves, 96)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferRDAMicroelectronics, 97)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferGibsonGuitars, 98)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferMiCommand, 99)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferBandXIInternational, 100)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferHewlettPackard, 101)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentifer9SolutionsOy, 102)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferGNNetcom, 103)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferGeneralMotors, 104)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferAAndDEngineering, 105)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferMindTree, 106)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferPolarElectroOY, 107)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferBeautifulEnterprise, 108)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferBriarTek, 109)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferSummitDataCommunications, 110
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferSoundID, 111)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferMonster, 112)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferConnectBlueAB, 113)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferShangHaiSuperSmartElectronics, 114
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferGroupSense, 115)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferZomm, 116)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferSamsungElectronics, 117)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferCreativeTechnology, 118)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferLairdTechnologies, 119)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferNike, 120)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferLessWire, 121)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferMStarTechnologies, 122)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferHanlynnTechnologies, 123)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferAAndRCambridge, 124)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferSeersTechnology, 125)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferSportsTrackingTechnologies, 126
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferAutonetMobile, 127)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferDeLormePublishingCompany, 128
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferWuXiVimicro, 129)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferSennheiserCommunications, 130
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferTimeKeepingSystems, 131)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferLudusHelsinki, 132)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferBlueRadios, 133)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferEquinux, 134)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferGarminInternational, 135)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferEcotest, 136)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferGNResound, 137)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferJawbone, 138)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferTopconPositioningSystems, 139
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferGimbal, 140)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferZscanSoftware, 141)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferQuintic, 142)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferTelitWirelessSolutions, 143
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferFunaiElectric, 144)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferAdvancedPANMOBILSystems, 145
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferThinkOptics, 146)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferUniversalElectriconics, 147
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferAirohaTechnology, 148)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferNECLightning, 149)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferODMTechnology, 150)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferConnecteDevice, 151)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferZero1TV, 152)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferITechDynamicGlobalDistribution, 153
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferAlpwise, 154)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferJiangsuToppowerAutomotiveElectronics,
            155,
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferColorfy, 156)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferGeoforce, 157)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferBose, 158)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferSuuntoOy, 159)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferKensingtonComputerProductsGroup, 160
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferSRMedizinelektronik, 161)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferVertu, 162)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferMetaWatch, 163)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferLinak, 164)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferOTLDynamics, 165)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferPandaOcean, 166)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferVisteon, 167)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferARPDevicesUnlimited, 168)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferMagnetiMarelli, 169)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferCaenRFID, 170)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferIngenieurSystemgruppeZahn, 171
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferGreenThrottleGames, 172)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferPeterSystemtechnik, 173)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferOmegawave, 174)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferCinetix, 175)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferPassifSemiconductor, 176)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferSarisCyclingGroup, 177)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferBekey, 178)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferClarinoxTechnologies, 179
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferBDETechnology, 180)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferSwirlNetworks, 181)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferMesoInternational, 182)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferTreLab, 183)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferQualcommInnovationCenter, 184
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferJohnsonControls, 185)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferStarkeyLaboratories, 186)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferSPowerElectronics, 187)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferAceSensor, 188)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferAplix, 189)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferAAMPofAmerica, 190)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferStalmartTechnology, 191)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferAMICCOMElectronics, 192)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferShenzhenExcelsecuDataTechnology, 193
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferGeneq, 194)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferAdidas, 195)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferLGElectronics, 196)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferOnsetComputer, 197)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferSelflyBV, 198)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferQuupa, 199)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferGeLo, 200)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferEvluma, 201)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferMC10, 202)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferBinauricSE, 203)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferBeatsElectronics, 204)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferMicrochipTechnology, 205)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferElgatoSystems, 206)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferARCHOS, 207)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferDexcom, 208)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferPolarElectroEurope, 209)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferDialogSemiconductor, 210)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferTaixingbangTechnology, 211
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferKawantech, 212)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferAustcoCommunicationsSystems, 213
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferTimexGroup, 214)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferQualcommTechnologies, 215
        )
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferQualcommConnectedExperiences, 216
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferVoyetraTurtleBeach, 217)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentifertxtrGMBH, 218)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferBiosentronics, 219)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferProctorAndGamble, 220)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferHosiden, 221)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferMusik, 222)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferMisfitWearables, 223)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferGoogle, 224)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferDanlers, 225)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferSemilink, 226)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferInMusicBrands, 227)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferLSResearch, 228)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferEdenSoftwareConsultants, 229
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferFreshtemp, 230)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferKSTechnologies, 231)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferACTSTechnologies, 232)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferVtrackSystems, 233)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferNielsenKellerman, 234)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferServerTechnology, 235)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferBioResearchAssociates, 236
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferJollyLogic, 237)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferAboveAverageOutcomes, 238
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferBitsplitters, 239)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferPayPal, 240)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferWitronTechnology, 241)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferMorseProject, 242)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferKentDisplays, 243)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferNautilus, 244)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferSmartifier, 245)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferElcometer, 246)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferVSNTechnologies, 247)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferAceUni, 248)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferStickNFind, 249)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferCrystalCode, 250)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferKOUKAMM, 251)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferDelphi, 252)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferValenceTech, 253)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferStanleyBlackAndDecker, 254
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferTypeProducts, 255)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferTomTomInternational, 256)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferFuGoo, 257)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferKeiser, 258)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferBangAndOlufson, 259)
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferPLUSLocationSystems, 260)
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferUbiquitousComputingTechnology, 261
        )
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferInnovativeYachtterSolutions, 262
        )
        self.assertEqual(
            IOBluetooth.kBluetoothCompanyIdentiferWilliamDemantHolding, 263
        )
        self.assertEqual(IOBluetooth.kBluetoothCompanyIdentiferInteropIdentifier, 65535)

        self.assertEqual(
            IOBluetooth.kBluetoothServiceClassMajorLimitedDiscoverableMode, 0x001
        )
        self.assertEqual(IOBluetooth.kBluetoothServiceClassMajorReserved1, 0x002)
        self.assertEqual(IOBluetooth.kBluetoothServiceClassMajorReserved2, 0x004)
        self.assertEqual(IOBluetooth.kBluetoothServiceClassMajorPositioning, 0x008)
        self.assertEqual(IOBluetooth.kBluetoothServiceClassMajorNetworking, 0x010)
        self.assertEqual(IOBluetooth.kBluetoothServiceClassMajorRendering, 0x020)
        self.assertEqual(IOBluetooth.kBluetoothServiceClassMajorCapturing, 0x040)
        self.assertEqual(IOBluetooth.kBluetoothServiceClassMajorObjectTransfer, 0x080)
        self.assertEqual(IOBluetooth.kBluetoothServiceClassMajorAudio, 0x100)
        self.assertEqual(IOBluetooth.kBluetoothServiceClassMajorTelephony, 0x200)
        self.assertEqual(IOBluetooth.kBluetoothServiceClassMajorInformation, 0x400)
        self.assertEqual(IOBluetooth.kBluetoothServiceClassMajorAny, fourcc(b"****"))
        self.assertEqual(IOBluetooth.kBluetoothServiceClassMajorNone, fourcc(b"none"))
        self.assertNotHasAttr(IOBluetooth, "kBluetoothServiceClassMajorEnd")

        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMajorMiscellaneous, 0x00)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMajorComputer, 0x01)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMajorPhone, 0x02)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMajorLANAccessPoint, 0x03)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMajorAudio, 0x04)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMajorPeripheral, 0x05)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMajorImaging, 0x06)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMajorWearable, 0x07)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMajorToy, 0x08)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMajorHealth, 0x09)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMajorUnclassified, 0x1F)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMajorAny, fourcc(b"****"))
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMajorNone, fourcc(b"none"))
        self.assertNotHasAttr(IOBluetooth, "kBluetoothDeviceClassMajorEnd")

        self.assertEqual(
            IOBluetooth.kBluetoothDeviceClassMinorComputerUnclassified, 0x00
        )
        self.assertEqual(
            IOBluetooth.kBluetoothDeviceClassMinorComputerDesktopWorkstation, 0x01
        )
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorComputerServer, 0x02)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorComputerLaptop, 0x03)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorComputerHandheld, 0x04)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorComputerPalmSized, 0x05)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorComputerWearable, 0x06)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorPhoneUnclassified, 0x00)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorPhoneCellular, 0x01)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorPhoneCordless, 0x02)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorPhoneSmartPhone, 0x03)
        self.assertEqual(
            IOBluetooth.kBluetoothDeviceClassMinorPhoneWiredModemOrVoiceGateway, 0x04
        )
        self.assertEqual(
            IOBluetooth.kBluetoothDeviceClassMinorPhoneCommonISDNAccess, 0x05
        )

        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorAudioUnclassified, 0x00)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorAudioHeadset, 0x01)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorAudioHandsFree, 0x02)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorAudioReserved1, 0x03)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorAudioMicrophone, 0x04)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorAudioLoudspeaker, 0x05)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorAudioHeadphones, 0x06)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorAudioPortable, 0x07)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorAudioCar, 0x08)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorAudioSetTopBox, 0x09)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorAudioHiFi, 0x0A)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorAudioVCR, 0x0B)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorAudioVideoCamera, 0x0C)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorAudioCamcorder, 0x0D)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorAudioVideoMonitor, 0x0E)
        self.assertEqual(
            IOBluetooth.kBluetoothDeviceClassMinorAudioVideoDisplayAndLoudspeaker, 0x0F
        )
        self.assertEqual(
            IOBluetooth.kBluetoothDeviceClassMinorAudioVideoConferencing, 0x10
        )
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorAudioReserved2, 0x11)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorAudioGamingToy, 0x12)

        self.assertEqual(
            IOBluetooth.kBluetoothDeviceClassMinorPeripheral1Keyboard, 0x10
        )
        self.assertEqual(
            IOBluetooth.kBluetoothDeviceClassMinorPeripheral1Pointing, 0x20
        )
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorPeripheral1Combo, 0x30)

        self.assertEqual(
            IOBluetooth.kBluetoothDeviceClassMinorPeripheral2Unclassified, 0x00
        )
        self.assertEqual(
            IOBluetooth.kBluetoothDeviceClassMinorPeripheral2Joystick, 0x01
        )
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorPeripheral2Gamepad, 0x02)
        self.assertEqual(
            IOBluetooth.kBluetoothDeviceClassMinorPeripheral2RemoteControl, 0x03
        )
        self.assertEqual(
            IOBluetooth.kBluetoothDeviceClassMinorPeripheral2SensingDevice, 0x04
        )
        self.assertEqual(
            IOBluetooth.kBluetoothDeviceClassMinorPeripheral2DigitizerTablet, 0x05
        )
        self.assertEqual(
            IOBluetooth.kBluetoothDeviceClassMinorPeripheral2CardReader, 0x06
        )
        self.assertEqual(
            IOBluetooth.kBluetoothDeviceClassMinorPeripheral2DigitalPen, 0x07
        )
        self.assertEqual(
            IOBluetooth.kBluetoothDeviceClassMinorPeripheral2HandheldScanner, 0x08
        )
        self.assertEqual(
            IOBluetooth.kBluetoothDeviceClassMinorPeripheral2GesturalInputDevice, 0x09
        )
        self.assertEqual(
            IOBluetooth.kBluetoothDeviceClassMinorPeripheral2AnyPointing,
            fourcc(b"poin"),
        )

        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorImaging1Display, 0x04)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorImaging1Camera, 0x08)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorImaging1Scanner, 0x10)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorImaging1Printer, 0x20)

        self.assertEqual(
            IOBluetooth.kBluetoothDeviceClassMinorImaging2Unclassified, 0x00
        )

        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorWearablePager, 0x02)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorWearableJacket, 0x03)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorWearableHelmet, 0x04)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorWearableGlasses, 0x05)

        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorToyRobot, 0x01)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorToyVehicle, 0x02)
        self.assertEqual(
            IOBluetooth.kBluetoothDeviceClassMinorToyDollActionFigure, 0x03
        )
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorToyController, 0x04)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorToyGame, 0x05)

        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorHealthUndefined, 0x00)
        self.assertEqual(
            IOBluetooth.kBluetoothDeviceClassMinorHealthBloodPressureMonitor, 0x01
        )
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorHealthThermometer, 0x02)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorHealthScale, 0x03)
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorHealthGlucoseMeter, 0x04)
        self.assertEqual(
            IOBluetooth.kBluetoothDeviceClassMinorHealthPulseOximeter, 0x05
        )
        self.assertEqual(
            IOBluetooth.kBluetoothDeviceClassMinorHealthHeartRateMonitor, 0x06
        )
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorHealthDataDisplay, 0x07)

        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorAny, fourcc(b"****"))
        self.assertEqual(IOBluetooth.kBluetoothDeviceClassMinorNone, fourcc(b"none"))

        self.assertNotHasAttr(IOBluetooth, "kBluetoothDeviceClassMinorEnd")

        self.assertEqual(IOBluetooth.kBluetoothGAPAppearanceUnknown, 0)
        self.assertEqual(IOBluetooth.kBluetoothGAPAppearanceGenericPhone, 64)
        self.assertEqual(IOBluetooth.kBluetoothGAPAppearanceGenericComputer, 128)
        self.assertEqual(IOBluetooth.kBluetoothGAPAppearanceGenericWatch, 192)
        self.assertEqual(IOBluetooth.kBluetoothGAPAppearanceGenericClock, 256)
        self.assertEqual(IOBluetooth.kBluetoothGAPAppearanceGenericDisplay, 320)
        self.assertEqual(IOBluetooth.kBluetoothGAPAppearanceGenericRemoteControl, 384)
        self.assertEqual(IOBluetooth.kBluetoothGAPAppearanceGenericEyeGlasses, 448)
        self.assertEqual(IOBluetooth.kBluetoothGAPAppearanceGenericTag, 512)
        self.assertEqual(IOBluetooth.kBluetoothGAPAppearanceGenericKeyring, 576)
        self.assertEqual(IOBluetooth.kBluetoothGAPAppearanceGenericMediaPlayer, 640)
        self.assertEqual(IOBluetooth.kBluetoothGAPAppearanceGenericBarcodeScanner, 704)
        self.assertEqual(IOBluetooth.kBluetoothGAPAppearanceGenericThermometer, 768)
        self.assertEqual(IOBluetooth.kBluetoothGAPAppearanceGenericHeartrateSensor, 832)
        self.assertEqual(IOBluetooth.kBluetoothGAPAppearanceGenericBloodPressure, 896)
        self.assertEqual(
            IOBluetooth.kBluetoothGAPAppearanceGenericHumanInterfaceDevice, 960
        )
        self.assertEqual(
            IOBluetooth.kBluetoothGAPAppearanceHumanInterfaceDeviceKeyboard, 961
        )
        self.assertEqual(
            IOBluetooth.kBluetoothGAPAppearanceHumanInterfaceDeviceMouse, 962
        )
        self.assertEqual(
            IOBluetooth.kBluetoothGAPAppearanceHumanInterfaceDeviceJoystick, 963
        )
        self.assertEqual(
            IOBluetooth.kBluetoothGAPAppearanceHumanInterfaceDeviceGamepad, 964
        )
        self.assertEqual(
            IOBluetooth.kBluetoothGAPAppearanceHumanInterfaceDeviceDigitizerTablet, 965
        )
        self.assertEqual(
            IOBluetooth.kBluetoothGAPAppearanceHumanInterfaceDeviceCardReader, 966
        )
        self.assertEqual(
            IOBluetooth.kBluetoothGAPAppearanceHumanInterfaceDeviceDigitalPen, 967
        )
        self.assertEqual(
            IOBluetooth.kBluetoothGAPAppearanceHumanInterfaceDeviceBarcodeScanner, 968
        )
        self.assertEqual(IOBluetooth.kBluetoothGAPAppearanceGenericGlucoseMeter, 1024)
        self.assertEqual(
            IOBluetooth.kBluetoothGAPAppearanceGenericRunningWalkingSensor, 1088
        )
        self.assertEqual(IOBluetooth.kBluetoothGAPAppearanceGenericCycling, 1152)

        self.assertEqual(IOBluetooth.kBluetoothL2CAPPSMSDP, 0x0001)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPPSMRFCOMM, 0x0003)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPPSMTCS_BIN, 0x0005)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPPSMTCS_BIN_Cordless, 0x0007)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPPSMBNEP, 0x000F)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPPSMHIDControl, 0x0011)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPPSMHIDInterrupt, 0x0013)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPPSMAVCTP, 0x0017)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPPSMAVDTP, 0x0019)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPPSMAVCTP_Browsing, 0x001B)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPPSMUID_C_Plane, 0x001D)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPPSMATT, 0x001F)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPPSMReservedStart, 0x0001)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPPSMReservedEnd, 0x1000)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPPSMDynamicStart, 0x1001)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPPSMAACP, 0x1001)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPPSMD2D, 0x100F)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPPSMDynamicEnd, 0xFFFF)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPPSMNone, 0x0000)

        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16Base, 0x0000)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16SDP, 0x0001)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16UDP, 0x0002)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16RFCOMM, 0x0003)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16TCP, 0x0004)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16TCSBIN, 0x0005)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16TCSAT, 0x0006)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16ATT, 0x0007)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16OBEX, 0x0008)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16IP, 0x0009)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16FTP, 0x000A)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16HTTP, 0x000C)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16WSP, 0x000E)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16BNEP, 0x000F)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16UPNP, 0x0010)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16HIDP, 0x0011)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16HardcopyControlChannel, 0x0012)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16HardcopyDataChannel, 0x0014)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16HardcopyNotification, 0x0016)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16AVCTP, 0x0017)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16AVDTP, 0x0019)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16CMPT, 0x001B)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16UDI_C_Plane, 0x001D)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16MCAPControlChannel, 0x001E)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16MCAPDataChannel, 0x001F)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16L2CAP, 0x0100)

        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassServiceDiscoveryServer, 0x1000
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassBrowseGroupDescriptor, 0x1001
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassPublicBrowseGroup, 0x1002
        )
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16ServiceClassSerialPort, 0x1101)
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassLANAccessUsingPPP, 0x1102
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassDialupNetworking, 0x1103
        )
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16ServiceClassIrMCSync, 0x1104)
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassOBEXObjectPush, 0x1105
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassOBEXFileTransfer, 0x1106
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassIrMCSyncCommand, 0x1107
        )
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16ServiceClassHeadset, 0x1108)
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassCordlessTelephony, 0x1109
        )
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16ServiceClassAudioSource, 0x110A)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16ServiceClassAudioSink, 0x110B)
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassAVRemoteControlTarget, 0x110C
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassAdvancedAudioDistribution, 0x110D
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassAVRemoteControl, 0x110E
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassAVRemoteControlController, 0x110F
        )
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16ServiceClassIntercom, 0x1110)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16ServiceClassFax, 0x1111)
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassHeadsetAudioGateway, 0x1112
        )
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16ServiceClassWAP, 0x1113)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16ServiceClassWAPClient, 0x1114)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16ServiceClassPANU, 0x1115)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16ServiceClassNAP, 0x1116)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16ServiceClassGN, 0x1117)
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassDirectPrinting, 0x1118
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassReferencePrinting, 0x1119
        )
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16ServiceClassImaging, 0x111A)
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassImagingResponder, 0x111B
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassImagingAutomaticArchive, 0x111C
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassImagingReferencedObjects, 0x111D
        )
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16ServiceClassHandsFree, 0x111E)
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassHandsFreeAudioGateway, 0x111F
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassDirectPrintingReferenceObjectsService,
            0x1120,
        )
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16ServiceClassReflectedUI, 0x1121)
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassBasicPrinting, 0x1122
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassPrintingStatus, 0x1123
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassHumanInterfaceDeviceService,
            0x1124,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassHardcopyCableReplacement, 0x1125
        )
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16ServiceClassHCR_Print, 0x1126)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16ServiceClassHCR_Scan, 0x1127)
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassCommonISDNAccess, 0x1128
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassVideoConferencingGW, 0x1129
        )
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16ServiceClassUDI_MT, 0x112A)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16ServiceClassUDI_TA, 0x112B)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16ServiceClassAudioVideo, 0x112C)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16ServiceClassSIM_Access, 0x112D)
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassPhonebookAccess_PCE, 0x112E
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassPhonebookAccess_PSE, 0x112F
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassPhonebookAccess, 0x1130
        )
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16ServiceClassHeadset_HS, 0x1131)
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassMessageAccessServer, 0x1132
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassMessageNotificationServer, 0x1133
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassMessageAccessProfile, 0x1134
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassGlobalNavigationSatelliteSystem,
            0x1135,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassGlobalNavigationSatelliteSystemServer,
            0x1136,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassPnPInformation, 0x1200
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassGenericNetworking, 0x1201
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassGenericFileTransfer, 0x1202
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassGenericAudio, 0x1203
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassGenericTelephony, 0x1204
        )
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16ServiceClassVideoSource, 0x1303)
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16ServiceClassVideoSink, 0x1304)
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassVideoDistribution, 0x1305
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassHealthDevice, 0x1400
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassHealthDeviceSource, 0x1401
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPUUID16ServiceClassHealthDeviceSink, 0x1402
        )
        self.assertEqual(IOBluetooth.kBluetoothSDPUUID16ServiceClassGATT, 0x1801)

        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierServiceRecordHandle, 0x0000
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierServiceClassIDList, 0x0001
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierServiceRecordState, 0x0002
        )
        self.assertEqual(IOBluetooth.kBluetoothSDPAttributeIdentifierServiceID, 0x0003)
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierProtocolDescriptorList, 0x0004
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierBrowseGroupList, 0x0005
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierLanguageBaseAttributeIDList,
            0x0006,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierServiceInfoTimeToLive, 0x0007
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierServiceAvailability, 0x0008
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierBluetoothProfileDescriptorList,
            0x0009,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierDocumentationURL, 0x000A
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierClientExecutableURL, 0x000B
        )
        self.assertEqual(IOBluetooth.kBluetoothSDPAttributeIdentifierIconURL, 0x000C)
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierAdditionalProtocolsDescriptorList,
            0x000D,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierVersionNumberList, 0x0200
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierServiceDatabaseState, 0x0201
        )
        self.assertEqual(IOBluetooth.kBluetoothSDPAttributeIdentifierGroupID, 0x0200)
        self.assertEqual(IOBluetooth.kBluetoothSDPAttributeIdentifierIPSubnet, 0x0200)
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierHIDReleaseNumber, 0x0200
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierHIDParserVersion, 0x0201
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierHIDDeviceSubclass, 0x0202
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierHIDCountryCode, 0x0203
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierHIDVirtualCable, 0x0204
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierHIDReconnectInitiate, 0x0205
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierHIDDescriptorList, 0x0206
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierHIDLangIDBaseList, 0x0207
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierHIDSDPDisable, 0x0208
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierHIDBatteryPower, 0x0209
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierHIDRemoteWake, 0x020A
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierHIDProfileVersion, 0x020B
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierHIDSupervisionTimeout, 0x020C
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierHIDNormallyConnectable, 0x020D
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierHIDBootDevice, 0x020E
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierHIDSSRHostMaxLatency, 0x020F
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierHIDSSRHostMinTimeout, 0x0210
        )

        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierServiceVersion, 0x0300
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierExternalNetwork, 0x0301
        )
        self.assertEqual(IOBluetooth.kBluetoothSDPAttributeIdentifierNetwork, 0x0301)
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierSupportedDataStoresList, 0x0301
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierFaxClass1Support, 0x0302
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierRemoteAudioVolumeControl, 0x0302
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierFaxClass2_0Support, 0x0303
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierSupporterFormatsList, 0x0303
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierFaxClass2Support, 0x0304
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierAudioFeedbackSupport, 0x0305
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierNetworkAddress, 0x0306
        )
        self.assertEqual(IOBluetooth.kBluetoothSDPAttributeIdentifierWAPGateway, 0x0307)
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierHomepageURL, 0x0308
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierWAPStackType, 0x0309
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierSecurityDescription, 0x030A
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierNetAccessType, 0x030B
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierMaxNetAccessRate, 0x030C
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierSupportedCapabilities, 0x0310
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierSupportedFeatures, 0x0311
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierSupportedFunctions, 0x0312
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierTotalImagingDataCapacity, 0x0313
        )

        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierServiceName, 0x0000
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierServiceDescription, 0x0001
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeIdentifierProviderName, 0x0002
        )

        self.assertIsEnumType(IOBluetooth.SDPAttributeDeviceIdentificationRecord)
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeDeviceIdentifierServiceDescription, 0x0001
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeDeviceIdentifierDocumentationURL, 0x000A
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeDeviceIdentifierClientExecutableURL,
            0x000B,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeDeviceIdentifierSpecificationID, 0x0200
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeDeviceIdentifierVendorID, 0x0201
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeDeviceIdentifierProductID, 0x0202
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeDeviceIdentifierVersion, 0x0203
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeDeviceIdentifierPrimaryRecord, 0x0204
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeDeviceIdentifierVendorIDSource, 0x0205
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeDeviceIdentifierReservedRangeStart, 0x0206
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPAttributeDeviceIdentifierReservedRangeEnd, 0x02FF
        )

        self.assertIsEnumType(IOBluetooth.ProtocolParameters)
        self.assertEqual(IOBluetooth.kBluetoothSDPProtocolParameterL2CAPPSM, 1)
        self.assertEqual(IOBluetooth.kBluetoothSDPProtocolParameterRFCOMMChannel, 1)
        self.assertEqual(IOBluetooth.kBluetoothSDPProtocolParameterTCPPort, 1)
        self.assertEqual(IOBluetooth.kBluetoothSDPProtocolParameterUDPPort, 1)
        self.assertEqual(IOBluetooth.kBluetoothSDPProtocolParameterBNEPVersion, 1)
        self.assertEqual(
            IOBluetooth.kBluetoothSDPProtocolParameterBNEPSupportedNetworkPacketTypeList,
            2,
        )

        self.assertIsEnumType(IOBluetooth.BluetoothHCIExtendedInquiryResponseDataTypes)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataTypeFlags, 0x01
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataType16BitServiceClassUUIDsWithMoreAvailable,
            0x02,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataType16BitServiceClassUUIDsCompleteList,
            0x03,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataType32BitServiceClassUUIDsWithMoreAvailable,
            0x04,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataType32BitServiceClassUUIDsCompleteList,
            0x05,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataType128BitServiceClassUUIDsWithMoreAvailable,
            0x06,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataType128BitServiceClassUUIDsCompleteList,
            0x07,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataTypeShortenedLocalName,
            0x08,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataTypeCompleteLocalName,
            0x09,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataTypeTransmitPowerLevel,
            0x0A,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataTypeSSPOOBClassOfDevice,
            0x0D,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataTypeSSPOOBSimplePairingHashC,
            0x0E,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataTypeSSPOOBSimplePairingRandomizerR,
            0x0F,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataTypeDeviceID, 0x10
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataTypeSecurityManagerTKValue,
            0x10,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataTypeSecurityManagerOOBFlags,
            0x11,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataTypePeripheralConnectionIntervalRange,
            0x12,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataTypeServiceSolicitation16BitUUIDs,
            0x14,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataTypeServiceSolicitation128BitUUIDs,
            0x15,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataTypeServiceData, 0x16
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataTypePublicTargetAddress,
            0x17,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataTypeRandomTargetAddress,
            0x18,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataTypeAppearance, 0x19
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataTypeAdvertisingInterval,
            0x1A,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataTypeLEBluetoothDeviceAddress,
            0x1B,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataTypeLERole, 0x1C
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataTypeSimplePairingHash,
            0x1D,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataTypeSimplePairingRandomizer,
            0x1E,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataTypeServiceSolicitation32BitUUIDs,
            0x1F,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataTypeServiceData32BitUUID,
            0x20,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataTypeServiceData128BitUUID,
            0x21,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataTypeSecureConnectionsConfirmationValue,
            0x22,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataTypeSecureConnectionsRandomValue,
            0x23,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataTypeURI, 0x24
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataTypeIndoorPositioning,
            0x25,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataTypeTransportDiscoveryData,
            0x26,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataType3DInformationData,
            0x3D,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataTypeManufacturerSpecificData,
            0xFF,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataTypeSlaveConnectionIntervalRange,
            IOBluetooth.kBluetoothHCIExtendedInquiryResponseDataTypePeripheralConnectionIntervalRange,
        )

        self.assertEqual(IOBluetooth.kBluetoothHCIVersionCoreSpecification1_0b, 0x00)
        self.assertEqual(IOBluetooth.kBluetoothHCIVersionCoreSpecification1_1, 0x01)
        self.assertEqual(IOBluetooth.kBluetoothHCIVersionCoreSpecification1_2, 0x02)
        self.assertEqual(IOBluetooth.kBluetoothHCIVersionCoreSpecification2_0EDR, 0x03)
        self.assertEqual(IOBluetooth.kBluetoothHCIVersionCoreSpecification2_1EDR, 0x04)
        self.assertEqual(IOBluetooth.kBluetoothHCIVersionCoreSpecification3_0HS, 0x05)
        self.assertEqual(IOBluetooth.kBluetoothHCIVersionCoreSpecification4_0, 0x06)
        self.assertEqual(IOBluetooth.kBluetoothHCIVersionCoreSpecification4_1, 0x07)
        self.assertEqual(IOBluetooth.kBluetoothHCIVersionCoreSpecification4_2, 0x08)
        self.assertEqual(IOBluetooth.kBluetoothHCIVersionCoreSpecification5_0, 0x09)
        self.assertEqual(IOBluetooth.kBluetoothHCIVersionCoreSpecification5_1, 0x0A)
        self.assertEqual(IOBluetooth.kBluetoothHCIVersionCoreSpecification5_2, 0x0B)
        self.assertEqual(IOBluetooth.kBluetoothHCIVersionCoreSpecification5_3, 0x0C)

        self.assertIsEnumType(IOBluetooth.BluetoothLMPVersions)
        self.assertEqual(IOBluetooth.kBluetoothLMPVersionCoreSpecification1_0b, 0x00)
        self.assertEqual(IOBluetooth.kBluetoothLMPVersionCoreSpecification1_1, 0x01)
        self.assertEqual(IOBluetooth.kBluetoothLMPVersionCoreSpecification1_2, 0x02)
        self.assertEqual(IOBluetooth.kBluetoothLMPVersionCoreSpecification2_0EDR, 0x03)
        self.assertEqual(IOBluetooth.kBluetoothLMPVersionCoreSpecification2_1EDR, 0x04)
        self.assertEqual(IOBluetooth.kBluetoothLMPVersionCoreSpecification3_0HS, 0x05)
        self.assertEqual(IOBluetooth.kBluetoothLMPVersionCoreSpecification4_0, 0x06)
        self.assertEqual(IOBluetooth.kBluetoothLMPVersionCoreSpecification4_1, 0x07)
        self.assertEqual(IOBluetooth.kBluetoothLMPVersionCoreSpecification4_2, 0x08)
        self.assertEqual(IOBluetooth.kBluetoothLMPVersionCoreSpecification5_0, 0x09)
        self.assertEqual(IOBluetooth.kBluetoothLMPVersionCoreSpecification5_1, 0x0A)
        self.assertEqual(IOBluetooth.kBluetoothLMPVersionCoreSpecification5_2, 0x0B)

    def test_inline_functions(self):
        minorClass = 0xFF

        self.assertEqual(
            IOBluetooth.BluetoothCoDMinorPeripheral1(minorClass), minorClass & 0x30
        )
        self.assertEqual(
            IOBluetooth.BluetoothCoDMinorPeripheral2(minorClass), minorClass & 0x0F
        )
