import trollius as asyncio
from trollius import From
 
@asyncio.coroutine
def my_coroutine(future, task_name, seconds_to_sleep=3):
    print('my_coroutine sleeping for: {0} seconds'.format(seconds_to_sleep))
    yield From(asyncio.sleep(seconds_to_sleep))
    1/0
    future.set_result('{0} is finished'.format(task_name))
 
loop = asyncio.get_event_loop()

def got_result(future):
    print future.result()

future1 = asyncio.Future()
future2 = asyncio.Future()

tasks = [
            my_coroutine(future1, 'task1', 3),
            my_coroutine(future2, 'task2', 1)]

future1.add_done_callback(got_result)
future2.add_done_callback(got_result)


loop.run_until_complete(
    asyncio.wait(tasks)
)
loop.close()
