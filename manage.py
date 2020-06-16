# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 17:43
# @Author  : Eric Lee
# @Email   : li.yan_li@neusoft.com
# @File    : manage.py.py
# @Software: PyCharm
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import db,create_app

app = create_app('develop')

manager = Manager(app)
#数据库迁移
Migrate(app, db)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()