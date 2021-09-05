import numpy as np

class NeuralNetwork:
    def __init__(self):
        self.synaptic_weights = np.random.randn(3, 1)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return self.sigmoid(x) * (1 - self.sigmoid(x))

    def ReLU(self, x):
        return np.maximum(0, x)

    def train(self, training_inputs, training_outputs, iterations):
        for i in range(iterations):
            outputs = self.sigmoid(np.dot(training_inputs, self.synaptic_weights))
            error = training_outputs - outputs
            adjustments = error * self.sigmoid_derivative(outputs)
            self.synaptic_weights += np.dot(training_inputs.T, adjustments)
        return outputs

    def user_data(self, inputs):
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))
        return output

if __name__ == "__main__":
    training_inputs = np.array([[0, 0, 1],
                                [1, 1, 0],
                                [0, 1, 1],
                                [1, 0, 1]])

    training_outputs = np.array([[0],
                                 [1],
                                 [0],
                                 [1]])

    network = NeuralNetwork()
    output = network.train(training_inputs, training_outputs, 10000)

    print(f"Weights: \n{network.synaptic_weights}")

    x = int(input("Enter Number 1: "))
    y = int(input("Enter Number 2: "))
    z = int(input("Enter Number 3: "))

    numbers = np.array([x, y, z])

    print(round(network.user_data(numbers)[0], 1))
