from tornado.platform.asyncio import AsyncIOMainLoop
import asyncio
import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
AsyncIOMainLoop().install()
asyncio.get_event_loop().run_forever()
