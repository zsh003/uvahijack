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
import { ref, onMounted, reactive } from 'vue';
import TrafficDisplayGeneral from '@/views/TrafficDisplayGeneral.vue'
import axios from 'axios'; // 使用 Axios 发送 HTTP 请求

const formLayout = 'vertical'; // 设置表单布局

// 定义初始值对象
const defaultValues = {
  deviceIp: '192.168.169.1', // 设备 IP 的初始值
  port: '8800'             // 端口的初始值
};
// 创建一个对象来存储表单的状态
const formState = reactive({
  deviceIp: '',
  port: ''
});

// 创建一个方法来重置表单状态为初始值
const resetToDefaults = () => {
  Object.assign(formState, defaultValues);
};

const pythonCode = ref( `import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # 创建原始套接字
sock.sendto(traffic1, (dst_ip, dst_port)) # 发送恶意流量包
sock.sendto(traffic2, (dst_ip, dst_port))
sock.close() # 关闭套接字
`);
onMounted(() => {
  // 这里爆红不用管，放在onMounted里面可以保证其他组件加载完毕后 再引入prism进行代码高亮
  import('prismjs').then(prism => prism.highlightAll());
});

// 处理按钮点击事件的方法
const isLoading = ref(false);  // 按钮的状态
const handleClick = async () => {
  try {
    // 设置按钮加载状态为 true
    isLoading.value = true;

    // 发送 POST 请求到 Flask 后端
    const response = await axios.post('http://localhost:5000/api/endpoint', {
      deviceIp: formState.deviceIp,
      port: formState.port
    });

    // 根据后端返回的数据执行相应操作
    console.log(response.data);

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
