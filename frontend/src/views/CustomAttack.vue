<template>
  <div id="CustomAttack" :style="{ padding: '24px 0' }">
    <a-form layout="horizontal">
      <a-form-item label="IP 地址">
        <a-input v-model:value="ipAddress" placeholder="请输入 IP 地址"/>
      </a-form-item>
      <a-form-item label="MAC 地址">
        <a-input v-model:value="macAddress" placeholder="请输入 MAC 地址"/>
      </a-form-item>
    </a-form>

    <TheWelcome />
  </div>
</template>

<script setup lang="ts">
import TheWelcome from '../components/TheWelcome.vue'

import { ref, watch } from 'vue';
const ipAddress = ref<string[]>([''])
const macAddress = ref<string[]>([''])
watch(ipAddress, () => {
  console.log(ipAddress.value);
});
watch(macAddress, () => {
  console.log(macAddress.value);
});
</script>
