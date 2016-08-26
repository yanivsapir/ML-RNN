import sys
import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import np_utils

filename = "dracula.txt"
file_text = open(filename).read()
file_text = file_text.lower()
charArray = sorted(list(set(file_text)))
char_to_int = dict((c, i) for i, c in enumerate(charArray))
int_to_char = dict((i, c) for i, c in enumerate(charArray))
charArrayLength = len(file_text)
vocabularyLength = len(charArray)
print "Total Characters: ", charArrayLength
print "Total Vocab: ", vocabularyLength
seq_length = 100
dataX = []
dataY = []
for i in range(0, charArrayLength - seq_length, 1):
	seq_in = file_text[i:i + seq_length]
	seq_out = file_text[i + seq_length]
	dataX.append([char_to_int[char] for char in seq_in])
	dataY.append(char_to_int[seq_out])
patternsLength = len(dataX)
print "Total Patterns: ", patternsLength
X = numpy.reshape(dataX, (patternsLength, seq_length, 1))
X = X / float(vocabularyLength)
y = np_utils.to_categorical(dataY)
model = Sequential()
model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2]), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(256))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))
filename = "weights-improvement-47-1.2219-bigger.hdf5"
model.load_weights(filename)
model.compile(loss='categorical_crossentropy', optimizer='adam')
start = numpy.random.randint(0, len(dataX)-1)
pattern = dataX[start]
print "Seed:"
print "\"", ''.join([int_to_char[value] for value in pattern]), "\""
for i in range(1000):
	x = numpy.reshape(pattern, (1, len(pattern), 1))
	x = x / float(vocabularyLength)
	prediction = model.predict(x, verbose=0)
	index = numpy.argmax(prediction)
	result = int_to_char[index]
	seq_in = [int_to_char[value] for value in pattern]
	sys.stdout.write(result)
	pattern.append(index)
	pattern = pattern[1:len(pattern)]
print "\nDone."