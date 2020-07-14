

'''
Start APP
'''

from app import *

import random
import os

# 初始化Flask应用并设置Static静态文件访问
app = Flask(__name__,static_url_path='/static',
            static_folder='static')






