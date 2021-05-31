# Project: Data Modeling with Apache Cassandra- Udacity Data Engineer Nanodegree

## 1. Introduction

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analysis team is particularly interested in understanding what songs users are listening to. Currently, there is no easy way to query the data to generate the results, since the data reside in a directory of CSV files on user activity on the app.

They'd like a data engineer to create an Apache Cassandra database which can create queries on song play data to answer the questions. My role is to create a database schema and ETL pipeline which transfer the data from local files to the database for this analysis.

I wanted to do this locally but my Windows crashed when installing Docker so I have to do it in Udacity's Project workspace.

I don't know if Notebooks is enough so I created python scripts which have the same structure as the Postgres project.

## 2. Project structure explanation

```
postgres-data-modeling
│   README.md               # Project description
│
└───event_data              # The dataset
|   | ...          
│      
└───notebooks               # Jupyter notebooks
|   |               
│   └───etl.ipynb           # ETL notebook  
|  
└───python_scripts
│   │  etl_preprocess.py    # Pre-processing script
|   |  create_tables.py     # Tables creation script
|   |  etl.py               # ETL script
|   |  sql_queries.py       # Definition of all sql queries
```

## 3. Run python scripts

```
cd python_scripts
python etl_preprocess.py
python create_tables.py
python etl.py
```