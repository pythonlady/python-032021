import requests
import pandas

r = requests.get(
    "https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/soybean-2-rot.csv"
)
open("soybean-2-rot.csv", "wb").write(r.content)

r = requests.get(
    "https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/auto.csv"
)
open("auto.csv", "wb").write(r.content)

from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split

#Input features jsou jméně sloupců v těch původních datech
# musíme přiřadit hodnoty těch values ke jménům sloupců, dáváme do seznamu = list
# plant satnd lt normal
# u toho stačí nám jedná proměnná dáme do vstupních dat jen to plant stand


data = pandas.read_csv("soybean-2-rot.csv")

print(data)
X = data.drop(columns=["class"])
print("X.shape before encoding: ", X.shape)
input_features = X.columns

y = data["class"]

oh_encoder = OneHotEncoder()
X = oh_encoder.fit_transform(X)
print("X.shape after encoding: ", X.shape)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=0
)

clf = DecisionTreeClassifier(max_depth=3, min_samples_leaf=1)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print(f1_score(y_test, y_pred, average="weighted"))
