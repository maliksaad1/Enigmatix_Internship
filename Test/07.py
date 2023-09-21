def sum_array(arr):
    return sum(sorted(arr)[1:-1])


print(sum_array([6, 2, 1, 8, 10]))

"""
Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ). You can not use the if statement
"""