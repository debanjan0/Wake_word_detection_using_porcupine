import struct
import pyaudio
import pvporcupine
from pyttsx3 import speak

porcupine = None
pa = None
audio_stream = None

try:
    porcupine = pvporcupine.create(access_key=<Access Key>,
                                   keywords=["computer", "jarvis"])

    pa = pyaudio.PyAudio()

    audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length)

    while True:
        pcm = audio_stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        keyword_index = porcupine.process(pcm)

        if keyword_index >= 0:
            print("Wake-word Detected")
            # add your funtion here to perform any task when the wake word detected
except:
    pass
