import pandas as pd

pts = pd.read_csv('points.txt', header=None)
pts = pts.rename(columns={0: 'Exercise', 1: 'Points'})

print(pts.dropna())
print('\n')
print('Total Points: ', pts['Points'].sum())
print('\n')