from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

# 创建扩展实例
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

# 创建应用实例
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SECRET_KEY'] = 'dev'  # 用于生成令牌的密钥
    
    # 初始化扩展
    db.init_app(app)
    login_manager.init_app(app)
    
    # 注册蓝图
    from app.routes import main
    from app.auth import auth
    app.register_blueprint(main)
    app.register_blueprint(auth)
    
    # 创建数据库表
    with app.app_context():
        db.create_all()
    
    return app
