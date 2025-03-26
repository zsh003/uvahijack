<template>
  <div id="device-display" :style="{ padding: '24px 24px', backgroundColor: '#f0f2f5' }">
    <h3>WiFi连接情况</h3>
    <a-list item-layout="horizontal" :data-source="wifiData">
      <template #renderItem="{ item }">
        <a-list-item>
          <a-list-item-meta :description="item.description">
            <template #title>
              <a>{{ item.title }}</a>
            </template>
            <template #avatar>
              <a-avatar :src="item.avatar" />
            </template>
          </a-list-item-meta>
        </a-list-item>
      </template>
    </a-list>
    <h3>设备探测信息</h3>
    <a-list item-layout="horizontal" :data-source="deviceData">
      <template #renderItem="{ item }">
        <a-list-item :key="item.title">
          <a-list-item-meta :description="item.description">
            <template #title>
              <a>{{ item.title }}</a>
            </template>
            <template #avatar>
              <a-avatar :src="item.avatar" />
            </template>
          </a-list-item-meta>
        </a-list-item>
      </template>
    </a-list>
    <h3>地理位置信息</h3>
    <ul v-if="geoPosition">
      <li>纬度: {{ geoPosition.coords.latitude }}</li>
      <li>经度: {{ geoPosition.coords.longitude }}</li>
      <li>精度: {{ geoPosition.coords.accuracy }} 米</li>
      <li v-if="geoPosition.coords.altitude">高度: {{ geoPosition.coords.altitude }} 米</li>
      <li v-if="geoPosition.coords.speed">速度: {{ geoPosition.coords.speed }} 米/秒</li>
      <li v-if="geoPosition.coords.heading">方向: {{ geoPosition.coords.heading }} 度</li>
      <li>时间戳: {{ new Date(geoPosition.timestamp).toLocaleString() }}</li>
    </ul>
    <p v-else-if="geoError">{{ geoError.valueOf }}</p>
    <p v-else>正在获取地理位置信息...</p>

  </div>
</template>

<script setup lang="ts">
//内容中参数配置固定栏设置
import { ref } from 'vue';
import { getLocalDevice } from '@/api/getLocalDevice';
import type { NetworkInterfaceInfo } from '@/utils/types';

const deviceData = ref<Array<any>>([]);

interface DataItem {
  title: string;
  description?: string;
  avatar?: string;
}

/*
对于连接类型的检测，你可以使用 Network Information API，它提供了一个 navigator.connection 对象（有时也可能是 navigator.mozConnection 或 navigator.webkitConnection，取决于浏览器）。这个对象包含了一些关于网络连接的信息，例如：
effectiveType: 返回一个字符串，表示当前的有效连接类型（如 'slow-2g', '2g', '3g', '4g'）。
type: 返回一个字符串，表示当前的物理连接类型（如 'bluetooth', 'cellular', 'ethernet', 'none', 'wifi', 'wimax', 'other', 'unknown'）。
downlink: 下行速度的最大估计值，单位为 Mbps。
saveData: 用户是否启用了减少数据使用的选项。
*/
const connection = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
const wifiData = ref<DataItem[]>([
  {
    title: `有效连接类型： ${connection.effectiveType}网络`,
    description: `设备状态：${navigator.onLine ? '在线' : '离线'}， 下行速度的最大估计值： ${connection?.downlink+' Mbps' || '未知'}， 往返时延： ${connection?.rtt+' ms' || '未知'}， 是否设置节流： ${connection.saveData}`,
    avatar: 'https://joeschmoe.io/api/v1/random'
  }
]);
//监听网络状态的变化
connection.addEventListener('change', () => {
  console.log("Network type changed to: " + connection.effectiveType);
});


// 地理位置信息和错误信息
const geoPosition = ref<Geoposition | null>(null);
const geoError = ref<string | null>(null);

//WiFi情况更新代码
function updateNetworkStatus(event: Event) {
  const status = navigator.onLine ? '在线' : '离线';
  console.log(`当前状态：${status}`, event);
  // 更新数据或触发其他逻辑
}

/* 将 updateNetworkStatus 函数定义在 setup 函数内，并使用它作为事件监听器
* 使用了 onMounted 和 onBeforeUnmount 生命周期钩子来替代 mounted 和 beforeDestroy
* */
import { onMounted, onBeforeUnmount } from 'vue';
/* onMounted 钩子会在其他组件挂载均完成后再调用
onBeforeUnmount 钩子会在组件卸载之前被调用
*/
onMounted(async () => {
  //网络状态更新
  window.addEventListener('online', updateNetworkStatus);
  window.addEventListener('offline', updateNetworkStatus);

  try {
    const response = await getLocalDevice();  // 修改解构方式
    console.log('Response:', response);
    if (response.code === 200) {
      deviceData.value = response.result
        .filter((intf: NetworkInterfaceInfo) => intf.ipv4)
        .map((intf: NetworkInterfaceInfo) => ({
          title: intf.name,
          description: `MAC: ${intf.mac} | IPv4: ${intf.ipv4}`,
          avatar: undefined
        }));
    } else {
      console.error('接口异常:', response.message);
    }
  } catch (error) {
    console.error('请求失败:', error);
  }

  //地理位置信息
  if ('geolocation' in navigator) {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        geoPosition.value = position;
        geoError.value = null;
        //console.log("Latitude: " + position.coords.latitude);
        //console.log("Longitude: " + position.coords.longitude);
      },
      (error) => {
        geoError.value = error.message;
        geoPosition.value = null;
        //console.error("Error Code = " + error.code + " - " + error.message);
      },
      {
        enableHighAccuracy: true,
        timeout: 5000,
        maximumAge: 0
      }
    );
  } else {
    geoError.value = '浏览器不支持地理定位功能';
  }
});
onBeforeUnmount(() => {
  window.removeEventListener('online', updateNetworkStatus);
  window.removeEventListener('offline', updateNetworkStatus);
});

</script>

<style scoped>
/* 样式可以根据需要添加 */
</style>
