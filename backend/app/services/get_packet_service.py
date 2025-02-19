
from scapy.all import Ether, IP, UDP, Raw, get_if_hwaddr
"""
import uuid  # 用于获取本地 MAC 地址
def get_local_mac():
    mac = uuid.getnode()  # 获取硬件地址
    mac_address = ':'.join(f"{(mac >> i) & 0xFF:02x}" for i in range(40, -1, -8))
    return mac_address
"""
# 获取本地MAC地址
def get_local_mac(iface):
    return get_if_hwaddr(iface)

def get_packet_raw(dst_mac, dst_ip, dst_port, src_mac, src_ip, src_port, data):

    data = bytes.fromhex(data)

    # 构造链路层 (Ethernet)
    ether_layer = Ether(src=src_mac, dst=dst_mac)

    # 构造 IP 层
    ip_layer = IP(src=src_ip, dst=dst_ip)

    # 构造 UDP 层
    udp_layer = UDP(sport=src_port, dport=dst_port)

    # 构造负载 (Raw 层)
    payload = Raw(load=data)

    # 构造完整数据包
    packet = ether_layer / ip_layer / udp_layer / payload

    # 转为Hex字符串
    packet_hex = bytes(packet).hex()

    # # 显示数据包的详细信息
    # packet.show()

    # 打印数据包的十六进制表示
    print("Get packet:")
    print(packet_hex)

    return packet_hex

if __name__ == '__main__':
    # 测试代码
    trafficData1 = "ef0258000202000100000000d5000000140066148080b38000020000000000000000000031990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000324b142d0000"
    trafficData2 = "ef0258000202000100000000d7000000140066148080ff800002000000000000000000007d990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000324b142d0000"

    dstMac = 'b8:3d:fb:5d:7e:ef'
    dstIp = '192.168.169.1'
    dstPort = 8800
    srcMac = '12:34:56:78:9a:bc'
    srcIp = '192.168.169.2'
    srcPort = 23456

    packet1 = get_packet_raw(dstMac, dstIp, dstPort, srcMac, srcIp, srcPort, trafficData1)
    packet2 = get_packet_raw(dstMac, dstIp, dstPort, srcMac, srcIp, srcPort, trafficData2)

    from scapy.all import sendp, conf

    def send_packet_raw(packet):
        packet = bytes.fromhex(packet)
        # 获取系统默认接口
        default_iface = conf.iface
        # print(f"\nDefault network interface: {default_iface}")
        # 发送数据包
        sendp(packet, iface=default_iface, verbose=True)
        print(f"Sent packet: {bytes(packet).hex()}")

    send_packet_raw(packet1)
    send_packet_raw(packet2)
