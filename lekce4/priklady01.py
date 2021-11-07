import os
import pandas
import numpy
import math
import psycopg2
import matplotlib.pyplot as plt
from sqlalchemy import create_engine, inspect

engine = create_engine('sqlite:///uzivatele.db', echo=True)
engine = create_engine('sqlite:///:memory:', echo=True)
engine = create_engine('sqlite://', echo=True)

HOST = "czechitaspsql.postgres.database.azure.com"
PORT = 5432
USER = "anetadedkova21"
USERNAME = f"{USER}@czechitaspsql"
DATABASE = "postgres"
PASSWORD = "CDYnBFQZZ!o4?s0s"

engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}", echo=False)


dreviny = pandas.read_sql("dreviny", con=engine)
#print(dreviny)

#smrk = pandas.read_sql("SELECT * FROM dreviny WHERE dd_txt = 'smrk' and dd_txt ='jedle' and dd_txt = 'douglaska'", con=engine)
#print(smrk)

smrk = pandas.read_sql("SELECT * FROM dreviny WHERE dd_txt = 'Smrk, jedle, douglaska'", con=engine)
#print(smrk)

nahodila_tezba = pandas.read_sql("SELECT * FROM dreviny WHERE druhtez_txt = 'Nahodilá těžba dřeva'", con=engine)
print(nahodila_tezba)

smrk.sort_values(by="hodnota").plot.bar(
    x="rok", y="hodnota", title="Těžba dřeva"
)

pivot = nahodila_tezba.pivot_table(values="hodnota", aggfunc=numpy.sum, columns="prictez_txt", index="rok")
pivot.plot()
plt.show()