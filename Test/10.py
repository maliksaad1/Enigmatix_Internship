def return_middle(string):
    mid = len(string)//2
    mid_f = len(string)//2
    if len(string)%2==0:
        return string[mid-1:mid+1]
    else:
        return string[mid_f]
    

print(return_middle('test'))
print(return_middle('testing'))

"""You are going to be given a word. Your job is to return the middle character of the
word. If the word's length is odd, return the middle character. If the word's length is
even, return the middle 2 characters"""