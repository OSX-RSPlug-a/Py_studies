from typing import List


def generate_ips(start_ip: str, count: int) -> List[str]:
    parts = start_ip.split('.')

    if len(parts) != 4:
        raise ValueError(f"'{start_ip}' is not a valid IPv4 address")

    base = int(parts[3])
    
    ips = []

    for i in range(count):
        octet = base + i

        if octet > 255:
            raise ValueError("IP range exceeded 255 in the last numbers")

        ips.append(f"{parts[0]}.{parts[1]}.{parts[2]}.{octet}")

    return ips


if __name__ == "__main__":
    ip_list = generate_ips("192.168.1.1", 100)

    for ip in ip_list:
        print(ip)