# coding: utf-8

from celery import Celery

broker = 'redis://127.0.0.1:6379/5'
backend = 'redis://127.0.0.1:6379/5'

MY_QUEUE_NAME = 'qq'

app = Celery('queue_name', broker=broker, backend=backend)

# 可以在创建task的时候, 指定queue name
@app.task(queue=MY_QUEUE_NAME)
def add(x, y):
    return x + y

# 如果运行下面一句, 则报错如下
app.conf.task_create_missing_queues = False
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#task-create-missing-queues

# Traceback (most recent call last):
#   File "my_client.py", line 5, in <module>
#     rslt = add.delay(1, 3)
#   File "/Library/Python/2.7/site-packages/celery/app/task.py", line 413, in delay
#     return self.apply_async(args, kwargs)
#   File "/Library/Python/2.7/site-packages/celery/app/task.py", line 536, in apply_async
#     **options
#   File "/Library/Python/2.7/site-packages/celery/app/base.py", line 713, in send_task
#     options, route_name or name, args, kwargs, task_type)
#   File "/Library/Python/2.7/site-packages/celery/app/routes.py", line 66, in route
#     options = self.expand_destination(options)  # expands 'queue'
#   File "/Library/Python/2.7/site-packages/celery/app/routes.py", line 93, in expand_destination
#     'Queue {0!r} missing from task_queues'.format(queue))
# celery.exceptions.QueueNotFound: u"Queue 'qq' missing from task_queues"
