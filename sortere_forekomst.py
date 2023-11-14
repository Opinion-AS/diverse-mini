import pandas as pd

df = pd.read_excel(r"FIL SOM SKAL LESES", header = None)
word_counts = df[0].value_counts().sort_values(ascending = False)
df_sorted = word_counts.reset_index()
df_sorted.to_excel(r"FIL SOM SKAL SKRIVES", index = False, header = None)
