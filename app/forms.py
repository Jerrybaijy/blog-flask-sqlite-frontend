from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import User

# 登录表单
class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    submit = SubmitField('登录')

# 注册表单
class RegistrationForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    password = PasswordField('密码', validators=[DataRequired()])
    password2 = PasswordField('确认密码', validators=[
        DataRequired(),
        EqualTo('password', message='两次输入的密码不一致！')
    ])
    submit = SubmitField('注册')

    def validate_username(self, username):
        # 验证用户名是否已存在
        if User.query.filter_by(username=username.data).first():
            raise ValidationError('该用户名已被使用！')  # 表单验证错误

    def validate_email(self, email):
        # 验证邮箱是否已存在
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('该邮箱已被注册！') 