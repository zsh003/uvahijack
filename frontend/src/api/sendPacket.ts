// src/api/sendPacket.ts

import myAxios from '@/utils/request';
import type { ApiResponse, SendPacketParams } from '@/utils/types';

/**
 * 启动油门劫持
 * @param params 请求参数
 * @returns 响应数据
 */
export const sendPacket = async (params: SendPacketParams): Promise<ApiResponse<object>> => {
  try {  // 在.env中配置了接口的根地址
    return await myAxios.post<ApiResponse<object>>('/SendPacket', {
      packet: params.packet
    });
  } catch (error) {
    console.error('流量发送失败:', error);
    throw error; // 抛出错误
  }
};
