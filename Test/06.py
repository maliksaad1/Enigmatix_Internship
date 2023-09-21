# You get an array of numbers, and return the sum of all of the positive ones. Example [1, -4, 7, 12] => 1+7+12 = 20. If there is nothing to sum return 0. You can not use the if statement.

import numpy as np

def sum_pos(nums):
    total = 0
    for i in nums:
        total += (i * (i > 0))
    return total

def sum_positive(nums):
    array = np.array(nums)
        
    positive_nums = array[array > 0 ]
    
    positive_sum = np.sum(positive_nums)
    
    return positive_sum



print(sum_positive([1, -4, 7, 12]))
print(sum_pos([1, -4, 7, 12]))