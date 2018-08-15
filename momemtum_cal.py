import pandas as pd
import  numpy as np

df = pd.read_csv("momentum_ranking.csv")
mom_df = df.loc["Ticker", "Sector"]
print(mom_df)