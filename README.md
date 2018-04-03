# Perceptron Algorithm
## Spec ##

This is to implement the perceptron learning algorithm ("PLA") for a linearly separable dataset. The input1.csv contains a series of data points. Each point is a comma-separated ordered triple, representing feature_1, feature_2, and the label for the point. You can think of the values of the features as the x- and y-coordinates of each point. The label takes on a value of positive or negative one. You can think of the label as separating the points into two categories.

The PLA is implemented in a file called problem1.py, which will be executed like so:
```$ python problem1.py input1.csv output1.csv```

This should generate an output file called output1.csv. With each iteration of the PLA, the program will print a new line to the output file, containing a comma-separated list of the weights w_1, w_2, and b in that order.

Upon convergence, the program will stop, and the final values of w_1, w_2, and b will be printed to the output file. This defines the decision boundary that the PLA has computed for the given dataset.
