def is_palindrome(s):
    s = s.lower().replace(" ", "")
    
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])


input_str = "АББ ББА"
result = is_palindrome(input_str)
print("YES" if result else "NO")
