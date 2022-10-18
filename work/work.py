from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)
@app.route("/")
def index():
    homepage = "<h1>資管二B 411003887 張家榛</h1>"
    homepage += "<a href=/introduce>我的個人簡介</a><br>"
    homepage += "<a href=/mis>MIS相關工作介紹</a><br>"
    homepage += "<a href=/a>職涯測驗結果</a><br>"
    homepage += "<a href=/autobiography>自傳</a><br>"
    return homepage




@app.route("/introduce")
def introduce():
    
    return render_template("introduce.html")

@app.route("/mis")
def mis():
    
    return render_template("mis.html")

@app.route("/a")
def a(): 

    return render_template("a.html")

@app.route("/autobiography")
def autobiography():
    
    return render_template("autobiography.html")



if __name__ == "__main__":
    app.run()
        
