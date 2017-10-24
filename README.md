1. redis-server

2. cd /path/to/queue_name/

3. python my_client.py

# 用-Q指定queue的名字
4. celery -A my_worker worker -Q qq

5. python my_consumer.py c8e59ee0-27c8-4554-ba98-43d3d5b8cf63
