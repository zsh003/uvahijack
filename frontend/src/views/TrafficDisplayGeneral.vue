<template>
  <!-- trafficHex1 的卡片和模态框 -->
  <a-card title="流量Hex展示" v-if="formattedHex1">
    <template #extra>
      <a-button type="primary" @click.prevent="showModal1">查看流量逐字节解析</a-button>
    </template>
    <pre class="hex-output">{{ formattedHex1 }}</pre>
  </a-card>

  <!-- trafficHex1 的模态框 -->
  <a-modal
    v-model:open="modalVisible1"
    width=97%
    @ok="handleOk"
    @cancel="handleCancel"
  >
    <a-row :gutter="[6, 0]">
      <a-col :span="11">
        <a-card title="流量Hex总览">
          <pre class="hex-output">{{ formattedHex1 }}</pre>
        </a-card>
        <TrafficDisplayGeneralv2/>
      </a-col>
      <a-col :span="13">
        <TrafficDisplay/>
      </a-col>
    </a-row>
  </a-modal>

  <!-- trafficHex2 的卡片和模态框 -->
  <a-card title="流量Hex展示" v-if="formattedHex2">
    <template #extra>
      <a-button type="primary" @click.prevent="showModal2">查看流量逐字节解析</a-button>
    </template>
    <pre class="hex-output">{{ formattedHex2 }}</pre>
  </a-card>

  <!-- trafficHex2 的模态框 -->
  <a-modal
    v-model:open="modalVisible2"
    width=97%
    @ok="handleOk"
    @cancel="handleCancel"
  >
    <a-row :gutter="[6, 0]">
      <a-col :span="11">
        <a-card title="流量Hex总览">
          <pre class="hex-output">{{ formattedHex2 }}</pre>
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
import { computed, ref } from 'vue';
import TrafficDisplay from '@/views/TrafficDisplay.vue';
import TrafficDisplayGeneralv2 from '@/views/TrafficDisplayGeneralv2.vue';
import { Modal } from 'ant-design-vue';
import { useTrafficHexStore } from '@/stores/useTrafficHexStore.ts';
import { useTrafficHexStore2 } from '@/stores/useTrafficHexStore2.ts';

// 模态框显示
const modalVisible1 = ref<boolean>(false);
const showModal1 = (): void => {
  modalVisible1.value = true;
};
const modalVisible2 = ref<boolean>(false);
const showModal2 = (): void => {
  modalVisible2.value = true;
};

const handleOk = (e: MouseEvent): void => {
  console.log('Clicked ok button', e);
};
const handleCancel = (e: MouseEvent): void => {
  console.log('Clicked cancel button', e);
};

// Hex字符串处理过程
const trafficHexStore = useTrafficHexStore();
const trafficHexStore2 = useTrafficHexStore2();
const trafficHex1 = computed(() => trafficHexStore.trafficHex);
const trafficHex2 = computed(() => trafficHexStore2.trafficHex2);

const formattedHex1 = computed(() => {
  const hexString = trafficHex1.value;
  if (!hexString) return '';

  const chunkSize = 32; // 每 16 个字节为一组
  return (
    hexString
      .match(new RegExp(`.{1,${chunkSize}}`, 'g'))
      ?.map((chunk, index) => {
        const offset = (index * 16).toString(16).toUpperCase().padStart(8, '0');
        const hexValues = chunk.match(/.{1,2}/g)?.join(' ') || '';
        const ascii =
          chunk
            .match(/.{1,2}/g)
            ?.map((byte) => {
              if (/^[0-9A-Fa-f]{2}$/.test(byte)) {
                const charCode = parseInt(byte, 16);
                return charCode >= 32 && charCode <= 126 ? String.fromCharCode(charCode) : '.';
              } else {
                return '.';
              }
            })
            .join('') || '';
        return `${offset}:  ${hexValues.padEnd(49)}  |${ascii}|`;
      })
      .join('\n') || ''
  );
});

const formattedHex2 = computed(() => {
  const hexString = trafficHex2.value;
  if (!hexString) return '';

  const chunkSize = 32; // 每 16 个字节为一组
  return (
    hexString
      .match(new RegExp(`.{1,${chunkSize}}`, 'g'))
      ?.map((chunk, index) => {
        const offset = (index * 16).toString(16).toUpperCase().padStart(8, '0');
        const hexValues = chunk.match(/.{1,2}/g)?.join(' ') || '';
        const ascii =
          chunk
            .match(/.{1,2}/g)
            ?.map((byte) => {
              if (/^[0-9A-Fa-f]{2}$/.test(byte)) {
                const charCode = parseInt(byte, 16);
                return charCode >= 32 && charCode <= 126 ? String.fromCharCode(charCode) : '.';
              } else {
                return '.';
              }
            })
            .join('') || '';
        return `${offset}:  ${hexValues.padEnd(49)}  |${ascii}|`;
      })
      .join('\n') || ''
  );
});
</script>

<style scoped>
.hex-output {
  font-family: monospace;
  white-space: pre-wrap;
  background-color: #f5f5f5;
  padding: 10px;
  border-radius: 4px;
  overflow-x: auto;
}
.a-row {
  height: 100%;
}
.a-col {
  height: 100%;
}
</style>
