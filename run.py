from app import create_app

# 创建应用实例
app = create_app()

if __name__ == '__main__':
    # 以调试模式运行应用
    app.run(debug=True)
