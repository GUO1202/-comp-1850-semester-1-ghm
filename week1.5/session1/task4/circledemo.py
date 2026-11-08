# Week 1.5, Session 1: Task 4

from geometry import Point, Circle

x = float(input("Enter centre x coordinate: "))
y = float(input("Enter centre y coordinate: "))
radius = float(input("Enter circle radius: "))
circle = Circle(radius, Point(x, y))
print(f"Area: {circle.area():.4f}")
print(f"Perimeter: {circle.perimeter():.4f}")
