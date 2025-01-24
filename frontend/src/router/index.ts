import { createRouter, createWebHistory } from 'vue-router'
import TransAttack from '@/views/TransAttack.vue'
import CustomAttack from '@/views/CustomAttack.vue'
import DeviceDisplay from '@/views/DeviceDisplay.vue'
import StartHijack from '@/views/StartHijack.vue'
import StopHijack from '@/views/StopHijack.vue'
import FlyHijack from '@/views/FlyHijack.vue'
import SwerveHijack from '@/views/SwerveHijack.vue'
import TcpFlood from '@/views/TcpFlood.vue'
import UdpFlood from '@/views/UdpFlood.vue'
import TrafficDisplay from '@/views/TrafficDisplay.vue'

//createRouter 实例化路由
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'init',
      redirect: '/TransAttack/DeviceDetect',  //初始路由重定向
    },
    {
      path: '/TrafficDisplay',
      name: 'TrafficDisplay',
      component: TrafficDisplay,  //查看流量逐字节解析
    },
    {
      path: '/TransAttack',
      name: 'TransAttack',
      children: [ // 嵌套路由配置
        {
          path: 'DeviceDisplay', //二级路由
          name: 'DeviceDisplay1',
          component: DeviceDisplay,
        },
        {
          path: 'StartHijack',
          name: 'StartHijack1',
          component: StartHijack,
        },
        {
          path: 'StopHijack',
          name: 'StopHijack1',
          component: StopHijack,
        },
        {
          path: 'FlyHijack',
          name: 'FlyHijack1',
          component: FlyHijack,
        },
        {
          path: 'SwerveHijack',
          name: 'SwerveHijack1',
          component: SwerveHijack,
        },
        {
          path: 'TcpFlood',
          name: 'TcpFlood1',
          component: TcpFlood,
        },
        {
          path: 'UdpFlood',
          name: 'UdpFlood1',
          component: UdpFlood,
        },
      ]
    },
    {
      path: '/CustomAttack',
      name: 'custom attack',
      children: [
        {
          path: 'DeviceDisplay', //二级路由
          name: 'DeviceDisplay2',
          component: DeviceDisplay,
        },
        {
          path: 'StartHijack',
          name: 'StartHijack2',
          component: StartHijack,
        },
        {
          path: 'StopHijack',
          name: 'StopHijack2',
          component: StopHijack,
        },
        {
          path: 'FlyHijack',
          name: 'FlyHijack2',
          component: FlyHijack,
        },
        {
          path: 'SwerveHijack',
          name: 'SwerveHijack2',
          component: SwerveHijack,
        },
        {
          path: 'TcpFlood',
          name: 'TcpFlood2',
          component: TcpFlood,
        },
        {
          path: 'UdpFlood',
          name: 'UdpFlood2',
          component: UdpFlood,
        },
      ]
    },

  ],
})

//导出路由
export default router
