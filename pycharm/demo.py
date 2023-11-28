import wx
from demoUI import MyFrame1
import pyaudio
from datetime import datetime
import numpy as np
from scipy.io import wavfile
from scipy.signal import stft
from pathConverter import resource_path
CHANNELS = 1
FRAME_RATE = 16000
RECORD_SECONDS = 0.1
AUDIO_FORMAT = pyaudio.paInt16
SAMPLE_SIZE = 2
chunk=2048

dt = np.dtype(np.int16)
dt = dt.newbyteorder('<')
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

def softmax(v):
    p=np.exp(v)/np.sum(np.exp(v))
    return p

class MyFrame(MyFrame1):
    def __init__(self, parent):
        MyFrame1.__init__(self, parent)
        self.OMconnected = False
        self.p = pyaudio.PyAudio()
        for i in range(self.p.get_device_count()):
            self.m_choice1.Append(self.p.get_device_info_by_index(i)['name'])

        self.models_reg = []
        self.models_reg.append(np.load(resource_path("subject1.weight150.npy")))
        self.models_reg.append(np.load(resource_path("subject2.weight150.npy")))
        self.models_reg.append(np.load(resource_path("subject3.weight150.npy")))
        self.frames = []
        self.v = np.array([], dtype=dt)

        self.m_bitmap1.SetBitmap(wx.Bitmap(resource_path("1.bmp")))
        self.m_bitmap2.SetBitmap(wx.Bitmap(resource_path("2.bmp")))
        self.m_bitmap3.SetBitmap(wx.Bitmap(resource_path("3.bmp")))


    def Closing(self, event):
        self.p.terminate()
        event.Skip()

    def startStop(self, event):
        if self.m_toggleBtn1.Value==True:
            self.stream = self.p.open(format=AUDIO_FORMAT,
                            channels=CHANNELS,
                            rate=FRAME_RATE,
                            input=True,
                            input_device_index=self.m_choice1.Selection,
                            frames_per_buffer=chunk)
            self.frames=[]
            self.v = np.array([], dtype=dt)
            self.m_timer1.Start(1,True)
        else:
            self.m_timer1.Stop()
            self.frame = []
            self.stream.stop_stream()
            self.stream.close()
            self.m_gauge1.Value =0
            self.m_gauge2.Value = 0
            self.m_gauge3.Value = 0
            self.m_gauge4.Value = 0
            print("Stopped")
        event.Skip()

    def tick(self, event):
        if self.m_toggleBtn1.Value == False:
            event.Skip()

        data = self.stream.read(chunk)
        self.frames.append(data)
        if len(self.frames) >= (FRAME_RATE * RECORD_SECONDS) / chunk:
            for e in self.frames:
                self.v = np.append(self.v, np.frombuffer(e, dtype=dt))
                self.v = self.v[-20480:]
                amplitue=np.mean(np.abs(self.v))
                if amplitue>self.m_gauge1.Range:
                    amplitue=self.m_gauge1.Range
                self.m_gauge1.Value=int(amplitue)
                f = data2fft(self.v)[0:150, :].transpose()
                realtime_pred = predictConf(f, self.models_reg)
                conf=softmax(np.mean(realtime_pred, axis=0))
                self.m_gauge2.Value = int(conf[0]*100)
                self.m_gauge3.Value = int(conf[1]*100)
                self.m_gauge4.Value = int(conf[2]*100)
            self.frames=[]

        self.m_timer1.Start(1, True)
        event.Skip()



if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None)
    frame.Show(True)
    app.MainLoop()