# Simple Keras Model Example from ML2

import sklearn.datasets as datasets
from keras.models import Sequential
from keras.layers import Dense
from keras.utils.np_utils import to_categorical

M = datasets.load_iris()['data']
L = to_categorical(datasets.load_iris()['target'])

n_cols = M.shape[1]
n_labels = L.shape[1]

model = Sequential()
model.add(Dense(25,input_dim=n_cols,activation='relu'))
model.add(Dense(n_labels,activation='softmax'))
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

model.fit(M,L,batch_size=10,epochs=25)