#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Xiuqin Gao'

import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get, post

from models import User, Comment, Blog, next_id

@get('/')
async def index(request):
    users = await User.findAll()
    comments = await Comment.findAll()
    return {
        '__template__': 'test.html', # the designated template is test.html, we create test.html under templates
        'users': users,
        'comments': comments
    }