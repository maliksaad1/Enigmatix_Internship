def decode_matrix(rows, columns, encoded_matrix):
    decoded_string = ""

    for j in range(columns):
        for i in range(rows):
            if encoded_matrix[i][j].isalpha() or encoded_matrix[i][j] == ' ':
                decoded_string += encoded_matrix[i][j]

    return decoded_string

# Example usage:
rows = 7
columns = 3
encoded_matrix = [
    ['T', 's', 'i'],
    ['h', '%', 'x'],
    ['i', ' ', '#'],
    ['s', 'M', ' '],
    ['$', 'a', ' '],
    ['#', 't', '%'],
    ['i', 'r', '!']
]
decoded_string = decode_matrix(rows, columns, encoded_matrix)
print(decoded_string)