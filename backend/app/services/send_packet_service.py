from scapy.all import sendp, conf

def send_packet_raw(packet):
    # 获取系统默认接口
    default_iface = conf.iface
    print(f"Default network interface: {default_iface}")

    # 发送数据包
    print("Sending packet...")
    sendp(packet, verbose=True)