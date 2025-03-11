from flask import Flask, render_template

# 创建 Flask 应用
app = Flask(__name__)

# 定义主页路由
@app.route('/')
def home():
    return render_template("index.html")


# 运行应用
if __name__ == '__main__':
    app.run(debug=True, port=80)