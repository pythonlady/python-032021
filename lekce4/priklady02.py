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

chicago = pandas.read_sql("SELECT * FROM crime WHERE \"PRIMARY_DESCRIPTION\" = 'MOTOR VEHICLE THEFT'", con=engine)
print(chicago.columns)
chicago_auta = chicago[chicago['SECONDARY_DESCRIPTION'] == 'AUTOMOBILE'][['PRIMARY_DESCRIPTION', 'SECONDARY_DESCRIPTION','DATE_OF_OCCURRENCE']]
chicago_auta["DATE_OF_OCCURRENCE"] = pandas.to_datetime(chicago_auta["DATE_OF_OCCURRENCE"])
chicago_auta["Month"] = chicago_auta["DATE_OF_OCCURRENCE"].dt.month
chicago_auta = chicago_auta.groupby(["Month"]).count()
chicago_auta= chicago_auta.sort_values(['SECONDARY_DESCRIPTION'], ascending=False)

print(chicago_auta)

