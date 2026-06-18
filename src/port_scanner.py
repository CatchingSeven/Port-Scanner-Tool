import argparse

from helpers import is_valid_ip, print_results
from scanner import scanner
import sys

from helpers import handle_arguments
from helpers import is_valid_port


def main():
    args = handle_arguments()
    ip = args.arg1
    port = args.arg2

    if not is_valid_port(port):
        raise Exception("Invalid Port number. Please enter a valid port number, in the range 1-65535")
    else:
        if is_valid_ip(ip):
            print("Scanning ", ip)
            results = scanner(ip, int(port))
            print_results(results, args.showAll)
        else:
            raise Exception("Invalid IP, only IPv4 addresses are allowed")


if __name__ == "__main__":
    main()





