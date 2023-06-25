def frequency(words_list):
    unique_words = len(set(words_list))
    frequency = []
    for i in range(unique_words):
        frequency.append(words_list.count(words_list[i]))
    return (unique_words,frequency)

def main():
    ans = frequency(['bcdef', 'abcdefg', 'bcde', 'bcdef'])
    unique = str(ans[0])
    print(unique)
    freq = ' '.join(map(str, ans[1]))
    print(freq)
main()