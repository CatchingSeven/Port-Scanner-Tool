import ipaddress



# do we consider private ipv4 addresses valid?
def is_valid_ip(ip_string):
    try:
        ipaddress.IPv4Address(ip_string)
        return True
    except ValueError:
        return False



def print_results(results):
    for i in range(len(results)):
        if results[i]["status"] == "open":
            print("Port: " + str(results[i]["port"]) + " Status: " + results[i]["status"])




