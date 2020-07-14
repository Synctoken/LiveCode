

'''
Start APP
'''

from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect


import random
import os
import jinja2

# 初始化Flask应用并设置Static静态文件访问
app = Flask(__name__,static_url_path='/static',
            static_folder='static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite3.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['SECRET_KEY'] = 'some key'


db = SQLAlchemy(app)




class View():
    # 处理渲染的各种内容
    def getBase(self,body):
        nav = jinja2.Template(open('templates/nav/nouser.html','r',encoding="utf-8").read()).render()
        return jinja2.Template(open('templates/base.html','r',encoding="utf-8").read()).render(body=body,nav=nav)
    
    def getindex(self):
        body = jinja2.Template(open('templates/index.html','r',encoding="utf-8").read()).render()
        return self.getBase(body=body)
    
    def getregister(self):
        body = jinja2.Template(open('templates/register.html','r',encoding="utf-8").read()).render()
        return self.getBase(body=body)


view = View()



@app.route('/')
def viewIndex():
    return view.getindex()

@app.route('/join')
def viewRegister():
    return view.getregister()



app.run()



