import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Flask应用配置类
    SECRET_KEY = 'dev'  # 设置密钥
    
    # SQLAlchemy配置
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
