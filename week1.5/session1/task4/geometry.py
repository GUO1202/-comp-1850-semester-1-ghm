# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

class Point:
    """A point in 2D space."""
    def __init__(self, x, y):
        """Create a point with x and y coordinates."""
        self.x, self.y = x, y
    def distance(self):
        """Return distance from origin."""
        return math.hypot(self.x, self.y)
    def distance_to(self, point):
        """Return distance to another point."""
        return math.hypot(self.x-point.x, self.y-point.y)

class Circle:
    """A circle with a radius and a Point centre."""
    def __init__(self, radius, centre=Point(0.0, 0.0)):
        """Create a circle with radius and optional centre."""
        self.radius, self.centre = radius, centre
    def area(self):
        """Return the circle's area."""
        return math.pi * self.radius ** 2
    def perimeter(self):
        """Return the circle's circumference."""
        return 2 * math.pi * self.radius

# Don't add any testing code to this file!
