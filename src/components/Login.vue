<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div class="login-container">
    <el-card class="login-card">
      <h2>登录</h2>
      <el-form :model="loginForm" ref="loginForm" :rules="loginRules" label-width="80px">
        <el-form-item label="账号" prop="username">
          <el-input v-model="loginForm.username" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input type="password" v-model="loginForm.password" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button style="margin-left: -45px;" type="primary" @click="login">登录</el-button>
        </el-form-item>
        <el-link style="margin-left: 30px;" type="primary"><a href="/auth/register">没有账号?点击注册</a></el-link>
      </el-form>
    </el-card>
  </div>
</template>

<script>
import { Message } from 'element-ui'; // 导入elementui组件库

export default {
data() {
  return {
    loginForm: {
      username: '',
      password: '',
    },
    loginRules: {
      username: [{ required: true, message: '请输入账号', trigger: 'blur' }],
      password: [{ required: true, message: '请输入密码', trigger: 'blur' }],
    },
    showWelcomeMessage: false,
  };
},
methods: {
login() {
  const data = {
    username: this.loginForm.username,
    password: this.loginForm.password,
  };
  // 向后端发送请求，将数据和数据库信息做对比
  this.$axios({
    method: 'post',
    url: 'http://192.168.0.7:8000/auth/login',
    data: data, 
    headers: {
      'Content-Type': 'application/json'
    }
  })
  .then(response => {
    // 登录时和数据库信息做比较是否一致
    if (response.data.success === '登录成功') {
      Message.success("登录成功");
      this.$router.push('/');
      // 如果失败提示用户
    } else {
      Message.error("登录失败，请检查用户名和密码。");
    }
})
  // 网络不好的时候给用户提示信息
  .catch(error => {
    console.error('Login failed:', error.response);
    const errorMessage = error.response ? error.response.data.error : '请求错误，请重试';
    this.$message.error(errorMessage);
  });
},
},
};

</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-image: url(../assets/img/02.jpg);
  background-size: cover;
  background-position: center;
}

.login-card {
  width: 400px;
  padding: 20px;
}
</style>
