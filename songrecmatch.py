import pandas as pd

df = pd.read_csv("csv\\ShapeOfYou1.csv")
print(max(df.frequency),min(df.frequency))
