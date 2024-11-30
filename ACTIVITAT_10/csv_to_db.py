from db_connect.db_connect import create_connection
from db_utils.create_words_table import create_table, insert_record
import pandas


def csv_to_db():
    dataframe = pandas.read_csv("./ACTIVITAT_10/paraules_temàtica_penjat.csv")

    dict_list = dataframe.to_dict(
        orient="records"  # per a que cada diccionari siga una fila
    )

    create_table()

    insert_record(dict_list)


csv_to_db()
