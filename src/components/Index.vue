<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <el-container style="height: calc(100vh - 50px);">
    <!-- 侧边栏 -->
    <el-aside width="120px" style="background-color: #545c64; color: #ffffff;">
      <el-menu default-active="$route.path" class="el-menu-vertical-demo" @select="handleMenuSelect" style="background-color: #545c64;">
        <router-link to="/" style="text-decoration: none;">
          <el-menu-item index="1">首页</el-menu-item>
        </router-link>
        <router-link to="/auth/Department" style="text-decoration: none;">
          <el-menu-item index="2">用户管理</el-menu-item>
        </router-link>
        <router-link to="/auth/Attendance" style="text-decoration: none;">
          <el-menu-item index="3">考勤管理</el-menu-item>
        </router-link>
        <router-link to="/auth/Purchasing" style="text-decoration: none;">
          <el-menu-item index="4"  style="margin-left:-8px">房地产订单管理</el-menu-item>
        </router-link>
        <router-link to="/auth/commodity" style="text-decoration: none;">
          <el-menu-item index="5">商品订单管理</el-menu-item>
        </router-link>
        <router-link to="/auth/finance" style="text-decoration: none;">
          <el-menu-item index="6">财务管理</el-menu-item>
        </router-link>
        <router-link to="/auth/admin" style="text-decoration: none;">
          <el-menu-item index="7">个人信息</el-menu-item>
        </router-link>
        <router-link to="/auth/login" style="text-decoration: none;">
          <el-menu-item index="8" @click="logout">退出登录</el-menu-item>
        </router-link>
      </el-menu>
    </el-aside>
    <!-- 主体内容区域 -->
    <el-container>
      <el-header style="background-color: #409EFF; color: #fff; text-align: center; font-size: 45px;">欢迎来到管理系统</el-header>
      <el-main style="display: flex; justify-content: space-between; padding: 20px;">
        <!-- 树形统计图 -->
        <div style="width: 50%;">
          <canvas ref="pieChart" width="0" height="100"></canvas>
        </div>
        <!-- 饼形统计图 -->
        <div style="width: 50%;">
          <canvas ref="treeChart" width="0" height="100"></canvas>
        </div>
      </el-main>
    </el-container>

</el-container>
</template>

<script>
import Chart from 'chart.js/auto';

export default {
  data() {
  return {
  };
},
  methods: {
    // 饼图统计图数据
    initPieChart() {
      const ctx = this.$refs.pieChart.getContext('2d');
      new Chart(ctx, {
        type: 'doughnut',
        data: {
          labels: ['北京', '上海', '南京', '深圳', '广州', '杭州', '西安'],
          datasets: [{
            label: '分公司数量',
            data: [120, 60, 100, 80, 70, 110, 130],
            backgroundColor: [
              'rgba(255, 99, 132, 0.6)',
              'rgba(54, 162, 235, 0.6)',
              'rgba(255, 206, 86, 0.6)',
              'rgba(75, 192, 192, 0.6)',
              'rgba(153, 102, 255, 0.6)',
              'rgba(255, 159, 64, 0.6)',
              'rgba(22, 99, 132, 0.6)'
            ],
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false
        }
      });
    },
    // 树形统计图数据
    initTreeChart() {
      const ctx = this.$refs.treeChart.getContext('2d');
      new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ['出售', '入库', '进账', '收入', '支出', '营业额', '总季度'],
          datasets: [{
            label: '本月账单',
            data: [100, 60, 100, 80, 70, 110, 130],
            backgroundColor: [
              'rgba(255, 99, 132, 0.6)',
              'rgba(54, 162, 235, 0.6)',
              'rgba(255, 206, 86, 0.6)',
              'rgba(75, 192, 192, 0.6)',
              'rgba(153, 102, 255, 0.6)',
              'rgba(255, 159, 64, 0.6)',
              'rgba(22, 99, 132, 0.6)'
            ],
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false
        }
      });
    },
    // 使用统计图样式
    initCharts() {
      this.initPieChart();
      this.initTreeChart();
    },
  },
  // 钩子函数挂载
    mounted() {
      this.$nextTick(() => {
        this.initCharts();
      });
    },
};
</script>

<style scoped>
.el-container {
  border: 1px solid #ebeef5;
}

.el-aside {
  border-right: 1px solid #ebeef5;
}

.el-header {
  border-bottom: 1px solid #ebeef5;
}
</style>
