import numpy as np


def activation(x):
    return 1 / (1 + np.exp(-x))


def naive_forward_net(n_layers, x, w, b):
    for l in range(n_layers - 1):
        print("layer now is ", l)
        if l == 0:
            node_in = x
            print("input layer")
        else:
            node_in = h

        h = np.zeros((w[l].shape[0],))
        for i in range(w[l].shape[0]):
            f_sum = 0
            for j in range(w[l].shape[1]):
                f_sum += w[l][i][j] * node_in[j]
            f_sum += b[l][i]
            h[i] = activation(f_sum)
    print(h)
    return h


w1 = np.array([[0.2, 0.2, 0.2], [0.4, 0.4, 0.4], [0.6, 0.6, 0.6]])
w2 = np.zeros((1, 3))
w2[0, :] = np.array([0.5, 0.5, 0.5])

b1 = np.array([0.8, 0.8, 0.8])
b2 = np.array([0.2])

w = [w1, w2]
b = [b1, b2]
x = [1.5, 2.0, 3.0]
naive_forward_net(3, x, w, b)
