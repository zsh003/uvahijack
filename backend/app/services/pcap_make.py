from scapy.all import IP, UDP, Raw, hexdump
import uuid  # 用于获取本地 MAC 地址
from scapy.all import Ether, IP, UDP, Raw, hexdump, sendp, conf
def pcap_make(mac, ip, timestamp, instruct): # 还要指定端口

    instruct = f"ef0258000202000100000000d5000000140066148080{instruct[0]}80000200000000000000000000{instruct[1]}990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000324b142d0000"
    instruct =  bytes.fromhex(instruct)
    # 获取本地 MAC 地址
    def get_local_mac():
        mac = uuid.getnode()  # 获取硬件地址
        mac_address = ':'.join(f"{(mac >> i) & 0xFF:02x}" for i in range(40, -1, -8))
        return mac_address

    # 获取本地 MAC 地址
    local_mac = get_local_mac()
    print(f"Local MAC Address: {local_mac}")

    # 构造链路层 (Ethernet)
    ether_layer = Ether(src=local_mac, dst=mac)

    # 构造 IP 层
    ip_layer = IP(src="192.168.169.2", dst=ip)

    # 构造 UDP 层
    udp_layer = UDP(sport=54321, dport=8800)

    # 构造负载 (Raw 层)
    payload = Raw(load=instruct)

    # 构造完整数据包
    packet = ether_layer / ip_layer / udp_layer / payload

    # # 显示数据包的详细信息
    # packet.show()

    # 打印数据包的十六进制表示
    print("Hexdump of the packet:")
    hexdump(packet)

    # 获取系统默认接口
    default_iface = conf.iface
    print(f"Default network interface: {default_iface}")

    # 发送数据包
    print("Sending packet...")
    sendp(packet, verbose=True)

pcap_make("b8:3d:fb:5d:7e:ef", "192.168.169.1", "1234", ["b3", "31"])
pcap_make("b8:3d:fb:5d:7e:ef", "192.168.169.1", "1234", ["ff", "7d"])
