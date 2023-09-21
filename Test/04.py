def replace_occurrences(s):
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count+=1
        else:
            print((count, s[i-1]), end='')
            count = 1
    print((count, s[i]),end='')

def main():
    s = '1222311'
    result = replace_occurrences(s)
    print(result)
main()

"""
You are given a string. Suppose a character ‘c’ occurs 4 times in the string. Replace
these consecutive occurrences of the character 'c' with (4, c) in the string.
Input format: A single line of input consisting of string s
Output format: A single line of output consisting of the modified string.
Input:
1222311
Output:
(1, 1) (3, 2) (1, 3) (2, 1)
"""