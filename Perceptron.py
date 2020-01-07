import decimal as d
import random as r
import turtle as t

#supervised learning
#We know the answer

lr = 0.1



w = [r.random(), r.random()]

#actuation function that process the sum and return either 1 or -1
def actuation_func(n):
    if n >= 0: 
        return 1
    elif n < 0:
        return -1
    
#calculate the sum of input*wieghts 
def total(a, b):
    return a[0]*b[0] + a[1]*b[1]


def train(data, point, target):    
        error = target - data
        print(error)
        #tune all the weights
        for i in range(len(w)):
            w[i] += error * point[i] * lr
       

def paint(i):
    t.penup()
    t.setpos(i)
    t.pendown()
    t.dot(10)

def setcanvas():
    t.setup(width = 500, height = 500, startx = 0, starty = 0)
    t.ht()
    t.pu()
    t.setpos(-250,-250)
    t.pd()
    t.pencolor("red")
    t.setpos(250,250)
    t.pu()
    t.setpos(-250,0)
    t.pd()
    t.setpos(250,0)
    t.pu()
    t.setpos(0,250)
    t.pd()
    t.setpos(0,-250)

def main():

    row = 20
    
    

    setcanvas()

    

    rand = [[float(r.randrange(-250, 250)) for i in range(2)] for j in range(row)]
    '''rand = [[-240.0, 52.0],
            [-196.0, 206.0],
            [-31.0, -99.0],
            [-211.0, 203.0],
            [-173.0, 91.0]]'''


    
    
    target = [0]*row
    for i in range(row):
        if rand[i][0] > rand[i][1]:
            target[i] = 1
        else:
            target[i] = -1
    
    
    to = [0]*row
    t.pencolor("black")
    for i in rand:
        print(i)
        paint(i)
        
    for i in range(row):
        to[i] = actuation_func(total(rand[i],w))

    print(to)

    print(w)
    i = 0
    flag = False
    while not flag:
        while i < row:
            print("This is index:", i)
            train(to[i], rand[i], target[i])
            #print('before:', to[i], '--', target[i])
            to[i] = actuation_func(total(rand[i],w))
            #print('after:', to[i], '--', target[i])
            if to[i] != target[i]:
                t.pencolor("red")
                paint(rand[i])
                #print(i, "Wrong!")
                flag = False
                i = 0
            else:
                t.pencolor("green")
                paint(rand[i])
                #print(i, "resolve")
                i+=1
        i = 0
        while i < row:
            to[i] = actuation_func(total(rand[i],w))
            if to[i] != target[i]:
                i = 0
                print("not pass second test")
                break
            else:
                i+=1
                flag = True
                
        
            
    print(w)
    print(target)
    print(to)
    print()
    print("Check")
    for i in range(row):
        to[i] = actuation_func(total(rand[i],w))
        if to[i] != target[i]:
            print("index:", i, "wrong")

    print()
    print(w)
    print(target)
    print(to)
    
    
    

main()



    
