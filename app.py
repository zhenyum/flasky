from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    title = 'python的键值对'
    author = 'tom_jack'
    # return render_template('index.html',var1=title,var2=author)
    # 如果视图有多个变量值都需要传递给模板，可以使用**locals()方法
    return render_template('index.html', **locals())


@app.route('/user/<username>')
def user(username):
    return render_template("user.html")


if __name__ == '__main__':
    app.run(debug=True)