import CoreMedia as _CoreMedia


def CMTAG_IS_VALID(tag):
    return tag.dataType != _CoreMedia.kCMTagDataType_Invalid


def CMTAG_IS_INVALID(tag):
    return tag.dataType == _CoreMedia.kCMTagDataType_Invalid


def CMTIMERANGE_IS_VALID(aRange):
    return (
        CMTIME_IS_VALID(aRange.start)
        and CMTIME_IS_VALID(aRange.duration)
        and aRange.duration.epoch == 0
        and aRange.duration.value >= 0
    )


def CMTIMERANGE_IS_INVALID(aRange):
    return not CMTIMERANGE_IS_VALID(aRange)


def CMTIMERANGE_IS_INDEFINITE(aRange):
    return CMTIMERANGE_IS_VALID(aRange) and (
        CMTIME_IS_INDEFINITE(aRange.start) or CMTIME_IS_INDEFINITE(aRange.duration)
    )


def CMTIMERANGE_IS_EMPTY(aRange):
    return CMTIMERANGE_IS_VALID(aRange) and aRange.duration == _CoreMedia.kCMTimeZero


def CMTIMEMAPPING_IS_VALID(mapping):
    return CMTIMERANGE_IS_VALID(mapping.target)


def CMTIMEMAPPING_IS_INVALID(mapping):
    return not CMTIMEMAPPING_IS_VALID(mapping)


def CMTIMEMAPPING_IS_EMPTY(mapping):
    return not CMTIME_IS_NUMERIC(mapping.source.start) and CMTIMERANGE_IS_VALID(
        mapping.target
    )


def CMSimpleQueueGetFullness(queue):
    if _CoreMedia.CMSimpleQueueGetCapacity(queue):
        return _CoreMedia.CMSimpleQueueGetCount(
            queue
        ) / _CoreMedia.CMSimpleQueueGetCapacity(queue)
    else:
        return 0.0


def CMTIME_IS_VALID(time):
    return (time.flags & _CoreMedia.kCMTimeFlags_Valid) != 0


def CMTIME_IS_INVALID(time):
    return not CMTIME_IS_VALID(time)


def CMTIME_IS_POSITIVE_INFINITY(time):
    return (
        CMTIME_IS_VALID(time)
        and (time.flags & _CoreMedia.kCMTimeFlags_PositiveInfinity) != 0
    )


def CMTIME_IS_NEGATIVE_INFINITY(time):
    return (
        CMTIME_IS_VALID(time)
        and (time.flags & _CoreMedia.kCMTimeFlags_NegativeInfinity) != 0
    )


def CMTIME_IS_INDEFINITE(time):
    return (
        CMTIME_IS_VALID(time) and (time.flags & _CoreMedia.kCMTimeFlags_Indefinite) != 0
    )


def CMTIME_IS_NUMERIC(time):
    return (
        time.flags
        & (_CoreMedia.kCMTimeFlags_Valid | _CoreMedia.kCMTimeFlags_ImpliedValueFlagsMask)
    ) == _CoreMedia.kCMTimeFlags_Valid


def CMTIME_HAS_BEEN_ROUNDED(time):
    return (
        CMTIME_IS_NUMERIC(time)
        and (time.flags & _CoreMedia.kCMTimeFlags_HasBeenRounded) != 0
    )
