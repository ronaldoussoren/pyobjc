#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <CoreAudio/CoreAudio.h>

/* This functions are copies of the definition in the CoreAudio headers,
 * with minor tweaks to make them valid C instead of C++.
 *
 * Copy was introduced to be able to build wheels targeting older macOS
 * versions using Xcode 27.
 */
static bool
IsAudioFormatNativeEndian(const AudioStreamBasicDescription* f)
{
    return (f->mFormatID == kAudioFormatLinearPCM)
           && ((f->mFormatFlags & kAudioFormatFlagIsBigEndian)
               == kAudioFormatFlagsNativeEndian);
}

static AudioFormatFlags
CalculateLPCMFlags(UInt32 inValidBitsPerChannel, UInt32 inTotalBitsPerChannel,
                   bool inIsFloat, bool inIsBigEndian, bool inIsNonInterleaved)
{
    return (inIsFloat ? kAudioFormatFlagIsFloat : kAudioFormatFlagIsSignedInteger)
           | (inIsBigEndian ? ((UInt32)kAudioFormatFlagIsBigEndian) : 0)
           | ((inValidBitsPerChannel == inTotalBitsPerChannel)
                  ? kAudioFormatFlagIsPacked
                  : kAudioFormatFlagIsAlignedHigh)
           | (inIsNonInterleaved ? ((UInt32)kAudioFormatFlagIsNonInterleaved) : 0);
}

static void
FillOutASBDForLPCM(AudioStreamBasicDescription* outASBD, Float64 inSampleRate,
                   UInt32 inChannelsPerFrame, UInt32 inValidBitsPerChannel,
                   UInt32 inTotalBitsPerChannel, bool inIsFloat, bool inIsBigEndian,
                   bool inIsNonInterleaved)
{
    outASBD->mSampleRate = inSampleRate;
    outASBD->mFormatID   = kAudioFormatLinearPCM;
    outASBD->mFormatFlags =
        CalculateLPCMFlags(inValidBitsPerChannel, inTotalBitsPerChannel, inIsFloat,
                           inIsBigEndian, inIsNonInterleaved);
    outASBD->mBytesPerPacket =
        (inIsNonInterleaved ? 1 : inChannelsPerFrame) * (inTotalBitsPerChannel / 8);
    outASBD->mFramesPerPacket = 1;
    outASBD->mBytesPerFrame =
        (inIsNonInterleaved ? 1 : inChannelsPerFrame) * (inTotalBitsPerChannel / 8);
    outASBD->mChannelsPerFrame = inChannelsPerFrame;
    outASBD->mBitsPerChannel   = inValidBitsPerChannel;
}

static void
FillOutAudioTimeStampWithSampleTime(AudioTimeStamp* outATS, Float64 inSampleTime)
{
    outATS->mSampleTime    = inSampleTime;
    outATS->mHostTime      = 0;
    outATS->mRateScalar    = 0;
    outATS->mWordClockTime = 0;
    memset(&(outATS->mSMPTETime), 0, sizeof(SMPTETime));
    outATS->mFlags = kAudioTimeStampSampleTimeValid;
}

static void
FillOutAudioTimeStampWithHostTime(AudioTimeStamp* outATS, UInt64 inHostTime)
{
    outATS->mSampleTime    = 0;
    outATS->mHostTime      = inHostTime;
    outATS->mRateScalar    = 0;
    outATS->mWordClockTime = 0;
    memset(&(outATS->mSMPTETime), 0, sizeof(SMPTETime));
    outATS->mFlags = kAudioTimeStampHostTimeValid;
}

static void
FillOutAudioTimeStampWithSampleAndHostTime(AudioTimeStamp* outATS, Float64 inSampleTime,
                                           UInt64 inHostTime)
{
    outATS->mSampleTime    = inSampleTime;
    outATS->mHostTime      = inHostTime;
    outATS->mRateScalar    = 0;
    outATS->mWordClockTime = 0;
    memset(&(outATS->mSMPTETime), 0, sizeof(SMPTETime));
    outATS->mFlags = kAudioTimeStampSampleTimeValid | kAudioTimeStampHostTimeValid;
}

static PyObjC_function_map function_map[] = {
    {"IsAudioFormatNativeEndian", (PyObjC_Function_Pointer)&IsAudioFormatNativeEndian},
    {"CalculateLPCMFlags", (PyObjC_Function_Pointer)&CalculateLPCMFlags},
    {"FillOutASBDForLPCM", (PyObjC_Function_Pointer)&FillOutASBDForLPCM},
    {"FillOutAudioTimeStampWithSampleTime",
     (PyObjC_Function_Pointer)&FillOutAudioTimeStampWithSampleTime},
    {"FillOutAudioTimeStampWithHostTime",
     (PyObjC_Function_Pointer)&FillOutAudioTimeStampWithHostTime},
    {"FillOutAudioTimeStampWithSampleAndHostTime",
     (PyObjC_Function_Pointer)&FillOutAudioTimeStampWithSampleAndHostTime},
#if PyObjC_BUILD_RELEASE >= 1011
    {"AudioChannelLayoutTag_GetNumberOfChannels",
     (PyObjC_Function_Pointer)&AudioChannelLayoutTag_GetNumberOfChannels},
#endif
    {0, 0}};

static PyMethodDef mod_methods[] = {
    {0, 0, 0, 0} /* sentinel */
};

static int
mod_exec_module(PyObject* m)
{
    if (PyModule_AddObject(m, "_inline_list_", PyObjC_CreateInlineTab(function_map))
        < 0) {
        return -1;
    }

    return 0;
}

static struct PyModuleDef_Slot mod_slots[] = {
    {.slot = Py_mod_exec, .value = (void*)mod_exec_module},
#if PY_VERSION_HEX >= 0x030c0000
    {
        /* This extension does not use the CPython API other than initializing
         * the module, hence is safe with subinterpreters and per-interpreter
         * GILs
         */
        .slot  = Py_mod_multiple_interpreters,
        .value = Py_MOD_PER_INTERPRETER_GIL_SUPPORTED,
    },
#endif
#if PY_VERSION_HEX >= 0x030d0000
    {
        /* The code in this extension should be safe to use without the GIL */
        .slot  = Py_mod_gil,
        .value = Py_MOD_GIL_NOT_USED,
    },
#endif
    {/* Sentinel */
     .slot  = 0,
     .value = 0}};

static struct PyModuleDef mod_module = {
    .m_base     = PyModuleDef_HEAD_INIT,
    .m_name     = "_inlines",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit__inlines(void);

PyObject* __attribute__((__visibility__("default")))
PyInit__inlines(void)
{
    return PyModuleDef_Init(&mod_module);
}
