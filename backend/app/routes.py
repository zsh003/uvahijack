from flask import request, jsonify
from time import sleep
import socket
import psutil

from .services.hijack_service import throttle_start_hijack
from .services.hijack_service import throttle_stop_hijack
from .services.hijack_service import uav_fly_hijack
from .services.hijack_service import uav_swerve_hijack

from .services.get_packet_service import get_packet_2layer
from .services.get_packet_service import get_packet_3layer
from .services.get_packet_service import get_local_mac
from .services.send_packet_service import send_packet_scapy_from_hex
from .services.send_packet_service import send_packet_scapy_from_hex_3layer

from .services.ddos_flood import udp_flood
from .services.ddos_flood import tcp_flood

# 定义路由和视图函数
def init_routes(app):
    @app.route('/api/SendCustomPacket', methods=['POST'])
    def send_packet():
        try:
            data = request.json
            iface = data.get('iface')
            packets = data.get('packet')

            for key, packet in packets.items():
                if packet == "":
                    continue
                send_packet_scapy_from_hex(iface, packet)
                sleep(0.3)

            return jsonify({
                "message": "Send packet successfully",
            }), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/api/Send3LayerPacket', methods=['POST'])
    def send_packet_3layer():
        try:
            data = request.json
            packets = data.get('packet')

            for key, packet in packets.items():
                if packet == "":
                    continue
                send_packet_scapy_from_hex_3layer(packet)
                sleep(0.3)

            return jsonify({
                "message": "Send packet successfully",
            }), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/api/GetCustomPacket', methods=['POST'])
    def get_packet():
        try:
            data = request.json
            dst_mac = data.get('dstMac')
            dst_ip = data.get('dstIp')
            dst_port = data.get('dstPort')
            src_mac = data.get('srcMac')
            src_ip = data.get('srcIp')
            src_port = data.get('srcPort')
            iface = data.get('iface')
            timestamp = data.get('timestamp')
            instruct = data.get('instruct')

            packet = get_packet_2layer(dst_mac, dst_ip, dst_port, src_mac, src_ip, src_port, iface, timestamp, instruct)

            return jsonify({
                "message": "Get traffic successfully",
                "result": [str(packet)]
            }), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/api/Get3LayerPacket', methods=['POST'])
    def get_3layer_packet():
        try:
            data = request.json
            dst_ip = data.get('dstIp')
            dst_port = data.get('dstPort')
            src_ip = data.get('srcIp')
            src_port = data.get('srcPort')
            timestamp = data.get('timestamp')
            instruct = data.get('instruct')

            packet = get_packet_3layer(dst_ip, dst_port, src_ip, src_port, timestamp, instruct)

            return jsonify({
                "message": "Get traffic successfully",
                "result": [str(packet)]
            }), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/api/GetLocalDevice', methods=['GET'])
    def get_local_device():
        try:
            result = []
            # 获取所有网络接口信息
            addrs = psutil.net_if_addrs()
            stats = psutil.net_if_stats()

            for interface, addresses in addrs.items():
                # 过滤无效接口（状态非UP或回环接口）
                if not stats[interface].isup or interface == 'Loopback Pseudo-Interface 1':
                    continue

                ipv4 = next((addr.address for addr in addresses if addr.family == socket.AF_INET), None)
                mac = next((addr.address for addr in addresses if addr.family == psutil.AF_LINK), '00:00:00:00:00:00')

                if ipv4:
                    result.append({
                        "name": interface,
                        "mac": mac.upper().replace('-', ':'),  # 统一MAC地址格式
                        "ipv4": ipv4,
                        "internal": False  # Windows下不精确判断内部接口
                    })

            return jsonify({
                "code": 200,
                "message": "Success",
                "result": result
            })
        except Exception as e:
            return jsonify({
                "code": 500,
                "message": "Failed to get network interfaces",
                "result": None
            }), 500


    @app.route('/api/StartHijack', methods=['POST'])
    def start_hijack():
        try:
            data = request.json
            dst_ip = data.get('dstIp')
            dst_port = data.get('dstPort')

            if not dst_ip or not dst_port:
                return jsonify({"error": "Missing deviceIp or dstPort"}), 400

            # 调用外部文件的处理逻辑
            result = throttle_start_hijack(dst_ip, dst_port)

            return jsonify({
                "message": "Hijack started successfully",
                "dstIp": dst_ip,
                "dstPort": dst_port,
                "result": result
            }), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/api/StopHijack', methods=['POST'])
    def stop_hijack():
        try:
            data = request.json
            dst_ip = data.get('dstIp')
            dst_port = data.get('dstPort')

            if not dst_ip or not dst_port:
                return jsonify({"error": "Missing deviceIp or dstPort"}), 400

            # 调用外部文件的处理逻辑
            result = throttle_stop_hijack(dst_ip, dst_port)

            return jsonify({
                "message": "Hijack started successfully",
                "dstIp": dst_ip,
                "dstPort": dst_port,
                "result": result
            }), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/api/FlyHijack', methods=['POST'])
    def fly_hijack():
        try:
            data = request.json
            dst_ip = data.get('dstIp')
            dst_port = data.get('dstPort')

            if not dst_ip or not dst_port:
                return jsonify({"error": "Missing deviceIp or dstPort"}), 400

            # 调用外部文件的处理逻辑
            result = uav_fly_hijack(dst_ip, dst_port)

            return jsonify({
                "message": "Hijack started successfully",
                "dstIp": dst_ip,
                "dstPort": dst_port,
                "result": result
            }), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/api/SwerveHijack', methods=['POST'])
    def swerve_hijack():
        try:
            data = request.json
            dst_ip = data.get('dstIp')
            dst_port = data.get('dstPort')

            if not dst_ip or not dst_port:
                return jsonify({"error": "Missing deviceIp or dstPort"}), 400

            # 调用外部文件的处理逻辑
            result = uav_swerve_hijack(dst_ip, dst_port)

            return jsonify({
                "message": "Hijack started successfully",
                "dstIp": dst_ip,
                "dstPort": dst_port,
                "result": result
            }), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500


    @app.route('/api/UdpFlood', methods=['POST'])
    def udp_flood_attack():
        try:
            data = request.json
            dst_ip = data.get('dstIp')
            dst_port = data.get('dstPort')
            attack_duration = data.get('attackDuration')

            if not dst_ip or not dst_port:
                return jsonify({"error": "Missing deviceIp or dstPort"}), 400

            # 调用外部文件的处理逻辑
            result = udp_flood(dst_ip, dst_port, attack_duration)

            return jsonify({
                "message": "Hijack started successfully",
                "dstIp": dst_ip,
                "dstPort": dst_port,
                "result": result
            }), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/api/TcpFlood', methods=['POST'])
    def tcp_flood_attack():
        try:
            data = request.json
            dst_ip = data.get('dstIp')
            dst_port = data.get('dstPort')
            attack_duration = data.get('attackDuration')

            if not dst_ip or not dst_port:
                return jsonify({"error": "Missing deviceIp or dstPort"}), 400

            # 调用外部文件的处理逻辑
            result = tcp_flood(dst_ip, dst_port, attack_duration)

            return jsonify({
                "message": "Hijack started successfully",
                "dstIp": dst_ip,
                "dstPort": dst_port,
                "result": result
            }), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500