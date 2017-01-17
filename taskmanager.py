# -*- coding: utf-8 -*-
"""
Created on : 17-1-16 上午11:03

@author: zcj
"""

import random, time, Queue
from multiprocessing.managers import BaseManager

task_Queue = Queue.Queue()
result_Queue = Queue.Queue()

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue', callable=lambda: task_Queue)
QueueManager.register('get_result_queue', callable=lambda: result_Queue)

manager = QueueManager(address=('', 5000), authkey='abc')
manager.start()

task = manager.get_task_queue()
result = manager.get_result_queue()

for i in range(10):
    n = random.randint(1, 10000)
    print('Put task %d...' % n)
    task.put(n)

print('Try get result...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)

manager.shutdown()

