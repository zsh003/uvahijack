# 应用的入口文件，用于启动Flask应用

from app import create_app
from dotenv import load_dotenv
'''
cd backend
..\.venv\Scripts\python.exe -m python run.py
or
..\.venv\Scripts\python.exe -m flask run
'''


load_dotenv()  # dotenv管理环境变量，load加载.env文件
# FLASK_APP环境变量：指向你的应用入口文件
# FLASK_ENV环境变量：启用调试模式可以自动重启服务器并在浏览器中显示错误信息

app = create_app()

# 运行 Flask 应用
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # 调试模式，开发时使用