class Line ():
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        d = ((coordinate2[0]-coordinate1[0])**2 +
             (coordinate2[1]-coordinate1[1])**2)**0.5
        print("d is : ", d)

    def slope(self):
        m = (coordinate2[1]-coordinate1[1]) / (coordinate2[0]-coordinate1[0])
        print("m is : ", m)


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)

li.distance()

li.slope()
