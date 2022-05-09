
#!/usr/bin/env python

class Network:
    # https://towardsdatascience.com/understanding-backpropagation-algorithm-7bb3aa2f95fd
    def __init__(self, inputs, outputs, hidden_count, hidden_size):
        self.layers = []
        self.layers.append([0] * inputs)
        for i in range(hidden_count):
            self.layers.append([0] * hidden_size)
        self.layers.append([0] * outputs)

        self.weights = []
        for i in range(hidden_count + 1):
            weights.append(len(self.layers[i]) * [len(self.layers[i+1] * [0])])
