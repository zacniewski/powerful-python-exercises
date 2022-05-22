words = ["bib", "bias", "dad", "eye", "deed", "tooth"]


def is_palindrome(s: str) -> bool:
    return s == s[::-1]


palindroms_with_comprehensions = [word for word in words if is_palindrome(word)]
print(palindroms_with_comprehensions)
