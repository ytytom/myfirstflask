#coding: utf-8
from flask import Flask
from flask_cors import CORS
from flask_restful import Api,Resource
from flask import url_for
from flask import redirect
from flask import render_template
from flask import request
import datetime
from flask import Flask, make_response, request, session, render_template, redirect


import json
app = Flask(__name__)
#app.config.from_object(config)
api = Api(app)
CORS(app, supports_credentials=True)
app.config['SECRET_KEY']='aixieshaxiesha,yuefuzayuehao%$'
todos = {}


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        if 'uname' in session:
            return redirect('/')

        else:
            if 'uname' in request.cookies:
                uname = request.cookies.get('uname')
                session['uname'] = uname
                return redirect('/')
            else:
                return render_template('login.html')

    else:
        uname = request.form.get('uname')
        upwd = request.form.get('upwd')
        if uname == 'admin' and upwd == 'admin':
            resp = redirect('/')
            session['uname'] = uname
            if 'isSaved' in request.form:
                resp.set_cookie('uname',uname,60*60*24*7)
            return resp
        else:
            return redirect('login')














class test_Api(Resource):
    def get(self):
        return {'hello': 'world'}
    # def put(self):

api.add_resource(test_Api,'/test_Api')


class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id:todos[todo_id]}
    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id:todos[todo_id]}


api.add_resource(TodoSimple,'/test_Api1/<string:todo_id>')

# class emergency(Resource):
#     def get(self,yuan):
#         return

#请求当前时间的API
class Timenow(Resource):
    def get(self):
        return {'time':str(datetime.datetime.now())}

api.add_resource(Timenow,'/time')



# 请求预案的API
class emergency_drill(Resource):
    def get(self,drillnum):
        if drillnum == 'str':
            return {"my sql" : "select * form alerts"}

api.add_resource(emergency_drill,'/emergency/<string:drillnum>')



emergency_form = {
    1:{'name':'广域网单边链路中断应急预案'},
    2:{'name':'广域网单边链路丢包应急预案'},
    3:{'name':'次生产互联网区域YZXCRT03路由器故障应急预案'},
    4:{'name':'次生产区域第三方IpSec接入网关第一台YZXIPSECFW04故障应急预案'},
    5:{'name':'次生产区域第三方IpSec接入网关第二台YZXIPSECFW05故障应急预案'},
    6:{'name':'次生产区域第三方路由器故障应急预案'},
    7:{'name':'省市体彩中心数据端二次认证服务失效应急预案'},
    8:{'name':'虚拟化环境rtp单机失效启用备机应急预案'},
    9:{'name':'高频Windows群集故障应急预案'},
    10:{'name':'高频数据库主节点NTP服务异常停止应急预案'},
    11:{'name':'乐透二代GoldenGate包状态异常应急预案'},
    12:{'name':'ESXi宿主机网络隔离故障应急预案'},
    13:{'name':' SSL网关异常宕机应急预案'},
    14:{'name':' 从LDAP服务器进程异常停止应急预案'}
}






class emergency_form_get(Resource):
    def get(self, drill_num):
        return emergency_form[drill_num]
    def put(self, drill_num):
        emergency_test(drill_num)

        # drill_id = int(max(emergency_form.keys())) + 1
        # drill_id = '%i' % drill_id
        # drill_id = {'name':request.form['name']}

        return emergency_form[drill_num]
api.add_resource(emergency_form_get,'/drill/<int:drill_num>')



def emergency_test(drill_num):
    for key in emergency_form.keys():
        if drill_num == key:
            print emergency_form[key].values()







#
# drill = {}
#
# # 执行预案的API
# class emergency_action(Resource):
#     def post(self,time,dirllnum):
#         for i in drill:
#             if dirllnum == i:
#                 # return drill的sql
#                 return drill
#                 dosometiong(drill)
#





# def dosometiong(drillnum):
    # test = os.popen('ll -lrht| grep %s',%drillnum ).read()
    # print test

@app.route('/')
def hello_world():
    print (url_for('index'))
    #url 翻转
    #url 反转用的是路由下的函数名
    test = url_for('index')
    return redirect(test)
    print (url_for('show_user_profile',username="DDM"))
    return 'Hello World! tetetes'

@app.route('/index')
def index():
    return u'欢迎来到首页'

@app.route('/index/login')
def index_login():
    #用后台给前台传送数据的方法之一
    return render_template('/18.x/18.3/index.html',username=u'杨廷耀',passwd='123456')
    #index.html只是相对路径，flask只会去templates目录下去寻找(目录名字错了都会报错)
@app.route('/index/login2')
def index_login2():
    #用后台给前台传送数据的方法之一
    return render_template('/18.x/18.8/index.html')
    #index.html只是相对路径，flask只会去templates目录下去寻找(目录名字错了都会报错)

@app.route('/index/login1')
def index_login1():
    context = {
        'username':u'杨廷耀',
        'passwd':'1234567789',
        'name': 'DDM',
        'age': '12',
        'sex': u'男',
    }
    #用后台给前台传送数据的方法之一
    return render_template('/18.x/18.1/index.html',**context)

@app.route('/user/<username>/')
def show_user_profile(username):
    # show the user profile for that user
    #请求的参数
    #这个参数就可以用到后台去
    return u'你请求的用户名为  User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id






if __name__ == '__main__':
    CORS(app,support_credentials=True)
    app.run(debug=True,port=5000)



# 在模板中使用一个变量要{{params}}
