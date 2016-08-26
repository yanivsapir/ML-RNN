# Machine Learning Final Project 

##Submittors
Yaniv Sapir

Tamir Amid

##Project Description
This project is about experiencing with long short-term memory (LSTM) algorithm which is a recurrent neural network (RNN) algorithm.

##References
* [RNN Tutorial](http://www.wildml.com/2015/09/recurrent-neural-networks-tutorial-part-1-introduction-to-rnns/)
* [RNN toy example](https://www.youtube.com/watch?v=z61VFeALk3o)
* We followed [this article](http://machinelearningmastery.com/text-generation-lstm-recurrent-neural-networks-python-keras/) which was very intuitive.

##Main Packages
In this project we used:
* [Keras](https://keras.io/)
* [Theano BE]
* [Numpy](http://www.numpy.org)
* [Anaconda2](https://www.continuum.io/downloads) package.

##Project Flow
Downloaded partiall text of the Dracula book
* Read text from file & prepared data set 
* First we created a small LSTM - RNN
* Trained the machine model with our  data set
* Generated new senetences
* Calculated the Diffs between new sentences which generated and the real ones

##Model Training Time
3 days for each run.

##Diff Calculation
We decided to use the `Minhash` algorythm beause it's quickly estimating how similar two sets are, and coding that was pretty simple.

##Code
Our code End-To-End is the file `RunCode.py`

##Result
Because of the lack of time we ran the code only twice and we think we got an interesting results:

![accuracy](https://github.com/yanivsapir/ML-RNN/blob/master/accuracy.png)
