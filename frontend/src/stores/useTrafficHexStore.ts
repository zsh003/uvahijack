import { defineStore } from "pinia"
import { ref } from "vue"

export const useTrafficHexStore = defineStore('trafficHex', () => {
  const trafficHex = ref<string>('')
  // 设置流量内容
  function setTrafficHex(newTrafficHex: string) {
    trafficHex.value = newTrafficHex;
  }

  return { trafficHex, setTrafficHex }
})
