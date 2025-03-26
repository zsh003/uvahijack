from flask import request, jsonify
from .services.hijack_service import throttle_start_hijack
from .services.hijack_service import throttle_stop_hijack
from .services.get_packet_service import get_packet_raw
from .services.get_packet_service import get_local_mac
from .services.send_packet_service import send_packet_scapy_from_hex

# 定义路由和视图函数
def init_routes(app):
    @app.route('/api/SendCustomPacket', methods=['POST'])
    def send_packet():
        #try:
        data = request.json
        iface = data.get('iface')
        packets = data.get('packet')

        for key, packet in packets.items():
            if packet == "":
                continue
            print(packet)
            send_packet_scapy_from_hex(iface, packet)

        return jsonify({
            "message": "Send packet successfully",
        }), 200

        # except Exception as e:
        #     return jsonify({"error": str(e)}), 500

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
            print(instruct)

            packet = get_packet_raw(dst_mac, dst_ip, dst_port, src_mac, src_ip, src_port, iface, timestamp, instruct)

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
            device_ip = data.get('deviceIp')
            port = data.get('port')
            trafficHex = data.get('trafficHex')

            if not device_ip or not port:
                return jsonify({"error": "Missing deviceIp or port"}), 400

            # 调用外部文件的处理逻辑
            result = throttle_start_hijack(device_ip, port)

            # result = {}
            # for key, payload in payloads.items():
            #     packet = get_packet_raw(dst_mac, dst_ip, dst_port, src_mac, src_ip, src_port, iface, timestamp,
            #                             instruct)
            #     result[key] = packet
            #
            # return jsonify({
            #     "message": "Get traffic successfully",
            #     "result": result
            # }), 200

            return jsonify({
                "message": "Hijack started successfully",
                "deviceIp": device_ip,
                "port": port,
                "trafficHex": trafficHex,
                "result": result
            }), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/api/StopHijack', methods=['POST'])
    def stop_hijack():
        try:
            data = request.json
            device_ip = data.get('deviceIp')
            port = data.get('port')
            trafficHex = data.get('trafficHex')

            if not device_ip or not port:
                return jsonify({"error": "Missing deviceIp or port"}), 400

            # 调用外部文件的处理逻辑
            result = throttle_stop_hijack(device_ip, port)

            return jsonify({
                "message": "Hijack started successfully",
                "deviceIp": device_ip,
                "port": port,
                "trafficHex": trafficHex,
                "result": result
            }), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500