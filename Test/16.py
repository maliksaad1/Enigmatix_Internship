# Complete the solution so that the function will break up camel casing, using a space between words.

def solution(s):
    result = ''
    for i in s:
        if i.isupper():
            result += ' '
        result += i
    return result

print(solution("camelSasing"))
