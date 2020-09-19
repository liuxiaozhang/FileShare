# 通用配置
import socket
class Config:
    DEBUG = True
    LOCAL_IP = socket.gethostbyname(socket.gethostname())
    LOCAL_PORT = 8080
    SECRET_KEY = "123456aaaaafdaw"
    SERVER_NAME = None

    # sql连接地址
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://FileShare:password@127.0.0.1:3306/FileShare'

    # http://www.pythondoc.com/flask-sqlalchemy/config.html?highlight=sqlalchemy_track_modifications
    # 官方建议关闭
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_ECHO = True

# 开发环境配置
class DevelopmentConfig(Config):
    ENV = 'development'
    secret_key = 'abc123456'

# 生产环境配置
class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False
