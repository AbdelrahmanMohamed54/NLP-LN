import soundfile as sf

# Path to a sample WAV file
wav_file_path = "83f9c4ab_nohash_0.wav"

# Open the WAV file and get its sample rate
with sf.SoundFile(wav_file_path) as wav_file:
    sample_rate = wav_file.samplerate

print("Sample rate:", sample_rate, "Hz")
