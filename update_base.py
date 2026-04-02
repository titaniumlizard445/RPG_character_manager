
import utill_functions
import pandas
import faker

import math
import random
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
class data_visualisation:
    def __init__(self):
        self.figuer,self.axis=plt.subplots()
    def radar_graph(self,catigorys,vals,lables,radius,definition):
        shape=RegularPolygon((0,0),numVertices=len(catigorys),radius=radius,facecolor="none",edgecolor="black",linewidth=1)
        self.axis.add_patch(shape)
        angles=360/len(catigorys)
        for x in range(len(catigorys)):
            target=[radius*math.cos(math.radians(angles*x)),(radius*math.sin(math.radians(angles*x)))]
            plt.plot([0,0],[target[0],target[1]])
        for x in range(definition):
            shape=RegularPolygon((0,0),numVertices=len(catigorys),radius=x*(radius/definition),facecolor="none",edgecolor="black",linewidth=.5)
            self.axis.add_patch(shape)
        self.axis.set_xlim(-10, 10)
        self.axis.set_ylim(-10, 10)
        self.axis.set_aspect('equal') # Keeps it from being squashed
        self.axis.axis("off")
        plt.show()
            
test=data_visualisation()
test.radar_graph(["bob","turtle","jeff","liam","dog"],[1,8,4,7,2],[7,3,7,2,2],10,5)