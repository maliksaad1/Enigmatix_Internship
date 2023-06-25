"""
Your task is to sort a given string. Each word in the string will contain a single
number. This number is the position the word should have in the result. Note:
Numbers can be from 1 to 9. So 1 will be the first word (not 0). If the input string is
empty, return an empty string. The words in the input String will only contain valid
consecutive numbers. """

def order(sentence):
    if sentence == "":
        return ""
    else:
        words = sentence.split()
        result = {}
        for word in words:
            result[int(''.join(filter(str.isdigit, word)))] = word
        return " ".join(result[i] for i in range(1, len(words)+1))

print(order("is2 Thi1s T4est 3a"))