<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div class="register-container">
    <el-card class="register-card">
      <h2>注册</h2>
      <el-form :model="registerForm" ref="registerForm" :rules="registerRules" label-width="80px">
        <el-form-item label="账号" prop="username">
          <el-input v-model="registerForm.username" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input type="password" v-model="registerForm.password" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button style="margin-left: -45px;" type="primary" @click="register">注册</el-button>
        </el-form-item>
        <el-link style="margin-left: 40px;"><a href="/auth/login">已有账号?点击登录</a></el-link>
      </el-form>
    </el-card>
  </div>
</template>

<script>
import { Message } from 'element-ui'; // 引入elementui组件库

export default {
  data() {
    return {
      registerForm: {
        username: '',
        password: '',
      },
      registerRules: {
        username: [{ required: true, message: '请输入3~10位的账号', trigger: 'blur' }],
        password: [{ required: true, message: '请输入6~13位的密码', trigger: 'blur' }],
      },
    };
  },
  methods: {
    register() {
      const data = {
        username: this.registerForm.username,
        password: this.registerForm.password,
      };

      // 想后端发Flask发送请求
      this.$axios.post('/auth/register', data,{
            headers: {
        'Content-Type': 'application/json'
      }
      })
        // eslint-disable-next-line no-unused-vars
        .then(response => {
          // 注册成功
          Message.success('注册成功.....即将跳转登录页面'); // 对用户弹出提示信息
          // 跳转登录页面
          this.$router.push('/auth/login');
        })
        .catch(error => {
          console.error('Registration failed:', error);
          // 注册失败,提示用户信息
          Message.error('注册失败，请重试');
        });
    },
  },
};
</script>

<style scoped>
.register-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-image: url(../assets/img/01.jpg);
  background-size: cover;
  background-position: center;
}

.register-card {
  width: 400px;
  padding: 20px;
}
</style>
