import wave
import numpy as np
import matplotlib.pyplot as plt


def read_wav_file(file_path):
    with wave.open(file_path, 'rb') as wav_file:
        # Get the audio file parameters
        sample_width = wav_file.getsampwidth()
        frame_rate = wav_file.getframerate()
        num_frames = wav_file.getnframes()
        num_channels = wav_file.getnchannels()

        # Read the audio data
        audio_data = wav_file.readframes(num_frames)
    # Convert binary data to a numpy array
    audio_array = np.frombuffer(audio_data, dtype=np.int16)
    # Reshape the array according to the number of channels
    audio_array = audio_array.reshape(-1, num_channels)

    return audio_array, frame_rate


def process_audio(audio_array, frame_rate):
    # Extract left channel (assuming stereo audio)
    left_channel = audio_array[:, 0]

    # Cut out 2048 points every second and perform FFT
    window_size = 2048
    overlap = 0  # No overlap for simplicity, you may adjust this if needed

    num_windows = len(left_channel) // (window_size - overlap)

    # Initialize an array to store the log-scaled FFT results
    log_specgram = np.zeros((num_windows, 150))

    for i in range(num_windows):
        start = i * (window_size - overlap)
        end = start + window_size

        # Apply window function (e.g., Hamming window)
        window = np.hamming(window_size)
        windowed_data = left_channel[start:end] * window

        # Perform FFT using numpy
        fft_result = np.fft.fft(windowed_data)
        fft_magnitude = np.abs(fft_result)[:window_size // 2 + 1]

        # Convert to log scale using numpy
        log_specgram[i, :] = np.log10(1e-10 + fft_magnitude[0:150])

    return log_specgram


# Example usage
file_path = "../IIR/wav1.wav"  # Replace with the path to your WAV file
audio_array, frame_rate = read_wav_file(file_path)
log_specgram = process_audio(audio_array, frame_rate)

# Plotting the log-scaled spectrogram
plt.imshow(log_specgram.T, aspect='auto', origin='lower', cmap='viridis')
plt.colorbar(label='Log Magnitude (dB)')
plt.xlabel('Time Window')
plt.ylabel('Frequency Bin')
plt.title('Log-scaled Spectrogram')
plt.show()