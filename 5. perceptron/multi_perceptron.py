import numpy as np


class Perceptron:
    def __init__(self, d):
        self.weight = np.random.randn(1, d)[0]

    def h(self, x):
        return np.dot(self.weight.T, x)

    def optimize_weight(self, X_train, Y_train):
        A = np.dot(X_train.T, X_train)
        b = np.dot(X_train.T, Y_train)
        return np.dot(np.linalg.pinv(A), b).T[0]

    def getWeight(self):
        return self.weight

    def PrintPerceptron(self):
        print("\tNode: ", end=" ")
        print(self.weight)


class Layer:
    def __init__(self, N, d):
        self.numsOfPerceptron = N
        self.layer = []  # list of Perceptron
        self.layer_weight = d  # list of weigh of perceptron
        self.lable = None
        for i in range(N):
            perceptron = Perceptron(d)
            self.layer.append(perceptron)
        # lable = "input", "hiden" or "output"

    def setAsInputLayer(self):
        self.lable = "input"

    def setAsHidenLayer(self):
        self.lable = "hiden"

    def setAsOutputLayer(self):
        self.lable = "output"

    def getPerceptron(self, index):
        return self.layer[index]

    def addPerceptron(self, perceptron):
        self.layer.append(perceptron)

    def PrintLayer(self):
        for i in range(self.numsOfPerceptron):
            self.layer[i].PrintPerceptron()

    def getLayer(self):
        return self.layer

    def getPerceptron(self, index):
        return self.layer[index]


class Network:
    def __init__(self, list_of_Layer, d):
        self.numsLayer = len(list_of_Layer)
        self.network = []  # list of layer
        for nums_of_Perceptron in list_of_Layer:
            layer = Layer(nums_of_Perceptron, d)
            layer.setAsHidenLayer()
            self.network.append(layer)
            d = nums_of_Perceptron
        self.network[0].setAsInputLayer()
        self.network[0].setAsOutputLayer()
        self.output = []

    def getNetwork(self):
        return self.network

    def PrintNetwork(self):
        for i in range(self.numsLayer):
            print("Layer " + str(i) + ":")
            self.network[i].PrintLayer()
            print(" ")

    def getOutput(self, X=None):
        output = []
        for i in X:
            layer_input = i.copy()
            for layer in self.network:
                layer_output = []
                for perceptron in layer.getLayer():
                    layer_output.append(perceptron.h(layer_input))
                layer_input = np.array(layer_output)
            output.append(layer_output)
        self.output = np.array(output)
        return self.output

    def training(self, X_train, Y_actual):
        pass


if __name__ == "__main__":
    print("Multi Perceptron Network: ")
    X_train = np.array([[2, 1], [4, 8], [9, 6], [4, 11]])
    network = Network([4, 1, 3, 5, 1, 6, 1], X_train.shape[1])
    network.PrintNetwork()
    print("input:  ")
    print(X_train)
    print("output: ")
    print(network.getOutput(X_train))
