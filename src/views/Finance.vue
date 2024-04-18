<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <el-container style="height: calc(100vh - 50px);">
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
        <h2>员工财务信息表</h2>
        <!-- 添加员工信息框 -->
        <div v-if="showAddForm" class="overlay"></div>
        <div v-if="showAddForm" class="centered-container">
        <el-form v-if="showAddForm" :model="formData" ref="formData" label-width="80px">
            <el-form-item label="姓名" prop="name">
              <el-input v-model="formData.name"></el-input>
            </el-form-item>
            <el-form-item label="年龄" prop="age">
              <el-input v-model.number="formData.age"></el-input>
            </el-form-item>
            <el-form-item label="工资" prop="salary">
              <el-input v-model.number="formData.salary"></el-input>
            </el-form-item>
            <el-form-item label="爱好" prop="hobby">
              <el-input v-model="formData.hobby"></el-input>
            </el-form-item>
            <el-form-item label="岗位" prop="position">
              <el-input v-model="formData.position"></el-input>
            </el-form-item>
            <el-form-item label="名族" prop="ethnicity">
              <el-input v-model="formData.ethnicity"></el-input>
            </el-form-item>
            <el-form-item>
        <el-button type="primary" @click="addUser">确定</el-button>
        <el-button @click="cancelAdd">取消</el-button>
      </el-form-item>
        </el-form>
        </div>
        <!-- 搜索功能
        <el-input v-show="showSearch" v-model="searchKeyword" placeholder="请输入关键字" style="margin-bottom: 20px;"></el-input>
        <el-button type="primary" @click="searchUser">搜索</el-button>
        <el-button v-show="showSearchCancel" type="info" @click="Searchcancel">取消</el-button> -->
        <!-- 添加员工信息功能 -->
        <el-table :data="filteredUsers" style="margin-top: 20px;">
        <el-table-column label="姓名" prop="name"></el-table-column>
        <el-table-column label="年龄" prop="age"></el-table-column>
        <el-table-column label="工资" prop="salary"></el-table-column>
        <el-table-column label="爱好" prop="hobby"></el-table-column>
        <el-table-column label="岗位" prop="position"></el-table-column>
        <el-table-column label="民族" prop="ethnicity"></el-table-column>
        <!-- 添加作栏 -->
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button size="small" @click="toggleAddForm(scope.row)" type="primary">添加</el-button>
          </template>
        </el-table-column>
        <!-- 查看操作栏 -->
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button size="small" @click="viewUser(scope.row)" type="primary">查看</el-button>
          </template>
        </el-table-column>
        <!-- 编辑操作栏 -->
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button size="small" @click="editUser(scope.row)" type="success">编辑</el-button>
          </template>
        </el-table-column>
        <!-- 删除操作栏 -->
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button size="small" @click="confirmDeleteUser(scope.row)" type="danger">删除</el-button>
          </template>
        </el-table-column>
        </el-table>
        <!-- 编辑功功能表单框 -->
        <el-dialog :visible.sync="editDialogVisible" title="编辑用户信息">
          <el-form :model="editFormData" label-width="80px">
            <el-form-item label="姓名" prop="name">
              <el-input v-model="editFormData.name"></el-input>
            </el-form-item>
            <el-form-item label="年龄" prop="age">
              <el-input v-model="editFormData.age"></el-input>
            </el-form-item>
            <el-form-item label="工资" prop="salary">
              <el-input v-model="editFormData.salary"></el-input>
            </el-form-item>
            <el-form-item label="爱好" prop="hobby">
              <el-input v-model="editFormData.hobby"></el-input>
            </el-form-item>
            <el-form-item label="岗位" prop="position">
              <el-input v-model="editFormData.position"></el-input>
            </el-form-item>
            <el-form-item label="民族" prop="ethnicity">
              <el-input v-model="editFormData.ethnicity"></el-input>
            </el-form-item>
          </el-form>
          <div slot="footer" class="dialog-footer">
            <el-button @click="cancelEdit">取消</el-button>
            <el-button type="primary" @click="saveEdit">保存</el-button>
          </div>
        </el-dialog>
        <!-- 查看功能 -->
        <el-dialog :visible.sync="viewDialogVisible" title="查看用户信息">
          <p>姓名：{{ selectedUser.name }}</p>
          <p>年龄：{{ selectedUser.age }}</p>
          <p>工资：{{ selectedUser.salary }}</p>
          <p>爱好：{{ selectedUser.hobby }}</p>
          <p>岗位：{{ selectedUser.position }}</p>
          <p>民族：{{ selectedUser.ethnicity }}</p>
        </el-dialog>
        <!-- 分页器 -->
        <el-pagination
            @current-change="handlePageChange"
            :current-page="currentPage"
            :page-size="[10, 20, 30, 40]"
            :total="total"
            layout="total, sizes, prev, pager, next, jumper"
        ></el-pagination>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import { Message, MessageBox } from 'element-ui';
import axios from 'axios'

export default {
  data() {
    return {
      addDialogVisible: false, // 控制添加数据对话框的显示与隐藏
      currentPage: 1, // 当前页码
      pageSize: 10, // 每页显示条数
      total: 0, // 总条数
      // 显示添加表单框
      showAddForm: false,
      // 表单框数据栏
      formData: {
        name: '',
        age: null,
        salary: '',
        hobby: '',
        position: '',
        ethnicity: '',
      },
      // 死数据
      users: [
        { name: '张三', age: 25, salary: 3200, hobby: '打篮球', position: '开发前端', ethnicity: '汉族' },
        { name: '李四', age: 30, salary: 2300, hobby: '打羽毛球', position: '开发后端', ethnicity: '汉族' },
      ],
      // 搜搜框
      searchKeyword: '',
      viewDialogVisible: false,
      selectedUser: {},
      // 搜索框是否显示 false则为不显示
      showSearch: false,
      // 搜索取消隐藏按钮
      showSearchCancel: false,
      // 编辑是否显示
      editDialogVisible: false,
      editedUserIndex: -1,
      editFormData: {
        id:null,
        name: '',
        age: null,
        salary: '',
        hobby: '',
        position: '',
        ethnicity: '',
      },
    };
  },
  // 计算属性
  computed: {
    filteredUsers() {
      return this.users.filter(user =>
        user.name.toLowerCase().includes(this.searchKeyword.toLowerCase())
      );
    },
  },
  // 钩子函数
  created(){
  this.getUsers();
  },
  methods: {
    // 每一页展示的数据
    handleSizeChange(val) {
      this.pageSize = val;
      this.getUsers();
    },
    // 当前为与第几页数据
    handlePageChange(val) {
      this.currentPage = val;
      this.getUsers();
    },
    // 页面总数数
    handleCurrentChange(val) {
      this.currentPage = val;
      this.getUsers();
    },
    // 点击添加用户后显示表单
    toggleAddForm() {
      this.showAddForm = !this.showAddForm;
    },
    // 添加员工信息方法
    addUser() {
  // 发送员工财务信息数据到后端路由
  axios.post('/finance/add', this.formData)
    .then(response => {
      // 如果添加成功，手动将新添加的数据添加到数组中
      this.users.push({
        name: this.formData.name,
        age: this.formData.age,
        salary: this.formData.salary,
        hobby: this.formData.hobby,
        position: this.formData.position,
        ethnicity: this.formData.ethnicity
      });
      Message.success('财务信息添加成功！');
      console.log(response);
      setTimeout(() => {
        this.getUsers();
        this.showAddForm = false;
      }, 100);
    })
    .catch(error => {
      console.error(error);
      Message.error('添加财务信息失败！');
    });
    },
    // 取消添加员工信息之后隐藏表单
    cancelAdd() {
      this.$refs.formData.resetFields();
      this.showAddForm = false;
      Message({        
        type: 'info',
        message: '用户取消添加操作！',})
    },
    // 从后端获取数据
    getUsers() {
      const startIndex = (this.currentPage - 1) * this.pageSize;
      const endIndex = startIndex + this.pageSize;
      axios.get('/finance/all')
          .then(response => {
        if (response.status === 200) {
          this.users = response.data; // 将响应数据赋值给组件中的 users 数组
          this.total = response.data.length; // 获取总条数
          this.tableData = response.data.slice(startIndex, endIndex); // 根据页码和每页显示条数截取需要展示的数据
          } else {
            this.$message.error('获取用户信息失败');
                }
            })
           .catch(error => {
              console.error('获取用户信息失败:', error);
            this.$message.error('获取用户信息失败');
          });
    },
    // 取消搜索表单自动隐藏
    Searchcancel() {
      this.showSearch = false;
      this.showSearchCancel = false;
    },
    // 点击搜索员工按钮时显示出搜索框表单
    searchUser() {
      this.showSearch = true;
      this.showSearchCancel = true;
    },
    // 查看员工信息方法
    viewUser(user) {
      this.selectedUser = user;
      this.viewDialogVisible = true;
    },
    // 编辑员工信息方法
    editUser(user) {
      this.editFormData = { ...user };
      this.editedUserIndex = this.users.indexOf(user);
      this.editDialogVisible = true;
    },
    // 保存新编辑的数据并返回到桌面上
    saveEdit() {
      // 发送请求保存编辑后的员工财务信息到后端
      axios.post('/finance/edit', this.editFormData)
      .then(response => {
        this.$message.success('员工信息编辑成功！');
        console.error(response);
        this.getUsers(); // 编辑之后修改员工数据之后展示在页面当中
        this.editDialogVisible = false; // 添加成功之后隐藏编辑表单
      })
      .catch(error => {
        this.$message.error('员工信息编辑失败！');
              console.error(error);
      })
    },
    // 取消编辑方法
    cancelEdit() {
      this.editDialogVisible = false;
      this.editedUserIndex = -1;
      this.editFormData = {
        name: '',
        age: null,
        salary: '',
        hobby: '',
        position: '',
        ethnicity: '',
      };
      Message({
        type: 'info',
        message: '用户取消编辑！',
      });
    },
    // 删除员工信息方法
    confirmDeleteUser(user) {
      MessageBox.confirm('确定删除这条数据吗?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
      })
        .then(() => {
          // 发送删除请求到后端
          axios.post('/finance/delete', { id: user.id })
            .then(response => {
              const index = this.users.indexOf(user);
              if (index !== -1) {
                this.users.splice(index, 1); // 从前端数组中删除选定的数据
                console.log(response);
                Message({
                  type: 'success',
                  message: '删除成功！',
                });
              }
            })
            .catch(error => {
              console.error('删除失败:', error);
              Message.error('删除失败！');
            });
        })
        .catch(() => {
          // 用户点击取消时执行的操作
          Message({
            type: 'info',
            message: '用户取消删除操作！',
          });
        });
    },
    // 菜单栏
    handleMenuSelect(index) {
      console.log('Selected menu:', index);
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
.centered-container {
  position: fixed;
  top: 50%;
  left: 50%;
  width: 400px;
  transform: translate(-50%, -50%);
  background: #fff; /* Set a background color if needed */
  padding: 20px;
  border-radius: 8px;
  z-index:200;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  z-index: 100; /* Lower z-index to allow interactions with elements above it */
}
</style>
