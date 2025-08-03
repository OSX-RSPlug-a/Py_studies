import os
import sys
from scapy.all import IP, ICMP, sr1

@ATMT.state()
def ping(host):
    packet = IP(dst=host)/ICMP()
    response = sr1(packet, timeout=2, verbose=0)
    
    if response:
        return f"{host} is online"
    else:
        return f"{host} is OFFline"
    
host_to_scan = "theverge.com"

result = ping(host_to_scan)
print (result)