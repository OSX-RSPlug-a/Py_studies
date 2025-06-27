import socket
import concurrent.futures

def check_port(host, port):
    host_ip = socket.gethostbyname(host)
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((host_ip, int(port)))
            if result == 0:
                print(f"Port {port} on {host} is OPEN")
            else:
                print(f"Port {port} on {host} is CLOSED (error: {result})")
    except Exception as e:
        print(f"Port {port} on {host}: Error - {e}")

if __name__ == "__main__":
    import sys
    print("\n Insert the host for ports 80, 443 and 22 pre scan and run: python check_ports.py <host> <ports...>")
    HOST = input()
    PORTS = ['80', '443', '22']
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(lambda p: check_port(HOST, p), PORTS)


###############################
print("\n")
print("\n ####################### And other scan ####################### \n")

def check_port_by_(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, int(port)))
        if result == 0:
            print(f"Port {port} on {host} is OPEN")
        else:
            print(f"Port {port} on {host} is CLOSED or requires higher privileges")
    except Exception as e:
        print(f"Error checking port {port}: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: python check_ports.py host [ports...]")
        sys.exit(1)
    
    HOST = sys.argv[1]
    PORTS = sys.argv[2:]
    
    for port in PORTS:
        check_port(HOST, port)



#####################