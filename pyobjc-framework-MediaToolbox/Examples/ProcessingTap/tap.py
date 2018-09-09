import AVFoundation
import CoreAudio
import Foundation
import MediaToolbox
import objc

MEDIAPATH="/System/Library/CoreServices/Language Chooser.app/Contents/Resources/VOInstructions-en.m4a"

def init(tap, info, storage):
    print("Init", tap)
    return info

def finalize(tap):
    print("Finalize")

def prepare(tap, maxFrames, processingFormat):
    print(f"prepare {tap}, maxFrames={maxFrames}")

    format4cc = Foundation.CFSwapInt32HostToBig(processingFormat.mFormatID)

    print(f"Sample Rate: {processingFormat.mSampleRate}")
    print(f"Channels: {processingFormat.mChannelsPerFrame}")
    print(f"Bits: {processingFormat.mBitsPerChannel}")
    print(f"BytesPerFrame: {processingFormat.mBytesPerFrame}")
    print(f"BytesPerPacket: {processingFormat.mBytesPerPacket}")
    print(f"FramesPerPacket: {processingFormat.mFramesPerPacket}")
    print(f"Format Flags: {processingFormat.mFormatFlags}")

def process(tap, numberFrames, flags, bufferList, framesOut, flagsOut):
    #print("process", bufferList)

    res, flagsOut, timeRangeOut, framesOut = MediaToolbox.MTAudioProcessingTapGetSourceAudio(
        tap, numberFrames, bufferList, None, objc.NULL, None)

    #print(f"res: {res}, flagsOut: {flagsOut}, framesOut: {framesOut}")

    # Do something here

    return (bufferList, framesOut, flagsOut)

def unprepare(tap):
    print("Unprepare", tap)



def main():
    asset = AVFoundation.AVAsset.assetWithURL_(Foundation.NSURL.fileURLWithPath_isDirectory_(MEDIAPATH, False))
    playerItem = AVFoundation.AVPlayerItem.playerItemWithAsset_(asset)

    callbacks = (MediaToolbox.kMTAudioProcessingTapCallbacksVersion_0, 42, init, finalize, prepare, unprepare, process)
    #callbacks = (MediaToolbox.kMTAudioProcessingTapCallbacksVersion_0, 42, None, None, None, None, process)
    err, tap = MediaToolbox.MTAudioProcessingTapCreate(None, callbacks, MediaToolbox.kMTAudioProcessingTapCreationFlag_PostEffects, None)

    print("Creating tap", err, tap)

    inputParams = AVFoundation.AVMutableAudioMixInputParameters.audioMixInputParametersWithTrack_(asset.tracks()[0])
    inputParams.setAudioTapProcessor_(tap)

    audioMix = AVFoundation.AVMutableAudioMix.audioMix()
    audioMix.setInputParameters_([inputParams])
    playerItem.setAudioMix_(audioMix)

    player = AVFoundation.AVPlayer.playerWithPlayerItem_(playerItem)
    player.play()

    Foundation.NSRunLoop.currentRunLoop().runUntilDate_(Foundation.NSDate.dateWithTimeIntervalSinceNow_(5))

    playerItem.setAudioMix_(None)
    player.pause()
    del player


if __name__ == "__main__":
    main()
