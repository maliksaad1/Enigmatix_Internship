# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.


def valid_parentheses(string):
    count = 0
    stack = []
    for i in string:
        if i == '(':
            stack.append(i)
            count += 1
        elif i == ')':
            if count == 0:
                return False
            stack.pop()
            count -= 1
    return count == 0


print(valid_parentheses("()()"))
print(valid_parentheses("hi(hi)("))
print(valid_parentheses("hi(hi)())"))
print(valid_parentheses("hi(hi)())("))