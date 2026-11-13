import scapy.all as scapy
import time

def arp_scan(ip_range):
    print("\n scanning network for active hosts  \n")
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet=broadcast/arp_request
    answered=scapy.srp(packet, timeout=2, verbose=False)[0]
    devices=[]

    for sent, received in answered:
        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc
        })

    return devices
    

#ping(response time)

def get_response_time(ip):
    pkt=scapy.IP(dst=ip) / scapy.ICMP()

    start_time = time.time()
    reply= scapy.sr1(pkt, timeout=1, verbose=False)
    end_time= time.time()

    if reply:
        return round((end_time-start_time) * 1000,2)# in ms
    else:
        return None

ip_range=input("Enter the ip range to scan :")

#arp scan
devices=arp_scan(ip_range)

print("IP address  \t\t MAC ADDRESS \t\t  RESPONSE TIME(ms) ")
print("--" * 70)

#response time

for device in devices:
    response_time=get_response_time(device["ip"])

    if response_time:
     print(f"{device['ip']} \t {device['mac']} \t {response_time} ms")
    else:
        print(f"{device['ip']} \t {device['mac']} \t no response")  
