import csv
from sqlmodel import Field, SQLModel, create_engine, Session
from typing import Optional

class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    id_vuelo: int = Field(..., ge=0, le=1000000)
    nombre: str = Field(..., min_length=3, max_length=50)
    nombre_mascota: str = Field(..., min_length=3, max_length=50)

DATABASE_URL = "postgresql://uaaxitnpmzqpjj4qfyhh:xzn2GEMmztcr1ZFmUDZaiqaBBBxH9I@bnbzawfplrlhmtkwamnb-postgresql.services.clever-cloud.com:50013/bnbzawfplrlhmtkwamnb"
engine = create_engine(DATABASE_URL)

def create_table():
    SQLModel.metadata.create_all(engine)

def insert_users_from_csv(csv_path: str):
    with open(csv_path, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        entries = []

        for row in reader:
            row["id"] = int(row["id"]) if row.get("id") else None
            entry = Users(**row)
            entries.append(entry)

        with Session(engine) as session:
            session.add_all(entries)
            session.commit()

if __name__ == "__main__":
    create_table()
    insert_users_from_csv("users.csv")
    print("Datos de usuarios insertados correctamente.")
