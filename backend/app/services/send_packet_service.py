from scapy.all import *
import socket

def send_packet_scapy(iface, packet):
    # sendp 用于发送链路层（Layer 2）数据包，而 send 用于网络层（Layer 3）
    sendp(packet, iface=iface, verbose=0)

def send_packet_scapy_from_hex(iface, packet_hex):
    packet = bytes.fromhex(packet_hex)
    sendp(packet, iface=iface, verbose=0)
    # send(packet, verbose=0)
    print("已发送流量：", packet_hex)

def send_packet_scapy_from_hex_3layer(packet_hex):
    packet_bytes = bytes.fromhex(packet_hex)
    packet = IP(packet_bytes)  # 重新构造 Packet 对象
    send(packet, verbose=0)
    # send(packet, verbose=0)
    print("已发送流量：", packet_hex)

# 发送十六进制数据包
def send_packet_from_hex(iface, packet_hex):
    # 将十六进制字符串转换为字节串
    packet_bytes = bytes.fromhex(packet_hex)

    # 创建原始套接字
    sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)  # 注：socket.AF_PACKET只有Linux环境才有，Windows就只能用scapy了
    sock.bind((iface, 0))  # 绑定到指定网络接口

    # 发送数据包
    sock.send(packet_bytes)
    print("发送成功！")

    # 关闭套接字
    sock.close()


if __name__ == '__main__':
    from time import sleep
    iface = "WLAN"
    packet1 = 'b83dfb5d7eeff46d3f286e64080045000074000100004011a723c0a8a902c0a8a901c9d522600060fb72ef0258000202000100000000d5000000140066148080b38000020000000000000000000031990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000324b142d0000'
    packet2 = 'b83dfb5d7eeff46d3f286e64080045000074000100004011a723c0a8a902c0a8a901c9d5226000605972ef0258000202000100000000df000000140066148080ff800002000000000000000000007d990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000324b142d0000'
    packet3 = 'b83dfb5d7eeff46d3f286e64080045000074000100004011a723c0a8a902c0a8a901c9d5226000603573ef0258000202000100000000fd000000140066148080008000020000000000000000000082990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000324b142d0000'
    send_packet_scapy_from_hex(iface, packet1)
    send_packet_scapy_from_hex(iface, packet2)
    sleep(3)
    send_packet_scapy_from_hex(iface, packet3)