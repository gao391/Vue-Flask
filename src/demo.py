from flask import Blueprint, redirect, session, request, jsonify
from exts import db
from Models.models import Users
from Models.models import Employee
import traceback
from datetime import datetime
bp = Blueprint('employee', __name__, url_prefix="/employee")

# 添加员工考勤员工考勤路由
@bp.route('/Attendance/add', methods=['GET' ,'POST'])
def add_attendance():
    try:
        data = request.json
        name = data.get('name')
        position = data.get('position')
        start_date_str = data.get('start_date')
        start_date = datetime.strptime(start_date_str, '%Y-%m-%dT%H:%M:%S.%fZ')
        status = data.get('status')
        on_duty = data.get('on_duty')
        end_date = data.get('end_date') or None

        # 创建员工考勤对象
        employee = Employee(
            name=name,
            position=position,
            start_date=start_date,
            status=status,
            on_duty=on_duty,
            end_date=end_date   
        )
        # 将员工考勤对象添加到数据库
        db.session.add(employee)
        db.session.commit()

        # 返回添加的员工考勤信息
        return jsonify({
            'message': 'Employee attendance data added successfully',
            'employee': {
                'id': employee.id,
                'name': employee.name,
                'position': employee.position,
                'start_date': employee.start_date.strftime('%Y-%m-%d'),
                'status': employee.status,
                'on_duty': employee.on_duty,
                'end_date': employee.end_date.strftime('%Y-%m-%d') if employee.end_date else None
            }
        }), 201
    except Exception as e:
        db.session.rollback()
        error_message = traceback.format_exc()
        return jsonify({'message': 'Failed to add employee attendance data', 'error': str(e), 'traceback': error_message}), 500

# 前端来获取所有员工考勤信息
@bp.route('/Attendance/all', methods=['GET', 'POST'])
def get_all_attendance():
    try:
        employees = Employee.query.all()
        employee_data = []
        for employee in employees:
            employee_data.append({
                'id': employee.id,
                'name': employee.name,
                'position': employee.position,
                'start_date': employee.start_date.strftime('%Y-%m-%d'),
                'status': employee.status,
                'on_duty': employee.on_duty,
                'end_date': employee.end_date.strftime('%Y-%m-%d') if employee.end_date else None
            })
        return jsonify(employee_data), 200
    except Exception as e:
        error_message = traceback.format_exc()
        return jsonify({'message': 'Failed to fetch employee attendance data', 'error': str(e), 'traceback': error_message}), 500

# 编辑员工路由信息将员工信息重新更新到页面上
@bp.route('/Attendance/edit', methods=['GET', 'POST'])
def edit_attendance():
    try:
        data = request.json
        employee_id = data.get('id')
        employee = Employee.query.get(employee_id)
        if not employee:
            return jsonify({'message': 'Employee not found'}), 404

        employee.name = data.get('name')
        employee.position = data.get('position')
        employee.start_date = datetime.strptime(data.get('start_date'), '%Y-%m-%d')
        employee.status = data.get('status')
        employee.on_duty = data.get('on_duty')
        employee.end_date = datetime.strptime(data.get('end_date'), '%Y-%m-%d') if data.get('end_date') else None

        db.session.commit()

        return jsonify({'message': 'Employee information updated successfully'}), 200
    except Exception as e:
        db.session.rollback()
        error_message = traceback.format_exc()
        return jsonify({'message': 'Failed to update employee information', 'error': str(e), 'traceback': error_message}), 500

# 员工转正路由信息
@bp.route('/Attendance/Employee_regularization', methods=['POST'])
def convert_to_full_time():
    data = request.json
    employee_id = data.get('id')

    employee = Employee.query.get(employee_id)
    if not employee:
        return jsonify({'message': 'Employee not found'}), 404

    employee.status = '正式工'
    db.session.commit()

    return jsonify({'message': 'Employee status updated successfully', 'employee': employee.serialize()}), 200

# 在 Flask 蓝图中添加以下路由
@bp.route('/Attendance/resign', methods=['POST'])
def resign_employee():
    try:
        data = request.json
        employee_id = data.get('id')
        # end_date_str = data.get('end_date')
        # end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
        end_date_str = data.get('end_date')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%dT%H:%M:%S.%fZ')
        reason = data.get('reason')
        status = data.get('status')
        on_duty = data.get('on_duty')

        # 更新员工信息，标记为离职
        employee = Employee.query.get(employee_id)
        employee.end_date = end_date
        employee.status = status
        employee.on_duty = on_duty

        db.session.commit()

        return jsonify({'message': 'Employee resigned successfully'}), 200
    except Exception as e:
        db.session.rollback()
        error_message = traceback.format_exc()
        return jsonify({'message': 'Failed to resign employee', 'error': str(e), 'traceback': error_message}), 500
# ------------------------------------------------------------------------ #
    

    from exts import db
from werkzeug.security import generate_password_hash, check_password_hash


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Commodity(db.Model):
    __tablename__ = 'commodity'
    id = db.Column(db.Integer, primary_key=True)
    bill_number = db.Column(db.String(255, collation='utf8_general_ci'))
    date = db.Column(db.Date)
    product_info = db.Column(db.String(255, collation='utf8_general_ci'))
    state = db.Column(db.String(255, collation='utf8_general_ci'))


class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 名字
    name = db.Column(db.String(255), nullable=False)
    # 职位
    position = db.Column(db.String(255), nullable=False)
    # 入职日期
    start_date = db.Column(db.Date, nullable=False)
    # 离职日期
    end_date = db.Column(db.Date, default=None)
    # 员工状态
    status = db.Column(db.String(255), nullable=False)
    # 是否在岗位
    on_duty = db.Column(db.String(255), nullable=False)
    # 是否离职
    is_delete = db.Column(db.Boolean, default=False, nullable=False)
    # 离职原因
    reason_for_leaving = db.Column(db.String(512), nullable=True)
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'position': self.position,
            'start_date': self.start_date.strftime('%Y-%m-%d'),
            'status': self.status,
            'on_duty': self.on_duty,
            'end_date': self.end_date.strftime('%Y-%m-%d') if self.end_date else None,
            'reason_for_leaving': self.reason_for_leaving,
        }