import random as r

class perceptron:
    w = [0]*2
    def __init__():
        for i in range(len(w)):
            w[i] = r.random()

    #actuation function that process the sum and return either 1 or -1
    def actuation_func(n):
        if n >= 0: 
            return 1
        elif n < 0:
            return -1
    def guess(data):
        total = 0
        for i in range(len(w)):
            total += data[i]*weighs[i]
        output = actualtion_func(total)


    def train(data, point, target):
        
        i = 0
        flag = False
        while not flag:
            while i < len(w):
                error = target - data
                print(error)
                for i in range(len(w)):
                    w[i] += error * point[i] * lr

                
            
