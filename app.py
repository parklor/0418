from flask import Flask, render_template
from flask import send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def index():
    # 定義要傳給網頁的資料
    user_data = {
        "name": "Luo Wan-hsun"
    }
    # 關鍵點：後面的 user=user_data 必須寫，HTML 才能抓到 'user' 這個變數
    return render_template("index.html", user=user_data)

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/results")
def results():
    return render_template("results.html")

@app.route("/mis-test")
def mis_test():
    return render_template("mis_test.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

from flask import send_from_directory
import os

# 加入這段路由處理 image 資料夾
@app.route('/image/<path:filename>')
def custom_static(filename):
    # 這裡會去你根目錄的 image 資料夾找檔案
    return send_from_directory(os.path.join(app.root_path, 'image'), filename)

if __name__ == "__main__":
    app.run(debug=True)