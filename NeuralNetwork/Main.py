import random

import activation_relu


class Neuron:
    def __init__(self, input_count, activation_module):
        # generate random weights and bias
        self.weights = [random.uniform(-1, 1) for i in range(input_count)]
        self.bias = random.uniform(-1, 1)
        self.inputs = []
        self.output = 0.0
        self.activation = activation_module
        # backprop
        self.local_d_weights = []
        self.local_d_bias = 0.0
        self.local_d_inputs = []
        self.d_inputs = [] # for passing back to previous nodes

    def forwards(self, inputs):
        self.inputs = inputs
        self.output = 0.0
        for i in range(len(inputs)):
            self.output += self.weights[i] * inputs[i]
        self.output += self.bias
        self.output = self.activation.forwards(self.output)

        # prep for backprop
        self.local_d_bias = 1
        self.local_d_weights = self.inputs
        self.local_d_inputs = self.weights # sum when passed back
        self.d_activation = self.activation.derivative(self.output)

    def backwards(self, output_derivative, learning_rate):
        total_d_bias = self.local_d_bias * output_derivative
        total_d_weights = [w * output_derivative for w in self.local_d_weights]

        self.bias -= total_d_bias * learning_rate
        self.weights = [dw * learning_rate for dw in total_d_weights]


def calc_loss(results, targets):
    losses = []
    for i in range(len(results)):
        losses.append((targets[i] - results[i]) ** 2)
    return losses

X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [[0], [0], [0], [1]]
# neuron goal
# weights = [1, 1]
# bias = -1

neuron = Neuron(2, activation_relu)

for epoch in range(20):
    for i in range(4):
        neuron.forwards(X[i])
        print(X[i])
        print(y[i])
        print(neuron.output)
        # neuron.backwards(0.05, y[i][0] - neuron.output)
    print()

print()
print(neuron.weights)
print(neuron.bias)