import random
import numpy as np
import matplotlib.pyplot as plt
import math


def h(w, x):
    z = np.dot(w.T, x)
    return 1 if z > 0 else -1


def check(X_train, Y_train, w):
    Y_result = []
    for x in X_train:
        Y_result.append([h(w, x)])
    Y_result = np.array(Y_result)
    re = True if np.array_equal(Y_result, Y_train) else False
    return re


def perception(X_train, Y_train):
    collum = X_train.shape[1]
    row = X_train.shape[0]
    w_init = np.random.randn(1, collum)
    w = [w_init[0]]
    while True:
        mix_id = np.random.permutation(row)
        for i in range(row):
            xi = X_train[mix_id[i], :]
            yi = Y_train[mix_id[i], 0]
            if (h(w[-1], xi) != yi):
                w_new = w[-1] + yi*xi
                w.append(w_new)
        if check(X_train, Y_train, w[-1]):
            break
    return w[-1]


if __name__ == "__main__":
    print("Wait for a minute ...")
    N = 70
    X = []
    Y = []
    a = random.randint(-19, 20)
    while a == 0:
        a = random.randint(-19, 20)
    b = random.randint(-19, 20)
    while b == 0:
        b = random.randint(-19, 20)
    for i in range(N):
        x = random.randint(-19, 20)
        y = random.randint(-19, 20)
        X.append([x, y])
        t = h(np.array([a, b]), np.array([x, y]))
        Y.append([t])
        if (t > 0):
            plt.scatter(np.array([x]), np.array([y]), marker='o', color='red')
        else:
            plt.scatter(np.array([x]), np.array([y]), marker='^', color='blue')

    X_train = np.array(X)
    Y_train = np.array(Y)
    print(np.concatenate((X_train, Y_train), axis=1))
    w = perception(X_train=X_train, Y_train=Y_train)
    print(w)
    print(np.array([a, b]))
    z = np.array([-19, 19])
    plt.plot(z, -a/b*z)
    plt.plot(z, -w[0]/w[1]*z)
    plt.show()
