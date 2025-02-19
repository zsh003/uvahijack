# uvahijack
基于vue+flask前后端开发的无人机劫持系统，支持前后端分离开发。

前端使用vite+vue3，支持TypeScript，包含ESLint语法检查、router-view路由支持、Axios请求支持、Pinia状态管理等。
后端使用flask3开发，使用dotenv管理flask环境变量，启用CORS允许跨域请求，支持flask路由、配置分离管理。

- 前端使用 Ant Design Vue 组件库，提炼自企业级中后台产品的交互语言和视觉风格。详见其[官方文档](https://www.antdv.com/docs/vue/introduce-cn).
- 增加了 Axios 全局配置及请求封装，包含请求拦截器、响应拦截器、错误处理、请求方法封装等，使得 Axios 请求将更加模块化、易于维护，并且在遇到问题时能够快速定位和处理错误。详见其[官方文档](https://www.axios-http.cn/docs/intro).
- 增加了 Pinia 全局状态管理，使用组合式 API 风格跨组件或页面共享状态，详见其[官方文档](https://pinia.vuejs.org/zh/introduction.html).

启用前端：
```cmd
# Node.js version: v22.12.0
# npm version: 10.9.0
# https://mirrors.aliyun.com/nodejs-release/v22.12.0/
cd frontend
npm install
npm run dev
```
启用后端：
```cmd
# Python version: 3.11.9
# https://www.python.org/downloads/release/python-3119/
cd backend
..\.venv\Scripts\python.exe -m pip install -r requirements.txt
..\.venv\Scripts\python.exe -m flask run
```
注：我使用Pycharm作为IDE，通过本地Python创建虚拟环境，虚拟环境路径位于`..\.venv\Scripts\python.exe`，执行命令时注意自己的Python是否为当前虚拟环境的Python，根据实际情况调整。

若使用Linux操作系统，创建虚拟环境后执行`../.venv/Script/activate`即可激活虚拟环境，无需在命令中再指定python路径。

