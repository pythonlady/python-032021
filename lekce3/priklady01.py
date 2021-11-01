import pandas
import requests

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/lexikon-zvirat.csv")
open("lexikon-zvirat.csv", "wb").write(r.content)

lexikon1 = pandas.read_csv("lexikon-zvirat.csv", sep=";")
lexikon1 = lexikon1.dropna(how="all", axis="columns")
lexikon1 = lexikon1.dropna(how="all", axis = "rows")
lexikon1 = lexikon1.set_index("id")
print(lexikon1)

for radek in lexikon1.itertuples():
    check_url = isinstance(radek.image_src, str),
    check_url = radek.image_src.startswith("https://zoopraha.cz/images/"),
    check_url = radek.image_src.endswith("jpg")
    print(radek.title)