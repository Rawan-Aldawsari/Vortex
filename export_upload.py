import sqlite3
import pandas as pd

conn = sqlite3.connect('instance/vortex.db')

tables = [
    "user",
    "daily_challenge",
    "admin",
    "subject",
    "quiz_result",
    "quiz_battle",
    "puzzle_game",
    "chapter",
    "battle_participant",
    "upload",
    "review"
]

all_data = pd.DataFrame()

for table in tables:
    df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
    df["table_name"] = table  # نضيف اسم الجدول
    all_data = pd.concat([all_data, df], ignore_index=True)

all_data.to_excel("all_in_one.xlsx", index=False)

conn.close()