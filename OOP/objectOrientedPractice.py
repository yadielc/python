import numpy as np
import car

'''
objectOrientedPractice.property

This is a review of object oriented programming in Python. It creates a car object, importing
the information of the object from a file class called Car. 

'''

%matplotlib inline

%load_ext autoreload
%autoreload 2


height = 4
width = 6
world = np.zeros((height, width))

# Define the initial car state
initial_position = [0, 0] # [y, x] (top-left corner)
velocity = [0, 1] # [vy, vx] (moving to the right)


carla = car.Car(initial_position, velocity, world)
carla.display_world()
