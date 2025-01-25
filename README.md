# uvahijack
基于vue+flask前后端开发的无人机劫持系统，支持前后端分离开发。

前端使用vite+vue3，支持TypeScript，包含ESLint语法检查、router-view路由支持、Axios请求支持、Pinia状态管理等。
后端使用flask3开发，使用dotenv管理flask环境变量，启用CORS允许跨域请求，支持flask路由、配置分离管理。

- 前端使用 Ant Design Vue 组件库，提炼自企业级中后台产品的交互语言和视觉风格。详见其[官方文档](https://www.antdv.com/docs/vue/introduce-cn).
- 增加了 Axios 全局配置及请求封装，包含请求拦截器、响应拦截器、错误处理、请求方法封装等，使得 Axios 请求将更加模块化、易于维护，并且在遇到问题时能够快速定位和处理错误。
- 

启用前端：
```cmd
cd frontend
npm install
npm run dev
```
启用后端：
```cmd
# Python version: 3.11.9
cd backend
..\.venv\Scripts\python.exe -m pip install -r requirements.txt
..\.venv\Scripts\python.exe -m flask run
```
注：我使用Pycharm作为IDE，Python虚拟环境位于`..\.venv\Scripts\python.exe`，执行命令时注意自己的Python是否为当前虚拟环境的Python，根据实际情况调整。

若使用waitress模拟生产环境的话需要修改run.py：
```python
from waitress import serve
from app import create_app

app = create_app()

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
```
python run.py 即可让Flask应用通过waitress运行，用于测试生产环境。

