from src.helpers import is_valid_ip
from src.scanner import scanner


def main():
    results = {}
    print("Input valid IPv4 address(Press q to quit): ")
    while True:
        ip = input()
        if is_valid_ip(ip):
            print("Scanning ", ip)
            results = scanner(ip)
            for i in range(len(results)):
                if results[i]["status"] == "open":
                    print(results[i])
            break
        elif ip == 'q':
            break
        else:
            print("Invalid IPv4 address")

if __name__ == "__main__":
    main()





