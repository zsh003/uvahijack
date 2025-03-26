from flask import request, jsonify
from time import sleep

from .services.hijack_service import throttle_start_hijack
from .services.hijack_service import throttle_stop_hijack
from .services.hijack_service import fly_hijack
from .services.hijack_service import swerve_hijack

from .services.get_packet_service import get_packet_2layer
from .services.get_packet_service import get_packet_3layer
from .services.get_packet_service import get_local_mac
from .services.send_packet_service import send_packet_scapy_from_hex
from .services.send_packet_service import send_packet_scapy_from_hex_3layer

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
            result = fly_hijack(dst_ip, dst_port)

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
            result = swerve_hijack(dst_ip, dst_port)

            return jsonify({
                "message": "Hijack started successfully",
                "dstIp": dst_ip,
                "dstPort": dst_port,
                "result": result
            }), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500