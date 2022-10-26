from flask import Flask,url_for,redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    print("首先访问了index()这个函数了！")
    url1 = url_for('user_login')
    return redirect(url1)


@app.route('/user_login')
def user_login():
    return "这是用户登录页面，请您登陆，才能访问首页"


if __name__ == '__main__':
    app.run()
