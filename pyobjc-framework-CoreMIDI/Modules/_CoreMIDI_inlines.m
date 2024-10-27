#ifndef PyObjC_GIL_DISABLED
#define Py_LIMITED_API 0x03060000
#endif
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
    {0, 0}};

#if PyObjC_BUILD_RELEASE >= 1013
#pragma clang diagnostic pop
#endif

static PyMethodDef mod_methods[] = {
    {0, 0, 0, 0} /* sentinel */
};

/* Python glue */
static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "_inlines", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit__inlines(void);

PyObject*
PyInit__inlines(void)
{
    PyObject* m;
    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyModule_AddObject(m, "_inline_list_", PyObjC_CreateInlineTab(function_map))
        < 0) {
        return NULL;
    }

    return m;
}
