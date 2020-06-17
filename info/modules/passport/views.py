from flask import request

from . import passport_blu

@passport_blu.route('/image_code')
def get_image_code():
    request.args.get()