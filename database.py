import sqlite3

def save_database(df):

    conn = sqlite3.connect("database/retail.db")

    df.to_sql("sales", conn, if_exists="replace", index=False)

    conn.close()