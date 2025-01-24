# 应用的入口文件，用于启动Flask应用

from app import create_app
from dotenv import load_dotenv
'''
cd backend
..\.venv\Scripts\python.exe -m flask run
or
..\.venv\Scripts\python.exe run.py # 此方法需要修改 app.run(host='0.0.0.0', port=5000, debug=True)
'''


load_dotenv()
'''
dotenv管理环境变量，load加载.env文件
FLASK_APP环境变量：指向你的应用入口文件
FLASK_DEBUG环境变量：启用调试模式，等同于python run.py方法中，下面app.run(debug=True)
FLASK_RUN_HOST, FLASK_RUN_PORT：指定主机和端口
'''

app = create_app()

if __name__ == '__main__':
    app.run()