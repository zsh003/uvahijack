// src/utils/request.ts
// 全局请求定义文件
import axios from 'axios';
import type { AxiosInstance, InternalAxiosRequestConfig, AxiosResponse, AxiosError } from 'axios';
import type { ApiResponse } from './types'; // 导入定义的类型

// 创建 AxiosRequest 类
class AxiosRequest {
  private axiosInstance: AxiosInstance = axios.create({
    baseURL: import.meta.env.VITE_API_BASE_URL,  //后端api url
    timeout: 5000, // 请求超时时间
    headers: {
      'Content-Type': 'application/json',
    },
    withCredentials: false, //是否携带cookie
  });
  constructor() {
    // 请求拦截器
    this.axiosInstance.interceptors.request.use(
      function(config: InternalAxiosRequestConfig) {
        // 在发送请求之前做些什么，例如添加 token
        const token = localStorage.getItem('token');
        if (token) {
          config.headers.Authorization = `Bearer ${token}`;
        }
        console.log("请求发送成功：", config);
        return config;
      },
      function(error: AxiosError) {
        // 对请求错误做些什么
        return Promise.reject(error);
      }
    );

    // 响应拦截器
    this.axiosInstance.interceptors.response.use(   //使用了自定义的Api通用数据结构
      function(response: AxiosResponse<ApiResponse<object>>) {
        // 对响应数据做些什么
        const { data, status, statusText } = response;
        if (status === 401) {
          return Promise.reject(new Error(statusText || '未知错误'));
        }
        console.log("成功接收响应：", response);

        return response;
      },
      function(error: AxiosError) {
        // 统一错误处理
        let errorMessage;
        if (error.response) {
          errorMessage = error.response.statusText || '服务器异常';
        } else if (error.request) {
          errorMessage = '网络异常';
        } else {
          errorMessage = error.message;
        }
        return Promise.reject(new Error(errorMessage));
      }
    );
  }

  // 封装请求
  /**
   * GET 请求
   * @param url 请求地址
   * @param config 请求配置
   * @returns 响应数据
   */
  public get <T>(url: string, config?: InternalAxiosRequestConfig): Promise<ApiResponse<T>> {
    return this.axiosInstance
      .get<ApiResponse<T>>(url, config)
      .then(response => response.data);
  }

  /**
   * POST 请求
   * @param url 请求地址
   * @param data 请求体数据
   * @param config 请求配置
   * @returns 响应数据
   */
  public post<T>(url: string, data?: unknown, config?: InternalAxiosRequestConfig): Promise<ApiResponse<T>> {
    return this.axiosInstance
      .post<ApiResponse<T>>(url, data, config)
      .then(response => response.data);
  }

  /**
   * PUT 请求
   * @param url 请求地址
   * @param data 请求体数据
   * @param config 请求配置
   * @returns 响应数据
   */
  public put<T>(url: string, data?: unknown, config?: InternalAxiosRequestConfig): Promise<ApiResponse<T>> {
    return this.axiosInstance
      .put<ApiResponse<T>>(url, data, config)
      .then(response => response.data);
  }

  /**
   * DELETE 请求
   * @param url 请求地址
   * @param config 请求配置
   * @returns 响应数据
   */
  public delete<T>(url: string, config?: InternalAxiosRequestConfig): Promise<ApiResponse<T>> {
    return this.axiosInstance
      .delete<ApiResponse<T>>(url, config)
      .then((response) => response.data);
  }
}

// 创建一个 myAxios 实例
const myAxios = new AxiosRequest();
export default myAxios;
