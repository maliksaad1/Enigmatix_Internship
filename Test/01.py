def print_nextLine(num):
        while num > 0:
            digit = num % 10
            print(digit)
            num //= 10

def main():
    print_nextLine(12345)

main()

"""
Write a function which will take an integer as input and print each digit in a separate
line. You are not allowed to use str or any other method will convert the integer into
string.
Input: 1011
Output:
1
1
0
1
"""