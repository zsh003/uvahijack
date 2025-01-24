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
import 'prismjs/themes/prism.css'; // 引入样式
</script>

<style>

</style>
