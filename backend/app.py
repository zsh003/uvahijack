from flask import Flask, jsonify
from flask_cors import CORS

'''
.\.venv\Scripts\python.exe app.py
'''

# 创建 Flask 应用
app = Flask(__name__)

# 启用 CORS，允许跨域请求
CORS(app)

# 定义一个简单的 API 路由
@app.route('/api/hello', methods=['GET'])
def hello():
    """
    返回一个简单的 JSON 响应
    """
    return jsonify({"message": "Hello from Flask!"})

# 运行 Flask 应用
if __name__ == '__main__':
    app.run(debug=True)  # 调试模式，开发时使用