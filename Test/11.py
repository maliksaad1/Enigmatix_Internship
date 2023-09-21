# You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.


def longest_consecutive_str(list_str,k):
    ans = ""
    for i  in range(len(list_str)):
        if len("".join(list_str[i:i+k])) > len(ans):
            ans = "".join(list_str[i:i+k])
    return ans


strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"]
k = 2

print(longest_consecutive_str(strarr,k))
