from flask import Flask
from flask_cors import CORS

def create_app():

    # 注册 Flask 应用
    app = Flask(__name__)

    # 启用 CORS，允许跨域请求(前后端运行端口不同)
    CORS(app)

    # 加载配置
    app.config.from_pyfile('../config.py')

    # 注册路由
    from .routes import init_routes
    init_routes(app)

    return app