import re


def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))


print(is_valid_email("user@example.com"))    # True
print(is_valid_email("user.name@domain.co"))  # True
print(is_valid_email("invalid@email"))       # False
print(is_valid_email("user@.com"))           # False
