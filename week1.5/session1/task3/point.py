# Week 1.5, Session 1: Task 3

class Point:
    """
    A Point in 2D space.
    """

    def __init__(self, x, y):
        """Create a point with x and y coordinates."""
        self.x = x
        self.y = y

    def distance(self):
        """Return this point's distance from the origin."""
        return math.hypot(self.x, self.y)

    def distance_to(self, point):
        """Return the distance to another point."""
        return math.hypot(self.x - point.x, self.y - point.y)



p1 = Point(3, 4)
p2 = Point(6, 8)
print(p1.x, p1.y)
print(p1.distance())
print(p1.distance_to(p2))
