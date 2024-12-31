from flask import Blueprint, render_template
from flask_login import login_required, current_user

# 创建蓝图
main = Blueprint('main', __name__)

# 主页路由
@main.route('/')
def home():
    return render_template('index.html')

@main.route('/profile')
@login_required  # 这个装饰器会触发load_user来检查用户是否登录
def profile():
    return f'Hello, {current_user.username}!'
