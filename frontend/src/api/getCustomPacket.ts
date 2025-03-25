// src/api/getCustomPacket.ts

import myAxios from '@/utils/request';
import type { ApiResponse, GetPacketParams } from '@/utils/types';

/**
 * 获取流量数据
 * @param params 请求参数
 * @returns 响应数据
 */
export const getCustomPacket = async (params: GetPacketParams): Promise<ApiResponse<object>> => {
  try {  // 在.env中配置了接口的根地址
    return await myAxios.post<ApiResponse<object>>('/GetCustomPacket', {
      dstMac: params.dstMac,
      dstIp: params.dstIp,
      dstPort: params.dstPort,
      srcMac: params.srcMac,
      srcIp: params.srcIp,
      srcPort: params.srcPort,
      iface: params.iface,
      timestamp: params.timestamp,
      instruct: params.instruct
    });
  } catch (error) {
    console.error('获取流量失败:', error);
    throw error; // 抛出错误
  }
};
