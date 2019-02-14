import keras
from keras.layers import Input, Conv2D, Lambda, merge, Dense, Flatten, MaxPooling2D, Dropout
from keras.models import Model, Sequential
from keras.regularizers import l2
from keras import backend as K
from keras.optimizers import SGD, Adam
import numpy.random as rng
import numpy as np
import os

import siamese_preprocess


def W_init(shape, name=None):
    """Initialize weights as in paper"""
    values = rng.normal(loc=0, scale=1e-2, size=shape)
    return K.variable(values, name=name)


# //TODO: figure out how to initialize layer biases in keras.
def b_init(shape, name=None):
    """Initialize bias as in paper"""
    values = rng.normal(loc=0.5, scale=1e-2, size=shape)
    return K.variable(values, name=name)


def test_oneshot(model, k, verbose=0):
    """Test average N way oneshot learning accuracy of a siamese neural net over k one-shot tasks"""
    n_correct = 0
    for i in range(k):
        inputs, targets = siamese_preprocess.get_eval_batch()
        probs = model.predict(inputs)
        prob_max = np.argmax(probs)
        if targets[prob_max] == 1:
            n_correct += 1
    percent_correct = (100.0 * n_correct / k)
    if verbose:
        print("Got an average of {}% one-shot learning accuracy".format(percent_correct))
    return percent_correct


print('model build')
input_shape = (128, 128, 3)
left_input = Input(input_shape)
right_input = Input(input_shape)

convnet = Sequential()
convnet.add(Conv2D(64, (10, 10), activation='relu', input_shape=input_shape))
convnet.add(MaxPooling2D())
convnet.add(Conv2D(128, (7, 7), activation='relu'))
convnet.add(MaxPooling2D())
convnet.add(Conv2D(128, (4, 4), activation='relu'))
convnet.add(MaxPooling2D())
convnet.add(Conv2D(256, (4, 4), activation='relu'))
# convnet.add(Dropout(0.25))
convnet.add(Flatten())
convnet.add(Dense(2048, activation='sigmoid'))

encoded_l = convnet(left_input)
encoded_r = convnet(right_input)

L1_layer = Lambda(lambda tensors: K.abs(tensors[0] - tensors[1]))
L1_distance = L1_layer([encoded_l, encoded_r])
prediction = Dense(1, activation='sigmoid')(L1_distance)
siamese_net = Model(inputs=[left_input, right_input], outputs=prediction)

# //TODO: get layerwise learning rates and momentum annealing scheme described in paperworking
siamese_net.compile(loss="binary_crossentropy", optimizer=keras.optimizers.Adadelta())
print(siamese_net.count_params())
print('train')

PATH = ''
evaluate_every = 100
loss_every = 100
batch_size = 32
n_iter = 9000
N_way = 20  # how many classes for testing one-shot tasks>
n_val = 100  # how mahy one-shot tasks to validate on?
best = -1
weights_path = os.path.join(PATH, "weights")
print("training")
for i in range(1, n_iter):
    (inputs, targets) = siamese_preprocess.get_batch()
    loss = siamese_net.train_on_batch(inputs, targets)
    # print(loss)
    if i % loss_every == 0:
        print("iteration {}, training loss: {:.5f},".format(i, loss))
    if i % evaluate_every == 0:
        print("evaluating")
        val_acc = test_oneshot(siamese_net, n_val, verbose=True)
        # if val_acc >= best:
        #     print("saving")
        #     siamese_net.save(weights_path)
        #     best = val_acc
