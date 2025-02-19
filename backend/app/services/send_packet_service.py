from scapy.all import sendp, conf

def send_packet_raw(packet):
    #packet = bytes.fromhex(packet)
    # 获取系统默认接口
    default_iface = conf.iface
    print(f"Default network interface: {default_iface}")

    # 发送数据包
    print("Sending packet...")
    sendp(packet, iface=default_iface, verbose=True)

if __name__ == '__main__':
    packet1 = 'b83dfb5d7eeff46d3f286e68080045000074000100004011a723c0a8a902c0a8a901d43122600060f116ef0258000202000100000000d5000000140066148080b38000020000000000000000000031990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000324b142d0000'
    packet2 = 'b83dfb5d7eeff46d3f286e68080045000074000100004011a723c0a8a902c0a8a901d431226000605916ef0258000202000100000000d5000000140066148080ff800002000000000000000000007d990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000324b142d0000'
    send_packet_raw(packet1)
    send_packet_raw(packet2)