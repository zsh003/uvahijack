<template>
  <a-card title="流量逐字节解析">
    <!-- 使用预格式化文本标签显示 HEX 数据 -->
    <pre class="hex-output">
      <div v-for="(line, index) in formattedHex" :key="index" class="hex-line">
        <span class="hex-offset">{{ line.offset }}</span>
        <span class="hex-values">
          <span
            v-for="(value, i) in line.hexValues"
            :key="i"
            :class="`hex-value ${value.color}`"
          >
            {{ value.text }}
          </span>
        </span>
        <span class="hex-annotations">
          <span
            v-for="(anno, j) in line.annotations"
            :key="j"
            :class="`hex-annotation ${anno.color}`"
          >
            {{ anno.text }}
          </span>
        </span>
      </div>
    </pre>
  </a-card>
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps<{
  hexString: string
}>()

// 定义颜色映射
const colorMap = {
  ethernetDest: 'color-ethernet-dest',
  ethernetSrc: 'color-ethernet-src',
  ethernetType: 'color-ethernet-type',
  ipv4Version: 'color-ipv4-version',
  ipv4HeaderLength: 'color-ipv4-header-length',
  ipv4Dscp: 'color-ipv4-dscp',
  ipv4TotalLength: 'color-ipv4-total-length',
  ipv4Identification: 'color-ipv4-identification',
  ipv4Flags: 'color-ipv4-flags',
  ipv4FragmentOffset: 'color-ipv4-fragment-offset',
  ipv4Ttl: 'color-ipv4-ttl',
  ipv4Protocol: 'color-ipv4-protocol',
  ipv4Checksum: 'color-ipv4-checksum',
  ipv4SourceAddress: 'color-ipv4-source-address',
  ipv4DestinationAddress: 'color-ipv4-destination-address',
  udpSourcePort: 'color-udp-source-port',
  udpDestinationPort: 'color-udp-destination-port',
  udpLength: 'color-udp-length',
  udpChecksum: 'color-udp-checksum',
  udpPayload: 'color-udp-payload',
}

// 解析 UDP 流量包的结构
const parsePacket = ({ hexString }: { hexString: string }) => {
  const annotations = []

  // Ethernet II (14 bytes)
  annotations.push({
    start: 0,
    end: 11,
    description: 'Ethernet II: Destination MAC',
    color: colorMap.ethernetDest,
  })
  annotations.push({
    start: 12,
    end: 23,
    description: 'Ethernet II: Source MAC',
    color: colorMap.ethernetSrc,
  })
  annotations.push({
    start: 24,
    end: 27,
    description: 'Ethernet II: Type (IPv4)',
    color: colorMap.ethernetType,
  })

  // IPv4 (20 bytes)
  annotations.push({
    start: 28,
    end: 28,
    description: 'IPv4: Version',
    color: colorMap.ipv4Version,
  })
  annotations.push({
    start: 29,
    end: 29,
    description: 'IPv4: Header Length',
    color: colorMap.ipv4HeaderLength,
  })
  annotations.push({
    start: 30,
    end: 31,
    description: 'IPv4: Differentiated Services Field',
    color: colorMap.ipv4Dscp,
  })
  annotations.push({
    start: 32,
    end: 35,
    description: 'IPv4: Total Length',
    color: colorMap.ipv4TotalLength,
  })
  annotations.push({
    start: 36,
    end: 39,
    description: 'IPv4: Identification',
    color: colorMap.ipv4Identification,
  })
  annotations.push({ start: 40, end: 41, description: 'IPv4: Flags', color: colorMap.ipv4Flags })
  annotations.push({
    start: 42,
    end: 43,
    description: 'IPv4: Fragment Offset',
    color: colorMap.ipv4FragmentOffset,
  })
  annotations.push({
    start: 44,
    end: 45,
    description: 'IPv4: Time to Live',
    color: colorMap.ipv4Ttl,
  })
  annotations.push({
    start: 46,
    end: 47,
    description: 'IPv4: Protocol (UDP)',
    color: colorMap.ipv4Protocol,
  })
  annotations.push({
    start: 48,
    end: 51,
    description: 'IPv4: Header Checksum',
    color: colorMap.ipv4Checksum,
  })
  annotations.push({
    start: 52,
    end: 59,
    description: 'IPv4: Source Address',
    color: colorMap.ipv4SourceAddress,
  })
  annotations.push({
    start: 60,
    end: 67,
    description: 'IPv4: Destination Address',
    color: colorMap.ipv4DestinationAddress,
  })

  // UDP (8 bytes)
  annotations.push({
    start: 68,
    end: 71,
    description: 'UDP: Source Port',
    color: colorMap.udpSourcePort,
  })
  annotations.push({
    start: 72,
    end: 75,
    description: 'UDP: Destination Port',
    color: colorMap.udpDestinationPort,
  })
  annotations.push({ start: 76, end: 79, description: 'UDP: Length', color: colorMap.udpLength })
  annotations.push({
    start: 80,
    end: 83,
    description: 'UDP: Checksum',
    color: colorMap.udpChecksum,
  })

  // Data (剩余部分)
  annotations.push({
    start: 84,
    end: hexString.length - 1,
    description: 'UDP Payload',
    color: colorMap.udpPayload,
  })

  return annotations
}

// 将 HEX 字符串按每 16 个字节（32 个字符）分组并格式化
const formattedHex = computed(() => {
  const hexString = props.hexString
  const annotations = parsePacket({ hexString })
  const chunkSize = 32 // 每 16 个字节为一组
  const lines = []

  for (let i = 0; i < hexString.length; i += chunkSize) {
    const chunk = hexString.slice(i, i + chunkSize)
    const offset = i.toString(32).toUpperCase().padStart(8, '0') // 偏移量

    // 处理 HEX 值
    const hexValues = []
    let currentColor = null
    let currentValue = ''
    for (let j = 0; j < chunk.length; j += 2) {
      const byteStart = i + j
      const byteEnd = i + j + 1
      const byteValue = chunk.slice(j, j + 2)

      // 查找当前字节的注解
      const annotation = annotations.find((anno) => byteStart >= anno.start && byteEnd <= anno.end)
      const color = annotation ? annotation.color : ''

      //hexValues.push({ text: byteValue, color });
      if (color !== currentColor) {
        // 如果颜色变化了（或者这是第一个字节），则推入之前收集的字节（如果有）
        if (currentValue) {
          hexValues.push({ text: currentValue, color: currentColor })
        }
        // 开始新的颜色分组
        currentValue = byteValue
        currentColor = color
      } else {
        // 如果颜色没有变化，继续添加到当前值
        currentValue += byteValue
      }
    }
    // 推入最后一组字节
    if (currentValue) {
      hexValues.push({ text: currentValue, color: currentColor })
    }

    // 处理注解
    const lineAnnotations = annotations
      .filter((anno) => i <= anno.end && i + chunkSize > anno.start)
      .map((anno) => ({
        text: `${anno.description} (${anno.start}-${anno.end})`,
        color: anno.color,
      }))

    lines.push({
      offset,
      hexValues,
      annotations: lineAnnotations,
    })
  }

  return lines
})
console.log({
  formattedHex,
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

.hex-line {
  display: flex;
  align-items: flex-start;
  margin-bottom: 8px;
}

.hex-offset {
  color: #666;
  margin-right: 10px;
}

.hex-values {
  display: inline-block;
  margin-right: 20px;
}

.hex-value {
  margin-right: 4px;
}

.hex-annotations {
  flex-grow: 1;
}

/* 颜色定义 */
.color-ethernet-dest {
  color: #ff6347;
} /* Tomato */
.color-ethernet-src {
  color: #4682b4;
} /* SteelBlue */
.color-ethernet-type {
  color: #32cd32;
} /* LimeGreen */
.color-ipv4-version {
  color: #ff4500;
} /* OrangeRed */
.color-ipv4-header-length {
  color: #8a2be2;
} /* BlueViolet */
.color-ipv4-dscp {
  color: #dc143c;
} /* Crimson */
.color-ipv4-total-length {
  color: #20b2aa;
} /* LightSeaGreen */
.color-ipv4-identification {
  color: #ff8c00;
} /* DarkOrange */
.color-ipv4-flags {
  color: #9932cc;
} /* DarkOrchid */
.color-ipv4-fragment-offset {
  color: #00ced1;
} /* DarkTurquoise */
.color-ipv4-ttl {
  color: #ff1493;
} /* DeepPink */
.color-ipv4-protocol {
  color: #00bfff;
} /* DeepSkyBlue */
.color-ipv4-checksum {
  color: #ff69b4;
} /* HotPink */
.color-ipv4-source-address {
  color: #7b68ee;
} /* MediumSlateBlue */
.color-ipv4-destination-address {
  color: #ba55d3;
} /* MediumOrchid */
.color-udp-source-port {
  color: #3cb371;
} /* MediumSeaGreen */
.color-udp-destination-port {
  color: #dda0dd;
} /* Plum */
.color-udp-length {
  color: #ffa07a;
} /* LightSalmon */
.color-udp-checksum {
  color: #87cefa;
} /* LightSkyBlue */
.color-udp-payload {
  color: #778899;
} /* LightSlateGray */
</style>
