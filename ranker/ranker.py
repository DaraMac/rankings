import pandas as pd

albums = pd.read_csv("../Albums.csv")

albums_ranked = albums[albums["Date Listened"].str.contains("2021")].sort_values(by="Tier")
# albums_ranked.reset_index(inplace=True)
albums_ranked = albums_ranked[["Album", "Artist", "Tier"]]
albums_ranked.insert(0, "Rank Order", [str(i)+'.' for i in range(len(albums_ranked))])

def albumer(n):
    return str(n) + " by"

def artister(n):
    return str(n) + ","

# print(albums_ranked.to_string(index=False, header=False, formatters=[str, albumer, artister, str]))

books = pd.read_csv("../Books.csv")

books_ranked = books[books["Date Finished"].str.contains("2021")].sort_values(by="Tier")
books_ranked = books_ranked[["Book", "Author", "Tier"]]
books_ranked.insert(0, "Rank Order", [str(i)+'.' for i in range(len(books_ranked))])
print(books_ranked.to_string(index=False, header=False, formatters=[str, albumer, artister, str]))
