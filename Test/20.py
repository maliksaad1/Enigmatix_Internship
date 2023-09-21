"""
Given two positive integers m (width) and n (height), fill a two-dimensional list (or
array) of size m-by-n in the following way:
a. All the elements in the first and last row and column are 1.
b. All the elements in the second and second-last row and column are 2,
excluding the elements from step 1.
c. All the elements in the third and third-last row and column are 3, excluding the
elements from the previous steps.
d. And so on …
Given m = 10, n = 9, your function should return
[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 2, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 2, 3, 4, 4, 4, 4, 3, 2, 1],
[1, 2, 3, 4, 5, 5, 4, 3, 2, 1],
[1, 2, 3, 4, 4, 4, 4, 3, 2, 1],
[1, 2, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


"""




def rect(n,m):
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n-1 or j == 0 or j == m-1:
                print("1", end=" ")
            elif i == 1 or i == n-2 or j == 1 or j == m-2:
                print("2", end=" ")
            elif i == 2 or i == n-3 or j == 2 or j == m-3:
                print("3", end=" ")
            elif i == 3 or i == n-4 or j == 3 or j == m-4:
                print("4", end=" ")
            elif i == 4 or i == n-5 or j == 4 or j == m-5:
                print("5", end=" ")
            elif i == 5 or i == n-6 or j == 5 or j == m-6:
                print("6", end=" ")
        print()

rect(9,10)