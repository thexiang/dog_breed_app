import subprocess

import click
from environs import Env
from sqlalchemy import create_engine, schema, text

env = Env()


def init_connection():
    """
    Initialize connection with the SQLAlchemy engine
    """
    db_host = env.str("POSTGRES_HOST")
    db_user = env.str("POSTGRES_USER")
    db_port = env.int("POSTGRES_PORT")
    db_name = env.str("POSTGRES_DB")
    db_pass = env.str("POSTGRES_PASSWORD")
    engine = create_engine(
        f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
    )
    return engine.connect()



class CsvLoader:
    """
        Load mydata.csv into raw.mydata table
    """

    def __init__(self, file_path, table_name):
        self.file_path = file_path
        self.table_name = table_name

    def load_data(self):

        click.echo(f"Starting to load data {self.file_path}.")
        cmd = f"csvsql --db postgresql://postgres:postgres@db/data --insert --chunk-size 100 --db-schema raw --tables {self.table_name} -I -v -y 2048 {self.file_path}"
        run = subprocess.run(cmd, capture_output=True, shell=True)

        # If we had a non-0 return code.
        if run.returncode:
            raise Exception(f"csvsql exception:", run.stdout, run.stderr)
        else:
            click.echo(run.stdout)
            click.echo("Done loading data...")


@click.command()
def load():
    """Simple program to load files into our DB."""
    conn = init_connection()
    conn.execute(schema.CreateSchema("raw"))

    click.echo(f"Loading data set!")
    raw_data_loaders = [
        CsvLoader(
            file_path="./data/dog_breeds.csv",
            table_name="dog_breeds",
        ),
    ]
    for raw_data_loader in raw_data_loaders:
        raw_data_loader.load_data()
    click.echo("All Done!")


    conn.execute(text("CREATE SCHEMA report;"))

    conn.execute(text("""CREATE TABLE report.dog_breeds(
        type varchar(20)
    );"""
    ))


    conn.close()


if __name__ == "__main__":
    load()
