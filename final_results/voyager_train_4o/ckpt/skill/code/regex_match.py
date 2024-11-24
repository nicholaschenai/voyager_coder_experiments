import re

def regex_match(string, pattern):
    return (re.fullmatch(pattern, string) is not None)
