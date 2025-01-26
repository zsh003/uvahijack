import { defineStore } from "pinia"
import { ref } from "vue"

export const useTrafficHexStore2 = defineStore('trafficHex2', () => {
  const trafficHex2 = ref<string>('')
  // 设置流量内容
  function setTrafficHex2(newTrafficHex: string) {
    trafficHex2.value = newTrafficHex;
  }

  return { trafficHex2, setTrafficHex2 }
})
