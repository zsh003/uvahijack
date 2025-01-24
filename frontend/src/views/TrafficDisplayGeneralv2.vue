<template>
  <a-card title="按结构分布展示">
    <!-- 使用预格式化文本标签显示 HEX 数据 -->
    <pre class="hex-output">{{ formattedHex }}</pre>
  </a-card>
</template>

<script setup lang="ts">
import { computed } from 'vue';

// 假设你有一段 UDP 流量包的 HEX 字符串
const hexString = 'b83dfb5d7eef4cd577edadbd080045000074b4b440004011b26ec0a8a903c0a8a901c5e0226000604467ef0258000202000100000000f2000000140066148080808000020000000000000000000002990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000324b142d0000';

// 解析 UDP 流量包的结构
const parsePacket = ({hexString}:{hexString:string}) => {
  const annotations = [];

  // Ethernet II (14 bytes)
  annotations.push({ start: 0, end: 11, description: 'Ethernet II: Destination MAC' });
  annotations.push({ start: 12, end: 23, description: 'Ethernet II: Source MAC' });
  annotations.push({ start: 24, end: 27, description: 'Ethernet II: Type (IPv4)' });

  // IPv4 (20 bytes)
  annotations.push({ start: 28, end: 28, description: 'IPv4: Version' });
  annotations.push({ start: 29, end: 29, description: 'IPv4: Header Length' });
  annotations.push({ start: 30, end: 31, description: 'IPv4: Differentiated Services Field' });
  annotations.push({ start: 32, end: 35, description: 'IPv4: Total Length' });
  annotations.push({ start: 36, end: 39, description: 'IPv4: Identification' });
  annotations.push({ start: 40, end: 41, description: 'IPv4: Flags' });
  annotations.push({ start: 42, end: 43, description: 'IPv4: Fragment Offset' });
  annotations.push({ start: 44, end: 45, description: 'IPv4: Time to Live' });
  annotations.push({ start: 46, end: 47, description: 'IPv4: Protocol (UDP)' });
  annotations.push({ start: 48, end: 51, description: 'IPv4: Header Checksum' });
  annotations.push({ start: 52, end: 59, description: 'IPv4: Source Address' });
  annotations.push({ start: 60, end: 67, description: 'IPv4: Destination Address' });

  // UDP (8 bytes)
  annotations.push({ start: 68, end: 71, description: 'UDP: Source Port' });
  annotations.push({ start: 72, end: 75, description: 'UDP: Destination Port' });
  annotations.push({ start: 76, end: 79, description: 'UDP: Length' });
  annotations.push({ start: 80, end: 83, description: 'UDP: Checksum' });

  // Data (剩余部分)
  annotations.push({ start: 84, end: hexString.length - 1, description: 'UDP Payload' });

  return annotations;
};

// 将 HEX 字符串按每 16 个字节（32 个字符）分组并格式化
const formattedHex = computed(() => {
  const annotations = parsePacket({hexString});
  const chunkSize = 32; // 每 16 个字节为一组
  let output = '';

  // 遍历 HEX 字符串，按 chunkSize 分组
  for (let i = 0; i < hexString.length; i += chunkSize) {
    const chunk = hexString.slice(i, i + chunkSize);
    const offset = i.toString(16).toUpperCase().padStart(8, '0'); // 偏移量
    const hexValues = chunk.match(/.{1,2}/g)?.join(' ') || ''; // HEX 值

    // 查找当前行的注解
    const lineAnnotations = annotations
      .filter(anno => i <= anno.end && i + chunkSize > anno.start)
      .map(anno => {
        const start = Math.max(anno.start, i);
        const end = Math.min(anno.end, i + chunkSize - 1);
        return `${anno.description} (${start}-${end})`;
      })
      .join('; ');

    // 格式化输出
    output += `${offset}:  ${hexValues.padEnd(49)}  | ${lineAnnotations}\n`;
  }

  return output;
});
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
</style>
