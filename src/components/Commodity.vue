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
        <router-link to="/logout" style="text-decoration: none;">
          <el-menu-item index="8">退出登录</el-menu-item>
        </router-link>
      </el-menu>
    </el-aside>
    <!-- 主体内容区域 -->
    <el-container>
      <el-header style="background-color: #409EFF; color: #fff; text-align: center; font-size: 45px;">
        欢迎来到后台管理系统
      </el-header>
      <el-main style="padding: 20px;">
        <!-- 查询表单 -->
        <el-form :model="queryForm" label-width="80px">
          <el-row>
            <el-col :span="6">
              <el-form-item label="单据编号" prop="billNumber">
                <el-input v-model="queryForm.billNumber" placeholder="请输入单据编号"></el-input>
              </el-form-item>
            </el-col>
            <el-col :span="6">
              <el-form-item label="单据日期" prop="dateRange" style="margin-left: 30px;">
                <el-date-picker
                  v-model="queryForm.dateRange"
                  type="daterange"
                  range-separator="至"
                  start-placeholder="开始日期"
                  end-placeholder="结束日期"
                ></el-date-picker>
              </el-form-item>
            </el-col>
            <el-col :span="6">
              <el-form-item label="商品信息" prop="productInfo" style="margin-left: 140px;">
                  <el-input v-model="queryForm.productInfo" placeholder="请输入商品信息"></el-input> 
              </el-form-item>
            </el-col>
            <el-col :span="6" style="display: flex; align-items: flex-end;">
              <el-button type="primary" @click="handleQuery" style="margin-left: 190px;">查询</el-button>
              <el-button @click="handleReset">重置</el-button>
            </el-col>
          </el-row>
        </el-form>
          <!-- 新增、审核、删除、反审核、导出按钮 -->
          <el-row style="margin-top: 10px;">
          <el-col :span="4">
            <el-button type="primary" @click="handleAdd" style="margin-left: -200px;">新增</el-button>
          </el-col>
          <el-col :span="4">
              <el-button type="success" @click="handleAudit" style="margin-left: -480px;">审核</el-button>
          </el-col>
          <el-col :span="4">
              <el-button type="danger" @click="handleDelete" style="margin-left: -780px;">删除</el-button>
          </el-col>
          <el-col :span="4">
            <el-button type="warning" @click="handleReview" style="margin-left: -1050px;">反审核</el-button>
          </el-col>
          <el-col :span="4">
            <el-button type="info" @click="handleExport" style="margin-left: -1320px;">导出</el-button>
          </el-col>
        </el-row>
        <!-- 表格 -->
        <el-table :data="tableData" style="margin-top: 20px;" ref="table" @selection-change="handleSelectionChange" :row-key="row => row.billNumber">
            <el-table-column type="selection" width="55"></el-table-column>
            <el-table-column prop="billNumber" label="单据编号"></el-table-column>
            <el-table-column label="单据日期">
              <template slot-scope="scope">
                {{ formatDate(scope.row.startDate) }} ~ {{ formatDate(scope.row.endDate) }}
              </template>
            </el-table-column>
            <el-table-column prop="productInfo" label="商品信息"></el-table-column>
            <el-table-column prop="state" label="审核状态"></el-table-column>
            <el-table-column prop="customer" label="客户"></el-table-column>
            <el-table-column prop="money" label="金额"></el-table-column>
        </el-table>
          <!-- 添加数据对话框 -->
        <el-dialog title="添加数据" :visible.sync="addDialogVisible" width="30%">
          <el-form :model="addFormData" label-width="80px">
        <!-- 添加数据表单项 -->
          <el-form-item label="单据编号" prop="billNumber">
            <el-input v-model="addFormData.billNumber" placeholder="请输入单据编号"></el-input>
          </el-form-item>
          <el-form-item label="订单时间" prop="date">
            <el-date-picker
              v-model="addFormData.date"
              type="daterange"
              range-separator="至"
              start-placeholder="开始日期"
              end-placeholder="结束日期"
            ></el-date-picker>
          </el-form-item>
          <el-form-item label="商品信息" prop="productInfo">
            <el-input v-model="addFormData.productInfo" placeholder="请输入商品信息"></el-input>
          </el-form-item>
          <el-form-item label="交易金额" prop="productInfo">
            <el-input v-model="addFormData.money" placeholder="请输入交易金额"></el-input>
          </el-form-item>
          <el-form-item label="客户信息" prop="productInfo">
            <el-input v-model="addFormData.customer" placeholder="请输入客户信息"></el-input>
          </el-form-item>
          <el-form-item label="审核状态" prop="state">
            <el-radio-group v-model="addFormData.state">
              <el-radio label="通过">通过</el-radio>
              <el-radio label="未通过">未通过</el-radio>
            </el-radio-group>
          </el-form-item>
        <el-form-item>
          <!-- 提交和取消按钮 -->
          <el-button type="primary" @click="handleSubmit">提交</el-button>
          <el-button @click="handleCancel">取消</el-button>
        </el-form-item>
      </el-form>
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
import * as XLSX from 'xlsx';
export default {
  data() {
    return {
      addDialogVisible: false, // 控制添加数据对话框的显示与隐藏
      currentPage: 1, // 当前页码
      pageSize: 10, // 每页显示条数
      total: 0, // 总条数
    addFormData: {
      // 客户
      customer:'',
      // 交易金额
      money:'',
      // 开始日期
      start_date:'',
      // 结束日期
      end_date:'',
      // 订单编号
      billNumber: '',
      // 商品信息
      productInfo: '',
      // 审核状态
      state: '通过', // 默认为通过
    },
      queryForm: {
        billNumber: '',
        dateRange: [], // 使用数组保存日期范围
        productInfo: '',
      },
      // 死数据
      tableData: [
      { money:'322332',customer:'王总', billNumber: '123', startDate: '2022-01-01', endDate: '2022-08-05', productInfo:'月饼', state:'通过' },
      { money:'425452',customer:'李总',billNumber: '456', startDate: '2022-02-01', endDate: '2022-03-05', productInfo: '水果', state:'未通过' },
      { money:'425522',customer:'刘总',billNumber: '789', startDate: '2022-03-01', endDate: '2022-06-05', productInfo: '辣条', state:'未通过' },
      { money:'46564',customer:'张总',billNumber: '456', startDate: '2022-04-01', endDate: '2022-05-05', productInfo: '饮料', state:'未通过' },
    ],
    // 勾选框
    selectedRows: [],
    };
  },
  created(){
    this.loadData();
  },
  methods: {
    // 退出登录方法
  logout() {
  this.$axios.get('/auth/logout')
    .then(() => {
      localStorage.removeItem('token');
      this.$router.push('/auth/login');
    })
    .catch(error => {
      console.error('Logout failed:', error.response);
      this.$message.error('退出登录失败，请重试');
    });
  },
  // 修改日期时间格式
  formatDate(dateString) {
    const date = new Date(dateString);
    const year = date.getFullYear();
    const month = date.getMonth() + 1;
    const day = date.getDate();
    return `${year}-${month.toString().padStart(2, '0')}-${day.toString().padStart(2, '0')}`;
  },
  // 查找
  handleQuery() {
      // 处理查询逻辑
      console.log('Query Form:', this.queryForm);
  },

  // 勾选变化回调
  handleSelectionChange(selection) {
  this.selectedRows = selection;
  },
  // 重置按钮
  handleReset() {
      // 处理重置逻辑
      this.queryForm = {
        billNumber: '',
        dateRange: [],
        productInfo: '',
      };
  },
  // 搜索按钮
  handleMenuSelect(index) {
      console.log('Selected menu:', index);
  },
  // 提交处理数据 
  handleSubmit() {
   // 取出日期并格式化为 YYYY-MM-DD 的字符串
    const startDate = new Date(this.addFormData.date[0]).toISOString().split('T')[0];
    const endDate = new Date(this.addFormData.date[1]).toISOString().split('T')[0];
      // 发送添加信息的请求
    this.$axios.post('/commodity/add', {
        billNumber: this.addFormData.billNumber,
        startDate: startDate,
        endDate: endDate,
        productInfo: this.addFormData.productInfo,
        state: this.addFormData.state,
        money: this.addFormData.money,
        customer:this.addFormData.customer,
    })
    .then(response => {
      // 添加成功之后刷新页面或重新加载数据
      this.$message.success("添加成功");
      this.addDialogVisible = false;
      console.log(response)
      // 将新的数据添加到表格单当中展示
      this.tableData.push({
        billNumber: this.addFormData.billNumber,
        startDate: startDate,
        endDate: endDate,
        productInfo: this.addFormData.productInfo,
        state: this.addFormData.state,
        money: this.addFormData.money,
        customer:this.addFormData.customer,
      })
      // 重新加载数据，确保新数据显示在当前页
      this.loadData();
    })
    .catch(error => {
        console.error('信息添加失败', error);
        // this.$message.error('信息添加失败');
      });
  },
  // 添加表单
  handleAdd() {
      // 打开添加数据对话框
      this.addDialogVisible = true;
  },
  // 用户添加取消
  handleCancel() {
    this.addFormData = {
      // 客户
      customer:'',
      // 交易金额
      money:'',
      // 开始日期
      start_date:'',
      // 结束日期
      end_date:'',
      // 订单编号
      billNumber: '',
      // 商品信息
      productInfo: '',
    };
    // 关闭添加数据对话框
    this.addDialogVisible = false;
      // 提示用户信息操作取消
      this.$message.info('操作取消');
  },
  // 删除方法
  handleDelete() {
    if (this.selectedRows.length === 0) {
        this.$message.warning('请先勾选数据再进行删除操作');
        return;
    }
    this.$msgbox({
        title: '提示',
        message: '是否删除所选数据?',
        showCancelButton: true,
        confirmButtonText: '是',
        cancelButtonText: '否',
        type: 'error',
    })
        .then(action => {
            if (action === 'confirm') {
                // 像后端发送请求删除该条数据
                this.$axios.post('commodity/delete', {
                    selectedRows: this.selectedRows.map(row => row.billNumber)
                })
                .then(() => {
                    // 删除数据
                    this.tableData = this.tableData.filter(row => !this.selectedRows.includes(row));
                    // 清除表单或者重新加载页面
                    this.$refs.table.clearSelection();
                    // 删除成功提示用户信息
                    this.$message.success('删除成功');
                })
                .catch(error => {
                    console.error('删除失败', error);
                    this.$message.error('删除失败');
                });
            } else {
                this.$message.info('操作已取消');
            }
        })
        .catch(() => {
            this.$message.info('操作已取消');
        });
  },
  // 审核方法
  handleAudit() {
      if (this.selectedRows.length === 0) {
        this.$message.warning('请先勾选数据再进行审核操作');
        return;
      }
      this.$msgbox({
        title: '审核确认',
        message: '是否通过审核所选数据?',
        showCancelButton: true,
        confirmButtonText: '是',
        cancelButtonText: '否',
        type: 'success',
      })
      .then(action => {
        if (action === 'confirm') {
          let hasApprovedData = this.selectedRows.some(row => row.state === '通过');
          if (hasApprovedData) {
            this.$message.warning('勾选的数据已经通过审核');
            return;
          }

          this.selectedRows.forEach(row => {
            row.state = '通过';
          });

          // 向后端发送请求，更新数据库中的数据状态
          this.$axios.post('/commodity/updateState', {
            selectedRows: this.selectedRows
          })
          .then(() => {
            // 更新成功后的操作，例如刷新页面或重新加载数据
            this.$refs.table.clearSelection();
            this.$message.success('审核成功');
          })
          .catch(error => {
            console.error('审核失败', error);
            this.$message.error('审核失败');
          });
        } else {
          this.$message.info('审核已取消');
        }
      })
      .catch(() => {
        this.$message.info('审核已取消');
      });
  },
  // 反审核方法
  handleReview() {
      if (this.selectedRows.length === 0) {
        this.$message.warning('请先勾选数据再进行反审核操作');
        return;
      }
      this.$msgbox({
        title: '提示',
        message: '是否反审核所选数据?',
        showCancelButton: true,
        confirmButtonText: '是',
        cancelButtonText: '否',
        type: 'warning',
      })
      .then(action => {
        if (action === 'confirm') {
          let hasUnapprovedData = this.selectedRows.some(row => row.state === '未通过');
          if (hasUnapprovedData) {
            this.$message.warning('勾选的数据已经是未通过审核状态');
            return;
          }

          this.selectedRows.forEach(row => {
            row.state = '未通过';
          });

          // 向后端发送请求，更新数据库中的数据状态
          this.$axios.post('/commodity/updateState', {
            selectedRows: this.selectedRows
          })
          .then(() => {
            // 更新成功后的操作，例如刷新页面或重新加载数据
            this.$refs.table.clearSelection();
            this.$message.success('反审核成功');
          })
          .catch(error => {
            console.error('反审核失败', error);
            this.$message.error('反审核失败');
          });
        } else {
          this.$message.info('操作已取消');
        }
      })
      .catch(() => {
        this.$message.info('操作已取消');
      });
  },
  // 导出方法
  handleExport() {
    if (this.tableData.length === 0) {
      this.$message.warning('没有数据可导出');
      return;
    }

    const worksheet = XLSX.utils.json_to_sheet(this.tableData);
    const workbook = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(workbook, worksheet, 'Sheet 1');

    // Save the file
    XLSX.writeFile(workbook, 'exported_data.xlsx');

    this.$message.success('导出成功');
  },
  // 获取数据的方法
  loadData() {
      const startIndex = (this.currentPage - 1) * this.pageSize;
      const endIndex = startIndex + this.pageSize;
      this.$axios.get('/commodity/all')
        .then(response => {
          this.total = response.data.length; // 获取总条数
          this.tableData = response.data.slice(startIndex, endIndex); // 根据页码和每页显示条数截取需要展示的数据
        })
        .catch(error => {
          console.error('加载数据失败', error);
          this.$message.error('加载数据失败');
        });
  },
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

