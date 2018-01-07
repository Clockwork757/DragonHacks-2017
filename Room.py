#========================================
#Project Name: Room Type/Size
#Date:	04/15/2017
#Programmer Name: Matthew Marschall 
#Modified: 01/06/2018
#Modifier: Dresden Feitzinger
#========================================

import numpy as np

class Point:
    ''' Return a cartesian coordinate point '''
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        ''' Return a string representation of the
            coordinate point '''
        return "({0}, {1})".format(self.x, self.y)

    def get_x(self):
        ''' Return the x coordinate '''
        return self.x

    def get_y(self):
        ''' Return the y coordinate '''
        return self.y 

class Room():
    ''' Superclass for room types '''
    def __init__(self, t, name="Room"):
        #--- Public -----------
        self.type = t    # type of room
        self.name = name # name of room
        self.area = None # area of room
        #----------------------

    def get_area(self):
        ''' Return area of the room '''
        return self.area

    def set_area(self, area):
        ''' Set room area '''
        self.area = area

class Circle(Room):
    ''' Create a room of type circle '''
    def __init__(self, r):
        ''' Takes one positional argument: radius '''
        #--- Initialize Superclass -------
        t = 0
        Room.__init__(t)
        self.set_area(4*np.pi*(r**2))

        #--- Public ----------------------
        self.diameter = r*2
        self.radius   = r
        #---------------------------------

    def get_radius(self):
        ''' Return radius of the circle in centimeters '''
        return self.radius

    def calc_circumference(self):
        ''' Calculate the circumference of the room '''
        return 2 * np.pi * self.radius
		
class Rectangle(Room):
    ''' Create a room of type rectangle '''
    def __init__(self, w, l):
        #--- Initialize Superclass -------
        t = 1
        Room.__init__(t)
        self.set_area(w*l)
        #---------------------------------

        #--- Public ----------------------
        self.length = l
        self.width  = w
        #---------------------------------

    def get_width(self):
        ''' Return rectangle width in centimeters '''
        return self.width

    def get_length(self):
        ''' Return rectangle height in centimeters '''
        return self.length

    def calc_perimeter(self):
        ''' Return rectangle perimeter in centimeters '''
        return ((2 * self.width) + (2 * self.length))
