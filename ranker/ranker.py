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

def seasoner(n):
    return "Season " + str(n) + ","

# print(albums_ranked.to_string(index=False, header=False, formatters=[str, albumer, artister, str]))

books = pd.read_csv("../Books.csv")

books_ranked = books[books["Date Finished"].str.contains("2021")].sort_values(by="Tier")
books_ranked = books_ranked[["Book", "Author", "Tier"]]
books_ranked.insert(0, "Rank Order", [str(i)+'.' for i in range(len(books_ranked))])
# print(books_ranked.to_string(index=False, header=False, formatters=[str, albumer, artister, str]))

movies = pd.read_csv("../Movies.csv")
movies_ranked = movies[movies["Date Watched"].str.contains("2021")].sort_values(by="Tier")
movies_ranked = movies_ranked[["Movie", "Tier"]]
movies_ranked.insert(0, "Rank Order", [str(i)+'.' for i in range(len(movies_ranked))])
# print(movies_ranked.to_string(index=False, header=False, formatters=[str, artister, str]))

tv = pd.read_csv("../TvShows.csv")
tv_ranked = tv[tv["Date Started"].str.contains("2021")].sort_values(by="Tier")
tv_ranked = tv_ranked[["Show", "Season", "Tier"]]
tv_ranked.insert(0, "Rank Order", [str(i)+'.' for i in range(len(tv_ranked))])
print(tv_ranked.to_string(index=False, header=False, formatters=[str, str, seasoner, str]))
