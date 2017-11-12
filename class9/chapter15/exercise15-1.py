#!/usr/bin/env python3
import math
import copy

###############################################################################
#
print("\nExercise 15.1\n")
#
# Question 1
# 1. Write a definition for a class named Circle with attributes center and 
# radius, where center is a Point object and radius is a number.
#
class Circle:
    """Circle object
    
    attributes center, radius"""
    
class Point:
    """Point object
    
    attributes x,y"""
    
class Rectangle:
    """Represents a rectangle. 

    attributes: width, height, corner.
    """
#
# Question 2
# 2. Instantiate a Circle object that represents a circle with its center at 
# (150, 100) and radius 75.
# 
circle = Circle
circle.center = Point()
circle.center.x = 150.0
circle.center.y = 100.0
circle.radius = 75.0
#
# Question 3
# 3. Write a function named point_in_circle that takes a Circle and a Point and 
# returns True if the Point lies in or on the boundary of the circle.
# 
def point_in_circle(point, circle):
    dx = point.x - circle.center.x
    dy = point.y - circle.center.y
    dist = math.sqrt(dx**2 + dy**2)
    return dist <= circle.radius
#
# Question 4
# 4. Write a function named rect_in_circle that takes a Circle and a Rectangle 
# and returns True if the Rectangle lies entirely in or on the boundary of the 
# circle.
#
def rect_in_circle(rect, circle):
    p = copy.copy(rect.corner)
    if not point_in_circle(p, circle):
        return False

    p.x += rect.width
    if not point_in_circle(p, circle):
        return False
    
    p.y -= rect.height
    if not point_in_circle(p, circle):
        return False

    p.x -= rect.width
    if not point_in_circle(p, circle):
        return False

    return True
# Question 5
# 5. Write a function named rect_circle_overlap that takes a Circle and a 
# Rectangle and returns True if any of the corners of the Rectangle fall inside 
# the circle. Or as a more challenging version, return True if any part of the 
# Rectangle falls inside the circle.
# 

def rect_circle_overlap(rect, circle):
    p = copy.copy(rect.corner)
    if point_in_circle(p, circle):
        return True

    p.x += rect.width
    if point_in_circle(p, circle):
        return True

    p.y -= rect.height
    if point_in_circle(p, circle):
        return True

    p.x -= rect.width
    if point_in_circle(p, circle):
        return True

    return False



box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 50.0
box.corner.y = 50.0

print(box.corner.x)
print(box.corner.y)

print(circle.center.x)
print(circle.center.y)
print(circle.radius)

print(point_in_circle(box.corner, circle))
print(rect_in_circle(box, circle))
print(rect_circle_overlap(box, circle))
