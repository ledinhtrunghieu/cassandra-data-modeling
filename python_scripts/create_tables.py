from cassandra.cluster import Cluster
from sql_queries import *


            
def create_tables(session):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    for query in create_table_queries:
        try:
            session.execute(query)
        except Exception as e:
            print(e)


def create_keyspace(session):
    """
    Creates each table using keyspace_create. 
    """
    try:
        session.execute(keyspace_create)
    except Exception as e:
        print(e)


def drop_tables(session):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        try:
            session.execute(query)
        except Exception as e:
            print(e)


def main():
    """
    - Make a connection to a Cassandra instance your local machine (127.0.0.1)
    
    - To establish connection and begin executing queries, need a session
    
    - Drops all the tables if exist.  
    
    - Creates all tables needed.
    """
    cluster = Cluster()
    session = cluster.connect()
    
    create_keyspace(session)

    session.set_keyspace('sparkify_sp')
    
    drop_tables(session)
    create_tables(session)

    print('Tables created sucessfully.')


if __name__ == '__main__':
    main()
