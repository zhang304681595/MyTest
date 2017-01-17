# -*- coding: utf-8 -*-
"""
Created on : 17-1-11 下午2:01

@author: zcj
"""

import os
from sys import argv

str1 = argv[1]
all_path = os.walk('/home/zcj/program/')
for pathname, dirname, file_names in all_path:
    for x in [os.path.join(pathname, x) for x in file_names if str1 in x]:
        print x
