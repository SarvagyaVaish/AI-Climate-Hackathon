import os
import json
from pyairtable import Api, Base, Table
from dotenv import load_dotenv

# Load env vars
load_dotenv()

# Set up Airtable API
TOKEN = os.getenv("AIRTABLE_TOKEN")
BASE_ID = os.getenv("AIRTABLE_BASE_ID")
TABLE_NAME = os.getenv("AIRTABLE_TABLE_NAME")
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
