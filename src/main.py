from src.helpers import is_valid_ip
from src.scanner import scanner


def main():
    print("Input valid IPv4 address(Press q to quit): ")
    while True:
        ip = input()
        if is_valid_ip(ip):
            print("Scanning ", ip)
            if scanner(ip):
                print("Port 22 SSH open", ip)
            else:
                print("Port 22 SSH closed or unable to connect", ip)


            break
        elif ip == 'q':
            break
        else:
            print("Invalid IPv4 address")

if __name__ == "__main__":
    main()





