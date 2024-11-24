

def is_valid_ipv6(ip):
    if (ip.count(':') != 7):
        return False
    groups = ip.split(':')
    for group in groups:
        if ((not (1 <= len(group) <= 4)) or (not all(((c in '0123456789abcdefABCDEF') for c in group)))):
            return False
    return True
