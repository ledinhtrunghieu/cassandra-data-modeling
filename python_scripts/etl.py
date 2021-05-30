import pandas as pd
import cassandra
from sql_queries import *


def insert_data(session, query, df, df_columns):
    for i, row in df.iterrows():
        data = tuple([row[col] for col in df_columns])
        session.execute(query, data)


def main():
    cluster = Cluster()
    session = cluster.connect()
    session.set_keyspace('sparkify_sp')

    file = 'event_datafile_new.csv'
    df = pd.read_csv(file, encoding='utf8')

    insert_data(session, session_history_insert, df, ['sessionId', 'itemInSession', 'artist', 'song', 'length'])

    insert_data(session, user_history_insert, df, ['userId', 'sessionId', 'itemInSession', 'artist', 'song', 'user'])

    insert_data(session, song_history_insert, df, ['song', 'user'])

    print('Data inserted sucessfully.')


if __name__ == '__main__':
    main()
