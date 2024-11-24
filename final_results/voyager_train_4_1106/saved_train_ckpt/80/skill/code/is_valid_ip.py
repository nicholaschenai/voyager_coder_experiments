

def is_valid_ip(ip_str):
    octets = ip_str.split('.')
    if (len(octets) != 4):
        return False
    for octet in octets:
        if ((not octet.isdigit()) or (not (0 <= int(octet) <= 255))):
            return False
        if ((len(octet) > 1) and (octet[0] == '0')):
            return False
    return True
