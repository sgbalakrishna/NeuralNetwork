import numpy as np


def activation(x):
    return 1 / (1 + np.exp(-x))


def matrix_forward_net(n_layers, x, w):
    b = [np.random.rand(3 - 2, 3), np.random.rand(1, 1)]

    for l in range(n_layers - 1):
        print("layer now is ", l)
        if l == 0:
            node_in = x
            print("input layer")
        else:
            node_in = h

        z = w[l].dot(node_in) + b[l]
        h = activation(z)
    print(h)
    return h


####
x = np.array([1.5, 2.0])


def matrix_forward_deep_net(n_hidden_layers, x):
    w_hidden = np.random.rand(n_hidden_layers, x.shape[0], x.shape[0])
    w_final = np.random.rand(1, x.shape[0])
    w = [w_hidden, w_final]
    b = [np.random.rand(n_hidden_layers, x.shape[0]), np.random.rand(1, 1)]

    for l in range(n_hidden_layers):
        print("layer now is ", l)
        if l == 0:
            node_in = x
            print("input layer")
        else:
            node_in = h

        z = w[0][l].dot(node_in) + b[l]
        h = activation(z)
    print(h)
    return h


matrix_forward_deep_net(3, x)

####

w1 = np.random.rand(3, 3)
w2 = np.zeros((1, 3))
w2[0, :] = np.array([0.5, 0.5, 0.5])

b1 = np.array([0.8, 0.8, 0.8])
b2 = np.array([0.2])

w = [w1, w2]
b = [b1, b2]
x = np.array([1.5, 2.0, 3.0])

matrix_forward_net(3, x, w)
