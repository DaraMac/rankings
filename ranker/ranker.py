import pandas as pd

albums = pd.read_csv("../Albums.csv")

albums_ranked = albums[albums["Date Listened"].str.contains("2021")].sort_values(by="Tier")
# albums_ranked.reset_index(inplace=True)
albums_ranked = albums_ranked[["Album", "Artist", "Tier"]]
albums_ranked.insert(0, "Rank Order", [str(i)+'.' for i in range(len(albums_ranked))])
print(albums_ranked.to_string(index=False))
