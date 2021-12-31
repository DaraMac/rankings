import pandas as pd
albums = pd.read_csv("../Albums.csv")

c = albums[albums["Date Listened"].str.contains("2021")]
# b = albums[["2021" in str(a) for a in albums["Date Listened"]]]
# .sort_values(by="Tier")
