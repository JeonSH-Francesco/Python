import struct, requests, socket
from datetime import datetime
import pygeoip
mac_dict = {}

gi=pygeoip.GeoIP('GeoLiteCity.dat')

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
        print("Source mac:", self.smac, "Destination Mac:",self.dmac)
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

# class IP:
    
#     def __init__(self, data):
#         self.sip = socket.inet_ntoa(data[12:16])
#         self.dip = socket.inet_ntoa(data[16:20])
#         self.ttl = struct.unpack("<B", data[8:9])[0]
#         print("source IP : ", self.sip, "Dstination IP : ",self.dip, "TTL : ", self.ttl)

class IP:
    def __init__(self, data):
        self.version_header = bin(int(struct.unpack("<B", data[:1])[0])).replace("0b", "")
        self.verion = "0" * (8 - len(self.version_header)) + self.version_header[0:3]
        self.headr_length = "0" * (8 - len(self.version_header)) + self.version_header[4:8]
        #if int(self.headr_length, 2) * 4 != 20:
            
            #print(int(self.verion, 2), int(self.headr_length, 2) * 4)
            #input()         

        self.sip = socket.inet_ntop(socket.AF_INET, data[12:16])
        self.dip = socket.inet_ntop(socket.AF_INET, data[16:20])
        self.ttl = struct.unpack("<B", data[8:9])[0]
        self.proto_type = struct.unpack("<B", data[9:10])[0]
        print("Source IP:", self.sip, "Dstination IP:",self.dip, "TTL:", self.ttl)
        #land attack인 경우
        #if self.sip==self.dip:
            #print("Land Attack")
        
        print(self.sip, gi.record_by_addr(self.sip), self.dip, gi.record_by_addr(self.dip), self.ttl)
        #print("\n")
        #ip spoofing인 경우
        # if not (self.sip.startswith("192.168.0.") or self.dip.startswith("192.168.0")):
        #     input()
        if self.proto_type != 17:
            #input()#UDP가 아닌 경우
            pass
        if self.proto_type ==6:
            tcp_data = TCP(data[int(self.headr_length, 2) * 4:])
            
            
class TCP:
    def __init__(self,data):
        self.sport=struct.unpack(">H",data[0:2])[0]
        self.dport=struct.unpack(">H",data[2:4])[0]
        self.seq_number=struct.unpack("<L",data[4:8])[0]
        self.ack_number=struct.unpack("<L",data[8:12])[0]
        self.header_length = "0" + bin(int(struct.unpack("<B", data[12:13])[0])).replace("0b", "")[0:3]
        #self.header_length = "0" + bin(int(struct.unpack("<B", data[12:13])[0])).replace("0b", "")[0:3]
        self.header_length = int(self.header_length, 2) * 8
        self.flags = bin(int(struct.unpack("<B", data[13:14])[0])).replace("0b", "")
        self.flags = "0" * (6 - len(self.flags)) + self.flags
        if self.flags[0] == "1":
            print("urgent")
        if self.flags[1] == "1":
            print("ack")
        if self.flags[2] == "1":
            print("push")
        if self.flags[3] == "1":
            print("rst")
        if self.flags[4] == "1":
            print("syn")
        if self.flags[5] == "1":
            print("fin")
        
        print("Source Port : ",self.sport,"Destination Port:",self.dport)
        print("Seq_number:",self.seq_number, "Ack_number:",self.ack_number)
        print("flags:",self.flags)
        print("-----------------------------------")
        print("\n")
        
        #if self.flags[4] == "1":
        #   input()
        tcp_payload = data[self.header_length:]
        if len(tcp_payload) > 0 and (self.sport == 80 or self.dport == 80):
            print(tcp_payload, len(tcp_payload))
            try:
                tcp_payload = tcp_payload.decode("utf-8")
                if tcp_payload.startswith("GET ") or tcp_payload.startswith("POST "):
                    if tcp_payload.endswith("\r\n\r\n"):
                        print(tcp_payload) 
                        #input()
            except:
                pass
        #TCP-Follow-Stream
        # tcp_payload = data[self.header_length:]
        # if len(tcp_payload) > 0 and (self.sport == 80 or self.dport == 80):
        #     if self.sport == 44542 or self.dport == 44542:
        #         fd = open("a.txt", "a")
        #         fd.write(tcp_payload.decode("utf-8"))
        #         fd.close()
        
#"2.pcap" is my pcap file name. So, You should adjust your pcap_file_name.
fd = open("2.pcap", "rb")
data = fd.read()
fd.close()
offset = 0
global_header = data[offset : offset + 24]
offset += 24
packet_index = 0

while True:
    packet_index += 1
    print("-----------------------------------")
    print("Packet Index:",packet_index, "/ Offset :%x" % offset)
    packet_header = PacketHeader(data[offset : offset + 16])
    offset += 16
    packet_data = data[offset : offset + packet_header.incl_len]
    offset += packet_header.incl_len
    Ethernet(packet_data)
    if offset >= len(data):
        break
