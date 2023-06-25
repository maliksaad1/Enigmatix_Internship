"""
Our football team has finished the championship. Our team's match results are
recorded in a collection of strings. Each match is represented by a string in the
format x:y, where x is our team and y is our opponents score. The rules to calculate
score is
a. If x > y: 3 points
b. If x < y: 0 point
c. If x = y: 1 point
We need to write a function that takes this collection and returns the number of points
our team (x) got in the championship by the rules given above.
"""

def points(games):
    return sum([3 if i[0] > i[2] else 0 if i[0] < i[2] else 1 for i in games])

print(points(['3:1', '2:2', '0:1', '3:3', '1:0', '2:1', '3:0', '1:0', '0:1', '1:2']))