# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

def reverse_words(text):
    words = text.split(" ")
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
    reversed_text = " ".join(reversed_words)
    return reversed_text

print(reverse_words('The quick brown fox jumps over the lazy dog.'))

print(reverse_words("double  spaces"))