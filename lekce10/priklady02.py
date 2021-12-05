import requests
import pandas
import matplotlib.pyplot as plt
r = requests.get(
    "https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/soybean-2-rot.csv"
)
open("soybean-2-rot.csv", "wb").write(r.content)

r = requests.get(
    "https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/auto.csv"
)
open("auto.csv", "wb").write(r.content)

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import LinearSVC

#1)
data = pandas.read_csv("auto.csv", na_values=["?"])
data = data.dropna()
print(data)
print(data.shape)

#2)
# Po vyfiltrování kódu 1 ze sloupce origin vidím, že značky aut jsou z USA
data_1 = data[data["origin"] == 1]
#print(new_data_1)

# Po vyfiltrování kódu 2 ze sloupce origin vidím, že značky aut jsou z Evropy
data_2 = data[data["origin"] == 2]
#print(new_data_2)

# Po vyfiltrování kódu 3 ze sloupce origin vidím, že značky aut jsou z Evropy
data_3 = data[data["origin"] == 3]
#print(new_data_3)

#3)
auta_grouped = data.groupby(['year'])['mpg'].mean()
#print(auta_grouped)
auta_grouped.plot()
#plt.show()

#4)
X = data.drop(columns=["origin", "name"])
y = data["origin"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


model = DecisionTreeClassifier()
params = {
    "max_depth": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
    "min_samples_leaf": [1, 2, 3, 4, 5, 6]
}

gclf = GridSearchCV(model, params, scoring="f1_weighted")
gclf.fit(X_train, y_train)

print(gclf.best_params_)
print(gclf.best_score_)




#5)


#6)
