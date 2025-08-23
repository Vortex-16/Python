def longest_palindrome(s):
    res = ""
    for i in range(len(s)):
        # odd length palindrome
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > len(res):
                res = s[l:r+1]
            l -= 1
            r += 1

        # even length palindrome
        l, r = i, i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > len(res):
                res = s[l:r+1]
            l -= 1
            r += 1
    return res

print(longest_palindrome("babad"))  # "bab" or "aba"
