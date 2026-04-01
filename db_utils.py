import pandas as pd
import urllib
from sqlalchemy import create_engine

def get_engine():
    params = urllib.parse.quote_plus(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=supply_chain;"
        "Trusted_Connection=yes;"
    )
    engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
    return engine


def load_best_scenario(engine):
    query = "SELECT * FROM SupplyChain_BestScenario"
    df = pd.read_sql(query, engine)
    return df