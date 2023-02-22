def palindrome(s):
    # REMOVE SPACES STRING
    s = s.replace(' ', '')
    # CHECK the string is == reversed version of the string

    return s == s[::-1]


print(palindrome("I ama I"))
