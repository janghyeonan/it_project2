import sys
sys.path.append('/Users/janghyeonan/flask')
from flask import Flask, render_template, request, redirect
from werkzeug import secure_filename
import sqlite3
import os
import glob
import random
import google_speech

UPLOAD_FOLDER = '/Users/janghyeonan/flask/tmp/'
ALLOWED_EXTENSIONS = set(['wav'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/ff", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'sound.wav'))
            tts = google_speech.st_change('/Users/janghyeonan/flask/tmp/sound.wav')
            return render_template('talk_result.html', ff = tts)
    return """
    <!doctype html>
    <form action="" method=post enctype=multipart/form-data>
    <center><h1>억양에 따른 감정 평가</h1></center>
    <center>위에 표시된 내용을 감정을 섞어 얘기해주세요</center>
    <center>
    <table>
    <tr>
    <td><img src='../static/img/%s.jpg' height ='400px' width='300px' /></td>
    </tr>
    </table>
    </center>
    <center>
    <p><input type=file name=file>
    <input type=submit value=Upload>
    </center>
    </form>
    """ % "<br>".join(str(random.randint(1,3)))

@app.route("/")
def run():
    conn = sqlite3.connect('wanggun.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM general')
    rows = c.fetchall();
    return render_template("index.html", rows=rows)


@app.route('/modi')
def modi():
    id = request.args.get("id")

    conn = sqlite3.connect('wanggun.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM general where id=' + str(id))
    rows = c.fetchall();

    return render_template('modi.html', rows=rows)


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            war = request.form['war']
            id = request.form['id']

            with sqlite3.connect("wanggun.db") as con:
                cur = con.cursor()

                cur.execute("update general set war=" + str(war) + " where id=" + str(id))

                con.commit()
                msg = "정상적으로 입력되었습니다."
        except:
            con.rollback()
            msg = "입력과정에서 에러가 발생했습니다."

        finally:
            return render_template("result.html", msg=msg)
            con.close()


@app.route('/intro', methods=['POST', 'GET'])
def intro():
    if request.method == 'POST':
        return render_template('step.html')
    return render_template('intro.html')

@app.route('/step', methods=['POST', 'GET'])
def step():
    if request.method == 'POST':
        return render_template('step1.html')
    return render_template('step.html')

@app.route('/step1', methods=['POST', 'GET'])
def step1():
    if request.method == 'POST':
        return render_template('step2.html')
    return render_template('step1.html')

@app.route('/step2', methods=['POST', 'GET'])
def step2():
    if request.method == 'POST':
        return render_template('step3.html')
    return render_template('step2.html')

@app.route('/step3', methods=['POST', 'GET'])
def step3():
    if request.method == 'POST':
        return render_template('step4.html')
    return render_template('step3.html')

@app.route('/step4', methods=['POST', 'GET'])
def step4():
    if request.method == 'POST':
        return render_template('end.html')
    return render_template('step4.html')

@app.route('/end', methods=['POST', 'GET'])
def end():
    if request.method == 'POST':
        return render_template('report.html')
    return render_template('end.html')

@app.route('/report', methods=['POST', 'GET'])
def report():
    if request.method == 'POST':
        return render_template('index.html')
    return render_template('report.html')

@app.route('/talk', methods=['POST', 'GET'])
def talk():
    if request.method == 'POST':
        return render_template('talk_result.html')
    return render_template('talk.html', img ="../static/img/"+str(random.randint(1,3))+".jpg" )

@app.route('/talk_result', methods=['POST', 'GET'])
def talk_result():
    if request.method == 'POST':
        return render_template('index.html')
    return render_template('talk_result.html')

@app.route('/index2', methods=['POST', 'GET'])
def index2():
    if request.method == 'POST':
        return render_template('index.html')
    return render_template('index2.html')

@app.route('/audio', methods=['POST', 'GET'])
def audio():
    return render_template('record-live-audio.html')

app.run(host='localhost', port=8787, debug=True)
