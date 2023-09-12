import sqlite3
import polars as pl
from polars import DataFrame


def get_conn():
    con = sqlite3.connect("tutorial.db")
    con.execute('PRAGMA foreign_keys = ON')
    return con


def create_table():
    con = get_conn()
    cur = con.cursor()

    cur.execute("CREATE TABLE countries(name TEXT PRIMARY KEY, transport_cost REAL, tax REAL);")
    cur.execute(
        "CREATE TABLE cars(id INTEGER PRIMARY KEY, purchase REAL, sale REAL, transport_days INTEGER, country TEXT, "
        "FOREIGN KEY (country) REFERENCES countries(name));")
    con.commit()


def load_df():
    countries = pl.read_excel("data.xlsx", sheet_name="Countries")
    cars = pl.read_excel("data.xlsx", sheet_name="Cars", xlsx2csv_options={"ignore_formats": ["date"]}).drop_nulls()
    return countries, cars


def get_cars_list(cars: DataFrame) -> str:
    print(cars)
    new_df = cars.with_columns(
        pl.concat_str(
            [
                "(" + pl.col("Car").cast(pl.Utf8),
                pl.col("Purchase price"),
                pl.col("Sale price"),
                pl.col("Transport time"),
                "'" + pl.col("Country").str.replace(' ', '_').str.replace(' ', '_') + "')",
            ],
            separator=",",
        ).alias("sql"), )

    l = new_df["sql"].to_list()
    l = ",".join(l)
    return l


def get_countries_list(countries: DataFrame) -> str:
    new_df = countries.with_columns(
        pl.concat_str(
            [
                "('" + pl.col("Country") + "'",
                pl.col("Transport cost per day"),
                pl.col("Import tax").cast(pl.Utf8) + ")",
            ],
            separator=",",
        ).alias("sql"), )

    l = new_df["sql"].to_list()
    l = ",".join(l)
    return l


def insert_to_db(l_countries: list, l_cars: list):
    con = get_conn()
    cur = con.cursor()

    cur.execute(f"""INSERT INTO countries
    ( name, transport_cost, tax)
    VALUES
        {l_countries}""")
    con.commit()

    cur.execute(f"""INSERT INTO cars
    ( id, purchase, sale, transport_days, country )
    VALUES
        {l_cars}""")
    con.commit()


countries, cars = load_df()

l_countries = get_countries_list(countries)
l_cars = get_cars_list(cars)
print(l_countries)
print(l_cars)

# insert_to_db(l_countries, l_cars)
