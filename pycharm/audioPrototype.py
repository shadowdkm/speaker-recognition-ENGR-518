
import pyaudio
from datetime import datetime
import numpy as np
from scipy.io import wavfile
from scipy.signal import stft
import pandas as pd

def wav2fft(Path):
    # Load an audio file
    file_path = Path  # Replace with the path to your audio file
    sr, y = wavfile.read(file_path)

    # Compute the STFT
    n_fft = 2048  # Number of FFT points (window size)
    hop_length = 512  # Hop length between frames
    f, t, Zxx = stft(y, fs=sr, nperseg=n_fft, noverlap=hop_length)

    # Convert amplitude spectrogram to dB scale
    Zxx_db = 10 * np.log10(np.abs(Zxx)+0.0001)
    return Zxx_db

def data2fft(y):
    # Compute the STFT
    n_fft = 2048  # Number of FFT points (window size)
    hop_length = 512  # Hop length between frames
    f, t, Zxx = stft(y, fs=16000, nperseg=n_fft, noverlap=hop_length)

    # Convert amplitude spectrogram to dB scale
    Zxx_db = 10 * np.log10(np.abs(Zxx)+0.0001)
    return Zxx_db

def sigmoid(z):
    return 1 / (1 + np.exp(-z))
def predictConf(X, models):
    m = X.shape[0]
    X = np.hstack((np.ones((m, 1)), X))
    preds = np.array([sigmoid(X @ w) for w in models]).T
    #return np.argmax(preds, axis=1)
    return preds



CHANNELS = 1
FRAME_RATE = 16000
RECORD_SECONDS = 0.5
AUDIO_FORMAT = pyaudio.paInt16
SAMPLE_SIZE = 2
chunk=2048

p = pyaudio.PyAudio()

stream = p.open(format=AUDIO_FORMAT,
                channels=CHANNELS,
                rate=FRAME_RATE,
                input=True,
                input_device_index=1,
                frames_per_buffer=chunk)

frames = []
startTime=datetime.now()
print("start")

dt = np.dtype(np.int16)
dt = dt.newbyteorder('<')
v = np.array([], dtype=dt)
while (datetime.now()-startTime).seconds<10:

    data = stream.read(chunk)
    frames.append(data)
    if len(frames) >= (FRAME_RATE * RECORD_SECONDS) / chunk:
        #recordings.put(frames.copy())
        for e in frames:
            v = np.append(v,np.frombuffer(e, dtype=dt))
            v = v[-20480:]
            f = data2fft(v)[0:150, :].transpose()
            realtime_pred = predictConf(f, models_reg)
            print(np.mean(realtime_pred, axis=0))
        frames = []


print(v.shape)
stream.stop_stream()
stream.close()
p.terminate()
print("Section done")