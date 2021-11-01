import requests
import pandas

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/lexikon-zvirat.csv")
open("lexikon-zvirat.csv", "wb").write(r.content)

lexikon2 = pandas.read_csv("lexikon-zvirat.csv", sep=";")
lexikon2 = lexikon2.dropna(how="all", axis="columns")
lexikon2 = lexikon2.dropna(how="all", axis = "rows")
lexikon2 = lexikon2.set_index("id")
#print(lexikon2)

zvire_pozice =

def popisek(radek, bod):
    popis_zvirete = lexikon2["title"] preferuje následující typ stravy: lexikon2["food"]







lexikon2["popis"] = lexikon2.apply(popisek, axis=1, args=(zvire_pozice,))