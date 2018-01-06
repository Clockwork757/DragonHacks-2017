#========================================
#Project Name: Room Type/Size
#Project Description: Excersise 16.6 HW#1
#Date:	04/15/2017
#Programmer Name: Matthew Marschall 
#========================================

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
		
class Rectangle:
# A class to manufacture rectangle objects 

        def __init__(self, posn, w, h):
        #Initialize rectangle at posn, with width w, height h
                self.corner = posn
                self.width = w
                self.height = h

        def __str__(self):
                return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)
	
        def grow(self, delta_width, delta_height):
        # Grow (or shrink) this object by the deltas 
                self.width += delta_width
                self.height += delta_height
	
        def get_width(self):
                return self.width
		
        def get_height(self):
                return self.height
		
        def move(self, dx, dy):
        #Move this object by the deltas
                self.corner.x += dx
                self.corner.y += dy
		
        def same_coordinates(self, p1, p2):
                return (p1.x == p2.x) and (p1.y == p2.y)
		
        def area(self):
                return self.width*self.height
		
        def perimeter(self):
                return ((2 * self.width) + (2 * self.height))
	
        def flip(self):
                self.width, self.height = self.height, self.width
	
        def contains(self, point):
                x, y = point.get_x(), point.get_y()
                return 0 <= x < self.width and 0 <= y < self.height
