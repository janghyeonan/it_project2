import sys
sys.path.append('/Users/janghyeonan/flask')
from flask import Flask, render_template, request, redirect
from werkzeug import secure_filename
import os
import glob
import random

import google_speech
#import emotionPre
import main

UPLOAD_FOLDER = '/Users/janghyeonan/flask/tmp/' #업로드 파일 넣는 경로
ALLOWED_EXTENSIONS = set(['wav'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route("/analysis", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'sound.wav'))
            tts = google_speech.st_change('/Users/janghyeonan/flask/tmp/sound.wav')  #업로드한 파일의 경로
            #emo = emotionPre.main()#감정분석 #이전꺼
            emo = main.models()#감정분석
            return render_template('talk_result.html', ff = tts, gg = emo)

    return """
    <!doctype html>
    <style type="text/css">
    a { text-decoration:none }
    </style>
    <a href="/">첫화면</a>
    <form action="" method=post enctype=multipart/form-data>
    <br />
    <center><h1>✮억양에 따른 감정 분석✮</h1></center>
    <center><h2>아래 사진을 보고, 감정적으로 한마디 해주세요.</h2></center>
    <center>
    <table>
    <tr>
    <td><img src='../static/img/%s.PNG' height ='600px' width='500px' /></td>
    </tr>
    </table>
    </center>
    <center>- wav 파일생성은 여기서 <a href='https://vocaroo.com' target="_blank">클릭</a></center>
    <center>
    <p><input type=file name=file>
    <input type=submit value=업로드>    <font color ='red' size='2pt'>(파일 없이 누르면 에러나요!)</font>
    </center>
    </form>
    """ % "<br>".join(str(random.randint(1,8)))

@app.route('/talk_result', methods=['POST', 'GET'])
def talk_result():
    return render_template('talk_result.html', dd = 'dd')

@app.route("/")
def run():
    return render_template("index.html")

app.run(host='0.0.0.0', port=8787, debug=True)
