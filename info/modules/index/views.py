# -*- coding: utf-8 -*-
# @Time    : 2020/6/16 11:39
# @Author  : Eric Lee
# @Email   : li.yan_li@neusoft.com
# @File    : views.py
# @Software: PyCharm
from flask import render_template, current_app, session

from info.models import User
from . import index_blu
@index_blu.route('/')
def index():
    #获取当前用户id
    user_id = session.get('user_id')
    user = None
    #通过id查询用户信息
    if user_id:
        try:
            user = User.query.get(user_id)
        except Exception as e:
            current_app.logger.error(e)



    return render_template('news/index.html',data={'user_info':user.to_dict() if user else None})
    # return "dada"
#浏览器在访问,在访问每个网站的时候,都会发送一个Get请求,向/favicon.ico地址获取logo
#app中提供了方法send_static_file,会自动寻找static静态文件下面的资源
@index_blu.route('/favicon.ico')
def get_web_logo():

    return current_app.send_static_file('news/favicon.ico')