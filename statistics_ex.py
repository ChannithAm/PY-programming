#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : statistics_ex.py
# Author            : Channith Am <amcnith@gmail.com>
# Date              : 10.03.2019
# Last Modified Date: 10.03.2019
# Last Modified By  : Channith Am <amcnith@gmail.com>

import statistics

example_list = [4,6,2,6,7,8,6,5,78,4,6,7,2,2]

x = statistics.mean(example_list)

print(x)


y = statistics.stdev(example_list)
print(y)

z = statistics.variance(example_list)
print(z)
