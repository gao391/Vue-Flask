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
          <el-menu-item index="8">退出登录</el-menu-item>
        </router-link>
        </el-menu>
      </el-aside>
      <!-- 主体内容区域 -->
      <el-container>
        <el-header style="background-color: #409EFF; color: #fff; text-align: center; font-size: 45px;">欢迎来到后台管理系统</el-header>
        <el-main style="padding: 20px;">
          <!-- 个人信息表单 -->
          <el-form :model="personalInfo" ref="personalInfoForm" label-width="80px">
            <!-- 头像信息 -->
            <el-form-item label="头像">
              <el-avatar :src="personalInfo.avatar" size="100px" @click="viewImage"></el-avatar>
              <el-upload
                action="#"
                list-type="picture-card"
                :show-file-list="false"
                :before-upload="beforeUpload"
                @change="handleAvatarChange"
              >
                <i class="el-icon-plus"></i>
              </el-upload>
            </el-form-item>
            <!-- 表格栏信息 -->
            <el-form-item label="姓名" prop="name">
              <el-input v-model="personalInfo.name"></el-input>
            </el-form-item>
            <el-form-item label="职位" prop="identity">
              <el-input v-model="personalInfo.identity"></el-input>
            </el-form-item>
            <el-form-item label="部门" prop="department">
              <el-input v-model="personalInfo.department"></el-input>
            </el-form-item>
            <el-form-item label="爱好" prop="hobby">
              <el-input v-model="personalInfo.hobby"></el-input>
            </el-form-item>
            <el-form-item label="岗位" prop="posts">
              <el-input v-model="personalInfo.posts"></el-input>
            </el-form-item>
            <el-form-item label="名族" prop="motaion">
              <el-input v-model="personalInfo.motaion"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="savePersonalInfo">保存个人信息</el-button>
            </el-form-item>
          </el-form>
        </el-main>
      </el-container>
    </el-container>
    
  </template>
  
  <script>

  export default {
    data() {
      return {
        personalInfo: {
          avatar: 'https://i.imgur.com/xRpx5Rp.jpg',
          name: '张三',
          identity: '产品经理',
          department: '销售部',
          hobby: '打篮球',
          posts: '开发前端',
          motaion: '汉族',
        },
      };
    },
    methods: {
      savePersonalInfo() {
        this.$refs.personalInfoForm.validate((valid) => {
          if (valid) {
            console.log('Saved Personal Information:', this.personalInfo);
          } else {
            console.log("输出");
          }
        });
      },
      handleMenuSelect(index) {
        console.log('Selected menu:', index);
      },
      beforeUpload(file) {
        const isJPG = file.type === 'image/jpeg' || file.type === 'image/png';
        if (!isJPG) {
          this.$message.error('只能上传 JPG 或 PNG 格式的图片');
        }
        const isLt2M = file.size / 1024 / 1024 < 2;
        if (!isLt2M) {
          this.$message.error('图片大小不能超过 2MB');
        }
        return isJPG && isLt2M;
      },
      handleAvatarChange(file) {
        this.personalInfo.avatar = URL.createObjectURL(file.raw);
      },
      viewImage() {
        this.$alert(`<img src="${this.personalInfo.avatar}" style="width:100%">`, '头像预览', {
          dangerouslyUseHTMLString: true,
        });
      },
    },
  };
  </script>
  
  <style>
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