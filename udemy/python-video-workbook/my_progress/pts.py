import pandas as pd

pts = pd.read_csv('points.txt', header=None)

print(pts.dropna())
print('\n')
print('Total Points: ', pts[1].sum())