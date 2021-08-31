def isPalindrome(s):
    answer = "true"
    sl = s.lower().strip()
    s_arr = list(filter(lambda i:i.isalnum(), sl))
    leng = len(s_arr)
    for i in range(leng//2):
        if s_arr[i] != s_arr[leng - 1 - i]:
            return "false"
    return answer

print(isPalindrome("race a car"))