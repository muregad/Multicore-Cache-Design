import numpy as np
from numpy import argmax
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras import optimizers
# from sklearn.neural_network import MLPClassifier

# define example
class Neuralnet:
    def __init__(self, X_train, y_train):
        # X_train = [[1, 3, 2, 0, 3, 2], [2, 1, 3, 0, 3, 2], [1, 1, 3, 0, 5, 1], [2, 1, 3, 0, 3, 2]]
        # X_train = np.array(X_train)
        # y_train = [[1, 3, 2, 0], [0, 1, 2, 3], [1, 3, 2, 0]]
        # y_train = np.array(y_train)
        # print(y_train)
        # one hot encode
        encoded = np.array(np.append(to_categorical(X_train[0][0:4], num_classes=4), [X_train[0][4], X_train[0][5]]),
                           dtype=object).reshape(1, 18)

        for i in range(X_train.shape[0] - 1):
            encoded = np.append(encoded, np.append(to_categorical(X_train[i + 1][0:4], num_classes=4),
                                                   [X_train[i + 1][4], X_train[i + 1][5]]).reshape(1, 18), axis=0)

        # print(encoded)
        # print(encoded.shape)
        X_train = np.asarray(encoded).astype(np.float32)
        encoded = np.array(to_categorical(y_train[0], num_classes=4)).reshape(1, 16)
        # print(encoded)
        # print(encoded.shape)
        # print(X_train)

        for i in range(y_train.shape[0] - 1):
            encoded = np.append(encoded, to_categorical(y_train[i + 1], num_classes=4).reshape(1, 16), axis=0)

        y_train = np.asarray(encoded).astype(np.float32)
        print(y_train)
        print(y_train[0])

        self.model = Sequential()
        self.model.add(Dense(100, activation='relu', input_dim=X_train.shape[1]))
        self.model.add(Dropout(0.1))
        self.model.add(Dense(150, activation='relu'))
        self.model.add(Dropout(0.1))
        self.model.add(Dense(90, activation='relu'))
        self.model.add(Dropout(0.1))
        self.model.add(Dense(y_train.shape[1], activation="sigmoid"))
        optimizer = optimizers.Adam(lr=0.001)
        self.model.compile(loss="binary_crossentropy", optimizer=optimizer, metrics=["accuracy"])
        #
        self.model.fit(X_train, y_train, epochs=1000, validation_split=0.2, verbose=1)
        print("here i am")

    def pred(self, x):
        x = np.array(np.append(to_categorical(x[0:4], num_classes=4), [x[4], x[5]]),
                     dtype=object).reshape(1, 18)
        x = np.asarray(x).astype(np.float32)
        # print("x hot encoded :"+ str(x))
        y = self.model.predict(x)
        # print("y hot encoded :"+ str(y))
        y_inv = np.array([argmax(y[0][0:4]), argmax(y[0][4:8]),argmax(y[0][8:12]),argmax(y[0][12:16])]).reshape(1,4)
        for i in range(y.shape[0]-1):
            y_inv= np.append(y_inv, np.array([argmax(y[i+1][0:4]),argmax(y[i+1][4:8]),argmax(y[i+1][8:12]),argmax(y[i+1][12:16])]).reshape(1,4),axis=0)
        return y_inv

        # print(y_inv)
    # model.predict(X)
    # print(encoded)
    # # invert encoding
    # inverted = argmax(encoded[0])
    # print(inverted)
