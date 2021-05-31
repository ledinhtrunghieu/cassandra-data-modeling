import pandas as pd
from cassandra.cluster import Cluster
from sql_queries import *


def insert_tables(session,df):
    """
    Insert data into different tables.
    """
    for query in insert_table_queries:
        if query == session_table_insert:
            df_columns = ['sessionId', 'itemInSession', 'artist', 'song', 'length']
        elif query == user_table_insert:
            df_columns = ['userId', 'sessionId', 'itemInSession', 'artist', 'song', 'firstName','lastName']
        elif query == song_table_insert:
            df_columns = ['song', 'firstName','lastName']
        for i, row in df.iterrows():
            data = list([row[col] for col in df_columns])
            session.execute(query, data)
        
        
def verify_tables(session):
    """
    Do SELECT to verify that the data have been inserted into each table
    """
    for query in verify_table_queries:
        try:
            rows = session.execute(query)
        except Exception as e:
            print(e)
        if query == session_table_verify:
            for row in rows:
                print (row.session_id,row.item_in_session,row.artist_name,row.song_title,row.song_length)
        elif query == user_table_verify:
            for row in rows:
                print (row.user_id, row.session_id, row.item_in_session, row.artist_name, row.song_title, row.user_firstname, row.user_lastname)
        elif query == song_table_verify:
            for row in rows:
                print (row.song_title,row.user_firstname,row.user_lastname)

                
def main():
    
    cluster = Cluster()
    session = cluster.connect()
    session.set_keyspace('sparkify_sp')

    file = 'event_datafile_new.csv'
    music_df = pd.read_csv(file, encoding='utf8')

    insert_tables(session,music_df)
    print('Data inserted sucessfully.')

    verify_tables(session)

    

if __name__ == '__main__':
    main()
