#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# http://www.mingjiao.org:8088/

from flask import Flask, abort
import time
import argparse
from datetime import datetime
import os

node = Flask(__name__)

startup_delay = int(os.environ['startup_delay'])
liveliness_time = int(os.environ['liveliness_time'])
readiness_time = int(os.environ['readiness_time'])
startup_time = datetime.now()


# 静态路由,最简单页面
@node.route('/', methods=['GET'])
def index():
    return "qytang index"


@node.route('/startup', methods=['GET'])
def startup():
    now_time = datetime.now()
    if (now_time - startup_time).seconds > startup_delay:
        return f"qytang startup {startup_delay}"
    else:
        time.sleep(5)  # 制造超时


@node.route('/ready', methods=['GET'])
def readiness():
    now_time = datetime.now()
    if (now_time - startup_time).seconds > readiness_time:
        abort(404)
    else:
        return f"qytang ready"


@node.route('/live', methods=['GET'])
def liveliness():
    now_time = datetime.now()
    if (now_time - startup_time).seconds > liveliness_time:
        abort(404)
    else:
        return f"qytang live"


if __name__ == "__main__":
    node.run(host='0.0.0.0', port=8000)


