#!/usr/bin/env python
# coding: utf-8

import click
import pandas as pd
from sqlalchemy import create_engine

@click.command()
@click.option('--pg-user', default='root', help='PostgreSQL user')
@click.option('--pg-pass', default='root', help='PostgreSQL password')
@click.option('--pg-host', default='localhost', help='PostgreSQL host')
@click.option('--pg-port', default=5432, type=int, help='PostgreSQL port')
@click.option('--pg-db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--year', default=2025, type=int, help='Year of the data')
@click.option('--month', default=11, type=int, help='Month of the data')
@click.option('--target-table', default='green_taxi_data', help='Target table name')
def run(pg_user, pg_pass, pg_host, pg_port, pg_db, year, month, target_table):
    """Ingest NYC taxi data (Parquet) into PostgreSQL database."""
    
    # Parquet URL a GitHub-ról
    prefix = 'https://d37ci6vzurychx.cloudfront.net/trip-data'
    url = f'{prefix}/green_tripdata_{year}-{month:02d}.parquet'
    
    print(f"Adatok letöltése innen: {url}")
    
    # Kapcsolódás az adatbázishoz
    engine = create_engine(f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')

    # Parquet beolvasása (a Pandas a pyarrow-t fogja használni)
    # A Parquet fájlokat általában egyben olvassuk be, mert hatékonyabbak
    df = pd.read_parquet(url)

    print(f"Betöltés az adatbázisba... ({len(df)} sor)")

    # Adatok írása az adatbázisba
    # A Parquet sémája alapján automatikusan létrehozza a táblát
    df.to_sql(name=target_table, con=engine, if_exists='replace', index=False, chunksize=10000)

    print("Kész! Az adatok sikeresen bekerültek a Postgres-be.")

if __name__ == '__main__':
    run()
