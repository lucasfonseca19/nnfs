import numpy as np
import nnfs
from nnfs.datasets import spiral_data
nnfs.init()

## Criar mais pra frente um módulo para cada classe

# Dense Layer
class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        # Initialize weight and biases
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def foward(self, inputs):
        # Calculate output values from inputs, weights and biases
        self.output = np.dot(inputs, self.weights) + self.biases
# Relu activation
class Activation_ReLU:
    def foward(self,inputs):
        self.output = np.maximum(0,inputs)

# Create dataset
x,y = spiral_data(samples=100, classes=3)

# Create Dense Layer with 2 input features and 3 output values
dense1 = Layer_Dense(2,3)

#Create ReLU activation (to be used with Dense Layer)
activation1 = Activation_ReLU()

# Perform foward pass of our training data through this layeer
dense1.foward(x)

# Foward pass throught the activation function
# Takes in outputs from previous Layer
activation1.foward(dense1.output)

# Let's see the output of the first few samples
print(activation1.output[:5])
