#coding:utf-8
from flask import Flask, make_response, request, session, render_template, redirect
import paramiko
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/')
def home():
    # session['username'] = 'emergency'
    return '登录界面'

@app.route('/index')
def index():
    return '登录成功界面'





@app.route('/login',methods=['GET','POST'])
def login():
    # key = {'admin':'passwd'}
    if request.method == 'GET':

        if 'username' in session:
            return redirect('/index')
        else:
            if 'username' in request.cookies:
                uname = request.cookies.get('username')
                session['username'] = uname
                return redirect('/')
            else:
                return render_template('login.html')

    else:
        uname = request.form.get('username')
        upwd = request.form.get('password')
        if uname == 'admin' and upwd == 'passwd':
            resp = redirect('/index')
            session['username'] = uname
            if 'isSaved' in request.form:
                resp.set_cookie('username', uname, 60 * 60 * 24 * 365)
            return resp
        else:
            return redirect('login')




























# 执行插入sql语句
def emergency_do(cmd):

    # if drill_num == 1:


    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='172.20.13.231', port=22, username='root', password='Passw0rd')
    stdin, stdout, stderr = ssh.exec_command(cmd)
    print(stdout.read().decode())
    print(stderr.read().decode())
    # print(stdout.read().decode())
    ssh.close()

cmd = "nco_sql -server CSLCOBJ_V -user root -password '' < /root/data1.sql"
# emergency_do(cmd)

# emergency_do(1)























if __name__ == '__main__':
    # CORS(app,support_credentials=True)
    app.run(debug=True,port=5000)