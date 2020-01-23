import pandas as pd
import os


total = pd.DataFrame()
for dirname, _, filenames in os.walk('F:/天池/数字中国2020/hy_round1_testA_20200102/hy_round1_testA_20200102'):
    for filename in filenames:
        if filename == '7000.csv':
            part = pd.read_csv(f'F:/天池/数字中国2020/hy_round1_testA_20200102/hy_round1_testA_20200102/{filename}')
            total = part
        else:
            part = pd.read_csv(f'F:/天池/数字中国2020/hy_round1_testA_20200102/hy_round1_testA_20200102/{filename}')
            total = pd.concat([total, part], axis=0, ignore_index=True)


total = pd.read_feather('F:/天池/数字中国2020/train.feather')
print(total)

