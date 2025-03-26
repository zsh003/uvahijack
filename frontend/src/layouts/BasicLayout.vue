<template>
  <div id="BasicLayout">
    <a-layout>
      <!--- 顶部导航栏 --->
      <a-layout-header class="header">
        <div class="logo" >
          无人机的通信安全劫持系统
        </div>
        <a-menu
          class="menu"
          v-model:selectedKeys="selectedKeys1"
          theme="dark"
          mode="horizontal"
          :style="{ lineHeight: '64px', padding:'0 128px'}"
          :items="items"
          @click="doMenuClick"
        />

      </a-layout-header>

      <!--- 导航栏以下的内容 --->
      <a-layout class="wrapper">
        <!--- 小导航+侧边栏+内容部分 --->
        <a-layout-content class="container">
          <!--- 小导航 --->
          <a-breadcrumb style="margin: 16px 0">
            <a-breadcrumb-item>Home</a-breadcrumb-item>
            <a-breadcrumb-item>List</a-breadcrumb-item>
            <a-breadcrumb-item>App</a-breadcrumb-item>
          </a-breadcrumb>

          <a-layout class="content-wrapper">
            <!--- 侧边栏 --->
            <a-layout-sider class="basic-sider">
              <a-menu
                v-model:selectedKeys="selectedKeys2"
                mode="inline"
                :style="{height: '100%'}"
                @click="doSiderClick"
              >
                <a-menu-item key="/DeviceDisplay">
                  <span>
                    <laptop-outlined />
                    设备探测
                  </span>
                </a-menu-item>

                <a-sub-menu key="">
                  <template #title>
                    <span>
                      <laptop-outlined />
                      重放攻击劫持
                    </span>
                  </template>
                  <a-menu-item key="/StartHijack">油门启动劫持</a-menu-item>
                  <a-menu-item key="/StopHijack">油门关闭劫持</a-menu-item>
                  <a-menu-item key="/FlyHijack">起飞劫持</a-menu-item>
                  <a-menu-item key="/SwerveHijack">转向劫持</a-menu-item>
                </a-sub-menu>

                <a-sub-menu key="">
                  <template #title>
                    <span>
                      <laptop-outlined />
                      DDoS攻击劫持
                    </span>
                  </template>
                  <a-menu-item key="/TcpFlood">TCP泛洪攻击</a-menu-item>
                  <a-menu-item key="/UdpFlood">UDP泛洪攻击</a-menu-item>
                </a-sub-menu>

              </a-menu>
            </a-layout-sider>
            <!--- 内容部分 --->
            <a-layout-content class="container-content">
              <div class="container-routerview">
                <!--- 通过RouterView组件(配置：router/index.ts)动态替换页面内容 很重要！--->
                <router-view/>
              </div>
              <div>
                <!-- 动态组件1，根据侧边栏额外显示内容
                <component :is="currentComponent1"></component> -->
              </div>
              <div>
                <!-- 动态组件2，根据导航栏额外显示内容 -->
                <component :is="currentComponent2"></component>
              </div>
            </a-layout-content>
          </a-layout>

        </a-layout-content>
        <!--- 底部栏
        <a-layout-footer class="footer">
          20211631单凯
        </a-layout-footer> --->
      </a-layout>

    </a-layout>
  </div>
</template>

<script setup lang="ts">
// 导入页面
import TransAttack from '@/views/TransAttack.vue'
import CustomAttack from '@/views/CustomAttack.vue'
import TrafficDisplayGeneral from '@/views/TrafficDisplayGeneral.vue'

// 导航栏设置
import { MailOutlined, AppstoreOutlined, SettingOutlined } from '@ant-design/icons-vue';
import type { MenuProps } from 'ant-design-vue'
import { useRouter, useRoute } from 'vue-router'
import { h, ref,computed } from 'vue';

const items = ref<MenuProps['items']>([
  {
    key: '/TransAttack',
    icon: () => h(AppstoreOutlined),
    label: '通信攻击劫持展示',
    title: '通信攻击劫持展示',
  },
  {
    key: '/CustomAttack',
    icon: () => h(MailOutlined),
    label: '自定义流量劫持设置',
    title: '自定义流量劫持设置',
  },
]);
const router = useRouter();  //导航栏路由跳转
const route = useRoute();
const selectedKeys1 = ref<string[]>(['/TransAttack']);

// 动态组件渲染
const currentComponent1 = computed(() => {
  // 除了设备展示页面，其他页面均显示流量
  if (!route.path.includes('/DeviceDisplay')) return TrafficDisplayGeneral;
  return null; // 返回一个默认组件
});
const currentComponent2 = computed(() => {
  if (!route.path.includes('/DeviceDisplay')) {
    if (route.path.includes('/TransAttack')) return TransAttack;
    if (route.path.includes('/CustomAttack')) return CustomAttack;
  }
  return null;
});

//导航栏跳转
const doMenuClick = ({ key }: {key: string}) => {  // 这里的key就是template里面菜单的key
  router.push({
    path: key + selectedKeys2.value[0],
    //query: { key } //路由跳转参数
  });
}

//左侧菜单栏设置
import { UserOutlined, LaptopOutlined, NotificationOutlined } from '@ant-design/icons-vue'
const selectedKeys2 = ref<string[]>([]);

const doSiderClick = ({ key }: {key: string}) => {
  const path =  selectedKeys1.value[0] + key;
  router.push({
    path: path,
  });
}

// 每次点击菜单时，需要更新选中的菜单项显示（主要就是修改selectedKey1和2）
const updateSelectedKeys = () => {
  const path = route.path;
  const topLevelKeys = ['/TransAttack', '/CustomAttack']; // 添加所有顶级菜单的key
  // 清空之前的选中状态
  selectedKeys1.value = [];
  selectedKeys2.value = [];
  // 检查当前路径是否与顶级菜单匹配，并更新selectedKeys1
  if (topLevelKeys.some(key => path.startsWith(key))) {
    selectedKeys1.value = [path];
    selectedKeys2.value = [''];
  }
  // 如果路径包含更多层级，则更新selectedKeys2
  if (path.split('/').length > 2) {
    selectedKeys1.value = ['/'+path.split('/')[1]];
    selectedKeys2.value = ['/'+path.split('/')[2]];
  }
};
router.afterEach((to) => {
  updateSelectedKeys();
});

</script>

<style scoped>
/* 最上面大logo */
.header .logo {
  float: left;
  /* 让背景比文字更宽 */
  padding: 0 40px; /* 左右各增加40px的内边距 */
  height: 64px; /* 匹配布局的高度 */
  margin: 0 24px 0 0; /* 调整外边距 */
  background: rgba(255, 255, 255, 0.3);
  color: #fff;
  font-size: 20px;
  line-height: 64px; /* 文本垂直居中 */
  white-space: nowrap;   /* 文字不换行显示 */
  min-width: 200px; /* 设置最小宽度以确保背景足够宽 */
  box-sizing: border-box; /* 确保内边距和边框包含在元素的宽度和高度之内 */
}
.header .menu {

}

/* 包装导航栏以下的内容（小导航+侧边栏+内容部分+底部栏） */
.wrapper{
  padding: 8px 0;
  background: #f8f8f8;
  min-height: 100vh; /* 下面设置了 这里可以不设置，80vh=全屏幕视野*/
}
/* 小导航+侧边栏+内容部分 */
.container{
  padding: 0 50px;
}

/* 包装侧边栏+内容部分 */
.content-wrapper{
  padding: 24px 0;
  background: #fff;
  min-height: 80vh;   /*限制最小高度，很重要*/
  flex-direction: row;
}
/*侧边栏*/
.basic-sider {
  width: 250px;
  min-height: 80vh;
  background: #fff;
}
/*内容部分中固定栏+动态内容*/
.container-content {
  flex-direction: column;  /*固定栏和动态内容是上下or左右分布*/
  padding: 0 48px;
}

.container-routerview{
  padding: 24px 0;
}

/* 底部栏 */
.footer{
  background: #f8f8f8;
  text-align: center;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 12px;
}
</style>
