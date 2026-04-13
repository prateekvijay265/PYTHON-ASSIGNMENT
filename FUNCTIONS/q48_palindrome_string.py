def is_palindrome(text):
    cleaned = text.lower()
    return cleaned == cleaned[::-1]

print(is_palindrome('madam'))
print(is_palindrome('python'))
