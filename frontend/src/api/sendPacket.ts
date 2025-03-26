// src/api/sendCustomPacket.ts

import myAxios from '@/utils/request';
import type { ApiResponse, SendCustomPacketParams, Send3LayerPacketParams } from '@/utils/types';

/**
 * 自定义流量发送
 * @param params 请求参数
 * @returns 响应数据
 */
export const sendCustomPacket = async (params: SendCustomPacketParams): Promise<ApiResponse<object>> => {
  try {  // 在.env中配置了接口的根地址
    return await myAxios.post<ApiResponse<object>>('/SendCustomPacket', {
      iface: params.iface,
      packet: params.packet
    });
  } catch (error) {
    console.error('流量发送失败:', error);
    throw error; // 抛出错误
  }
};

/**
 * 自定义流量发送
 * @param params 请求参数
 * @returns 响应数据
 */
export const send3LayerPacket = async (params: Send3LayerPacketParams): Promise<ApiResponse<object>> => {
  try {  // 在.env中配置了接口的根地址
    return await myAxios.post<ApiResponse<object>>('/Send3LayerPacket', {
      packet: params.packet
    });
  } catch (error) {
    console.error('流量发送失败:', error);
    throw error; // 抛出错误
  }
};
