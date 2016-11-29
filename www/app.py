import logging; logging.basicConfig(level=logging.INFO)

import asyncio,os,json,time,aiomysql
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h2>bole</h2>')


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    server=yield from loop.create_server(app.make_handler(), '127.0.0.1', 5000)
    logging.info('server started at http://127.0.0.1:5000...')
    return server

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

@asyncio.coroutine
def create_pool(loop,**kw):
    logging.info('create database connection pool...')
    global __pool
    __pool=yield from aiomysql.create_pool(
        host=kw.get('host', '10.104.20.123'),
        port=kw.get('port', 3306),
        user=kw['developer'],
        password=kw['developer1015'],
        db=kw['awesome'],
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )

@asyncio.coroutine
def select(sql,args,size=None):
    log(sql,args)
