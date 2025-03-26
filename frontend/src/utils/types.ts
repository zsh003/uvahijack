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
 * 设备信息的请求参数
 */
export interface NetworkInterfaceInfo {
  name: string;       // 网卡名称
  mac: string;        // MAC地址
  ipv4?: string;      // IPv4地址
  ipv6?: string;      // IPv6地址
  internal: boolean;  // 是否内部接口
}

/**
 * 发送流量的请求参数
 */
export interface SendCustomPacketParams {
  iface: string;   // 网卡
  packet: object;  // 流量Hex字符串 {字符串1,字符串2,..}
}
export interface Send3LayerPacketParams {
  packet: object;  // 流量Hex字符串 {字符串1,字符串2,..}
}

/**
 * 劫持示例的请求参数
 */
export interface HijackParams {
  dstIp: string;        // 目标IP
  dstPort: number;      // 目标端口
}

/**
 * 泛洪攻击的请求参数
 */
export interface FloodAttackParams {
  dstIp: string;        // 目标IP
  dstPort: number;      // 目标端口
  attackDuration: number;  // 持续时间
}

/**
 * 获取流量的请求参数
 */
export interface GetCustomPacketParams {
  dstMac: string;       // 目标MAC地址
  dstIp: string;        // 目标IP
  dstPort: number;      // 目标端口
  srcMac: string;       // 源MAC地址
  srcIp: string;        // 源IP
  srcPort: number;      // 源端口
  iface: string;        // 网卡
  timestamp: string;    // 时间戳
  instruct: string;     // 指令
}

export interface Get3LayerPacketParams {
  dstIp: string;        // 目标IP
  dstPort: number;      // 目标端口
  srcIp: string;        // 源IP
  srcPort: number;      // 源端口
  timestamp: string;    // 时间戳
  instruct: string;     // 指令
}
