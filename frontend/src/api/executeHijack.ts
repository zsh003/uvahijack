// src/api/executeHijack.ts

import myAxios from '@/utils/request';
import type { ApiResponse, HijackParams } from '@/utils/types';

/**
 * 各种劫持攻击
 * @param params 请求参数
 * @returns 响应数据
 */
export const executeStartHijack = async (params: HijackParams): Promise<ApiResponse<object>> => {
  try {
    return await myAxios.post<ApiResponse<object>>('/StartHijack', {
      dstIp: params.dstIp,
      dstPort: params.dstPort
    });
  } catch (error) {
    console.error('油门启动劫持失败:', error);
    throw error; // 抛出错误
  }
};

export const executeStopHijack = async (params: HijackParams): Promise<ApiResponse<object>> => {
  try {
    return await myAxios.post<ApiResponse<object>>('/StopHijack', {
      dstIp: params.dstIp,
      dstPort: params.dstPort
    });
  } catch (error) {
    console.error('油门关闭劫持失败:', error);
    throw error; // 抛出错误
  }
};
export const executeFlyHijack = async (params: HijackParams): Promise<ApiResponse<object>> => {
  try {
    return await myAxios.post<ApiResponse<object>>('/FlyHijack', {
      dstIp: params.dstIp,
      dstPort: params.dstPort
    });
  } catch (error) {
    console.error('起飞劫持失败:', error);
    throw error; // 抛出错误
  }
};
export const executeSwerveHijack = async (params: HijackParams): Promise<ApiResponse<object>> => {
  try {
    return await myAxios.post<ApiResponse<object>>('/SwerveHijack', {
      dstIp: params.dstIp,
      dstPort: params.dstPort
    });
  } catch (error) {
    console.error('转向劫持失败:', error);
    throw error; // 抛出错误
  }
};
