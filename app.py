# !/user/bin/env python
# -*- coding:utf-8 -*-
# time: 2018/3/7--19:49
from flask import Flask
from flask import render_template, url_for, redirect, flash, session, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('./test.html')


if __name__ == '__main__':
    app.run()
