# You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

def longest_conec_k(list_str,k):
    ans = []
    for i in range(len(list_str)-k+1):
        temp = ''.join(list_str[i:i+k])
        ans.append(temp) 
    return max(ans, key=len)


strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"]
k = 2

print(longest_conec_k(strarr,k))
