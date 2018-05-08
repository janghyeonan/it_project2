import sys
sys.path.append('/Users/janghyeonan/flask') #다른 클래스 파일들을 불러오기 위한 경로 설정
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
            if tts =='음':
                tts = '인식이 잘 되지 않았네요.'
            #emo = emotionPre.main()#감정분석 #이전꺼
            emo, acc = main.models()#감정분석
            acc = '(' +str(acc*100)[0:4] + '%)'
            return render_template('talk_result.html', ff = tts, gg = emo, zz = acc)

    return """
    <!doctype html>
    <style type="text/css">
    a { text-decoration:none }
    </style>
    <a href="/">메인화면으로 이동</a>
    <form action="" method=post enctype=multipart/form-data>
    <br />
    <center><h1>✮음성분석을 통한 감정분류✮</h1></center>
    <center><h3>아래 사진을 보고, 말한 내용을 파일로 저장하여 업로드 해주세요. 감정이 나옵니다.</h3></center>
    <center>
    <table>
    <tr>
    <td><img src='../static/img/%s.PNG' height ='400px' width='300px' /></td>
    </tr>
    </table>
    </center>
    <center><font size ='5pt'> WAV 파일생성은 여기서 ->  <a href='https://vocaroo.com' target="_blank">클릭</a></font></center>
    <center><br/>
    <p><input type=file name=file>
    <input type=submit value=업로드>
    </center>
    </form>
    """ % "<br>".join(str(random.randint(1,8)))

@app.route('/talk_result', methods=['POST', 'GET'])
def talk_result():
    return render_template('talk_result.html')

@app.route("/")
def run():
    return render_template("index.html")

#예외 처리 구문 400에러
@app.errorhandler(400)
def uncaughtError(error):
    return """<script>alert('파일을 넣어주세요.');location.href='/analysis';</script>"""

#에러 처리 구문 500에러
@app.errorhandler(500)
def uncaughtError(error):
    return """<script>alert('업로드한 파일이 이상합니다. 다른 파일을 넣어주세요.');location.href='/analysis';</script>"""

app.run(host='0.0.0.0', port=8787, debug=False)