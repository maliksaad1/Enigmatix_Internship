import re

def decode(s):
    result = ''
    for i in range(len(s[0])):
        for j in range(len(s)):
            if re.match(r'[a-zA-Z ]', s[j][i]):
                result += s[j][i]
    return result

def main():
    encoded_matrix = [
        ['T', 's', 'i'],
        ['h', '%', 'x'],
        ['i', ' ', '#'],
        ['s', 'M', ' '],
        ['$', 'a', ' '],
        ['#', 't', '%'],
        ['i', 'r', '!']
    ]

    result = decode(encoded_matrix)
    print(result)

main()
