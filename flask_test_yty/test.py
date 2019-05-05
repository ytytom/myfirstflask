#coding: utf-8
from flask import Flask
from flask_cors import CORS
#import config
from flask_restful import Api,Resource
from flask import url_for
from flask import redirect
from flask import render_template
from flask import request
import datetime
import os


import json
app = Flask(__name__)
#app.config.from_object(config)
api = Api(app)
CORS(app, supports_credentials=True)

todos = {}

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
api.add_resource(Timenow,'/time/')



# 请求预案的API
class emergency_drill(Resource):
    def get(self,drillnum):
        if drillnum == 'str':
            return {"my sql" : "select * form alerts"}

api.add_resource(emergency_drill,'/emergency/<string:drillnum>')


drill={}
# 执行预案的API
class emergency_action(Resource):
    def post(self,time,dirllnum):
        for i in drill:
            if dirllnum == i:
                # return drill的sql
                return drill
                dosometiong(drill)















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
    return u'瞎鸡巴跳着玩'

@app.route('/index/login')
def index_login():
    #用后台给前台传送数据的方法之一
    return render_template('/18.x/18.1/index.html',username=u'杨廷耀',passwd='123456')
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
