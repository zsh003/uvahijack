# uvahijack
基于vue+flask前后端开发的无人机劫持系统，支持前后端分离开发。

前端使用vite+vue3，支持TypeScript，包含ESLint语法检查、Router-View路由支持、Pinia状态管理等。后端使用flask3开发，使用dotenv管理flask环境变量，启用CORS允许跨域请求，路由、配置分离管理。


配置环境：

python version: 3.11.9 

虚拟环境需要自己创建。我这里使用的PyCharm，

python路径如下：

```
.venv\Scripts\python.exe
```

启用后端：
```cmd
cd backend
pip install -r requirements.txt
..\.venv\Scripts\python.exe -m flask run
```
注：使用waitress模拟生产环境的话修改run.py：
```python
from waitress import serve
from app import create_app

app = create_app()

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
```
python run.py 即可让Flask应用通过waitress运行，适合测试生产环境的行为。

