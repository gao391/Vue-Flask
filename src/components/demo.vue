<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <el-container style="height: calc(100vh - 50px);" v-if="users.length">
    <!-- 侧边栏 -->
    <el-aside width="120px" style="background-color: #545c64; color: #ffffff;">
      <!-- 导航链接 -->
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
          <el-menu-item index="4">采购订单管理</el-menu-item>
        </router-link>
        <router-link to="/auth/commodity" style="text-decoration: none;">
          <el-menu-item index="5">商品订单管理</el-menu-item>
        </router-link>
        <router-link to="/auth/hobby" style="text-decoration: none;">
          <el-menu-item index="6">员工信息</el-menu-item>
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
      <el-header style="background-color: #409EFF; color: #fff; text-align: center; font-size: 45px;">
        欢迎来到后台管理系统
      </el-header>
        <!-- 添加、删除、禁用、启用按钮 -->
      <div style="margin-top:50px; margin-left: -1550px;">
        <el-button size="small" @click="toggleAddForm" type="primary">添加</el-button>
        <el-button size="small" @click="enableUsers(启用)" type="success">启用</el-button>
        <el-button size="small" @click="disableUsers('禁用')" type="warning">禁用</el-button>
      </div>
      <el-main>
        <!-- 添加数据框 -->
        <div class="employee-management">
        <div v-if="showAddForm" class="overlay"></div>
        <div v-if="showAddForm" class="centered-container">
          <el-form v-if="showAddForm" :model="formData" ref="formData" label-width="80px">
              <el-form-item label="登录名称" prop="login_name">
                <el-input v-model="formData.login_name" placeholder="默认密码为123456"></el-input>
              </el-form-item>
              <el-form-item label="用户名称" prop="users_name">
                <el-input v-model="formData.users_name"></el-input>
              </el-form-item>              
              <el-form-item label="用户类型" prop="customer_type">
                <el-input v-model="formData.customer_type"></el-input>
              </el-form-item>              
              <el-form-item label="角色" prop="role">
                <el-input v-model="formData.role"></el-input>
              </el-form-item>              
              <el-form-item label="电话号码" prop="phone">
                <el-input v-model="formData.phone"></el-input>
              </el-form-item>
              <el-form-item label="状态" prop="status">
                <el-input v-model="formData.status"></el-input>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="addUser">确定</el-button>
                <el-button @click="cancelAddUser">取消</el-button>
              </el-form-item>
          </el-form>
        </div>
        <!-- 用户管理表格 -->
        <el-table :data="users" border style="width: 100%" align="center" @selection-change="handleSelectionChange">
          <el-table-column type="selection" align="center"></el-table-column>
          <el-table-column prop="login_name" label="登录名称" align="center"></el-table-column>
          <el-table-column prop="users_name" label="用户姓名" align="center"></el-table-column>
          <el-table-column prop="customer_type" label="用户类型" align="center"></el-table-column>
          <el-table-column prop="role" label="角色" align="center"></el-table-column>
          <el-table-column prop="phone" label="电话号码" align="center"></el-table-column>
          <el-table-column prop="status" label="状态" align="center">
            <template slot-scope="scope">
              <el-tag :type="getStatusTagType(scope.row.status)">{{ scope.row.status }}</el-tag>
            </template>
          </el-table-column>
          <!-- 操作栏功能 -->
          <el-table-column label="操作" align="center">
            <template slot-scope="scope">
              <el-link type="primary" @click="editUser(scope.row)">编辑</el-link> |
              <el-link type="danger" @click="deleteUser(scope.row)">删除</el-link> | 
              <el-link type="warning" @click="resetPassword(scope.row)">重置密码</el-link>
            </template>
          </el-table-column>
        </el-table>
        </div>
      </el-main>
    </el-container>
  </el-container>
</template>
  
<script>
// import { Message, MessageBox } from 'element-ui';
import axios from 'axios'
export default {
  data() {
    return {
      filteredUsers: [],
      selectedRows: [], // 存储勾选的数据
      showAddForm: false, // 添加员工表单框是否显示false为不显示，反之true显示
      formData: {
        login_name: '',
        users_name: '',
        customer_type: '',
        role: '',
        phone: '',
        status: '',
        password: '123456'  // 默认密码
      },
      // 死数据
      users: [
        { login_name: 'SPGLY', users_name: '销售管理', customer_type: '普通', role: '销售经理', phone: 131345678953, status: '启用' },
        { login_name: 'SPGLY', users_name: '销售管理', customer_type: '普通', role: '销售经理', phone: 131345678953, status: '启用' },
      ],
    };
  },
  // 向后端发送请求获取数据展示在页面当中
  created() {
        this.getUsers();
      },
  methods: {
    // 表示状态栏状态是否启用或者禁用
    getStatusTagType(status) {
    return status === '启用' ? 'success' : 'danger'; // 根据状态返回标签的类型
  },
  deleteUser(row) {
  // 弹出确认框，确认删除操作
  this.$confirm('确定删除该用户吗？', '提示', {
    confirmButtonText: '确定',
    cancelButtonText: '取消',
    type: 'warning'
  }).then(() => {
    // 发送删除请求到后端
    axios.delete(`/department/delete_user/${row.id}`)
      .then(response => {
        if (response.data.success) {
          // 从界面上删除该用户
          const userId = row.userId;
          const index = this.users.findIndex(user => user.id === userId);
          if (index !== -1) {
            this.users.splice(index, 1);
            this.$message.success('删除成功');
          }
        } else {
          this.$message.error('删除失败，请重试');
        }
      })
      .catch(error => {
        console.error('删除失败:', error);
        this.$message.error('删除失败，请重试');
      });
  }).catch(() => {
    this.$message.info('取消删除操作');
  });
},

  // 从后端获取数据
  getUsers() {
      axios.get('/department/all')
        .then(response => {
          if (response.data.success) {
            this.users = response.data.data;
          } else {
            this.$message.error('获取用户信息失败');
          }
        })
        .catch(error => {
          console.error('获取用户信息失败:', error);
          this.$message.error('获取用户信息失败');
        });
    },
    // 点击添加用户后显示表单
    toggleAddForm() {
      this.showAddForm = !this.showAddForm;
    },
    // 添加用户方法
  addUser() {
      axios.post('/department/add_user', this.formData)
      .then(response => {
        if (response.data.success) {
          // 添加成功后注册一个账号进行登录
          axios.post('/department/register_login_user', { username: this.formData.login_name, password: '123456' })
            .then(response => {
              if (response.data.success) {
                this.showAddForm = false; // 隐藏表单
                // 添加成功后更新用户列表
                this.users.push(this.formData);
                // 重置表单数据
                this.formData = {
                  login_name: '',
                  users_name: '',
                  customer_type: '',
                  role: '',
                  phone: '',
                  status: '',
                  password: '123456'
                };
                this.$message.success('添加用户成功');
                this.getUsers();
              } else {
                this.$message.error('注册登录账号失败');
              }
            })
            .catch(error => {
              console.error('注册登录账号失败:', error);
              this.$message.error('注册登录账号失败');
            });
        } else {
          this.$message.error('添加用户失败');
        }
      })
      .catch(error => {
        console.error('添加用户失败:', error);
        this.$message.error('添加用户失败');
      });
},
    // 取消添加用户
    cancelAddUser() {
      this.showAddForm = false;
      this.$message.info('用户操作取消');
    },
    // 勾选数据
    handleSelectionChange(selection) {
      this.selectedRows = selection;
    },
    // 启用用户
    enableUsers() {
      if (this.selectedRows.length === 0) {
        this.$message.warning('请先勾选数据');
        return;
      }
      const hasDisabled = this.selectedRows.some(row => row.status === '禁用');
      if (hasDisabled) {
        this.$confirm('是否确认将选中的数据状态修改为启用?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          // 构造一个包含选中用户 ID 的数组
          const userIds = this.selectedRows.map(row => row.id); // 这里假设用户数据中有一个名为 id 的属性来表示用户的唯一标识符
          // 发送请求到后端
          axios.put('/department/enable_users', { userIds })
            .then(response => {
              if (response.data.success) {
                this.selectedRows.forEach(row => {
                  if (row.status === '禁用') {
                    row.status = '启用';
                  }
                });
                this.$message.success('状态修改成功');
                this.getUsers();
                // 更新 users 数据
                this.users = response.data.updatedUsers;
              } else {
                this.$message.error('状态修改失败，请重试');
              }
            })
            .catch(error => {
              console.error('状态修改失败:', error);
              this.$message.error('状态修改失败，请重试');
            });
        }).catch(() => {
          this.$message.info('用户取消操作');
        });
      } else {
        this.$message.warning('所选数据已是启用状态');
      }
    },
    // 禁用用户
    disableUsers() {
        if (this.selectedRows.length === 0) {
          this.$message.warning('请先勾选数据');
          return;
        }
        const hasEnabled = this.selectedRows.some(row => row.status === '启用');
        if (hasEnabled) {
          this.$confirm('是否确认将选中的数据状态修改为禁用?', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
          }).then(() => {
            // 构造一个包含选中用户 ID 的数组
            const userIds = this.selectedRows.map(row => row.id); // 这里假设用户数据中有一个名为 id 的属性来表示用户的唯一标识符
            // 发送请求到后端
            axios.put('/department/disable_users', { userIds })
              .then(response => {
                if (response.data.success) {
                  this.selectedRows.forEach(row => {
                    if (row.status === '启用') {
                      row.status = '禁用';
                    }
                  });
                  this.$message.success('状态修改成功');
                  this.getUsers();
                  // 更新 users 数据
                  this.users = response.data.updatedUsers;
                } else {
                  this.$message.error('状态修改失败，请重试');
                }
              })
              .catch(error => {
                console.error('状态修改失败:', error);
                this.$message.error('状态修改失败，请重试');
              });
          }).catch(() => {
            this.$message.info('用户取消操作');
          });
        } else {
          this.$message.warning('所选数据已是禁用状态');
        }
    }
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
  .el-dialog .el-form-item {
    display: flex;
    align-items: center;
  }
  .el-dialog .el-date-editor {
    width: 100%;
  }
  
  </style>

