#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : p1.py
# Author            : Channith Am <amcnith@gmail.com>
# Date              : 11.03.2019
# Last Modified Date: 11.03.2019
# Last Modified By  : Channith Am <amcnith@gmail.com>

import pandas as pd
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2019, 1, 1)

df = web.DataReader("XOM", "yahoo", start, end)

print(df.head())

df['Adj Close'].plot()
plt.show()
