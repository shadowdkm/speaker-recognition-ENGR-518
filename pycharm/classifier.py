import numpy as np
import pandas as pd
import scipy
import myFilterX6

# Logistic Regression Functions
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def cost_function_reg(X, y, weights, lambda_reg):
    m = X.shape[0]
    h = sigmoid(X @ weights)
    epsilon = 1e-5
    reg_term = (lambda_reg / (2 * m)) * np.sum(np.square(weights[1:]))
    cost = -1/m * np.sum(y * np.log(h + epsilon) + (1 - y) * np.log(1 - h + epsilon)) + reg_term
    return cost

def gradient_descent_reg(X, y, weights, learning_rate, iterations, lambda_reg):
    m = X.shape[0]
    cost_history = []

    for _ in range(iterations):
        weights[0] -= (learning_rate / m) * np.sum(sigmoid(X @ weights) - y)
        weights[1:] -= (learning_rate / m) * (X[:, 1:].T @ (sigmoid(X @ weights) - y) + lambda_reg * weights[1:])
        cost_history.append(cost_function_reg(X, y, weights, lambda_reg))

    return weights, cost_history

def train_one_vs_rest(X, y, num_classes, learning_rate, iterations, lambda_reg):
    models = []
    m, n = X.shape
    X = np.hstack((np.ones((m, 1)), X))

    for i in range(num_classes):
        y_ovr = np.where(y == i, 1, 0)
        weights = np.zeros(n + 1)
        weights, _ = gradient_descent_reg(X, y_ovr, weights, learning_rate, iterations, lambda_reg)
        models.append(weights)

    return models

def predict(X, models):
    m = X.shape[0]
    X = np.hstack((np.ones((m, 1)), X))
    preds = np.array([sigmoid(X @ w) for w in models]).T
    return np.argmax(preds, axis=1)

# Manual Data Splitting Function
def split_data(data, train_frac, test_frac):
    train_size = int(len(data) * train_frac)
    test_size = int(len(data) * test_frac)
    train_data = data[:train_size]
    validation_data = data[train_size:train_size + test_size]
    test_data = data[train_size + test_size:]
    return train_data, validation_data, test_data

# Manual Feature Scaling Function
def standardize_data(X):
    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)
    return (X - mean) / std

# Loading and Preprocessing Data
#file_paths = ['../matlab scripts/V1.csv', '../matlab scripts/V2.csv', '../matlab scripts/V3.csv']
#file_paths = ['./iir1.csv', './iir2.csv', './iir3.csv']
file_paths = ['./iir1_selfNorm.csv', './iir2_selfNorm.csv', './iir3_selfNorm.csv']
#file_paths = ['./iir1_selfNorm_subset.csv', './iir2_selfNorm_subset.csv', './iir3_selfNorm_subset.csv']
data = []

for i, file_path in enumerate(file_paths):
    df = pd.read_csv(file_path, header=None).T
    df['label'] = i
    data.append(df)

data = pd.concat(data, ignore_index=True)
#np.random.shuffle(data.values)  # Shuffle the data
data = data.sample(frac=1).reset_index(drop=True)

# Splitting Data
train_data, validation_data, test_data = split_data(data, 0.7, 0.15)
X_train, y_train = train_data.drop('label', axis=1), train_data['label']
X_val, y_val = validation_data.drop('label', axis=1), validation_data['label']
X_test, y_test = test_data.drop('label', axis=1), test_data['label']

# Feature Scaling
X_train_scaled= standardize_data(X_train)
X_val_scaled= standardize_data(X_val)
X_test_scaled= standardize_data(X_test)
X_train_scaled= (X_train)
X_val_scaled= (X_val)
X_test_scaled= (X_test)
# Training Parameters
learning_rate = 0.01
iterations = 3000
num_classes = 3
lambda_reg = 0.1

# Training the Models
models_reg = train_one_vs_rest(X_train_scaled, y_train, num_classes, learning_rate, iterations, lambda_reg)

# Validation and Testing
y_val_pred_reg = predict(X_val_scaled, models_reg)
accuracy_val = np.mean(y_val_pred_reg == y_val)

y_test_pred = predict(X_test_scaled, models_reg)
accuracy_test = np.mean(y_test_pred == y_test)

# Print the accuracy results
print(f"Validation Accuracy: {accuracy_val}")
print(f"Test Accuracy: {accuracy_test}")

###################################################################################

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


# Example usage
file_path = "../IIR/wav1.wav"  # Replace with the path to your WAV file
audio_array, frame_rate = read_wav_file(file_path)
audio_array=audio_array[10000:16000]
f, t, Zxx = scipy.signal.stft(audio_array, 16000, nperseg=2048)

print(Zxx)
plt.pcolormesh(t, f, np.abs(Zxx), vmin=0,  shading='gouraud')
plt.title('STFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()
