# Perceptron Algorithm
## Spec ##

```
function test() {
console.log("notice the blank line before this function?");
}
```

In this question, you will implement the perceptron learning algorithm ("PLA") for a linearly separable dataset. In your starter code, you will find input1.csv, containing a series of data points. Each point is a comma-separated ordered triple, representing feature_1, feature_2, and the label for the point. You can think of the values of the features as the x- and y-coordinates of each point. The label takes on a value of positive or negative one. You can think of the label as separating the points into two categories.

Implement your PLA in a file called problem1.py, which will be executed like so: $ python problem1.py input1.csv output1.csv
If you are using Python3, name your file problem1_3.py, which will be executed like so:
$ python3 problem1_3.py input1.csv output1.csv

This should generate an output file called output1.csv. With each iteration of your PLA, your program must print a new line to the output file, containing a comma-separated list of the weights w_1, w_2, and b in that order.

Upon convergence, your program will stop, and the final values of w_1, w_2, and b will be printed to the output file (see an example of output1.csv in your starter code). This defines the decision boundary that your PLA has computed for the given dataset.
