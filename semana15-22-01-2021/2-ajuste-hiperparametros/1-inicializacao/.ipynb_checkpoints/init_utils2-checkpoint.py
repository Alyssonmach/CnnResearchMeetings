import numpy as np
import matplotlib.pyplot as plt
import h5py
import sklearn
import sklearn.datasets

def sigmoid(x):
    '''Compute the sigmoid of x'''
    
    s = 1 / (1 + np.exp(-x))
    
    return s

def relu(x):
    '''Compute the relu of x'''
    
    s = np.maximum(0, x)
    
    return s

def forward_propagation(X, parameters):
    '''Implements the forward propagation (and compute the loss)'''
    
     # retrieve parameters
    W1 = parameters["W1"]
    b1 = parameters["b1"]
    W2 = parameters["W2"]
    b2 = parameters["b2"]
    W3 = parameters["W3"]
    b3 = parameters["b3"]
    
    # LINEAR -> RELU -> LINEAR -> RELU -> LINEAR -> SIGMOID
    z1 = np.dot(W1, X) + b1
    a1 = relu(z1)
    z2 = np.dot(W2, a1) + b2
    a2 = relu(z2)
    z3 = np.dot(W3, a2) + b3
    a3 = sigmoid(z3)
    
    cache = (z1, a1, W1, b1, z2, a2, W2, b2, z3, a3, W3, b3)
    
    return a3, cache

def backward_propagation(X, Y, cache):
    '''Implement the backward propagation'''
    
    m = X.shape[1]
    (z1, a1, W1, b1, z2, a2, W2, b2, z3, a3, W3, b3) = cache
    
    dz3 = 1./m * (a3 - Y)
    dW3 = np.dot(dz3, a2.T)
    db3 = np.sum(dz3, axis=1, keepdims = True)
    
    da2 = np.dot(W3.T, dz3)
    dz2 = np.multiply(da2, np.int64(a2 > 0))
    dW2 = np.dot(dz2, a1.T)
    db2 = np.sum(dz2, axis=1, keepdims = True)
    
    da1 = np.dot(W2.T, dz2)
    dz1 = np.multiply(da1, np.int64(a1 > 0))
    dW1 = np.dot(dz1, X.T)
    db1 = np.sum(dz1, axis=1, keepdims = True)
    
    gradients = {'dz3': dz3, 'dW3': dW3, 'db3': db3,
                 "da2": da2, "dz2": dz2, "dW2": dW2, "db2": db2,
                 "da1": da1, "dz1": dz1, "dW1": dW1, "db1": db1}
    
    return gradients

def update_parameters(parameters, grads, learning_rate):
    '''update parameters using gradient descent'''
    
    L = len(parameters) // 2 # number of layers in the neural networks
    
    # update rule for each parameter
    for k in range(L):
        
        parameters['W' + str(k + 1)] = parameters['W' + str(k + 1)] - learning_rate * grads['dW' + str(k + 1)]
        parameters['b' + str(k + 1)] = parameters['b' + str(k + 1)] - learning_rate * grads['db' + str(k + 1)]
        
    return parameters

def compute_loss(a3, Y):
    '''Implement the loss function'''
    
    m = Y.shape[1]
    logprobs = np.multiply(-np.log(a3), Y) + np.multiply(-np.log(1 - a3), 1 - Y)
    loss = 1./m * np.nansum(logprobs)
    
    return loss

def load_cat_dataset():
    '''Load the cat dataset'''
    
    train_dataset = h5py.File('datasets/train_catvnoncat.h5', 'r')
    train_set_x_orig = np.array(train_dataset['train_set_x'][:]) # your train set features
    train_set_y_orig = np.array(train_dataset['train_set_y'][:]) # your train set labels
    
    test_dataset = h5py.File('datasets/test_catvnoncat.h5', 'r')
    test_set_x_orig = np.array(test_dataset['test_set_x'][:]) # your test set features
    test_set_y_orig = np.array(test_dataset['test_set_y'][:]) # your test set lables
    
    classes = np.array(test_dataset['list_classes'][:]) # the list of classes
    
    train_set_y = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    test_set_y = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))
    
    train_set_x_orig = train_set_x_orig.reshape(train_set_x_orig.shape[0], -1).T
    test_set_x_orig = test_set_x_orig.reshape(test_set_x_orig.shape[0], -1).T
    
    train_set_x = train_set_x_orig / 255
    test_set_x = test_set_x_orig / 255
    
    return train_set_x, train_set_y, test_set_x, test_set_y, classes

def predict(X, y, parameters):
    '''This function is used to predict the results of a n-layer neural network'''
    
    m = X.shape[1]
    p = np.zeros((1, m), dtype = np.int)
    
    # forward propagation
    a3, caches = forward_propagation(X, parameters)
    
    # convert probas to 0/1 predictions
    for i in range(0, a3.shape[1]):
        if a3[0,i] > 0.5:
            p[0,i] = 1
        else:
            p[0,i] = 0
            
    # print results
    print('Accuracy:' + str(np.mean((p[0,:] == y[0, :]))))
        
    return p

def plot_decision_boundary(model, X, y):
    '''Plot decision boundary'''
    
    # set min and max values and give it some padding
    x_min, x_max = X[0, :].min() - 1, X[0, :].max() + 1
    y_min, y_max = X[1, :].min() - 1, X[1, :].max() + 1
    h = 0.01
    
    # generate a grid of points with distance h between them
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    
    # predict the function value for the whole grid
    Z = model(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    # plot the contour and training examples
    plt.contourf(xx, yy, Z, cmap = plt.cm.Spectral)
    plt.ylabel('x2')
    plt.xlabel('x1')
    plt.scatter(X[0, :], X[1, :], c =y, cmap = plt.cm.Spectral)
    plt.show()
    
    return None

def predict_dec(parameters, X):
    '''Used for plotting decision boundary'''
    
    # predict using forward propagation and a classification threshold of 0.5
    a3, cache = forward_propagation(X, parameters)
    predictions = (a3 > 0.5)
    
    return predictions

def load_dataset():
    '''Load the dataset'''
    
    np.random.seed(1)
    
    train_X, train_Y = sklearn.datasets.make_circles(n_samples = 300, noise = .05)
    test_X, test_Y = sklearn.datasets.make_circles(n_samples = 100, noise = .05)
    
    # visualize the data
    plt.scatter(train_X[:, 0], train_X[:, 1], c = train_Y, s = 40, cmap = plt.cm.Spectral)
    
    train_X = train_X.T
    test_X = test_X.T
    train_Y = train_Y.reshape((1, train_Y.shape[0]))
    test_Y = test_Y.reshape((1, test_Y.shape[0]))
    
    return train_X, train_Y, test_X, test_Y


    
    

    
    