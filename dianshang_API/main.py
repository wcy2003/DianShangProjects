from flask import Flask
from flask_cors import CORS
# 构建
app = Flask(__name__)
# 跨域请求处理
CORS(app)
# 路由
@app.route("/")
def index():
    return "Hello world"
# 启动程序
app.run(debug=True)