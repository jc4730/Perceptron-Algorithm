# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 15:54:41 2017

@author: jc9730; Jiada Chen; HW3_q1
"""

import sys
import csv
import numpy as np
import matplotlib.pyplot as plt

def main():
    inp_path = sys.argv[1]
    out_path = sys.argv[2]
    data = []
    labels= []
    
    # read data
    with open(inp_path,"r") as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            data.append(row[0:2])
            labels.append(row[2])
    
    data = np.array(data, dtype = float)
    labels = np.array(labels, dtype = float)

    # initialize param
    w = np.zeros(data.shape[1])
    b = 0
    
    w_prev = np.ones(data.shape[1])
    
    output = []

    # train
    while np.any(w_prev != w):
        w_prev = w
        for i in range(len(labels)):
            x = data[i]
            y = labels[i]
            if y * (np.dot(w,x) + b) <= 0:
                w = w + y * x
                b = b + y
        output_row = list(w)
        output_row.append(b)
        output.append(output_row)
        
    with open(out_path,'w') as f:
        writer = csv.writer(f,delimiter = ',')
        writer.writerows(output)
    
if __name__ == "__main__":
    main()
