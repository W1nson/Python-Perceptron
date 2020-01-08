import Point as pt
import Perceptron as p
import turtle as t

class runner:


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

    def paint(point):
        t.penup()
        t.setpos(point.x, point.y)
        t.pendown()
        t.dot(10)
        
def main():
    r = runner
    r.setcanvas()
    
    print(pt.getx(), pt.gety())
    r.paint(pt)


main()
    
        
