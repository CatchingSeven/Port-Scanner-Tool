import argparse

from helpers import is_valid_ip, print_results
from scanner import scanner
import sys















def main():
    ip = sys.argv[1]
    port_count = sys.argv[2]


    if is_valid_ip(ip):
        print("Scanning ", ip)
        results = scanner(ip, int(port_count))
        print_results(results)
    else:
        raise Exception("Invalid IP or Port number: use the format port_scanner.py [IPv4 address] [port count]")

if __name__ == "__main__":
    main()





