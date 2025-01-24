from flask import request, jsonify
from .services.hijack_service import perform_hijack

# 定义路由和视图函数
def init_routes(app):
    @app.route('/api/StartHijack', methods=['POST'])
    def start_hijack():
        try:
            data = request.json
            device_ip = data.get('deviceIp')
            port = data.get('port')

            if not device_ip or not port:
                return jsonify({"error": "Missing deviceIp or port"}), 400

            # 调用外部文件的处理逻辑
            result = perform_hijack(device_ip, port)

            return jsonify({
                "message": "Hijack started successfully",
                "deviceIp": device_ip,
                "port": port,
                "result": result
            }), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500