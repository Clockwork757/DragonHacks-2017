#========================================
#Project Name: Room Type/Size
#Project Description: Excersise 16.6 HW#1
#Date:	04/15/2017
#Programmer Name: Matthew Marschall 
#========================================

import numpy as np

class Point:
# Class to describe coord points
        def __init__(self, x=0, y=0):
                self.x = x
                self.y = y
	
        def __str__(self):
                return "({0}, {1})".format(self.x, self.y)
		
        def get_x(self):
                return self.x
		
        def get_y(self):
                return self.y 

class Room():
    ''' Superclass for room types '''
    def __init__(self, t):
        #--- Public -----------
        self.type = t
        self.area = None
        #----------------------

    def set_area(self, area):
        ''' Set room area '''
        self.area = area

class Circle(Room):
    ''' Create a room of type circle '''
    def __init__(self, r):
        ''' Takes one positional argument: radius '''
        #--- Initialize Superclass -------
        t = 1
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
    def __init__(self, w, h):
        #--- Initialize Superclass -------
        t = 0
        Room.__init__(t)
        self.set_area(w*h)
        #---------------------------------

        #--- Public ----------------------
        self.width = w
        self.height = h
        #---------------------------------

    def get_width(self):
        ''' Return rectangle width in centimeters '''
        return self.width

    def get_height(self):
        ''' Return rectangle height in centimeters '''
        return self.height

    def calc_perimeter(self):
        ''' Return rectangle perimeter in centimeters '''
        return ((2 * self.width) + (2 * self.height))
