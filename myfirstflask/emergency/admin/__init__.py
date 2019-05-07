from flask import Blueprint,Flask,render_template,request,url_for,session,redirect,make_response
from flask_restful import Api,Resource,reqparse


admin = Blueprint(
    'admin',
    __name__,
    template_folder='templates',
    static_folder='statics'
)
app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY']='12344'
app.secret_key='12344'
parser = reqparse.RequestParser()


parser.add_argument('task', type=str)

class user_login(Resource):
    def post(self):
        # username = {'username':request.form.get['username']}
        # password = {'password':request.form.get['password']}
        # username = request.args.get('username')
        # password = request.args.get('password')
        args = parser.parse_args()
        username = {'username':args['username']}
        password = {'password':args['password']}
        key = {'admin': 'Cslc@pass'}
        if username == key.keys() and password == key.values():
            print 22222222
            return render_template('emergency.html')

api.add_resource(user_login,'/login/')




@admin.route('/emergency/')
def emergency():
    return render_template('emergency.html')

@admin.route('/login1/', methods=['GET','POST'])
def login():
    return render_template('login.html')
    # key = {'admin':'Cslc@pass'}
    # if request.method == 'GET':
    #
    #     if 'uname' in session:
    #         return redirect('/index')
    #     else:
    #         if 'uname' in request.cookies:
    #             uname = request.cookies.get('uname')
    #             session['uname'] = uname
    #             return redirect('/')
    #         else:
    #             return render_template('login.html')
    #
    # else:
    #     uname = request.form.get('uname')
    #     upwd = request.form.get('upwd')
    #     if uname == 'admin' and upwd == 'admin':
    #         resp = redirect('/')
    #         session['uname'] = uname
    #         if 'isSaved' in request.form:
    #             resp.set_cookie('uname', uname, 60 * 60 * 24 * 365)
    #         return resp
    #     else:
    #         return redirect('login')



    # return render_template('login.html')