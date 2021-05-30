# DROP TABLES

session_table_drop = "DROP TABLE IF EXISTS session_table;"
user_table_drop = "DROP TABLE IF EXISTS user_table;"
song_table_drop = "DROP TABLE IF EXISTS song_table;"


# CREATE TABLES

session_table_create = """
    CREATE TABLE IF NOT EXISTS session_table
    (session_id INT, item_in_session INT, artist_name TEXT, song_title TEXT, song_length FLOAT,
    PRIMARY KEY(session_id, item_in_session))
"""

user_table_create = """
    CREATE TABLE IF NOT EXISTS user_table
    (user_id INT, session_id INT, item_in_session INT, artist_name TEXT, song_title TEXT, user_firstname TEXT, user_lastname TEXT,
    PRIMARY KEY((user_id), session_id, item_in_session))
"""

song_table_create = """
    (song_title TEXT, user_firstname TEXT,user_lastname TEXT,
    PRIMARY KEY(song_title, user_firstname,user_lastname))
"""


# CREATE KEYSPACE

keyspace_create = """
    CREATE KEYSPACE IF NOT EXISTS sparkify_sp
    WITH REPLICATION = 
    { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }"""


# INSERT DATA

session_table_insert = """
    INSERT INTO session_table (session_id, item_in_session, artist_name, song_title, song_length)
    VALUES(%s, %s, %s, %s, %s)
"""

user_table_insert = """
    INSERT INTO user_table (user_id, session_id, item_in_session, artist_name, song_title, user_firstname, user_lastname)
    VALUES(%s, %s, %s, %s, %s, %s, %s)
"""

song_table_insert = """
    INSERT INTO song_table (song_title, user_firstname, user_lastname)
    VALUES(%s, %s, %s)
"""


create_table_queries = [session_table_create, user_table_create, song_table_create]
drop_table_queries = [session_table_drop, user_table_drop, song_table_drop]
