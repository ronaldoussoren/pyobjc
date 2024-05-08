"""
Python mapping for the PHASE framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import AVFoundation
    import objc
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="PHASE",
        frameworkIdentifier="com.apple.audio.PHASE",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/PHASE.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(AVFoundation,),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("PHASESource", b"init"),
        ("PHASESource", b"new"),
        ("PHASEDistanceModelFadeOutParameters", b"init"),
        ("PHASEDistanceModelFadeOutParameters", b"new"),
        ("PHASEDistanceModelParameters", b"init"),
        ("PHASEDistanceModelParameters", b"new"),
        ("PHASEEnvelopeDistanceModelParameters", b"init"),
        ("PHASEEnvelopeDistanceModelParameters", b"new"),
        ("PHASEMetaParameterDefinition", b"init"),
        ("PHASEMetaParameterDefinition", b"new"),
        ("PHASENumberMetaParameterDefinition", b"init"),
        ("PHASENumberMetaParameterDefinition", b"new"),
        ("PHASEStringMetaParameterDefinition", b"init"),
        ("PHASEStringMetaParameterDefinition", b"new"),
        ("PHASEMappedMetaParameterDefinition", b"init"),
        ("PHASEMappedMetaParameterDefinition", b"new"),
        ("PHASEMappedMetaParameterDefinition", b"initWithValue:identifier:"),
        ("PHASEMappedMetaParameterDefinition", b"initWithValue:"),
        (
            "PHASEMappedMetaParameterDefinition",
            b"initWithValue:minimum:maximum:identifier:",
        ),
        ("PHASEMappedMetaParameterDefinition", b"initWithValue:minimum:maximum:"),
        ("PHASEMappedMetaParameterDefinition", b"minimum"),
        ("PHASEMappedMetaParameterDefinition", b"maximum"),
        ("PHASEMetaParameter", b"init"),
        ("PHASEMetaParameter", b"new"),
        ("PHASENumberMetaParameter", b"init"),
        ("PHASENumberMetaParameter", b"new"),
        ("PHASEStringMetaParameter", b"init"),
        ("PHASEStringMetaParameter", b"new"),
        ("PHASEEnvelope", b"init"),
        ("PHASEEnvelope", b"new"),
        ("PHASEMedium", b"init"),
        ("PHASEMedium", b"new"),
        ("PHASEEngine", b"init"),
        ("PHASEEngine", b"new"),
        ("PHASEShapeElement", b"init"),
        ("PHASEShapeElement", b"new"),
        ("PHASEShape", b"init"),
        ("PHASEShape", b"new"),
        ("PHASEOccluder", b"init"),
        ("PHASEOccluder", b"initWithEngine:"),
        ("PHASEOccluder", b"new"),
        ("PHASEGroupPresetSetting", b"init"),
        ("PHASEGroupPresetSetting", b"new"),
        ("PHASEGroupPreset", b"init"),
        ("PHASEGroupPreset", b"new"),
        ("PHASEMixerDefinition", b"init"),
        ("PHASEMixerDefinition", b"new"),
        ("PHASESpatialMixerDefinition", b"init"),
        ("PHASESpatialMixerDefinition", b"new"),
        ("PHASEAmbientMixerDefinition", b"init"),
        ("PHASEAmbientMixerDefinition", b"new"),
        ("PHASEChannelMixerDefinition", b"init"),
        ("PHASEChannelMixerDefinition", b"new"),
        ("PHASEMixer", b"init"),
        ("PHASEMixer", b"new"),
        ("PHASEMaterial", b"init"),
        ("PHASEMaterial", b"new"),
        ("PHASEDirectivityModelParameters", b"init"),
        ("PHASEDirectivityModelParameters", b"new"),
        ("PHASEGroup", b"init"),
        ("PHASEGroup", b"new"),
        ("PHASEListener", b"init"),
        ("PHASEListener", b"new"),
        ("PHASEDefinition", b"init"),
        ("PHASEDefinition", b"new"),
        ("PHASEDucker", b"init"),
        ("PHASEDucker", b"new"),
        ("PHASESpatialPipeline", b"init"),
        ("PHASESpatialPipeline", b"new"),
        ("PHASESoundEventNodeDefinition", b"init"),
        ("PHASESoundEventNodeDefinition", b"new"),
        ("PHASEGeneratorNodeDefinition", b"init"),
        ("PHASEGeneratorNodeDefinition", b"new"),
        ("PHASESamplerNodeDefinition", b"init"),
        ("PHASESamplerNodeDefinition", b"new"),
        ("PHASEBlendNodeDefinition", b"init"),
        ("PHASEBlendNodeDefinition", b"new"),
        ("PHASESwitchNodeDefinition", b"init"),
        ("PHASESwitchNodeDefinition", b"new"),
        ("PHASEPushStreamNodeDefinition", b"init"),
        ("PHASEPushStreamNodeDefinition", b"new"),
        ("PHASEPushStreamNode", b"init"),
        ("PHASEPushStreamNode", b"new"),
        ("PHASEObject", b"init"),
        ("PHASEObject", b"new"),
        ("PHASEAsset", b"init"),
        ("PHASEAsset", b"new"),
        ("PHASESoundAsset", b"init"),
        ("PHASESoundAsset", b"new"),
        ("PHASESoundEventNodeAsset", b"init"),
        ("PHASESoundEventNodeAsset", b"new"),
        ("PHASEGlobalMetaParameterAsset", b"init"),
        ("PHASEGlobalMetaParameterAsset", b"new"),
        ("PHASEAssetRegistry", b"init"),
        ("PHASEAssetRegistry", b"new"),
        ("PHASESoundEvent", b"init"),
        ("PHASESoundEvent", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)
    del sys.modules["PHASE._metadata"]


globals().pop("_setup")()
