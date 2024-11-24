import re

def is_palindrome(s):
    cleaned = re.sub('[^a-zA-Z0-9]', '', s).lower()
    return (cleaned == cleaned[::(- 1)])
