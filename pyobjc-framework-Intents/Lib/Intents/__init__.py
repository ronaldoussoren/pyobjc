"""
Python mapping for the Intents framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _Intents

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="Intents",
        frameworkIdentifier="com.apple.Intents",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/Intents.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _Intents,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("INFocusStatus", b"init"),
        ("INTicketedEvent", b"init"),
        ("INCallRecordFilter", b"init"),
        ("INPaymentMethod", b"init"),
        ("INShortcut", b"init"),
        ("INShortcut", b"new"),
        ("INVoiceShortcut", b"init"),
        ("INVoiceShortcut", b"new"),
        ("INCallRecord", b"init"),
        ("INTrainTrip", b"init"),
        ("INIntentDonationMetadata", b"init"),
        ("INAirport", b"init"),
        ("INGetReservationDetailsIntentResponse", b"init"),
        ("INPersonHandle", b"init"),
        ("INRentalCar", b"init"),
        ("INUnsendMessagesIntentResponse", b"init"),
        ("INShareFocusStatusIntentResponse", b"init"),
        ("INEditMessageIntentResponse", b"init"),
        ("INBoatReservation", b"init"),
        ("INBoatTrip", b"init"),
        ("INPerson", b"init"),
        ("INDateComponentsRange", b"init"),
        ("INReservation", b"init"),
        ("INObjectCollection", b"init"),
        ("INBusTrip", b"init"),
        ("INBusReservation", b"init"),
        ("INAirportGate", b"init"),
        ("INSendMessageIntentResponse", b"init"),
        ("INObjectSection", b"init"),
        ("INCurrencyAmount", b"init"),
        ("INSpeakableString", b"init"),
        ("INIntentResolutionResult", b"init"),
        ("INAirline", b"init"),
        ("INObject", b"init"),
        ("INHangUpCallIntentResponse", b"init"),
        ("INCallGroup", b"init"),
        ("INSeat", b"init"),
        ("INAnswerCallIntentResponse", b"init"),
        ("INInteraction", b"init"),
        ("INReservationAction", b"init"),
        ("INVoiceShortcutCenter", b"init"),
        ("INVoiceShortcutCenter", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["Intents._metadata"]


globals().pop("_setup")()
