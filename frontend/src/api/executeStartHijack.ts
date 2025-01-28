// src/api/executeStartHijack.ts

import myAxios from '@/utils/request';
import type { ApiResponse, StartHijackParams } from '@/utils/types';

/**
 * 启动油门劫持
 * @param params 请求参数
 * @returns 响应数据
 */
export const executeStartHijack = async (params: StartHijackParams): Promise<ApiResponse<object>> => {
  try {  // 在.env中配置了接口的根地址
    return await myAxios.post<ApiResponse<object>>('/StartHijack', {
      deviceIp: params.deviceIp,
      port: params.port,
      trafficHex: params.trafficHex
    });
  } catch (error) {
    console.error('启动油门劫持失败:', error);
    throw error; // 抛出错误
  }
};
