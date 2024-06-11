# This file is generated by objective.metadata
#
# Last update: Tue Jun 11 10:20:56 2024
#
# flake8: noqa

import objc, sys
from typing import NewType

if sys.maxsize > 2**32:

    def sel32or64(a, b):
        return b

else:

    def sel32or64(a, b):
        return a


if objc.arch == "arm64":

    def selAorI(a, b):
        return a

else:

    def selAorI(a, b):
        return b


misc = {}
constants = """$SKANErrorDomain$SKAdNetworkCoarseConversionValueHigh$SKAdNetworkCoarseConversionValueLow$SKAdNetworkCoarseConversionValueMedium$SKCloudServiceCapabilitiesDidChangeNotification$SKCloudServiceSetupActionSubscribe$SKCloudServiceSetupMessageIdentifierAddMusic$SKCloudServiceSetupMessageIdentifierConnect$SKCloudServiceSetupMessageIdentifierJoin$SKCloudServiceSetupMessageIdentifierPlayMusic$SKCloudServiceSetupOptionsActionKey$SKCloudServiceSetupOptionsAffiliateTokenKey$SKCloudServiceSetupOptionsCampaignTokenKey$SKCloudServiceSetupOptionsITunesItemIdentifierKey$SKCloudServiceSetupOptionsMessageIdentifierKey$SKDownloadTimeRemainingUnknown@d$SKErrorDomain$SKReceiptPropertyIsExpired$SKReceiptPropertyIsRevoked$SKReceiptPropertyIsVolumePurchase$SKStoreProductParameterAdNetworkAttributionSignature$SKStoreProductParameterAdNetworkCampaignIdentifier$SKStoreProductParameterAdNetworkIdentifier$SKStoreProductParameterAdNetworkNonce$SKStoreProductParameterAdNetworkSourceAppStoreIdentifier$SKStoreProductParameterAdNetworkSourceIdentifier$SKStoreProductParameterAdNetworkTimestamp$SKStoreProductParameterAdNetworkVersion$SKStoreProductParameterAdvertisingPartnerToken$SKStoreProductParameterAffiliateToken$SKStoreProductParameterCampaignToken$SKStoreProductParameterCustomProductPageIdentifier$SKStoreProductParameterITunesItemIdentifier$SKStoreProductParameterProductIdentifier$SKStoreProductParameterProviderToken$SKStorefrontCountryCodeDidChangeNotification$SKStorefrontIdentifierDidChangeNotification$"""
enums = """$SKANErrorAdNetworkIdMissing@2$SKANErrorImpressionMissingRequiredValue@0$SKANErrorImpressionNotFound@4$SKANErrorImpressionTooShort@11$SKANErrorInvalidAdvertisedAppId@8$SKANErrorInvalidCampaignId@5$SKANErrorInvalidConversionValue@6$SKANErrorInvalidSourceAppId@7$SKANErrorInvalidVersion@9$SKANErrorMismatchedSourceAppId@3$SKANErrorUnknown@10$SKANErrorUnsupported@1$SKCloudServiceAuthorizationStatusAuthorized@3$SKCloudServiceAuthorizationStatusDenied@1$SKCloudServiceAuthorizationStatusNotDetermined@0$SKCloudServiceAuthorizationStatusRestricted@2$SKCloudServiceCapabilityAddToCloudMusicLibrary@256$SKCloudServiceCapabilityMusicCatalogPlayback@1$SKCloudServiceCapabilityMusicCatalogSubscriptionEligible@2$SKCloudServiceCapabilityNone@0$SKDownloadStateActive@1$SKDownloadStateCancelled@5$SKDownloadStateFailed@4$SKDownloadStateFinished@3$SKDownloadStatePaused@2$SKDownloadStateWaiting@0$SKErrorClientInvalid@1$SKErrorCloudServiceNetworkConnectionFailed@7$SKErrorCloudServicePermissionDenied@6$SKErrorCloudServiceRevoked@8$SKErrorIneligibleForOffer@18$SKErrorInvalidOfferIdentifier@11$SKErrorInvalidOfferPrice@14$SKErrorInvalidSignature@12$SKErrorMissingOfferParams@13$SKErrorOverlayCancelled@15$SKErrorOverlayInvalidConfiguration@16$SKErrorOverlayPresentedInBackgroundScene@20$SKErrorOverlayTimeout@17$SKErrorPaymentCancelled@2$SKErrorPaymentInvalid@3$SKErrorPaymentNotAllowed@4$SKErrorPrivacyAcknowledgementRequired@9$SKErrorStoreProductNotAvailable@5$SKErrorUnauthorizedRequestData@10$SKErrorUnknown@0$SKErrorUnsupportedPlatform@19$SKOverlayPositionBottom@0$SKOverlayPositionBottomRaised@1$SKPaymentTransactionStateDeferred@4$SKPaymentTransactionStateFailed@2$SKPaymentTransactionStatePurchased@1$SKPaymentTransactionStatePurchasing@0$SKPaymentTransactionStateRestored@3$SKProductDiscountPaymentModeFreeTrial@2$SKProductDiscountPaymentModePayAsYouGo@0$SKProductDiscountPaymentModePayUpFront@1$SKProductDiscountTypeIntroductory@0$SKProductDiscountTypeSubscription@1$SKProductPeriodUnitDay@0$SKProductPeriodUnitMonth@2$SKProductPeriodUnitWeek@1$SKProductPeriodUnitYear@3$SKProductStorePromotionVisibilityDefault@0$SKProductStorePromotionVisibilityHide@2$SKProductStorePromotionVisibilityShow@1$"""
misc.update(
    {
        "SKProductDiscountPaymentMode": NewType("SKProductDiscountPaymentMode", int),
        "SKOverlayPosition": NewType("SKOverlayPosition", int),
        "SKProductDiscountType": NewType("SKProductDiscountType", int),
        "SKCloudServiceCapability": NewType("SKCloudServiceCapability", int),
        "SKPaymentTransactionState": NewType("SKPaymentTransactionState", int),
        "SKANError": NewType("SKANError", int),
        "SKProductStorePromotionVisibility": NewType(
            "SKProductStorePromotionVisibility", int
        ),
        "SKCloudServiceAuthorizationStatus": NewType(
            "SKCloudServiceAuthorizationStatus", int
        ),
        "SKErrorCode": NewType("SKErrorCode", int),
        "SKDownloadState": NewType("SKDownloadState", int),
        "SKProductPeriodUnit": NewType("SKProductPeriodUnit", int),
    }
)
misc.update({})
misc.update({})
functions = {"SKTerminateForInvalidReceipt": (b"v",)}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"NSObject",
        b"cloudServiceSetupViewControllerDidDismiss:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"paymentQueue:didRevokeEntitlementsForProductIdentifiers:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"paymentQueue:removedTransactions:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"paymentQueue:restoreCompletedTransactionsFailedWithError:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"paymentQueue:shouldAddStorePayment:forProduct:",
        {
            "required": False,
            "retval": {"type": b"Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"paymentQueue:shouldContinueTransaction:inStorefront:",
        {
            "required": False,
            "retval": {"type": b"Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"paymentQueue:updatedDownloads:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"paymentQueue:updatedTransactions:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"paymentQueueDidChangeStorefront:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"paymentQueueRestoreCompletedTransactionsFinished:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"paymentQueueShouldShowPriceConsent:",
        {"required": False, "retval": {"type": b"Z"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"productViewControllerDidFinish:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"productsRequest:didReceiveResponse:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"request:didFailWithError:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"requestDidFinish:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"storeOverlay:didFailToLoadWithError:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"storeOverlay:didFinishDismissal:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"storeOverlay:didFinishPresentation:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"storeOverlay:willStartDismissal:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"storeOverlay:willStartPresentation:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"SKAdNetwork",
        b"endImpression:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"SKAdNetwork",
        b"startImpression:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"SKAdNetwork",
        b"updatePostbackConversionValue:coarseValue:completionHandler:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"SKAdNetwork",
        b"updatePostbackConversionValue:coarseValue:lockWindow:completionHandler:",
        {
            "arguments": {
                4: {"type": b"Z"},
                5: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                },
            }
        },
    )
    r(
        b"SKAdNetwork",
        b"updatePostbackConversionValue:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"SKArcadeService",
        b"arcadeSubscriptionStatusWithNonce:resultHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"@"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"I"},
                            3: {"type": b"@"},
                            4: {"type": b"I"},
                            5: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"SKArcadeService",
        b"registerArcadeAppWithRandomFromLib:randomFromLibLength:resultHandler:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"I"},
                            3: {"type": b"@"},
                            4: {"type": b"I"},
                            5: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"SKCloudServiceController",
        b"requestAuthorization:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"q"}},
                    }
                }
            }
        },
    )
    r(
        b"SKCloudServiceController",
        b"requestCapabilitiesWithCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"Q"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"SKCloudServiceController",
        b"requestPersonalizationTokenForClientToken:withCompletionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"SKCloudServiceController",
        b"requestStorefrontCountryCodeWithCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"SKCloudServiceController",
        b"requestStorefrontIdentifierWithCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"SKCloudServiceController",
        b"requestUserTokenForDeveloperToken:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"SKCloudServiceSetupViewController",
        b"loadWithOptions:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"Z"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"SKMutablePayment",
        b"setSimulatesAskToBuyInSandbox:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"SKMutablePayment", b"simulatesAskToBuyInSandbox", {"retval": {"type": b"Z"}})
    r(
        b"SKOverlayAppConfiguration",
        b"setUserDismissible:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"SKOverlayAppConfiguration", b"userDismissible", {"retval": {"type": b"Z"}})
    r(
        b"SKOverlayTransitionContext",
        b"addAnimationBlock:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                }
            }
        },
    )
    r(b"SKPayment", b"simulatesAskToBuyInSandbox", {"retval": {"type": b"Z"}})
    r(b"SKPaymentQueue", b"canMakePayments", {"retval": {"type": b"Z"}})
    r(b"SKProduct", b"downloadable", {"retval": {"type": b"Z"}})
    r(b"SKProduct", b"isDownloadable", {"retval": {"type": b"Z"}})
    r(b"SKProduct", b"isFamilyShareable", {"retval": {"type": b"Z"}})
    r(
        b"SKProductStorePromotionController",
        b"fetchStorePromotionOrderWithCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"SKProductStorePromotionController",
        b"fetchStorePromotionVisibilityForProduct:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"q"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"SKProductStorePromotionController",
        b"updateStorePromotionOrder:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"SKProductStorePromotionController",
        b"updateStorePromotionVisibility:forProduct:completionHandler:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"SKStoreProductViewController",
        b"loadProductWithParameters:completionBlock:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"Z"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"SKStoreProductViewController",
        b"loadProductWithParameters:impression:completionBlock:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"Z"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
finally:
    objc._updatingMetadata(False)

objc.registerNewKeywordsFromSelector("SKOverlay", b"initWithConfiguration:")
objc.registerNewKeywordsFromSelector(
    "SKOverlayAppClipConfiguration", b"initWithPosition:"
)
objc.registerNewKeywordsFromSelector(
    "SKOverlayAppConfiguration", b"initWithAppIdentifier:position:"
)
objc.registerNewKeywordsFromSelector(
    "SKPaymentDiscount", b"initWithIdentifier:keyIdentifier:nonce:signature:timestamp:"
)
objc.registerNewKeywordsFromSelector(
    "SKProductsRequest", b"initWithProductIdentifiers:"
)
objc.registerNewKeywordsFromSelector(
    "SKReceiptRefreshRequest", b"initWithReceiptProperties:"
)
expressions = {
    "StoreKitBundle": "NSBundle.bundleWithPath_('/System/Library/Frameworks/StoreKit.framework')"
}

# END OF FILE
