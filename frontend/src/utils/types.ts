// src/utils/types.ts


/**
 * 通用 API 响应结构
 */
export interface ApiResponse<T> {
  data: T;
  status: number;
  statusText: string;
}

/**
 * 发送流量的请求参数
 */
export interface SendPacketParams {
  iface: string;   // 网卡
  packet: object;  // 流量Hex字符串 {字符串1,字符串2,..}
}

/**
 * 启动劫持接口的请求参数
 */
export interface StartHijackParams {
  deviceIp: string; // 设备 IP
  port: number; // 端口号
  trafficHex: object;  // 流量Hex字符串 {字符串1,字符串2,..}
}

/**
 * 获取流量的请求参数
 */
export interface GetPacketParams {
  dstMac: string;       // 目标MAC地址
  dstIp: string;        // 目标IP
  dstPort: number;      // 目标端口
  srcMac: string;       // 源MAC地址
  srcIp: string;        // 源IP
  srcPort: number;      // 源端口
  iface: string;        // 网卡
  timestamp: string;    // 时间戳
  instruct: object;     // 指令
}
