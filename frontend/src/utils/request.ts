// src/utils/request.ts
// 全局请求定义文件
import axios from 'axios';
import type { InternalAxiosRequestConfig, AxiosResponse, AxiosError } from 'axios';
import type { ApiResponse } from './types'; // 导入定义的类型

const baseURL = import.meta.env.VITE_API_BASE_URL as string;  //后端api url

// 创建 axios 实例
const myAxios = axios.create({
  baseURL,
  timeout: 10000, // 请求超时时间
  headers: {
    'Content-Type': 'application/json',
  },
  withCredentials: false, //是否携带cookie
});

// 请求拦截器
myAxios.interceptors.request.use(
  function (config: InternalAxiosRequestConfig) {
    // 在发送请求之前做些什么，例如添加 token
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  function (error: AxiosError) {
    // 对请求错误做些什么
    return Promise.reject(error);
  }
);

// 响应拦截器
myAxios.interceptors.response.use(
  function (response: AxiosResponse) {
    // 对响应数据做些什么
    console.log(response.data);
    return response.data;
  },
  function (error: AxiosError) {
    // 对响应错误做些什么
    if (error.response) {
      switch (error.response.status) {
        case 401:
          // 处理未授权的情况
          break;
        case 404:
          // 处理未找到资源的情况
          break;
        case 500:
          // 处理服务器错误的情况
          break;
        default:
          // 处理其他错误
          break;
      }
    }
    return Promise.reject(error);
  }
);

export default myAxios;
