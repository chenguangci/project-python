import asyncio, os, json, time
import logging; logging.basicConfig(level=logging.INFO)
from datetime import datetime
from aiohttp import web


routes = web.RouteTableDef()


@routes.get('/')
async def index():
    return web.Response(body='<h1>Hello BeiYi</h1>'.encode('utf-8'), content_type='text/html')


def init():
    app = web.Application()
    app.router.add_routes(routes)
    logging.info('Server started at http://127.0.0.1:8080')
    web.run_app(app, host='127.0.0.1', port=8080)


init()
