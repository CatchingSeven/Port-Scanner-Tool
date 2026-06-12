import ipaddress

# do we consider private ipv4 addresses valid?
def is_valid_ip(ip_string):
    try:
        ipaddress.IPv4Address(ip_string)
        return True
    except ValueError:
        return False

