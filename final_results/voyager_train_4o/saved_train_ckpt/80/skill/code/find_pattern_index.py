

def find_pattern_index(main_string, pattern):
    main_length = len(main_string)
    pattern_length = len(pattern)
    if (pattern_length == 0):
        return 0
    for i in range(((main_length - pattern_length) + 1)):
        if (main_string[i:(i + pattern_length)] == pattern):
            return i
    return (- 1)
