// src/api/getPacket.ts

import myAxios from '@/utils/request';
import type { ApiResponse, GetPacketParams } from '@/utils/types';

/**
 * 获取流量数据
 * @param params 请求参数
 * @returns 响应数据
 */
export const getPacket = async (params: GetPacketParams): Promise<ApiResponse<object>> => {
  try {  // 在.env中配置了接口的根地址
    return await myAxios.post<ApiResponse<object>>('/GetPacket', {
      dstMac: params.dstMac,
      dstIp: params.dstIp,
      dstPort: params.dstPort,
      srcMac: params.srcMac,
      srcIp: params.srcIp,
      srcPort: params.srcPort,
      trafficHex: params.trafficHex
    });
  } catch (error) {
    console.error('获取流量失败:', error);
    throw error; // 抛出错误
  }
};
