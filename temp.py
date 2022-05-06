# -*- coding:utf-8 -*-
# auth:ybb

import pandas as pd

s = pd.Series(data = ["0001", "abc", 123, {'dic1':5}],
    index = pd.Index(['001', 2, 'third', 4.4], name='my_idx'),
    dtype = 'object',
    name = 'my_series')

print(s)
