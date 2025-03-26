from scapy.all import *
from time import sleep

# 获取本地MAC地址
def get_local_mac(iface):
    return get_if_hwaddr(iface)

def get_packet_raw(dst_mac, dst_ip, dst_port, src_mac, src_ip, src_port, iface, timestamp, instruct):
    # 应用层数据
    data = f"ef0258000202000100000000{timestamp}0000140066148080{instruct[0:2]}80000200000000000000000000{instruct[2:4]}990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000324b142d0000"
    data_hex = bytes.fromhex(data)

    # 构造链路层 (Ethernet)
    ether_layer = Ether(src=src_mac, dst=dst_mac)

    # 构造 IP 层
    ip_layer = IP(src=src_ip, dst=dst_ip)

    # 构造 UDP 层
    udp_layer = UDP(sport=src_port, dport=dst_port)

    # 构造负载 (Raw 层)
    payload = Raw(load=data_hex)

    # 3层流量包
    packet = ip_layer / udp_layer / payload

    # 2层流量包
    packet_real = ether_layer / ip_layer / udp_layer / payload
    print("已构建流量包：")
    print(bytes(packet_real).hex())

    return bytes(packet_real).hex()

if __name__ == '__main__':

    iface = "WLAN"
    local_mac = str(get_if_hwaddr(iface))  # 获取本地mac
    print(local_mac)

    src_mac = local_mac
    src_ip = "192.168.169.2"
    src_port = 51669

    dst_mac = "b8:3d:fb:5d:7e:ef"
    dst_ip = "192.168.169.1"
    dst_port = 8800

    def throttle_start():
        packet1_hex = get_packet_raw(dst_mac, dst_ip, dst_port, src_mac, src_ip, src_port, iface, "d500", "b331")
        packet1 = bytes.fromhex(packet1_hex)
        sendp(packet1, iface=iface, verbose=0)
        #sleep(3)

        packet2_hex = get_packet_raw(dst_mac, dst_ip, dst_port, src_mac, src_ip, src_port, iface, "df00", "ff7d")
        packet2 = bytes.fromhex(packet2_hex)
        sendp(packet2, iface=iface, verbose=0)


    def throttle_stop():
        packet1_hex = get_packet_raw(dst_mac, dst_ip, dst_port, src_mac, src_ip, src_port, iface, "fd00", "0082")
        packet1 = bytes.fromhex(packet1_hex)
        sendp(packet1, iface=iface, verbose=0)

    throttle_start()
    #sleep(3)
    #throttle_stop()




