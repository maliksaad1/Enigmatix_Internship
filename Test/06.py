# You get an array of numbers, and return the sum of all of the positive ones. Example [1, -4, 7, 12] => 1+7+12 = 20. If there is nothing to sum return 0. You can not use the if statement.


def positive_sum(arr):
    return sum(filter(lambda x: x > 0, arr))


print(positive_sum([1, -4, 7, 12]))