# -*- coding: utf-8 -*-
"""
Created on : 17-1-16 下午2:13

@author: zcj
"""
import time, sys, Queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server_adr = '127.0.0.1'
print('Connect to server %s...' % server_adr)

m = QueueManager(address=(server_adr, 5000), authkey='abc')
m.connect()

task = m.get_task_queue()
result = m.get_result_queue()

for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d' %(n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')

print('worker exit.')
