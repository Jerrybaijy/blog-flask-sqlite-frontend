from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.forms import LoginForm, RegistrationForm
from app.models import User
from app import db

# 创建蓝图
auth = Blueprint('auth', __name__)

# 登录路由
@auth.route('/login', methods=['GET', 'POST'])
def login():
    # 如果已登录则重定向到首页
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user or not user.check_password(form.password.data):
            flash('用户名或密码错误')
            return redirect(url_for('auth.login'))
        
        login_user(user)
        return redirect(url_for('main.home'))
    
    return render_template('auth/login.html', form=form)

# 注册路由
@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('注册成功!')
        return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html', form=form)

# 登出路由
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home')) 