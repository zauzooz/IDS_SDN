import numpy as np


class Perceptron:
    def __init__(self, d):
        self.weight = np.random.randn(1, d)[0]

    def h(self, x):
        return np.dot(self.weight.T, x)

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

    def h(self, X):
        pass


class Network:
    def __init__(self, list_of_Layer, X):
        self.numsLayer = len(list_of_Layer)
        self.network = []  # list of layer
        d = X.shape[1]
        for nums_of_Perceptron in list_of_Layer:
            layer = Layer(nums_of_Perceptron, d)
            layer.setAsHidenLayer()
            self.network.append(layer)
            d = nums_of_Perceptron
        self.network[0].setAsInputLayer()
        self.network[0].setAsOutputLayer()
        self.input = X
        self.output = []

    def PrintNetwork(self):
        for i in range(self.numsLayer):
            print("Layer " + str(i) + ":")
            self.network[i].PrintLayer()
            print(" ")

    def getOutput(self):
        output = []
        for i in self.input:
            layer_input = i.copy()
            for layer in self.network:
                layer_output = []
                for perceptron in layer.getLayer():
                    layer_output.append(perceptron.h(layer_input))
                layer_input = np.array(layer_output)
            output.append(layer_output)
        self.output = np.array(output)
        return self.output


if __name__ == "__main__":
    print("Multi Perceptron Network: ")
    X_train = np.array([[2, 1], [4, 8]])
    network = Network([4, 1, 3, 5], X_train)
    network.PrintNetwork()
    print("input:  ")
    print(X_train)
    print("output: ")
    print(network.getOutput())
