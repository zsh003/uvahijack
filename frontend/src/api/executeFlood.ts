// src/api/executeFlood.ts

import myAxios from '@/utils/request';
import type { ApiResponse, FloodAttackParams } from '@/utils/types';

/**
 * UDP泛洪攻击
 * @param params 请求参数
 * @returns 响应数据
 */
export const executeUdpFlood = async (params: FloodAttackParams): Promise<ApiResponse<object>> => {
  try {
    return await myAxios.post<ApiResponse<object>>('/UdpFlood', {
      dstIp: params.dstIp,
      dstPort: params.dstPort,
      attackDuration: params.attackDuration
    });
  } catch (error) {
    console.error('UDP泛洪攻击失败:', error);
    throw error;
  }
};

/**
 * TCP泛洪攻击
 * @param params 请求参数
 * @returns 响应数据
 */
export const executeTcpFlood = async (params: FloodAttackParams): Promise<ApiResponse<object>> => {
  try {
    return await myAxios.post<ApiResponse<object>>('/TcpFlood', {
      dstIp: params.dstIp,
      dstPort: params.dstPort,
      attackDuration: params.attackDuration
    });
  } catch (error) {
    console.error('TCP泛洪攻击失败:', error);
    throw error;
  }
};
