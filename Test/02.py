def count_words(n,words):
    count={}

    for word in words:
        if word in count:
            count[word]+=1
        else:
            count[word]=1

    unique_words=list(count.keys())

    print("Lenth:",len(unique_words))
    print("Number of occurrences")
    for word in unique_words:
        print(count[word],end='')

    

count_words(4,["bcdef","abcdefg","bcde","bcdef"])

"""
You are given words. Some words may repeat. For each word, output its number of
occurrences. The output order should correspond with the input order of appearance
of the word. See the sample input/output for clarification.
Input format: two parameters: first number of words, second list of words to process
Output format: Output two lines
First line: Number of unique words
Second line: Number of occurrences for each distinct word according to their
appearance in the input.
Input:
4, [“bcdef”, “abcdefg”, “bcde”, “bcdef”]
Output:
3
211
Output explanation:
First output distinct words.
Second line shows the count for each word which occurred in the list.
"""
