<template>
  <a-card title="流量Hex展示">
    <template #extra>
      <a-button type="primary" @click.prevent="showModal">查看流量逐字节解析</a-button>
    </template>
    <!-- 使用预格式化文本标签显示 HEX 数据 -->
    <pre class="hex-output">{{ formattedHex }}</pre>

  </a-card>

  <!-- 模态框 -->
  <a-modal
    v-model:open="modalVisible"
    width=97%
    @ok="handleOk"
    @cancel="handleCancel"
  >
    <!-- 双栏布局   -->
    <a-row :gutter="[6, 0]"> <!-- gutter 设置列之间的间距 -->
      <a-col :span="11">
        <a-card title="流量Hex总览">
          <pre class="hex-output">{{ formattedHex }}</pre>
        </a-card>
        <TrafficDisplayGeneralv2/>
      </a-col>
      <a-col :span="13">
        <TrafficDisplay/>
      </a-col>
    </a-row>

  </a-modal>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import TrafficDisplay from '@/views/TrafficDisplay.vue'
import TrafficDisplayGeneralv2 from '@/views/TrafficDisplayGeneralv2.vue'

import { ref } from 'vue';
import { Modal } from 'ant-design-vue';

// 模态框显示
// 定义模态框可见性状态
const modalVisible = ref<boolean>(false);
// 显示模态框的方法
const showModal = (): void => {
  modalVisible.value = true;
};
// 点击确认按钮后的处理方法
const handleOk = (e: MouseEvent): void => {
  console.log('Clicked ok button', e);
  modalVisible.value = false;
};
// 点击取消按钮后的处理方法
const handleCancel = (e: MouseEvent): void => {
  console.log('Clicked cancel button', e);
  modalVisible.value = false;
};



// Hex字符串处理过程
const hexString =
  'b83dfb5d7eef4cd577edadbd080045000074b4b440004011b26ec0a8a903c0a8a901c5e0226000604467ef0258000202000100000000f2000000140066148080808000020000000000000000000002990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000324b142d0000'

// 将 HEX 字符串按每 16 个字节（32 个字符）分组并格式化
const formattedHex = computed(() => {
  const chunkSize = 32 // 每 16 个字节为一组
  return (
    hexString
      .match(new RegExp(`.{1,${chunkSize}}`, 'g')) // 按 chunkSize 分组
      ?.map((chunk, index) => {
        // 计算偏移量（地址）
        const offset = (index * 16).toString(16).toUpperCase().padStart(8, '0')
        // 将每两个字符（一个字节）用空格分隔
        const hexValues = chunk.match(/.{1,2}/g)?.join(' ') || ''
        // 将 HEX 转换为 ASCII 字符
        const ascii =
          chunk
            .match(/.{1,2}/g)
            ?.map((byte) => {
              // 检查是否为有效的 HEX 字节
              if (/^[0-9A-Fa-f]{2}$/.test(byte)) {
                const charCode = parseInt(byte, 16)
                // 只显示可打印字符（32-126），否则用 '.' 替代
                return charCode >= 32 && charCode <= 126 ? String.fromCharCode(charCode) : '.'
              } else {
                return '.' // 非 HEX 字节用 '.' 替代
              }
            })
            .join('') || ''
        // 返回带偏移量和 ASCII 的格式化字符串
        return `${offset}:  ${hexValues.padEnd(49)}  |${ascii}|`
      })
      .join('\n') || ''
  ) // 每组换行
})
</script>

<style scoped>
.hex-output {
  font-family: monospace; /* 使用等宽字体 */
  white-space: pre-wrap; /* 保留空格和换行 */
  background-color: #f5f5f5; /* 背景色 */
  padding: 10px; /* 内边距 */
  border-radius: 4px; /* 圆角 */
  overflow-x: auto; /* 如果内容超出宽度则允许水平滚动 */
}
.a-row {
  height: 100%; /* 如果需要确保行的高度占满整个模态框 */
}
.a-col {
  height: 100%;
}
</style>
