from flask import Flask, url_for, redirect
# 创建flask实例
app = Flask(__name__)


@app.route('/')
def index():
    # url_for第一个参数就是endpoint
    login_url = url_for('login', name="tony")
    print(login_url)  # 打印 /login/tony
    return redirect(login_url)  # 自动跳转到另一个URL所在的地址
    return '这是首页'


@app.route('/login/<name>')
def login(name):
    print("name=", name)
    return '这是登录页面'


if __name__ == '__main__':
    app.run()  # 默认端口5000
