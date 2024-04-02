## Pipeline Diagram
Attached is the link to the pipeline diagram of Assignment_4:
https://excalidraw.com/#json=sOMT6LcQE068eMmWviUKy,VFFxD-Ig8WHPF-TtXRJtBA

## Flow Pattern
- Data Generation:
    - The Data Engineer is to generate fake data (in csv), which he does so with a python script using the Faker library.
- Data Ingestion:
    - The csv now is to be ingested into the PostgreSQL database system using Airflow.
- Airflow Orchestration:    
    - The Directed Acyclic Graph (DAG), a python script was used to orchestrate and handle the ingestion of the data from the csv file into the PostgreSQL database system.
- Containerization with Docker:
    - PGadmin, PostgreSQL, and Airflow were run on Docker with a docker-compose yml file.
- User Interface with PGadmin:
    - PGadmin is the User Interface for the PostgreSQL engine.
