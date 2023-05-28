import json
from pyairtable import Api, Base, Table


TOKEN = "patBR14HpIcpAUg0H.75fa0ebb4bd94b95a8d687e4b1e4074c1455df5e4f5a60e6878acc0f04bba7b5"
BASE_ID = "appZyYmLDRabwozss"
TABLE_NAME = "tbl3LzRBmoLLZnPh3"

table = Table(TOKEN, BASE_ID, TABLE_NAME)


def clear_table():
    ids = []
    for row in table.all():
        ids.append(row["id"])
    table.batch_delete(ids)


def print_table():
    for row in table.all():
        print(json.dumps(row, indent=2))


def insert_row(row_json: dict):
    try:
        bad_keys = []
        for k, v in row_json.items():
            if v == "N.A":
                bad_keys.append(k)
            else:
                row_json[k] = str(v)

        for k in bad_keys:
            row_json.pop(k)

        table.create(row_json)
    except Exception as e:
        print("Error while adding this row:")
        print(row_json)
        print(e)
