import csv
from sqlmodel import Field, SQLModel, create_engine, Session
from typing import Optional

class Flights(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    origen: str = Field(..., min_length=3, max_length=50)
    destino: str = Field(..., min_length=3, max_length=50)
    fecha: str = Field(..., min_length=3, max_length=50)

DATABASE_URL = "postgresql://uftisxallj1wdertwjo7:grggYg9AzgZB3rN33IroNZMwPh3u9Y@blfbbxfkgyqnaoc4fkdq-postgresql.services.clever-cloud.com:50013/blfbbxfkgyqnaoc4fkdq"
engine = create_engine(DATABASE_URL)

def create_table():
    SQLModel.metadata.create_all(engine)

def insert_flights_from_csv(csv_path: str):
    with open(csv_path, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        entries = []

        for row in reader:
            row["id"] = int(row["id"]) if row.get("id") else None
            entry = Flights(**row)
            entries.append(entry)

        with Session(engine) as session:
            session.add_all(entries)
            session.commit()

if __name__ == "__main__":
    create_table()
    insert_flights_from_csv("flights.csv")
    print("Datos de vuelos insertados correctamente.")
