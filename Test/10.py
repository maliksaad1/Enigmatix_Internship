def return_middle(string):
    mid = len(string)//2
    mid_f = len(string)//2
    if len(string)%2==0:
        return string[mid-1:mid+1]
    else:
        return string[mid_f]
    

print(return_middle('test'))
print(return_middle('testing'))