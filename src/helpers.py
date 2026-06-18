import argparse
import ipaddress



# do we consider private ipv4 addresses valid?
def is_valid_ip(ip_string):
    try:
        ipaddress.IPv4Address(ip_string)
        return True
    except ValueError:
        return False

#validate that string can be converted to int, used before parsing to valid port
def validate_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

#validate that an entered port is in the correct range
def is_valid_port(port_count):
    if validate_int(port_count):
        port_count = int(port_count)
        try:
            if port_count < 1:
                return False
            if port_count > 65535:
                return False
            return True
        except ValueError:
            return False

def print_results(results, showAll=False):
    for i in range(len(results)):
        if showAll:
            print("Port: " + str(results[i]["port"]) + " Status: " + results[i]["status"])
        elif results[i]["status"] == "open":
            print("Port: " + str(results[i]["port"]) + " Status: " + results[i]["status"])



def handle_arguments():
    parser = argparse.ArgumentParser(description='Scanner tool')
    parser.add_argument('-a', '--all', action='store', help="scan all ports")
    parser.add_argument('-sA', '--showAll', action="store_true", help='Shows all ports, including closed ports')
    parser.add_argument('-t', '--threads', action='store', help="enable multithreaded scan")

    parser.add_argument('arg1', help="IP address to scan")
    parser.add_argument('arg2', nargs='?', default='100', help="ports to scan")

    args = parser.parse_args()
    return args
