<template>
  <div id="app">
    <BasicLayout />
  </div>
</template>

<script setup lang="ts">
import BasicLayout from '@/layouts/BasicLayout.vue'

// python代码高亮用
import 'prismjs';
import 'prismjs/components/prism-python'; // 引入Python语法支持
import 'prismjs/themes/prism.css';

import { useTrafficHexStore } from '@/stores/useTrafficHexStore.ts'
const trafficHexStore = useTrafficHexStore();

</script>

<style>

</style>
