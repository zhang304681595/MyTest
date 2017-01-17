# -*- coding: utf-8 -*-
"""
Created on : 17-1-16 下午4:06

@author: zcj
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print s.recv(1024)
for data in ['Michael', 'Tracy', 'Sarah']:
    s.send(data)
    print s.recv(1024)
s.send('exit')
s.close()