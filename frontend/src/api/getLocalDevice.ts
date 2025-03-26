import myAxios from '@/utils/request';
import type { ApiResponse, NetworkInterfaceInfo } from '@/utils/types';

export function getLocalDevice() {
  return myAxios.get<ApiResponse<NetworkInterfaceInfo[]>>('/GetLocalDevice');
}