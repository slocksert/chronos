import re

#regular expression email validator
def email_is_valid(email: str) -> bool:
    regex = r'\b[A-Za-z0-9._%+-]+@[A-za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    if re.fullmatch(regex, email):
        return True
    return False