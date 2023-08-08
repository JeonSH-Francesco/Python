import struct, requests, socket
from datetime import datetime
import pygeoip
mac_dict = {}

gi=pygeoip.GeoIP('GeoIPCity.dat')

class PacketHeader:    
    def __init__(self, data):
        offset = 0
        self.ts_sec = struct.unpack("<L", data[offset : offset + 4])[0]
        offset += 4
        self.ts_usec = struct.unpack("<L", data[offset : offset + 4])[0]
        offset += 4
        self.incl_len = struct.unpack("<L", data[offset : offset + 4])[0]
        offset += 4
        self.orig_len = struct.unpack("<L", data[offset : offset + 4])[0]
        ts = str(self.ts_sec) + "." + str(self.ts_usec)
        print("Time stamp : ",datetime.fromtimestamp(float(ts)), self.incl_len, self.orig_len)

class Ethernet:
    
    def __init__(self, data):
        offset = 0
        self.dmac = data[offset : offset + 6].hex()
        offset += 6
        self.smac = data[offset : offset + 6].hex()
        print("Source mac:", self.smac, "Destinatino Mac:",self.dmac)
        offset += 6
        self.ethernet_type = struct.unpack("<H", data[offset : offset + 2])[0]
        offset += 2
        if self.ethernet_type == 8:
            # ipv4
            self.ip = IP(data[offset:])
        # elif self.ethernet_type == 1544:
        #     # ARP
        #     input()
        #offset += 6
        '''
        if self.smac not in mac_dict:            
            url = "https://macvendors.com/query/" + self.smac
            response = requests.get(url)
            mac_dict[self.smac] = response.content
        if self.dmac not in mac_dict:
            url = "https://macvendors.com/query/" + self.dmac
            response = requests.get(url)
            mac_dict[self.dmac] = response.content
        print(self.smac, mac_dict[self.smac], self.dmac, mac_dict[self.dmac])
        '''

class IP:
    def __init__(self, data):
        self.version_header = bin(int(struct.unpack("<B", data[:1])[0])).replace("0b", "")
        self.verion = "0" * (8 - len(self.version_header)) + self.version_header[0:3]
        self.headr_length = "0" * (8 - len(self.version_header)) + self.version_header[4:8]
        if int(self.headr_length, 2) * 4 != 20:
            
            print(int(self.verion, 2), int(self.headr_length, 2) * 4)
            input()         

        
        self.sip = socket.inet_ntop(socket.AF_INET, data[12:16])
        self.dip = socket.inet_ntop(socket.AF_INET, data[16:20])
        self.ttl = struct.unpack("<B", data[8:9])[0]
        self.proto_type = struct.unpack("<B", data[9:10])[0]
        print("Source IP:", self.sip, "Dstination IP:",self.dip, "TTL:", self.ttl)
        #if self.sip==self.dip:
            #print("Land Attack") 
        print(self.sip, gi.record_by_addr(self.sip), self.dip, gi.record_by_addr(self.dip), self.ttl)
        if self.proto_type != 17:
            #input()#UDP가 아닌 경우
            pass
            
    

# class IP:
    
#     def __init__(self, data):
#         self.sip = socket.inet_ntoa(data[12:16])
#         self.dip = socket.inet_ntoa(data[16:20])
#         self.ttl = struct.unpack("<B", data[8:9])[0]
#         print("source IP : ", self.sip, "Dstination IP : ",self.dip, "TTL : ", self.ttl)


fd = open("2.pcap", "rb")
data = fd.read()
fd.close()
offset = 0
global_header = data[offset : offset + 24]
offset += 24
packet_index = 0

while True:
    packet_index += 1
    print(packet_index, "offset %x" % offset)
    packet_header = PacketHeader(data[offset : offset + 16])
    offset += 16
    packet_data = data[offset : offset + packet_header.incl_len]
    offset += packet_header.incl_len
    Ethernet(packet_data)
    if offset >= len(data):
        break
        
    


