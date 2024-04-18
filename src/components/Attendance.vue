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
      <el-header style="background-color: #409EFF; color: #fff; text-align: center; font-size: 45px;">
        欢迎来到后台管理系统
      </el-header>
      <h2>员工入职信息表</h2>
      <el-main>
        <div class="employee-management">
          <!-- 添加员工信息框 -->
          <div v-if="showAddForm" class="overlay"></div>
          <div v-if="showAddForm" class="centered-container">
            <el-form v-if="showAddForm" :model="formData" ref="formData" label-width="80px">
              <el-form-item label="姓名" prop="name">
                <el-input v-model="formData.name"></el-input>
              </el-form-item>
              <el-form-item label="职位" prop="position">
                <el-input v-model="formData.position"></el-input>
              </el-form-item>
              <el-form-item label="入职时间" prop="start_date">
                <el-date-picker v-model="formData.start_date" type="date" placeholder="选择日期"></el-date-picker>
              </el-form-item>
              <el-form-item label="员工状态" prop="status">
                <el-input v-model="formData.status"></el-input>
              </el-form-item>
              <el-form-item label="是否在岗" prop="on_duty">
                <el-input v-model="formData.on_duty"></el-input>
              </el-form-item>
              <el-table-column prop="end_date" label="离职日期">
                <template slot-scope="scope">
                  {{ scope.row.end_date || '无' }}
                </template>
              </el-table-column>
              <el-form-item>
                <el-button type="primary" @click="addUser">确定</el-button>
                <el-button @click="cancelAdd">取消</el-button>
              </el-form-item>
            </el-form>
          </div>
          <!-- 搜索功能 -->
          <el-input v-show="showSearch" v-model="searchKeyword" placeholder="请输入关键字" style="margin-bottom: 20px;"></el-input>
          <el-button type="primary" @click="searchUser">搜索</el-button>
          <el-button v-show="showSearchCancel" type="info" @click="Searchcancel">取消</el-button>
          <br>
          <br>
          <br>
          <!-- 表格信息 -->
          <el-table :data="employees" stripe style="width: 100%">
            <el-table-column prop="name" label="姓名"></el-table-column>
            <el-table-column prop="position" label="职位"></el-table-column>
            <el-table-column prop="start_date" label="入职日期">
            </el-table-column>
            <el-table-column prop="status" label="员工状态"></el-table-column>
            <el-table-column prop="on_duty" label="是否在岗"></el-table-column>
            <el-table-column prop="end_date" label="离职日期">
              <template slot-scope="scope">
                {{ scope.row.end_date ? scope.row.end_date : '无' }}
              </template>
            </el-table-column>
            <!-- 添加员工考勤操作功能 -->
            <el-table-column label="操作">
              <template slot-scope="scope">
                <el-button size="small" @click="toggleAddForm(scope.row)" type="primary" :disabled="scope.row.end_date !== null">添加</el-button>
              </template>
            </el-table-column>
            <!-- 编辑员工考勤功能 -->
            <el-table-column label="操作">
              <template slot-scope="scope">
                <el-button size="small" @click="showEditFormDialog(scope.row)(scope.row)" type="success" :disabled="scope.row.end_date !== null">编辑</el-button>
              </template>  
            </el-table-column>
            <!-- 员工考勤转正功能 -->
            <el-table-column label="操作">
              <template slot-scope="scope">
                <el-button size="small" @click="convertToFullTime(scope.row)" type="warning" :disabled="scope.row.end_date !== null">员工转正</el-button>
              </template>  
            </el-table-column>
            <!-- 离职员工考勤功能 -->
            <el-table-column label="操作">
              <template slot-scope="scope">
                <el-button size="small" @click="toggleResignForm(scope.row)" type="danger" :disabled="scope.row.end_date !== null">离职</el-button>
              </template>  
            </el-table-column>
          </el-table>
          <!-- 分页器按钮 -->
          <el-pagination
          @current-change="handlePageChange"
          :current-page="currentPage"
          :page-sizes="[10, 20, 30, 40]"
          layout="total, sizes, prev, pager, next, jumper"
          :total="total"
        ></el-pagination>
            <!-- 离职表单弹出窗口 -->
            <el-dialog title="员工离职信息" :visible.sync="showResignForm" width="30%">
                  <el-form :model="resignationFormData" label-width="80px">
                    <el-form-item label="离职日期" prop="end_date">
                      <el-date-picker v-model="resignationFormData.end_date" type="date" placeholder="选择日期"></el-date-picker>
                    </el-form-item>
                    <el-form-item label="离职原因" prop="reason">
                      <el-input v-model="resignationFormData.reason"></el-input>
                    </el-form-item>
                    <el-form-item label="员工状态" prop="status">
                    <el-input v-model="resignationFormData.status"></el-input>
                  </el-form-item>
                  <el-form-item label="是否在岗" prop="on_duty">
                    <el-input v-model="resignationFormData.on_duty"></el-input>
                    </el-form-item>
                  </el-form>
                <div slot="footer" class="dialog-footer">
                  <el-button @click="showResignForm = false">取消</el-button>
                  <el-button type="primary" @click="markAsResigned">确定</el-button>
                </div>
            </el-dialog>
            <!-- 编辑员工信息表单 -->
            <el-dialog title="编辑员工信息" :visible.sync="showEditForm" width="30%">
              <el-form :model="editFormData" ref="editForm" label-width="80px" :rules="editFormRules">
                <!-- 编辑表单内容 -->
                <el-form-item label="姓名" prop="name">
                  <el-input v-model="editFormData.name"></el-input>
                </el-form-item>
                <el-form-item label="职位" prop="position">
                  <el-input v-model="editFormData.position"></el-input>
                </el-form-item>
                <el-form-item label="入职时间" style="margin-left: 20px;" prop="start_date">
                  <el-date-picker v-model="editFormData.start_date" style="margin-left: -38px;" type="date" placeholder="选择日期"></el-date-picker>
                </el-form-item>
                <el-form-item label="员工状态" prop="status">
                  <el-input v-model="editFormData.status"></el-input>
                </el-form-item>
                <el-form-item label="是否在岗" prop="on_duty">
                  <el-input v-model="editFormData.on_duty"></el-input>
                </el-form-item>
                <el-form-item>
                  <el-button type="primary" @click="saveEdit" style="margin-left: 150px;">确定</el-button>
                  <el-button @click="cancelEdit">取消</el-button>
                </el-form-item>
              </el-form>
            </el-dialog>
        </div>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import { Message } from 'element-ui'; // 导入提示信息
import axios from 'axios'
// import Vue from 'vue'
export default {
  data() {
    return {
      currentPage:1,      // 当前页数为1
      total: 0, // 总条数
      showEditForm: false, // 是否显示编辑员工信息表单
      showAddForm: false, // 添加员工表单框是否显示false为不显示，反之true显示
      showResignForm: false, // 离职表单框是否显示false为不显示，反之true显示
      
      // 考勤表信息
      formData: {
        name: '', // 名字
        position: '', // 职位
        start_date: '', // 入职日期
        status: '', // 员工状态
        on_duty: '', //是否在岗
        end_date: ''// 离职日期
      },
      // 离职表信息
      resignationFormData: {
        id:null,
        end_date: '',// 离职时间
        reason: '', // 离职原因
        status: '', // 员工状态
        on_duty: '' // 是否在岗
      },
      // 正在编辑的员工信息
      editFormData: {
        id: null,
        name: '',
        position: '',
        start_date: '',
        status: '',
        on_duty: '',
        end_date: ''
      },
      // 编辑表单的验证规则
      editFormRules: {
        name: [
          { required: true, message: '请输入姓名', trigger: 'blur' },
          { min: 2, max: 10, message: '姓名长度在 2 到 10 个字符之间', trigger: 'blur' }
        ],
        position: [
          { required: true, message: '请输入职位', trigger: 'blur' },
          { min: 2, max: 10, message: '职位长度在 2 到 10 个字符之间', trigger: 'blur' }
        ],
        start_date: [
          { required: true, message: '请选择入职日期', trigger: 'change' }
        ]
      },
      // 死数据
      employees: [
        // 这里可以从后端获取员工列表数据，或者使用前端模拟数据
        { id: 1, name: '张三', position: '前端工程师', start_date: '2024-01-01', on_duty: '在岗', status: '试用期', end_date: '无' },
        { id: 2, name: '李四', position: '后端工程师', start_date: '2024-02-01', on_duty: '在岗', status: '正式员工', end_date: '无' },
        // 更多员工数据...
      ],
      // 计算属性
      computed: {
        filteredUsers() {
          return this.users.filter(user =>
            user.name.toLowerCase().includes(this.searchKeyword.toLowerCase())
          );
        },
      },
      searchKeyword: '',
      // 搜索框是否显示 false则为不显示,反之则显示
      showSearch: false,
      // 搜索取消隐藏按钮,false则为不显示,反之则显示
      showSearchCancel: false,
    }
  },
  created() {
    this.fetchEmployees(); // 页面加载时调用方法获取数据
  },
  methods: {
    // 显示编辑员工信息表单
    showEditFormDialog(employee) {
      this.editFormData = { ...employee };
      this.showEditForm = true;
    },
    // 取消编辑员工信息
    cancelEdit() {
      this.showEditForm = false;
      this.$message.info('取消操作');
    },
    // 保存编辑后的员工信息
    saveEdit() {
      this.$refs.editForm.validate(valid => {
        if (valid) {
          // 发送请求保存编辑后的员工信息到后端
          axios.post('/employee/Attendance/edit', this.editFormData)
            .then(response => {
              this.$message.success('员工信息编辑成功！');
              console.error(response);
              this.fetchEmployees(); // 刷新员工数据
              this.showEditForm = false; // 隐藏编辑表单
            })
            .catch(error => {
              this.$message.error('员工信息编辑失败！');
              console.error(error);
            });
        }
      });
    },
   // 是否显示添加员工考勤表单
    toggleAddForm() {
      this.showAddForm = !this.showAddForm
    },
    // 添加员工成功后手动设置入职时间为当前日期
    addUser() {
    if (!this.formData.name || !this.formData.position || !this.formData.start_date || !this.formData.status || !this.formData.on_duty) {
        this.$message.error('请完整填写员工信息！');
        return;
    }
    if (!this.formData.start_date || isNaN(Date.parse(this.formData.start_date))) {
        this.$message.error('请输入有效的日期！');
        return;
    }
    // 将入职日期加一天
    const startDate = new Date(this.formData.start_date);
    startDate.setDate(startDate.getDate() + 1);
    // 将日期转换为期望的格式
    const formattedStartDate = startDate.toISOString().split('T')[0] + 'T00:00:00.000Z';
    axios.post('/employee/Attendance/add', { ...this.formData, start_date: formattedStartDate },{
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        this.$message.success('员工考勤信息添加成功！');
        this.fetchEmployees(); // 在添加员工成功后刷新数据
        // 添加成功后将返回的员工考勤信息添加到数组中
        this.employees.push(response.data.employee);

        this.formData = {
            name: '',
            position: '',
            start_date: '',
            status: '',
            on_duty: '',
            end_date: '无'
        };
        this.showAddForm = false;
    })
    .catch(error => {
        this.$message.error('员工考勤信息添加失败！');
        console.error(error);
    });
    },
    // 分页器
    handlePageChange(page) {
      if (page < 1 || page > this.totalPages) {
    return; // 如果页数小于1或大于总页数，则不执行后续操作
  }
    this.currentPage = page;
    this.fetchEmployees();
    },
    // 添加数据之后更新数据刷新页面
    fetchEmployees() {
    const perPage = 10; //  每页一个10条数据
    const startIndex = (this.currentPage - 1) * perPage;
    const endIndex = startIndex + perPage;

      axios.get('/employee/Attendance/all')
        .then(response => {
          this.total = response.data.length; // 获取总条数
          this.employees = response.data.slice(startIndex, endIndex);
          this.totalPages = Math.ceil(response.data.length / perPage); // 计算总页数
        // 如果当前页数超过总页数，则重置当前页数
        if (this.currentPage > this.totalPages) {
        this.currentPage = this.totalPages;
      }
        })
        .catch(error => {
          console.error(error);
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
    // 取消搜索表单自动隐藏
    Searchcancel() {
      this.showSearch = false;
      this.showSearchCancel = false;
    },
    // 点击搜索员工按钮时显示出搜索框表单
    searchUser() {
    this.showSearch = true;
    this.showSearchCancel = true;
    this.employees = this.employees.filter(employee =>
      employee.name.toLowerCase().includes(this.searchKeyword.toLowerCase())
    );
    },
    // 点击离职按钮时显示离职表单
    toggleResignForm(employee) {
      this.resignationFormData = {
        id: employee.id,
        end_date: '', // 离职日期
        reason: '', // 离职原因
        status: employee.status, // 员工状态
        on_duty: employee.on_duty // 是否在岗
      };
      this.showResignForm = true;
    },
    // 提交离职信息
    markAsResigned() {
      const index = this.employees.findIndex(employee => employee.id === this.resignationFormData.id);
      if (index !== -1) {
        // 验证日期是否有效
        const resignationDate = new Date(this.resignationFormData.end_date);
        if (isNaN(resignationDate.getTime())) {
          this.$message.error('请输入有效的日期！');
          return;
        }
        // 离职日期加1，确保日期正确显示
        resignationDate.setDate(resignationDate.getDate() + 1);
        // 使用 Vue.set 更新员工信息，确保 Vue 能够检测到属性变化
        this.$set(this.employees[index], 'end_date', resignationDate.toISOString().split('T')[0]);
        this.$set(this.employees[index], 'reason', this.resignationFormData.reason);
        this.$set(this.employees[index], 'status', this.resignationFormData.status);
        this.$set(this.employees[index], 'on_duty', this.resignationFormData.on_duty);
        axios.post('/employee/Attendance/resign', { ...this.resignationFormData, end_date: resignationDate })
          .then(response => {
            this.$message.success('操作成功！');
            this.showResignForm = false;
            console.log(response)
          })
          .catch(error => {
            this.$message.error('员工离职失败！');
            console.error(error);
          });
      }
    },
    //  员工转正功能
    convertToFullTime(employee) {
        if (employee.status !== '正式工') {
          this.$confirm('确定将该员工转为正式员工吗？', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
          }).then(() => {
            // 向后端发送请求将数据修改
            axios.post('/employee/Attendance/Employee_regularization', { id: employee.id })
              .then(response => {
                // 更新员工状态的数据
                const index = this.employees.findIndex(emp => emp.id === employee.id);
                if (index !== -1) {
                  this.$set(this.employees, index, { ...employee, status: '正式工' });
                  this.$message.success('员工转为正式员工成功！');
                  console.log(response)
                }
              })
              .catch(error => {
                this.$message.error('员工转为正式员工失败！');
                console.error(error);
              });
          }).catch(() => {
            this.$message.info('取消转为正式员工操作');
          });
        } else {
          this.$message.info('该员工已经是正式员工！');
        }
    },
  }
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
