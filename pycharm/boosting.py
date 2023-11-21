import numpy as np
import pandas as pd

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
file_paths = ['../IIR/iir1.csv', '../IIR/iir2.csv', '../IIR/iir3.csv']
#file_paths = ['./wav1.csv', './wav2.csv', './wav3.csv']
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

# Training Parameters
learning_rate = 0.01
iterations = 3000
num_classes = 3
lambda_reg = 2097152
ind=1
while lambda_reg>0.01:
    # Training the Models
    models_reg = train_one_vs_rest(X_train_scaled, y_train, num_classes, learning_rate, iterations, lambda_reg)

    # Validation and Testing
    y_val_pred_reg = predict(X_val_scaled, models_reg)
    accuracy_val = np.mean(y_val_pred_reg == y_val)

    y_test_pred = predict(X_test_scaled, models_reg)
    accuracy_test = np.mean(y_test_pred == y_test)

    # Print the accuracy results
    print(f"Lamba:{lambda_reg}, Validation Accuracy: {accuracy_val}, Test Accuracy:{accuracy_test}")
    dataframe = pd.DataFrame.from_records(models_reg)
    dataframe.to_csv("./boost_%d.csv"%ind, header=False, index=False)
    lambda_reg/=2;
    ind+=1;

