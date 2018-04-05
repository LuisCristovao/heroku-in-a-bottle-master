#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os import environ as env
from sys import argv

import bottle
from bottle import default_app, request, route, response, get

bottle.debug(True)

@get('/')
def index():
    

    return '''<h1 id="random"></h1><script>document.getElementById("random").innerHTML=Math.random()*10;</script>'''

bottle.run(host='0.0.0.0', port=argv[1])
