import os
import whisper
import pyaudio
import numpy as np
import torch
import pyttsx3

# Load Whisper model on GPU with fp16
model_size = "medium.en"
device = "cpu"
model = whisper.load_model(model_size, device=device)



print(f"✅ Loaded {model_size} on {device}")

# PyAudio setup
CHUNK = 512 # number of frames per buffer
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 5  # smaller chunks = lower latency

p = pyaudio.PyAudio()
stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK,
    input_host_api_specific_stream_info=None,
    start=True
)


# Initialize TTS

accumulated_transcription = ""

print("🎤 Real-time transcription started... Press Ctrl+C to stop")

try:
    while True:
        frames = []

        # Record short chunk
        for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK, exception_on_overflow=False)
            frames.append(data)

        # Convert bytes to float32 numpy array
        audio_bytes = b''.join(frames)
        audio_np = np.frombuffer(audio_bytes, dtype=np.int16).astype(np.float32) / 32768.0

        # Transcribe directly from numpy
        result = model.transcribe(audio_np, fp16=(device != "cpu"))

        transcription = result["text"].strip()

        if transcription:
            print("📝", transcription)
            accumulated_transcription += transcription + " "

except KeyboardInterrupt:
    print("\n🛑 Stopped recording.")

finally:
    stream.stop_stream()
    stream.close()
    p.terminate()

    print("\n🔹 Full transcript:")
    print(accumulated_transcription)
    pyttsx3.speak(accumulated_transcription)

    # Save to log
    with open("log.txt", "w", encoding="utf-8") as f:
        f.write(accumulated_transcription)