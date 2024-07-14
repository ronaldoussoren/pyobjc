#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"
#import <CoreMIDI/CoreMIDI.h>

/*
 * The definitions below can cause warnings when using
 * -Wunguarded-availability, but those warnings are harmless
 * because the functions are inline functions and hence will
 * be available on all macOS versions once compiled.
 */
#if PyObjC_BUILD_RELEASE >= 1013
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wunguarded-availability"
#endif

static PyObjC_function_map function_map[] = {
#if PyObjC_BUILD_RELEASE >= 1100
    {"MIDIMessageTypeForUPWord", (PyObjC_Function_Pointer)&MIDIMessageTypeForUPWord},
    {"MIDI1UPChannelVoiceMessage", (PyObjC_Function_Pointer)&MIDI1UPChannelVoiceMessage},
    {"MIDI1UPNoteOff", (PyObjC_Function_Pointer)&MIDI1UPNoteOff},
    {"MIDI1UPNoteOn", (PyObjC_Function_Pointer)&MIDI1UPNoteOn},
    {"MIDI1UPControlChange", (PyObjC_Function_Pointer)&MIDI1UPControlChange},
    {"MIDI1UPPitchBend", (PyObjC_Function_Pointer)&MIDI1UPPitchBend},
    {"MIDI1UPSystemCommon", (PyObjC_Function_Pointer)&MIDI1UPSystemCommon},
    {"MIDI2ChannelVoiceMessage", (PyObjC_Function_Pointer)&MIDI2ChannelVoiceMessage},
    {"MIDI2NoteOn", (PyObjC_Function_Pointer)&MIDI2NoteOn},
    {"MIDI2NoteOff", (PyObjC_Function_Pointer)&MIDI2NoteOff},
    {"MIDI2PolyPressure", (PyObjC_Function_Pointer)&MIDI2PolyPressure},
    {"MIDI2RegisteredPNC", (PyObjC_Function_Pointer)&MIDI2RegisteredPNC},
    {"MIDI2AssignablePNC", (PyObjC_Function_Pointer)&MIDI2AssignablePNC},
    {"MIDI2PerNoteManagment", (PyObjC_Function_Pointer)&MIDI2PerNoteManagment},
    {"MIDI2ControlChange", (PyObjC_Function_Pointer)&MIDI2ControlChange},
    {"MIDI2RegisteredControl", (PyObjC_Function_Pointer)&MIDI2RegisteredControl},
    {"MIDI2AssignableControl", (PyObjC_Function_Pointer)&MIDI2AssignableControl},
    {"MIDI2RelRegisteredControl", (PyObjC_Function_Pointer)&MIDI2RelRegisteredControl},
    {"MIDI2RelAssignableControl", (PyObjC_Function_Pointer)&MIDI2RelAssignableControl},
    {"MIDI2ProgramChange", (PyObjC_Function_Pointer)&MIDI2ProgramChange},
    {"MIDI2ChannelPressure", (PyObjC_Function_Pointer)&MIDI2ChannelPressure},
    {"MIDI2PitchBend", (PyObjC_Function_Pointer)&MIDI2PitchBend},
    {"MIDI2PerNotePitchBend", (PyObjC_Function_Pointer)&MIDI2PerNotePitchBend},
#endif
#if PyObjC_BUILD_RELEASE >= 1200
    {"MIDI1UPSysEx", (PyObjC_Function_Pointer)&MIDI1UPSysEx},
    {"MIDI1UPSysExArray", (PyObjC_Function_Pointer)&MIDI1UPSysExArray},
#endif
#if PyObjC_BUILD_RELEASE >= 1500
    {"MIDI1UPPolyPressure", (PyObjC_Function_Pointer)&MIDI1UPPolyPressure},
    {"MIDI1UPProgramChange", (PyObjC_Function_Pointer)&MIDI1UPProgramChange},
    {"MIDI1UPChannelPressure", (PyObjC_Function_Pointer)&MIDI1UPChannelPressure},
    {"MIDI2StreamMessage", (PyObjC_Function_Pointer)&MIDI2StreamMessage},
    {"MIDI2StreamMessageFromData", (PyObjC_Function_Pointer)&MIDI2StreamMessageFromData},
    {"MIDI2EndpointDiscoveryMessage", (PyObjC_Function_Pointer)&MIDI2EndpointDiscoveryMessage},
    {"MIDI2EndpointInfoNotificationMessage", (PyObjC_Function_Pointer)&MIDI2EndpointInfoNotificationMessage},
    {"MIDI2EndpointDeviceIdentityNotificationMessage", (PyObjC_Function_Pointer)&MIDI2EndpointDeviceIdentityNotificationMessage},
    {"MIDI2EndpointNameNotificationMessage", (PyObjC_Function_Pointer)&MIDI2EndpointNameNotificationMessage},
    {"MIDI2EndpointProductInstanceIDNotificationMessage", (PyObjC_Function_Pointer)&MIDI2EndpointProductInstanceIDNotificationMessage},
    {"MIDI2StreamConfigurationRequestMessage", (PyObjC_Function_Pointer)&MIDI2StreamConfigurationRequestMessage},
    {"MIDI2StreamConfigurationNotificationMessage", (PyObjC_Function_Pointer)&MIDI2StreamConfigurationNotificationMessage},
    {"MIDI2FunctionBlockDiscoveryMessage", (PyObjC_Function_Pointer)&MIDI2FunctionBlockDiscoveryMessage},
    {"MIDI2FunctionBlockInfoNotificationMessage", (PyObjC_Function_Pointer)&MIDI2FunctionBlockInfoNotificationMessage},
    {"MIDI2FunctionBlockNameNotificationMessage", (PyObjC_Function_Pointer)&MIDI2FunctionBlockNameNotificationMessage},
    {"MIDI2StartOfClipMessage", (PyObjC_Function_Pointer)&MIDI2StartOfClipMessage},
    {"MIDI2EndOfClipMessage", (PyObjC_Function_Pointer)&MIDI2EndOfClipMessage},
    {"MIDINoOpMessage", (PyObjC_Function_Pointer)&MIDINoOpMessage},
    {"MIDIJitterReductionClockMessage", (PyObjC_Function_Pointer)&MIDIJitterReductionClockMessage},
    {"MIDIJitterReductionTimestampMessage", (PyObjC_Function_Pointer)&MIDIJitterReductionTimestampMessage},
    {"MIDIDeltaClockstampTicksPerQuarterNoteMessage", (PyObjC_Function_Pointer)&MIDIDeltaClockstampTicksPerQuarterNoteMessage},
    {"MIDITicksSinceLastEventMessage", (PyObjC_Function_Pointer)&MIDITicksSinceLastEventMessage},
    {"MIDI2FlexDataMessage", (PyObjC_Function_Pointer)&MIDI2FlexDataMessage},

#endif
    {0, 0}};

#if PyObjC_BUILD_RELEASE >= 1013
#pragma clang diagnostic pop
#endif

static PyMethodDef mod_methods[] = {
    {0, 0, 0, 0} /* sentinel */
};

static int mod_exec_module(PyObject* m)
{
    if (PyModule_AddObject(m, "_inline_list_", PyObjC_CreateInlineTab(function_map))
        < 0) {
        return -1;
    }

    return 0;
}

static struct PyModuleDef_Slot mod_slots[] = {
    {
        .slot = Py_mod_exec,
        .value = (void*)mod_exec_module
    },
#if PY_VERSION_HEX >= 0x030c0000
    {
        /* This extension does not use the CPython API other than initializing
         * the module, hence is safe with subinterpreters and per-interpreter
         * GILs
         */
        .slot = Py_mod_multiple_interpreters,
        .value = Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED,
    },
#endif
#if PY_VERSION_HEX >= 0x030d0000
    {
        /* The code in this extension should be safe to use without the GIL */
        .slot = Py_mod_gil,
        .value = Py_MOD_GIL_USED,
    },
#endif
    {  /* Sentinel */
        .slot = 0,
        .value = 0
    }
};

static struct PyModuleDef mod_module = {
    .m_base = PyModuleDef_HEAD_INIT,
    .m_name = "_inlines",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit__inlines(void);

PyObject* __attribute__((__visibility__("default"))) PyInit__inlines(void)
{
    return PyModuleDef_Init(&mod_module);
}
