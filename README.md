

# How to Run

1. Clone this repository
1. Install Docker and Docker-Compose if you do not yet have them
1. Add raw data files to the directory `data/`
1. Run `docker-compose up --build`

If everything worked you should be able to hit http://localhost:8001 and see your app



# Overview

# Architecture

## Containers / Services
 - `db`: a local PostgreSQL database
 - `app`: a simple Streamlit app  
 - `loader`: python basic ETL of raw data to a format used by the app




# Debugging Steps

*Get a shell to the loader*
`docker-compose run loader bash`

Build a single container
`docker-compose build loader`

*Get a shell to the app*
`docker-compose exec app bash`

*Test a DB connection*
`psql postgres://postgres:postgres@db`

*database*
1. `docker exec -it <db-container> bash`
2. `psql -U postgres`
3. `\c postgres`
4. `\dt your_schema.*`


*connect with Pgadmin*
```
host: 0.0.0.0
port: 54321
username: postgres
password: postgres
```

Directly load data (Rarely needed)
```
docker run *loader --network <docker_compose_network_id> --db postgresql://db --insert /data/*.csv
```

## How to add a page
1. prepare SQL Query for the datasource, and save your query in `sql_query.py`
2. transform your source data into desired format in `page_content.py`
3. create a new page in `/pages` folder, and render page_content

