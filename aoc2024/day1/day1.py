import pandas as pd

filepath = 'input.txt'

df = pd.read_csv(filepath, sep="\s+", header=None, names=["Left", "Right"])

left_series = df['Left']
right_series = df['Right']

left_series = left_series.sort_values().reset_index(drop=True)
right_series = right_series.sort_values().reset_index(drop=True)

df = pd.DataFrame({"Left": left_series, "Right": right_series})

df['diff'] = abs(df['Left'] - df['Right'])

print(df['diff'].sum())

df['left_in_right'] = df['Left'].apply(lambda x: (df['Right'] == x).sum() * x)

print(df['left_in_right'].sum())